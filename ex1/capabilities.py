#!/usr/bin/env python3
"""Capability interfaces, independent from the Creature hierarchy."""

from abc import ABC, abstractmethod


class HealCapability(ABC):
    """Abstract interface of the Creatures that can heal."""

    @abstractmethod
    def heal(self) -> str:
        """Return the heal message of the Creature."""


class TransformCapability(ABC):
    """Abstract interface of the Creatures that can transform."""

    # Kalici durum: transform() True yapar, revert() False'a döndürür.
    # Bu bayrak, bu capability ile birlesen Creature'larin attack()
    # davranisini degistirir.
    transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        """Return the transform message of the Creature."""

    @abstractmethod
    def revert(self) -> str:
        """Return the revert message of the Creature."""
