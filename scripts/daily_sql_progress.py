"""Utility for generating realistic daily product updates and changelog entries.

This script simulates a small engineering task that might happen over multiple days
while building a SQL-generation product layer.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def create_progress_entry(day: str, summary: str) -> None:
    target = ROOT / "docs" / "daily-progress" / f"{day}.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        "# Daily progress\n\n"
        f"Date: {day}\n\n"
        f"Summary: {summary}\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    today = date.today().strftime("%Y-%m-%d")
    create_progress_entry(
        today,
        "Added schema-aware prompt scaffolding and validation notes for SQL generation.",
    )
    print(f"Created progress entry for {today}")
