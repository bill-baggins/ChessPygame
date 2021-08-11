# family.py: Contains the Family class, which uses a list to hold
# multiple game game_component.

from dataclasses import dataclass
from .window import Window


@dataclass
class Family:
    """
    A simple class that contains game game_component that are related to one another
    in some way. For example, there can be a family of main menu buttons and a
    family of option menu buttons.
    """
    entities: list = None

    def init_entities(self, window: Window):
        raise NotImplementedError

    def init_entity_list(self) -> None:
        self.entities = []
        for attribute in self.__dict__.values():
            if (not str(attribute).startswith("__")
                    and not isinstance(attribute, list)
                    and attribute is not None):
                self.entities.append(attribute)