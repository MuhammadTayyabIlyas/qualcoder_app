"""
app.py - Modern Streamlit UI for QualCoder
Professional dashboard with 3-stage qualitative coding
Run:
    streamlit run app.py
"""

import streamlit as st
from pathlib import Path
import tempfile
import shutil
import json
import io
from typing import List
import pandas as pd
try:
    from PIL import Image
except ImportError:
    Image = None

from qualcoder_core import (
    load_codebook, make_output_folder, process_single_transcript,
    DEFAULT_CODEBOOK, suggest_keywords_from_texts, extract_text_from_file
)

# ===============================
# Page Configuration
# ===============================
st.set_page_config(
    page_title="QualCoder Pro",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===============================
# Custom CSS for Modern UI
# ===============================
st.markdown("""
<style>
    /* Main container styling */
    .main {
        padding: 2rem 1rem;
    }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 2rem;
    }
    
    /* Card styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    
    .stTabs [data-baseweb="tab"] {
        padding: 10px 24px;
        font-weight: 500;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.5rem 2rem;
        font-weight: 500;
        border-radius: 5px;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    /* Success/Info alerts styling */
    .stAlert {
        border-radius: 10px;
        padding: 1rem;
    }
    
    /* Metric cards */
    [data-testid="metric-container"] {
        background: white;
        border: 1px solid #e0e0e0;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# ===============================
# Initialize Session State
# ===============================
if 'suggested_keywords' not in st.session_state:
    st.session_state['suggested_keywords'] = []
if 'analysis_complete' not in st.session_state:
    st.session_state['analysis_complete'] = False
if 'results' not in st.session_state:
    st.session_state['results'] = []
if 'uploaded_files' not in st.session_state:
    st.session_state['uploaded_files'] = None
if 'research_questions' not in st.session_state:
    st.session_state['research_questions'] = []
if 'domain_keywords' not in st.session_state:
    st.session_state['domain_keywords'] = []
if 'manual_keywords_raw' not in st.session_state:
    st.session_state['manual_keywords_raw'] = ""
if 'codebook' not in st.session_state:
    st.session_state['codebook'] = DEFAULT_CODEBOOK
if 'picked_keywords' not in st.session_state:
    st.session_state['picked_keywords'] = []
if 'research_questions_text' not in st.session_state:
    st.session_state['research_questions_text'] = ""

# ===============================
# Header Section
# ===============================
col_logo, col_header, col_developer = st.columns([1, 6, 2])

with col_logo:
    st.write("")  # Spacer

with col_header:
    st.markdown("""
    <div class="main-header">
        <h1 style="margin: 0; font-size: 2.5rem;">🔬 QualCoder Pro</h1>
        <p style="margin: 0.5rem 0 0 0; font-size: 1.1rem; opacity: 0.95;">
            Advanced 3-Stage Qualitative Coding Analysis Platform
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_developer:
    # Developer info in header
    st.markdown("""
    <div style="text-align: center; padding: 10px; background: rgba(255,255,255,0.9); border-radius: 10px; margin-top: 10px;">
        <p style="font-size: 0.85rem; margin: 0; color: #666;">Developed by</p>
        <p style="font-size: 1rem; font-weight: 600; margin: 0; color: #333;">Muhammad Tayyab Ilyas</p>
        <p style="font-size: 0.8rem; margin: 0; color: #666;">PhD Student, UAB</p>
    </div>
    """, unsafe_allow_html=True)

# ===============================
# Main Content Area with Tabs
# ===============================
tab1, tab2, tab3, tab4 = st.tabs(["📁 **Data Input**", "🔧 **Configuration**", "📊 **Analysis**", "📈 **Results**"])

# ===============================
# Tab 1: Data Input
# ===============================
with tab1:
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("### 📄 Upload Transcripts")
        uploaded_files = st.file_uploader(
            "Select your transcript files",
            accept_multiple_files=True,
            type=['docx', 'pdf', 'txt'],
            help="Support for DOCX, PDF, and TXT formats"
        )
        # Store in session state for cross-tab access
        st.session_state['uploaded_files'] = uploaded_files
        
        if uploaded_files:
            st.success(f"✅ {len(uploaded_files)} file(s) uploaded successfully")
            
            # File preview
            with st.expander("📋 View uploaded files", expanded=False):
                for idx, file in enumerate(uploaded_files, 1):
                    col_icon, col_name, col_size = st.columns([1, 8, 3])
                    with col_icon:
                        st.write(f"{idx}.")
                    with col_name:
                        st.write(f"📄 {file.name}")
                    with col_size:
                        size_kb = len(file.getvalue()) / 1024
                        st.write(f"{size_kb:.1f} KB")
    
    with col2:
        st.markdown("### 📚 Codebook Configuration")
        
        codebook_option = st.radio(
            "Choose codebook option:",
            ["Use default codebook", "Upload custom codebook"],
            help="Select how you want to configure your coding framework"
        )
        
        codebook = st.session_state['codebook']
        
        if codebook_option == "Upload custom codebook":
            uploaded_codebook = st.file_uploader(
                "Upload codebook JSON",
                type=['json'],
                help="JSON format: {\"label\": [\"keyword1\", \"keyword2\", ...]}"
            )
            
            if uploaded_codebook:
                try:
                    cb = json.load(uploaded_codebook)
                    if isinstance(cb, dict):
                        codebook = cb
                        st.session_state['codebook'] = cb
                        st.success("✅ Custom codebook loaded successfully")
                        
                        # Preview codebook
                        with st.expander("View codebook structure", expanded=False):
                            st.json(cb)
                    else:
                        st.error("❌ Codebook must be a valid JSON object")
                except Exception as e:
                    st.error(f"❌ Failed to load codebook: {e}")

# ===============================
# Tab 2: Configuration
# ===============================
with tab2:
    st.markdown("### 🎯 Project Configuration")
    
    col1, col2 = st.columns(2)
    
    with col1:
        project_name = st.text_input(
            "Project Name",
            value="MyProject",
            placeholder="Enter project name",
            help="This will be used for output folder naming"
        )
        
        st.markdown("### 📝 Research Questions")
        rq_text = st.text_area(
            "Enter your research questions (one per line)",
            value=st.session_state.get('research_questions_text', ''),
            height=200,
            placeholder="Example:\n• What barriers do teachers face in implementing technology?\n• What strategies are used to overcome challenges?\n• How do teachers perceive the impact on student learning?",
            help="Each line will be treated as a separate research question"
        )
        # Store research questions text in session state
        st.session_state['research_questions_text'] = rq_text
        # Store research questions in session state
        research_questions = [rq.strip() for rq in rq_text.splitlines() if rq.strip()]
        st.session_state['research_questions'] = research_questions
    
    with col2:
        st.markdown("### 🔍 Domain Keywords")
        
        # NLP suggestion settings
        use_nlp = st.checkbox("Enable NLP keyword suggestions", value=True)
        
        if use_nlp:
            top_n = st.slider(
                "Number of keywords to suggest",
                min_value=5,
                max_value=50,
                value=20,
                step=5,
                help="TF-IDF based keyword extraction"
            )
            
            if st.button("🤖 Generate Keyword Suggestions", use_container_width=True):
                uploaded_files = st.session_state.get('uploaded_files')
                if not uploaded_files:
                    st.warning("⚠️ Please upload transcripts first")
                else:
                    with st.spinner("Analyzing documents..."):
                        texts = []
                        for uf in uploaded_files:
                            with tempfile.NamedTemporaryFile(delete=False, suffix=Path(uf.name).suffix) as tf:
                                tf.write(uf.getbuffer())
                                tmp_path = Path(tf.name)
                            txt = extract_text_from_file(tmp_path)
                            texts.append(txt)
                            try:
                                tmp_path.unlink()
                            except Exception:
                                pass
                        
                        suggestions = suggest_keywords_from_texts(texts, top_n=top_n)
                        st.session_state['suggested_keywords'] = suggestions
                        
                        if suggestions:
                            st.success(f"✅ Generated {len(suggestions)} keyword suggestions")
        
        # Display and select keywords
        if st.session_state.get('suggested_keywords'):
            st.markdown("#### 📌 Select Keywords")
            picked = st.multiselect(
                "Choose keywords to include",
                options=st.session_state['suggested_keywords'],
                default=st.session_state['suggested_keywords'][:10],
                help="Select relevant keywords for your analysis"
            )
            # Store picked keywords in session state
            st.session_state['picked_keywords'] = picked
        else:
            picked = st.session_state.get('picked_keywords', [])
        
        # Manual keyword input
        st.markdown("#### ✏️ Manual Keywords")
        manual_keywords_raw = st.text_area(
            "Add custom keywords (comma-separated)",
            value=st.session_state.get('manual_keywords_raw', ''),
            placeholder="e.g., online learning, student engagement, assessment strategies",
            height=100
        )
        # Store manual keywords in session state
        st.session_state['manual_keywords_raw'] = manual_keywords_raw

# ===============================
# Tab 3: Analysis
# ===============================
with tab3:
    st.markdown("### 🚀 Run Analysis")
    
    # Get data from session state
    uploaded_files = st.session_state.get('uploaded_files')
    research_questions = st.session_state.get('research_questions', [])
    codebook = st.session_state.get('codebook', DEFAULT_CODEBOOK)
    manual_keywords_raw = st.session_state.get('manual_keywords_raw', '')
    
    # Parse manual keywords
    manual_list = []
    if manual_keywords_raw:
        manual_list = [kw.strip() for kw in manual_keywords_raw.replace('\n', ',').split(',') if kw.strip()]
    
    # Get picked keywords from session state
    picked = st.session_state.get('picked_keywords', [])
    domain_keywords = list(dict.fromkeys(picked + manual_list))
    st.session_state['domain_keywords'] = domain_keywords
    
    # Analysis summary
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Files", len(uploaded_files) if uploaded_files else 0)
    with col2:
        st.metric("Research Questions", len(research_questions))
    with col3:
        st.metric("Keywords", len(domain_keywords))
    
    # Configuration preview
    with st.expander("📋 Review Configuration", expanded=True):
        config_col1, config_col2 = st.columns(2)
        
        with config_col1:
            st.markdown("**Research Questions:**")
            if research_questions:
                for i, rq in enumerate(research_questions, 1):
                    st.write(f"{i}. {rq}")
            else:
                st.write("*No research questions defined*")
        
        with config_col2:
            st.markdown("**Domain Keywords:**")
            if domain_keywords:
                st.write(", ".join(domain_keywords[:20]))
                if len(domain_keywords) > 20:
                    st.write(f"*...and {len(domain_keywords)-20} more*")
            else:
                st.write("*No keywords defined*")
    
    # Analysis settings
    st.markdown("### ⚙️ Analysis Options")
    preview_toggle = st.checkbox("Show segment preview in results", value=True)
    
    # Run analysis button
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔬 **Start Analysis**", use_container_width=True, type="primary"):
            if not uploaded_files:
                st.error("❌ Please upload at least one transcript file")
            elif not research_questions:
                st.error("❌ Please enter at least one research question")
            else:
                st.session_state['analysis_complete'] = False
                out_folder = make_output_folder(project_name)
                
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                results = []
                with tempfile.TemporaryDirectory() as td:
                    td_path = Path(td)
                    total_files = len(uploaded_files)
                    
                    for idx, uf in enumerate(uploaded_files):
                        progress = (idx / total_files)
                        progress_bar.progress(progress)
                        status_text.text(f"Processing: {uf.name} ({idx+1}/{total_files})")
                        
                        target = td_path / uf.name
                        with open(target, 'wb') as f:
                            f.write(uf.getbuffer())
                        
                        try:
                            s1, s2, s3 = process_single_transcript(
                                target, out_folder, codebook, 
                                research_questions, domain_keywords=domain_keywords
                            )
                            results.append((uf.name, s1, s2, s3))
                        except Exception as e:
                            st.error(f"❌ Failed processing {uf.name}: {e}")
                    
                    progress_bar.progress(1.0)
                    status_text.text("Analysis complete!")
                
                st.session_state['results'] = results
                st.session_state['analysis_complete'] = True
                st.session_state['out_folder'] = out_folder
                
                st.success("✅ Analysis completed successfully!")
                st.balloons()

# ===============================
# Tab 4: Results
# ===============================
with tab4:
    if st.session_state.get('analysis_complete') and st.session_state.get('results'):
        st.markdown("### 📊 Analysis Results")
        
        results = st.session_state['results']
        out_folder = st.session_state['out_folder']
        
        # Download all results
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            shutil.make_archive(str(out_folder), 'zip', root_dir=out_folder)
            zip_path = out_folder.with_suffix('.zip')
            with open(zip_path, 'rb') as f:
                zip_bytes = f.read()
            st.download_button(
                "📥 **Download All Results (ZIP)**",
                data=zip_bytes,
                file_name=f"{out_folder.name}.zip",
                use_container_width=True
            )
        
        st.markdown("---")
        
        # Individual file results
        for fname, s1, s2, s3 in results:
            with st.expander(f"📄 {fname}", expanded=True):
                if s1 is not None and not s1.empty:
                    result_col1, result_col2 = st.columns([3, 1])
                    
                    with result_col1:
                        if preview_toggle:
                            st.markdown("**Sample Segments (First 5):**")
                            st.dataframe(
                                s1.head(5),
                                use_container_width=True,
                                hide_index=True
                            )
                    
                    with result_col2:
                        st.markdown("**Statistics:**")
                        st.metric("Total Segments", len(s1))
                        st.metric("Unique Codes", s1['Initial_Code'].nunique())
                    
                    # Download buttons for individual files
                    st.markdown("**Download Options:**")
                    file_cols = st.columns(3)
                    col_idx = 0
                    for fx in out_folder.rglob(f"{Path(fname).stem}*"):
                        if fx.suffix.lower() in ['.xlsx', '.txt']:
                            with open(fx, 'rb') as f:
                                with file_cols[col_idx % 3]:
                                    st.download_button(
                                        f"📥 {fx.name}",
                                        data=f.read(),
                                        file_name=fx.name,
                                        use_container_width=True
                                    )
                                col_idx += 1
        
        # Aggregate analytics
        st.markdown("---")
        st.markdown("### 📈 Aggregate Analytics")
        
        all_stage1 = pd.concat(
            [r[1] for r in results if r[1] is not None and not r[1].empty],
            ignore_index=True
        ) if results else pd.DataFrame()
        
        if not all_stage1.empty:
            analytics_col1, analytics_col2 = st.columns(2)
            
            with analytics_col1:
                st.markdown("#### Top 10 Initial Codes")
                top_codes = all_stage1['Initial_Code'].value_counts().head(10).reset_index()
                top_codes.columns = ['Code', 'Frequency']
                st.dataframe(
                    top_codes,
                    use_container_width=True,
                    hide_index=True
                )
            
            with analytics_col2:
                st.markdown("#### Summary Statistics")
                total_segments = len(all_stage1)
                unique_codes = all_stage1['Initial_Code'].nunique()
                avg_segments_per_file = total_segments / len(results) if results else 0
                
                st.metric("Total Segments Analyzed", total_segments)
                st.metric("Unique Codes Identified", unique_codes)
                st.metric("Avg Segments/File", f"{avg_segments_per_file:.1f}")
    else:
        st.info("📊 No results available yet. Please run the analysis first in the Analysis tab.")

# ===============================
# Sidebar (with Developer Bio)
# ===============================
with st.sidebar:
    # Developer Photo and Bio
    st.markdown("### 👨‍🎓 Developer")
    
    # Display photo if available
    try:
        if Image is not None:
            # Resolve image path relative to this file, with optional assets folder
            img_path = Path(__file__).parent / "Tayyab.png"
            if not img_path.exists():
                alt_path = Path(__file__).parent / "assets" / "Tayyab.png"
                if alt_path.exists():
                    img_path = alt_path
            if img_path.exists():
                img = Image.open(str(img_path))
                # Create a centered column for the image
                col1, col2, col3 = st.columns([1, 3, 1])
                with col2:
                    st.image(img, use_container_width=True, caption="Muhammad Tayyab Ilyas")
    except Exception as e:
        pass  # If image loading fails, continue without it
    
    st.markdown("""
    **Muhammad Tayyab Ilyas**  
    *PhD Student*  
    Faculty of Educational Sciences  
    Universitat Autònoma de Barcelona  
    Barcelona, Spain
    """)
    
    with st.expander("📖 Biography", expanded=False):
        st.markdown("""
        Tayyab is a PhD scholar at Universitat Autònoma de Barcelona exploring how 
        digital technologies and artificial intelligence reshape teaching and learning 
        in universities. Drawing on a decade of classroom and administrative experience 
        in education, his research examines the intersection of pedagogical practice, 
        technological innovation, and institutional transformation across diverse 
        cultural contexts.
        """)
    
    with st.expander("📧 Contact", expanded=False):
        st.markdown("""
        **Email:** MuhammadTayyab.Ilyas@autonoma.cat  
        **Tel:** +34 664 667 464  
        **Twitter:** [@tayyabcheema777](https://twitter.com/tayyabcheema777)  
        **LinkedIn:** [tayyabcheema777](https://www.linkedin.com/in/tayyabcheema777/)
        """)
    
    st.markdown("---")
    
    st.markdown("### 📌 About QualCoder")
    st.info(
        "**QualCoder Pro** performs 3-stage qualitative coding:\n\n"
        "1. **Stage 1:** Initial coding\n"
        "2. **Stage 2:** Pattern analysis\n"
        "3. **Stage 3:** Theme generation\n\n"
        "All processing is performed locally."
    )
    
    st.markdown("---")
    st.markdown("### 🔗 Resources")
    st.markdown(
        "• [Documentation](https://example.com/docs)\n"
        "• [Support](https://example.com/support)\n"
        "• [GitHub](https://github.com/MuhammadTayyabIlyas)"
    )
    
    st.markdown("---")
    st.caption("QualCoder Pro v1.0 | © 2024 Muhammad Tayyab Ilyas")
