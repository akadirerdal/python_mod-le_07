#!/usr/bin/env python3
"""Abstract strategy pattern: how a Creature acts in the tournament."""

from abc import ABC, abstractmethod

from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    """Raised when a strategy is used with an unsuitable Creature."""


class BattleStrategy(ABC):
    """Abstract strategy of the tournament battles."""

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Return True when the Creature suits this strategy."""

    @abstractmethod
    def act(self, creature: Creature) -> None:
        """Make the Creature act according to this strategy."""


class NormalStrategy(BattleStrategy):
    """Strategy that suits any Creature: it simply attacks."""

    def is_valid(self, creature: Creature) -> bool:
        """Any Creature can fight normally."""
        return True

    def act(self, creature: Creature) -> None:
        """Attack with the Creature."""
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    """Strategy that suits the Creatures with transform capability."""

    def is_valid(self, creature: Creature) -> bool:
        """Only a Creature with the transform capability suits."""
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        """Transform, attack and revert with the Creature."""
        # isinstance hem gecerlilik kontrolu hem de mypy icin tip
        # daraltmasi (narrowing) saglar: asagida transform()/revert()
        # yalnizca capability'nin kendisinde tanimlidir.
        if not isinstance(creature, TransformCapability):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
            )
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    """Strategy that suits the Creatures with heal capability."""

    def is_valid(self, creature: Creature) -> bool:
        """Only a Creature with the heal capability suits."""
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        """Attack and then heal with the Creature."""
        if not isinstance(creature, HealCapability):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                "for this defensive strategy"
            )
        print(creature.attack())
        print(creature.heal())
