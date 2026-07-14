import os
import random

import pytest


def flake_probability(default: float) -> float:
    override = os.getenv("DEMO_FLAKE_PROBABILITY")
    if override is None:
        return default

    try:
        probability = float(override)
    except ValueError as error:
        raise ValueError("DEMO_FLAKE_PROBABILITY must be a number.") from error

    if probability < 0 or probability > 1:
        raise ValueError("DEMO_FLAKE_PROBABILITY must be between 0 and 1.")

    return probability


def maybe_fail(probability: float, reason: str) -> None:
    if os.getenv("DEMO_DISABLE_FLAKES") == "1":
        return

    probability = flake_probability(probability)

    if random.random() < probability:
        pytest.fail(
            f"Demo flaky failure ({probability * 100:.1f}% chance): {reason}"
        )
