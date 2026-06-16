from pathlib import Path

from scripts import render_svg_charts as charts


def test_chart_renderer_reserves_space_for_title_and_subtitle():
    assert charts.TOP >= 100
    svg = charts.render_fixture(charts.DATA_DIR / "clean-room-optimism-doom.fixture.json", "clean-room")
    assert f'x="{charts.LEFT}" y="{charts.TOP}"' in svg
    assert 'y="56.0"' in svg
    assert 'y="82.0"' in svg


def test_chart_renderer_reserves_right_margin_and_avoids_edge_annotations():
    assert charts.RIGHT >= 96
    svg = charts.render_fixture(charts.DATA_DIR / "clean-room-optimism-doom.fixture.json", "clean-room")
    assert "neutral α=0.5" not in svg
    assert "aria-label=\"Semantic trend teaching chart" in svg


def test_chart_renderer_keeps_bars_in_dedicated_lower_lane():
    assert charts.BAR_LANE_H <= 72
    assert charts.BAR_LANE_GAP >= 14
    svg = charts.render_fixture(charts.DATA_DIR / "misleading-volume-optimism-doom.fixture.json", "misleading-volume")
    assert "data-layer=\"volume-bars\"" in svg
    assert "data-layer=\"semantic-lines\"" in svg
    assert "low volume" in svg


def test_chart_renderer_writes_document_counts_for_low_volume_bars():
    svg = charts.render_fixture(charts.DATA_DIR / "misleading-volume-optimism-doom.fixture.json", "misleading-volume")
    assert "18 docs" in svg
    assert "1,400 docs" in svg
