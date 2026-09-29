#!/usr/bin/env python3
"""Test script for the ex2 package: tournament of strategies."""

from ex0.creature import Creature
from ex0.factory import AquaFactory, CreatureFactory, FlameFactory
from ex1.factory import HealingCreatureFactory, TransformCreatureFactory
from ex2.strategy import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
    NormalStrategy,
)

Opponent = tuple[CreatureFactory, BattleStrategy]
Tournament = tuple[str, list[Opponent]]


def battle(opponents: list[Opponent]) -> None:
    """Make each opponent fight once all the other opponents."""
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    roster: list[tuple[Creature, BattleStrategy]] = [
        (factory.create_base(), strategy) for factory, strategy in opponents
    ]
    try:
        for first in range(len(roster)):
            for second in range(first + 1, len(roster)):
                first_creature, first_strategy = roster[first]
                second_creature, second_strategy = roster[second]
                print("* Battle *")
                print(first_creature.describe())
                print("vs.")
                print(second_creature.describe())
                print("now fight!")
                first_strategy.act(first_creature)
                second_strategy.act(second_creature)
    except InvalidStrategyError as error:
        print(f"Battle error, aborting tournament: {error}")


def format_opponents(opponents: list[Opponent]) -> str:
    """Return the summary line listing every opponent of a tournament."""
    parts: list[str] = []
    for factory, strategy in opponents:
        name = type(strategy).__name__.replace("Strategy", "")
        parts.append(f"({factory.label}+{name})")
    return "[ " + ", ".join(parts) + " ]"


def main() -> None:
    """Create the factories, the strategies and run the tournaments."""
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()
    flame = FlameFactory()
    aqua = AquaFactory()
    healing = HealingCreatureFactory()
    transform = TransformCreatureFactory()
    tournaments: list[Tournament] = [
        ("basic", [(flame, normal), (healing, defensive)]),
        ("error", [(flame, aggressive), (healing, defensive)]),
        (
            "multiple",
            [(aqua, normal), (healing, defensive), (transform, aggressive)],
        ),
    ]
    for index, (label, opponents) in enumerate(tournaments):
        print(f"Tournament {index} ({label})")
        print(format_opponents(opponents))
        battle(opponents)


if __name__ == "__main__":
    main()
