from math import sin, cos


def matrix_product(A, B):
    """
    Computes the product of two matrices A and B.

    Args:
        A (list of list of float): The first matrix of size n x r.
        B (list of list of float): The second matrix of size r x m.

    Returns:
        list of list of float: The resulting matrix of size n x m.
    """
    n = len(A)  # Number of rows in A
    r = len(B)  # Number of rows in B (or columns in A)
    m = len(B[0])  # Number of columns in B

    # Initialize the result matrix with zeros
    mat = [[0 for _ in range(m)] for _ in range(n)]

    # Perform matrix multiplication
    for i in range(n):
        for j in range(m):
            for k in range(r):
                mat[i][j] += A[i][k] * B[k][j]  # Multiply and accumulate
    return mat


def rotation_x(angle):
    """
    Generates a 3x3 rotation matrix for rotation about the X-axis.

    Args:
        angle (float): The angle of rotation in radians.

    Returns:
        list of list of float: The 3x3 rotation matrix.
    """
    return [[1, 0, 0], [0, cos(angle), -sin(angle)], [0, sin(angle), cos(angle)]]


def rotation_y(angle):
    """
    Generates a 3x3 rotation matrix for rotation about the Y-axis.

    Args:
        angle (float): The angle of rotation in radians.

    Returns:
        list of list of float: The 3x3 rotation matrix.
    """
    return [[cos(angle), 0, sin(angle)], [0, 1, 0], [-sin(angle), 0, cos(angle)]]


def rotation_z(angle):
    """
    Generates a 3x3 rotation matrix for rotation about the Z-axis.

    Args:
        angle (float): The angle of rotation in radians.

    Returns:
        list of list of float: The 3x3 rotation matrix.
    """
    return [[cos(angle), -sin(angle), 0], [sin(angle), cos(angle), 0], [0, 0, 1]]
