#!/usr/bin/env python3
"""Concrete Creatures mixing the Creature base with capabilities."""

from ex0.creature import Creature

from .capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    """Base Creature of the healing family."""

    def __init__(self) -> None:
        """Build a Sproutling."""
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        """Return the Sproutling attack message."""
        return "Sproutling uses Vine Whip!"

    def heal(self) -> str:
        """Return the Sproutling heal message."""
        return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    """Evolved Creature of the healing family."""

    def __init__(self) -> None:
        """Build a Bloomelle."""
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        """Return the Bloomelle attack message."""
        return "Bloomelle uses Petal Dance!"

    def heal(self) -> str:
        """Return the Bloomelle heal message."""
        return "Bloomelle heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    """Base Creature of the transform family."""

    def __init__(self) -> None:
        """Build a Shiftling."""
        super().__init__("Shiftling", "Normal")

    def attack(self) -> str:
        """Return the attack message, boosted while transformed."""
        if self.transformed:
            return "Shiftling performs a boosted strike!"
        return "Shiftling attacks normally."

    def transform(self) -> str:
        """Shift into the sharper form and keep the state."""
        self.transformed = True
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        """Return to the normal form and keep the state."""
        self.transformed = False
        return "Shiftling returns to normal."


class Morphagon(Creature, TransformCapability):
    """Evolved Creature of the transform family."""

    def __init__(self) -> None:
        """Build a Morphagon."""
        super().__init__("Morphagon", "Normal/Dragon")

    def attack(self) -> str:
        """Return the attack message, boosted while transformed."""
        if self.transformed:
            return "Morphagon unleashes a devastating morph strike!"
        return "Morphagon attacks normally."

    def transform(self) -> str:
        """Morph into the battle form and keep the state."""
        self.transformed = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        """Stabilize the form and keep the state."""
        self.transformed = False
        return "Morphagon stabilizes its form."
