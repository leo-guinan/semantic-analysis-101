#!/usr/bin/env python3
"""Render teaching SVGs from Semantic Axis fixture JSON files.

The graph is deliberately conservative: semantic lines get their own lane,
document-count bars get a separate lower lane, and labels have reserved margins.
The previous version drew the title and axis labels inside the plot. One might call
that "dense" if one were feeling charitable. We are not.
"""
from __future__ import annotations

import html
import json
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
OUT_DIR = ROOT / "docs" / "assets"

DATASETS = {
    "clean-room": "clean-room-optimism-doom.fixture.json",
    "misleading-volume": "misleading-volume-optimism-doom.fixture.json",
    "null-shuffled": "null-shuffled-optimism-doom.fixture.json",
    "close-margin": "close-margin-high-correlation.fixture.json",
}

WIDTH = 1040
HEIGHT = 560
CARD_X = 24
CARD_Y = 24
CARD_W = WIDTH - 48
CARD_H = HEIGHT - 48
LEFT = 92
RIGHT = 120
TOP = 104
LINE_PLOT_H = 260
BAR_LANE_GAP = 18
BAR_LANE_H = 64
BOTTOM = HEIGHT - (TOP + LINE_PLOT_H + BAR_LANE_GAP + BAR_LANE_H)
PLOT_W = WIDTH - LEFT - RIGHT
LINE_BOTTOM = TOP + LINE_PLOT_H
BAR_TOP = LINE_BOTTOM + BAR_LANE_GAP
BAR_BASE = BAR_TOP + BAR_LANE_H


def sx(i: int, n: int) -> float:
    """X-coordinate for bucket centers.

    Buckets are rendered as slots inside the plot width. The old endpoint scale
    put the first/last data point exactly on the border, which made centered
    document bars protrude outside the chart box. Useful if the goal is proving
    SVG can betray you quietly. Not useful for a quiz.
    """
    if n <= 1:
        return LEFT + PLOT_W / 2
    slot_w = PLOT_W / n
    return LEFT + slot_w * (i + 0.5)


def sy_alpha(value: float) -> float:
    # Teaching range: alpha usually 0..1, with 0.5 neutral. Keep full scale visible.
    return TOP + (1.0 - value) * LINE_PLOT_H


def sy_cos(value: float) -> float:
    # Cosines in fixtures roughly 0.4..0.9. Use 0..1 to avoid exaggeration.
    return TOP + (1.0 - value) * LINE_PLOT_H


def points(values: list[float], y_fn: Callable[[float], float]) -> str:
    return " ".join(f"{sx(i, len(values)):.1f},{y_fn(v):.1f}" for i, v in enumerate(values))


def line(x1: float, y1: float, x2: float, y2: float, color: str = "#d7dde8", width: float = 1.0, dash: str | None = None) -> str:
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{width}"{dash_attr}/>'


def text(x: float, y: float, value: str, size: int = 13, color: str = "#d7dde8", anchor: str = "start", weight: str = "400") -> str:
    return f'<text x="{x:.1f}" y="{y:.1f}" fill="{color}" font-family="Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{html.escape(value)}</text>'


def safe_title(value: str, max_chars: int = 58) -> str:
    value = " ".join(value.split())
    if len(value) <= max_chars:
        return value
    return value[: max_chars - 1].rstrip() + "…"


def bucket_label(label: str) -> str:
    return label.replace("2025-", "'25-").replace("2026-", "'26-")


def render_fixture(path: Path, slug: str) -> str:
    fixture: dict[str, Any] = json.loads(path.read_text())
    ts = fixture["timeseries"]
    labels = [b["bucket"] for b in ts]
    alphas = [float(b["alpha"]) for b in ts]
    cos_a = [float(b["cosine_to_pole_a"]) for b in ts]
    cos_b = [float(b["cosine_to_pole_b"]) for b in ts]
    counts = [int(b["document_count"]) for b in ts]
    max_count = max(counts)
    min_count = min(counts)
    total = int(fixture["total_documents"])
    interp = fixture.get("expected_interpretation", {})
    correct = str(interp.get("correct_interpretation", interp.get("strongest_pattern", "see answer key"))).replace("_", " ")

    parts: list[str] = []
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-label="Semantic trend teaching chart for {html.escape(slug)}">')
    parts.append('<rect width="100%" height="100%" fill="#09111f"/>')
    parts.append(f'<rect x="{CARD_X}" y="{CARD_Y}" width="{CARD_W}" height="{CARD_H}" rx="18" fill="#101b2e" stroke="#27364d"/>')
    parts.append(text(48, 56, safe_title(fixture["measurement_name"]), 21, "#f4f7fb", weight="700"))
    parts.append(text(48, 82, f"Synthetic teaching fixture · {total:,} documents · {len(ts)} buckets", 13, "#94a3b8"))

    # Plot and bar lanes. Kept separate so bars do not visually chew through the semantic lines.
    parts.append(f'<rect x="{LEFT}" y="{TOP}" width="{PLOT_W}" height="{LINE_PLOT_H}" fill="#0c1627" stroke="#203047"/>')
    parts.append(f'<rect x="{LEFT}" y="{BAR_TOP}" width="{PLOT_W}" height="{BAR_LANE_H}" fill="#0a1424" stroke="#203047"/>')
    parts.append(text(LEFT, TOP - 12, "Semantic similarity / α", 12, "#94a3b8"))
    parts.append(text(LEFT + PLOT_W, BAR_TOP - 8, f"Document count, max {max_count:,}", 12, "#94a3b8", "end"))

    for a in [0.25, 0.5, 0.75, 1.0]:
        y = sy_alpha(a)
        parts.append(line(LEFT, y, LEFT + PLOT_W, y, "#23344d", 1, "4 5" if a == 0.5 else None))
        parts.append(text(LEFT - 16, y + 4, f"{a:.2f}", 11, "#7f8ea3", "end"))
    parts.append(text(LEFT + 8, TOP + 18, "doom", 11, "#f87171"))
    parts.append(text(LEFT + 8, LINE_BOTTOM - 10, "optimism", 11, "#60a5fa"))
    parts.append(text(LEFT + 8, sy_alpha(0.5) - 8, "neutral", 11, "#94a3b8"))

    # Volume bars, in a dedicated lower lane.
    parts.append('<g data-layer="volume-bars">')
    bar_w = min(40, PLOT_W / max(len(ts), 1) * 0.46)
    for i, c in enumerate(counts):
        x = sx(i, len(ts)) - bar_w / 2
        h = max(4, (c / max_count) * (BAR_LANE_H - 12))
        y = BAR_BASE - h
        is_low_volume = c == min_count and min_count < max_count * 0.1
        color = "#f59e0b" if is_low_volume else "#334155"
        parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{h:.1f}" rx="2" fill="{color}" opacity="0.74"/>')
        if is_low_volume:
            parts.append(text(x + bar_w / 2, y - 8, f"low volume: {c} docs", 12, "#fbbf24", "middle", "700"))
        elif c == max_count:
            parts.append(text(x + bar_w / 2, y - 8, f"{c:,} docs", 11, "#cbd5e1", "middle", "700"))
    parts.append('</g>')

    # Semantic lines.
    parts.append('<g data-layer="semantic-lines">')
    parts.append(f'<polyline points="{points(alphas, sy_alpha)}" fill="none" stroke="#f8fafc" stroke-width="3.2" stroke-linejoin="round" stroke-linecap="round"/>')
    parts.append(f'<polyline points="{points(cos_a, sy_cos)}" fill="none" stroke="#60a5fa" stroke-width="1.9" opacity="0.72" stroke-linejoin="round"/>')
    parts.append(f'<polyline points="{points(cos_b, sy_cos)}" fill="none" stroke="#f87171" stroke-width="1.9" opacity="0.72" stroke-linejoin="round"/>')
    for i, a in enumerate(alphas):
        x = sx(i, len(ts))
        parts.append(f'<circle cx="{x:.1f}" cy="{sy_alpha(a):.1f}" r="4.5" fill="#f8fafc" stroke="#09111f" stroke-width="1.5"/>')
    parts.append('</g>')

    # X labels: show endpoints and a middle anchor only. The full labels are in the fixture/table, not crammed into a tiny axis.
    label_indexes = {0, len(ts) // 2, len(ts) - 1}
    for i, label in enumerate(labels):
        if i in label_indexes:
            parts.append(text(sx(i, len(ts)), BAR_BASE + 24, bucket_label(label), 10, "#94a3b8", "middle"))

    # Legend lives below the graph lanes, not on top of data.
    lx = LEFT
    ly = HEIGHT - 64
    parts.append(f'<circle cx="{lx}" cy="{ly}" r="5" fill="#f8fafc"/>')
    parts.append(text(lx + 12, ly + 4, "α semantic lean", 12, "#d7dde8"))
    parts.append(f'<rect x="{lx + 160}" y="{ly - 7}" width="15" height="12" fill="#334155" opacity="0.74"/>')
    parts.append(text(lx + 183, ly + 4, "document count", 12, "#d7dde8"))
    parts.append(line(lx + 328, ly, lx + 360, ly, "#60a5fa", 2))
    parts.append(text(lx + 368, ly + 4, "cos optimism", 12, "#d7dde8"))
    parts.append(line(lx + 500, ly, lx + 532, ly, "#f87171", 2))
    parts.append(text(lx + 540, ly + 4, "cos doom", 12, "#d7dde8"))

    parts.append(text(LEFT, HEIGHT - 28, f"Correct reading: {correct}", 13, "#cbd5e1", weight="700"))
    parts.append('</svg>')
    return "\n".join(parts)


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for slug, filename in DATASETS.items():
        svg = render_fixture(DATA_DIR / filename, slug)
        out = OUT_DIR / f"{slug}.svg"
        out.write_text(svg)
        print(f"wrote {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
