#!/usr/bin/python3
"""
Matrix multiplication function.
"""

def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Returns:
        list: The result of the matrix multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list or not a list of lists, or if an element is not an integer or float.
        ValueError: If m_a or m_b is empty or if matrices cannot be multiplied.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not m_a or any(not isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if any(not isinstance(element, (int, float)) for row in m_a for element in row):
        raise TypeError("m_a should contain only integers or floats")
    if any(len(row) != len(m_a[0]) for row in m_a[1:]):
        raise TypeError("each row of m_a must be of the same size")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not m_b or any(not isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")
    if any(not isinstance(element, (int, float)) for row in m_b for element in row):
        raise TypeError("m_b should contain only integers or floats")
    if any(len(row) != len(m_b[0]) for row in m_b[1:]):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]

    return result
