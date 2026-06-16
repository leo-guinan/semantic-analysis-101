from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GAME = ROOT / "docs" / "game" / "index.html"


def test_chart_interpretation_game_exists_and_contains_four_cases():
    assert GAME.exists(), "docs/game/index.html should exist"
    html = GAME.read_text()
    for case_id in ["clean-room", "misleading-volume", "null-shuffled", "close-margin"]:
        assert case_id in html
        assert f"../assets/{case_id}.svg" in html


def test_chart_interpretation_game_has_scoring_and_explanations():
    html = GAME.read_text()
    for phrase in [
        "Chart Interpretation Quiz",
        "data-answer",
        "score",
        "explanation",
        "low-volume",
        "18 documents",
        "No meaningful semantic drift",
        "both poles are high",
        "Try again",
    ]:
        assert phrase.lower() in html.lower()


def test_readme_links_to_quiz_game():
    readme = (ROOT / "README.md").read_text()
    assert "docs/game/index.html" in readme
    assert "Chart Interpretation Quiz" in readme


def test_pages_landing_links_to_quiz():
    landing = (ROOT / "docs" / "index.html").read_text()
    assert "Semantic Analysis 101" in landing
    assert "game/" in landing
    assert "Play the Chart Interpretation Quiz" in landing
