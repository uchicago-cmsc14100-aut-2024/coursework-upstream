"""
CMSC 14100
Autumn 2024
Homework #7

Do NOT modidy this file.
"""

class Vector:
    """
    A class for representing immutable vectors.
    """
    def __init__(self, elements):
        """
        Vector Constructor

        Args:
            elements (List[int |float] | Tuple[int |float]): the elements of the vector
        """
        self.__elements = tuple(elements)


    def get_elements(self):
        """
        Returns (Tuple[int |float]): the elements as a tuple
        """
        return self.__elements


    def add(self, other):
        """
        Creates a new Vector that is the element-wise sum
        of the elements of the operands.

        Args:
            other (Vector): the second operand

        Returns (Vector): a new vector that is the
            element-wise sum of the two vectors
        """
        assert len(self) == len(other)
        elements = []
        for i, val in enumerate(self.__elements):
            elements.append(val + other.__elements[i])
        return Vector(elements)

    def scale(self, factor):
        """
        Create a new Vector with the original elements scaled by the
        specified factor.

        Args:
            factor (int |float): the factor to scale by

        Returns (Vector): a new vector with the the original elements
            scaled by the factor.
        """
        assert isinstance(factor, (float, int))
        elements = []
        for val in self.__elements:
            elements.append(val * factor)
        return Vector(elements)
        
    def __len__(self):
        """
        Returns (int): the length of the vector
        """
        return len(self.__elements)

    def __str__(self):
        """
        Returns (str): a client-facing string for the vector
        """
        # evaluating self._elements will yield the necessary parentheses
        return f"Vector{self.__elements}"
    
    def __repr__(self):
        """
        Returns (str): a developer-facing string for the vector
        """
        # evaluating self._elements will yield the necessary parentheses
        return f"Vector{self.__elements}"

    def __eq__(self, other):
        """
        Do self and other have the same values?

        Returns (bool): True, if self and other have the same
            values element-wise and False, otherwise.
        """
        if not isinstance(other, Vector):
            return False
        return self.__elements == other.__elements
    
        
        
