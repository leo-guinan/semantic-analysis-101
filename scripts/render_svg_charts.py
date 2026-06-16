#!/usr/bin/env python3
"""Render simple teaching SVGs from Semantic Axis fixture JSON files."""
from __future__ import annotations

import html
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
OUT_DIR = ROOT / "docs" / "assets"

DATASETS = {
    "clean-room": "clean-room-optimism-doom.fixture.json",
    "misleading-volume": "misleading-volume-optimism-doom.fixture.json",
    "null-shuffled": "null-shuffled-optimism-doom.fixture.json",
    "close-margin": "close-margin-high-correlation.fixture.json",
}

WIDTH = 920
HEIGHT = 430
LEFT = 72
RIGHT = 40
TOP = 54
BOTTOM = 76
PLOT_W = WIDTH - LEFT - RIGHT
PLOT_H = HEIGHT - TOP - BOTTOM


def sx(i: int, n: int) -> float:
    if n == 1:
        return LEFT + PLOT_W / 2
    return LEFT + (PLOT_W * i / (n - 1))


def sy_alpha(value: float) -> float:
    # Teaching range: alpha usually 0..1, with 0.5 neutral. Keep full scale visible.
    return TOP + (1.0 - value) * PLOT_H


def sy_cos(value: float) -> float:
    # Cosines in fixtures roughly 0.4..0.9. Use 0..1 to avoid exaggeration.
    return TOP + (1.0 - value) * PLOT_H


def points(values: list[float], y_fn) -> str:
    return " ".join(f"{sx(i, len(values)):.1f},{y_fn(v):.1f}" for i, v in enumerate(values))


def line(x1: float, y1: float, x2: float, y2: float, color: str = "#d7dde8", width: float = 1.0, dash: str | None = None) -> str:
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{width}"{dash_attr}/>'


def text(x: float, y: float, value: str, size: int = 13, color: str = "#d7dde8", anchor: str = "start", weight: str = "400") -> str:
    return f'<text x="{x:.1f}" y="{y:.1f}" fill="{color}" font-family="Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{html.escape(value)}</text>'


def render_fixture(path: Path, slug: str) -> str:
    fixture = json.loads(path.read_text())
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
    parts.append('<rect x="20" y="20" width="880" height="390" rx="18" fill="#101b2e" stroke="#27364d"/>')
    parts.append(text(42, 48, fixture["measurement_name"], 20, "#f4f7fb", weight="700"))
    parts.append(text(42, 72, f"Synthetic teaching fixture · {total:,} documents · {len(ts)} buckets", 13, "#94a3b8"))

    # plot area
    parts.append('<rect x="72" y="54" width="808" height="300" fill="#0c1627" stroke="#203047"/>')
    for a in [0.25, 0.5, 0.75]:
        y = sy_alpha(a)
        parts.append(line(LEFT, y, LEFT + PLOT_W, y, "#23344d", 1, "4 5" if a == 0.5 else None))
        parts.append(text(52, y + 4, f"{a:.2f}", 11, "#7f8ea3", "end"))
    parts.append(text(48, TOP + 8, "doom", 11, "#f87171", "end"))
    parts.append(text(48, TOP + PLOT_H + 4, "optimism", 11, "#60a5fa", "end"))
    parts.append(text(LEFT + PLOT_W + 8, sy_alpha(0.5) + 4, "neutral α=0.5", 11, "#94a3b8"))

    # volume bars, behind lines
    bar_w = min(34, PLOT_W / max(len(ts), 1) * 0.52)
    for i, c in enumerate(counts):
        x = sx(i, len(ts)) - bar_w / 2
        h = max(3, (c / max_count) * 76)
        y = TOP + PLOT_H - h
        color = "#f59e0b" if c == min_count and min_count < max_count * 0.1 else "#334155"
        parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{h:.1f}" fill="{color}" opacity="0.72"/>')

    # lines
    parts.append(f'<polyline points="{points(alphas, sy_alpha)}" fill="none" stroke="#f8fafc" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>')
    parts.append(f'<polyline points="{points(cos_a, sy_cos)}" fill="none" stroke="#60a5fa" stroke-width="1.8" opacity="0.65" stroke-linejoin="round"/>')
    parts.append(f'<polyline points="{points(cos_b, sy_cos)}" fill="none" stroke="#f87171" stroke-width="1.8" opacity="0.65" stroke-linejoin="round"/>')

    for i, (label, a, c) in enumerate(zip(labels, alphas, counts)):
        x = sx(i, len(ts))
        parts.append(f'<circle cx="{x:.1f}" cy="{sy_alpha(a):.1f}" r="4.5" fill="#f8fafc" stroke="#09111f" stroke-width="1.5"/>')
        if i == 0 or i == len(ts) - 1 or c == min_count:
            parts.append(text(x, TOP + PLOT_H + 22, label, 10, "#94a3b8", "middle"))
        if c == min_count and min_count < max_count * 0.1:
            parts.append(text(x, sy_alpha(a) - 18, f"low volume: {c} docs", 12, "#fbbf24", "middle", "700"))

    # legend
    lx = LEFT + 10
    ly = HEIGHT - 48
    parts.append(f'<circle cx="{lx}" cy="{ly}" r="5" fill="#f8fafc"/>')
    parts.append(text(lx + 12, ly + 4, "α semantic lean", 12, "#d7dde8"))
    parts.append(f'<rect x="{lx + 145}" y="{ly - 7}" width="15" height="12" fill="#334155" opacity="0.72"/>')
    parts.append(text(lx + 168, ly + 4, "document count", 12, "#d7dde8"))
    parts.append(line(lx + 305, ly, lx + 335, ly, "#60a5fa", 2))
    parts.append(text(lx + 342, ly + 4, "cos optimism", 12, "#d7dde8"))
    parts.append(line(lx + 448, ly, lx + 478, ly, "#f87171", 2))
    parts.append(text(lx + 485, ly + 4, "cos doom", 12, "#d7dde8"))

    parts.append(text(LEFT, HEIGHT - 20, f"Correct reading: {correct}", 13, "#cbd5e1", weight="700"))
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
