from logic_utils import check_guess

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"  # FIX: unpack tuple before asserting

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"  # FIX: assert on outcome only

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"  # FIX: assert on outcome only
from logic_utils import check_guess

def test_hint_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message  # make sure the message matches the fix

def test_hint_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
