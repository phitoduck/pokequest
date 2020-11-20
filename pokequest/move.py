from abc import ABC, abstractmethod
from pokequest.pokemon import Pokemon

class Move(ABC):
    def __init__(self, name, description):
        self.name
        self.description

    @abstractmethod
    def do_move(self, mover: Pokemon, target: Pokemon) -> None:
        pass