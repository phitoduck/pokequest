from abc import ABC, abstractmethod
from typing import List
from pokequest.move import Move

class Pokemon(ABC):
    def __init__(self, max_health, moves: List[Move]):
        self.max_health = max_health # save the max health
        self.health = max_health # start off at full health
        self.moves = []