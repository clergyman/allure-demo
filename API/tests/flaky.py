import os
import random

import pytest


def maybe_fail(probability: float, reason: str) -> None:
    if os.getenv("DEMO_DISABLE_FLAKES") == "1":
        return

    if random.random() < probability:
        pytest.fail(
            f"Demo flaky failure ({probability * 100:.1f}% chance): {reason}"
        )
