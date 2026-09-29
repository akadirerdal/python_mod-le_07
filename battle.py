#!/usr/bin/env python3
"""Test script for the ex0 package: abstract creature factories."""

from ex0.factory import AquaFactory, CreatureFactory, FlameFactory


def test_factory(factory: CreatureFactory) -> None:
    """Create, describe and attack with both Creatures of a factory."""
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def battle(first: CreatureFactory, second: CreatureFactory) -> None:
    """Make the base Creatures of two factories fight each other."""
    print("Testing battle")
    first_creature = first.create_base()
    second_creature = second.create_base()
    print(first_creature.describe())
    print("vs.")
    print(second_creature.describe())
    print("fight!")
    print(first_creature.attack())
    print(second_creature.attack())


def main() -> None:
    """Run the ex0 test scenario."""
    test_factory(FlameFactory())
    test_factory(AquaFactory())
    battle(FlameFactory(), AquaFactory())


if __name__ == "__main__":
    main()
