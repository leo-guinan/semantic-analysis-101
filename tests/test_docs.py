from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_required_docs_exist_and_reference_all_graphs():
    readme = (ROOT / "README.md").read_text()
    required = [
        "docs/assets/clean-room.svg",
        "docs/assets/misleading-volume.svg",
        "docs/assets/null-shuffled.svg",
        "docs/assets/close-margin.svg",
        "docs/lessons/01-what-is-a-semantic-trend.md",
        "docs/lessons/02-how-to-read-the-graph.md",
        "docs/lessons/03-four-teaching-datasets.md",
        "docs/lessons/04-common-failures.md",
        "docs/checklists/before-quoting.md",
    ]
    for path in required:
        assert (ROOT / path).exists(), path
        assert path in readme, f"README should link {path}"


def test_svg_charts_include_answer_key_and_volume_language():
    for svg_path in (ROOT / "docs/assets").glob("*.svg"):
        text = svg_path.read_text()
        assert "Correct reading:" in text
        assert "document count" in text

    misleading = (ROOT / "docs/assets/misleading-volume.svg").read_text()
    assert "low volume: 18 docs" in misleading


def test_guide_contains_required_interpretation_warnings():
    corpus = "\n".join(p.read_text() for p in [ROOT / "README.md", *sorted((ROOT / "docs/lessons").glob("*.md")), ROOT / "docs/checklists/before-quoting.md"])
    for phrase in [
        "document counts",
        "raw cosine",
        "bucket size",
        "low-volume",
        "screenshot",
        "corpus",
        "pole terms",
        "No meaningful semantic drift",
    ]:
        assert phrase.lower() in corpus.lower()
