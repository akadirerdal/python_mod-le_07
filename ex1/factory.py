#!/usr/bin/env python3
"""Factories of the Creatures with capabilities."""

from ex0.creature import Creature
from ex0.factory import CreatureFactory

from .creatures import Bloomelle, Morphagon, Shiftling, Sproutling


class HealingCreatureFactory(CreatureFactory):
    """Factory of the healing family (Sproutling -> Bloomelle)."""

    label = "Healing"

    def create_base(self) -> Creature:
        """Create the base healing Creature."""
        return Sproutling()

    def create_evolved(self) -> Creature:
        """Create the evolved healing Creature."""
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    """Factory of the transform family (Shiftling -> Morphagon)."""

    label = "Transform"

    def create_base(self) -> Creature:
        """Create the base transform Creature."""
        return Shiftling()

    def create_evolved(self) -> Creature:
        """Create the evolved transform Creature."""
        return Morphagon()
