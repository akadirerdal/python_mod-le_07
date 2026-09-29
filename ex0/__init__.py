#!/usr/bin/env python3
"""DataDeck ex0 package: only Creature factories are exposed.

Somut Creature siniflari (Flameling, Pyrodon, ...) bilerek disa
acilmaz; disaridan Creature uretmek icin fabrikalar kullanilir.
"""

from .factory import AquaFactory, FlameFactory

__all__ = ["AquaFactory", "FlameFactory"]
