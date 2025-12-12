from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass(frozen=True)
class Grade:
    """Represents a single grade entry (0..100) optionally bound to a date."""
    value: int
    when: Optional[date] = None

    def __post_init__(self) -> None:
        if not (0 <= self.value <= 100):
            raise ValueError("Grade value must be in range 0..100")
