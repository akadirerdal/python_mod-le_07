#!/usr/bin/env python3
"""Abstract Creature base class and the flame/aqua Creature families."""

from abc import ABC, abstractmethod


class Creature(ABC):
    """Abstract Creature card: a name, a type and an abstract attack."""

    def __init__(self, name: str, creature_type: str) -> None:
        """Store the name and the type of the Creature."""
        self.name = name
        self.type = creature_type
        # Kooperatif super zinciri: capability mixin'leri (ex1) kendi
        # durumlarını buradan sonra kurabilsin. ex0'da object'e gider.
        super().__init__()

    @abstractmethod
    def attack(self) -> str:
        """Return the attack message of the Creature."""

    def describe(self) -> str:
        """Return the standard description of the Creature."""
        return f"{self.name} is a {self.type} type Creature"


class Flameling(Creature):
    """Base Creature of the flame family."""

    def __init__(self) -> None:
        """Build a Flameling."""
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        """Return the Flameling attack message."""
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    """Evolved Creature of the flame family."""

    def __init__(self) -> None:
        """Build a Pyrodon."""
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        """Return the Pyrodon attack message."""
        return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):
    """Base Creature of the aqua family."""

    def __init__(self) -> None:
        """Build an Aquabub."""
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        """Return the Aquabub attack message."""
        return "Aquabub uses Water Gun!"


class Torragon(Creature):
    """Evolved Creature of the aqua family."""

    def __init__(self) -> None:
        """Build a Torragon."""
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        """Return the Torragon attack message."""
        return "Torragon uses Hydro Pump!"
