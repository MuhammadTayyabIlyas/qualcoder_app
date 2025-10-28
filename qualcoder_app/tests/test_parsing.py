import pytest
from pathlib import Path
from qualcoder_core import extract_participant_responses, generate_initial_code, DEFAULT_CODEBOOK

def test_extract_participant_responses_basic():
    text = "Interviewer: Hello\nParticipant: I teach math and use Zoom.\nInterviewer: Thanks"
    parts = extract_participant_responses(text)
    assert len(parts) == 1
    assert "Zoom" in parts[0]

def test_generate_initial_code_keywords():
    s = "I use PowerPoint and slides for my lectures."
    code, note = generate_initial_code(s, DEFAULT_CODEBOOK)
    assert "Presentation" in code or "presentation" in code.lower() or "presentation" in code
