#!/usr/bin/env python3
"""Test script for the ex1 package: Creature with capabilities."""

from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability
from ex1.factory import HealingCreatureFactory, TransformCreatureFactory


def test_healing(creature: Creature) -> None:
    """Describe, attack and heal a healing Creature."""
    print(creature.describe())
    print(creature.attack())
    if isinstance(creature, HealCapability):
        print(creature.heal())


def test_transform(creature: Creature) -> None:
    """Describe, attack, transform, attack again and revert."""
    print(creature.describe())
    print(creature.attack())
    if isinstance(creature, TransformCapability):
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


def main() -> None:
    """Run the ex1 test scenario."""
    healing_factory = HealingCreatureFactory()
    print("Testing Creature with healing capability")
    print("base:")
    test_healing(healing_factory.create_base())
    print("evolved:")
    test_healing(healing_factory.create_evolved())
    transform_factory = TransformCreatureFactory()
    print("Testing Creature with transform capability")
    print("base:")
    test_transform(transform_factory.create_base())
    print("evolved:")
    test_transform(transform_factory.create_evolved())


if __name__ == "__main__":
    main()
