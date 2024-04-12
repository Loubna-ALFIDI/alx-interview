#!/usr/bin/python3
""" Pascal Triangle """


def pascal_triangle(n):
    """
    Pascal triangle
    """
    if n <= 0:
        return []
    triangle = [[1]]
    while len(triangle) != n:
        temp = [1]
        for i in range(len(triangle[-1]) - 1):
            temp.append(triangle[-1][i] + triangle[-1][i + 1])
        temp.append(1)
        triangle.append(temp)
    return triangle
