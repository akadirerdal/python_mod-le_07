#!/usr/bin/env python3
"""Abstract factory pattern: one factory builds one Creature family."""

from abc import ABC, abstractmethod

from .creature import Aquabub, Creature, Flameling, Pyrodon, Torragon


class CreatureFactory(ABC):
    """Abstract factory of a Creature family (base + evolved)."""

    label: str

    @abstractmethod
    def create_base(self) -> Creature:
        """Create the base Creature of the family."""

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Create the evolved Creature of the family."""


class FlameFactory(CreatureFactory):
    """Factory of the flame family (Flameling -> Pyrodon)."""

    label = "Flameling"

    def create_base(self) -> Creature:
        """Create the base flame Creature."""
        return Flameling()

    def create_evolved(self) -> Creature:
        """Create the evolved flame Creature."""
        return Pyrodon()


class AquaFactory(CreatureFactory):
    """Factory of the aqua family (Aquabub -> Torragon)."""

    label = "Aquabub"

    def create_base(self) -> Creature:
        """Create the base aqua Creature."""
        return Aquabub()

    def create_evolved(self) -> Creature:
        """Create the evolved aqua Creature."""
        return Torragon()
