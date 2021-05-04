"""TEMP."""

from collections import namedtuple


class RootNode:
    """Represents the root of the tree."""

    def __init__(self, name='Root'):
        """TEMP."""
        self.name = name
        self.children = []

    def __str__(self):
        """TEMP."""
        return f'{self.name}'

    def __repr__(self):
        """TEMP."""
        return f'RootNode({self.name})'
        # return repr(self.__dict__)


class Node:
    """Represents an entity capable of having properties."""

    def __init__(self, type=None, name=None, parameters=None):
        """TEMP."""
        self.type = type
        self.name = name
        self.children = []
        self.parameters = parameters

    def __eq__(self, other):
        """TEMP."""
        if other is None:
            return False
        return (
            self.type == other.type and
            self.name == other.name and
            self.parameters == other.parameters and
            set(self.children) == set(other.children)
        )

    def __str__(self):
        """TEMP."""
        return f'{" ".join(filter(None, (self.type, self.name, self.parameters)))}'

    def __repr__(self):
        """TEMP."""
        return f'Node({self.type}, {self.name}, {self.parameters})'
        # return repr(self.__dict__)


class PropertyNode:
    """Represents a property of a node."""

    def __init__(self, name=None, value=None, parameters=None):
        """TEMP."""
        self.name = name
        self.value = value
        self.parameters = parameters

    def __eq__(self, other):
        """TEMP."""
        if other is None:
            return False
        return (
            self.name == other.name and
            self.value == other.value and 
            self.parameters == other.parameters
        )

    def __str__(self):
        """TEMP."""
        return f'{" ".join(filter(None, (self.name, self.value, self.parameters)))}'
        # return f'{self.name} {self.value}'

    def __repr__(self):
        """TEMP."""
        return f'PropertyNode({self.name}, {self.value}, {self.parameters})'
        # return repr(self.__dict__)


Token = namedtuple('Token', ['type', 'value'])
