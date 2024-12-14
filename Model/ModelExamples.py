from Model.Model import Model


class Cube(Model):
    """
    A class representing a 3D cube model.
    Inherits from the Model base class.
    """

    def create(self):
        """
        Creates the vertices of the cube.

        Returns:
            list: A list of vertices, each represented as a 3x1 matrix.
        """
        return [
            [
                [-self.size / 2],
                [-self.size / 2],
                [-self.size / 2],
            ],  # Bottom-left-back corner
            [
                [self.size / 2],
                [-self.size / 2],
                [-self.size / 2],
            ],  # Bottom-right-back corner
            [
                [-self.size / 2],
                [self.size / 2],
                [-self.size / 2],
            ],  # Top-left-back corner
            [
                [-self.size / 2],
                [-self.size / 2],
                [self.size / 2],
            ],  # Bottom-left-front corner
            [
                [self.size / 2],
                [-self.size / 2],
                [self.size / 2],
            ],  # Bottom-right-front corner
            [
                [-self.size / 2],
                [self.size / 2],
                [self.size / 2],
            ],  # Top-left-front corner
            [
                [self.size / 2],
                [self.size / 2],
                [-self.size / 2],
            ],  # Top-right-back corner
            [
                [self.size / 2],
                [self.size / 2],
                [self.size / 2],
            ],  # Top-right-front corner
        ]

    def link(self):
        """
        Defines the edges of the cube by connecting vertices.

        Returns:
            list: A list of tuples, where each tuple represents an edge.
        """
        return [
            (0, 1),
            (0, 2),
            (0, 3),  # Connections from vertex 0
            (1, 4),
            (1, 6),  # Connections from vertex 1
            (2, 6),
            (2, 5),  # Connections from vertex 2
            (3, 5),
            (3, 4),  # Connections from vertex 3
            (4, 7),  # Connections from vertex 4
            (5, 7),  # Connections from vertex 5
            (6, 7),  # Connections from vertex 6
        ]


class Tetrahedron(Model):
    """
    A class representing a 3D tetrahedron model.
    Inherits from the Model base class.
    """

    def create(self):
        """
        Creates the vertices of the tetrahedron.

        Returns:
            list: A list of vertices, each represented as a 3x1 matrix.
        """
        return [
            [[-self.size / 2], [-self.size / 2], [-self.size / 2]],  # Base vertex 1
            [[self.size / 2], [-self.size / 2], [-self.size / 2]],  # Base vertex 2
            [[self.size / 2], [self.size / 2], [-self.size / 2]],  # Base vertex 3
            [[0], [0], [self.size / 2]],  # Apex vertex
        ]

    def link(self):
        """
        Defines the edges of the tetrahedron by connecting vertices.

        Returns:
            list: A list of tuples, where each tuple represents an edge.
        """
        return [
            (0, 1),
            (1, 2),
            (2, 0),  # Base edges
            (0, 3),
            (1, 3),
            (2, 3),  # Edges connecting the apex
        ]


class Pyramid(Model):
    """
    A class representing a 3D pyramid model.
    Inherits from the Model base class.
    """

    def create(self):
        """
        Creates the vertices of the pyramid.

        Returns:
            list: A list of vertices, each represented as a 3x1 matrix.
        """
        return [
            [[-self.size / 2], [-self.size / 2], [0]],  # Base vertex 1
            [[self.size / 2], [-self.size / 2], [0]],  # Base vertex 2
            [[self.size / 2], [self.size / 2], [0]],  # Base vertex 3
            [[-self.size / 2], [self.size / 2], [0]],  # Base vertex 4
            [[0], [0], [self.size]],  # Apex vertex
        ]

    def link(self):
        """
        Defines the edges of the pyramid by connecting vertices.

        Returns:
            list: A list of tuples, where each tuple represents an edge.
        """
        return [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 0),  # Base edges
            (0, 4),
            (1, 4),
            (2, 4),
            (3, 4),  # Edges connecting the apex
        ]


class Octahedron(Model):
    """
    A class representing a 3D octahedron model.
    Inherits from the Model base class.
    """

    def create(self):
        """
        Creates the vertices of the octahedron.

        Returns:
            list: A list of vertices, each represented as a 3x1 matrix.
        """
        return [
            [[0], [0], [self.size / 2]],  # Top vertex
            [[self.size / 2], [0], [0]],  # Right vertex
            [[0], [self.size / 2], [0]],  # Front vertex
            [[-self.size / 2], [0], [0]],  # Left vertex
            [[0], [-self.size / 2], [0]],  # Back vertex
            [[0], [0], [-self.size / 2]],  # Bottom vertex
        ]

    def link(self):
        """
        Defines the edges of the octahedron by connecting vertices.

        Returns:
            list: A list of tuples, where each tuple represents an edge.
        """
        return [
            (0, 1),
            (0, 2),
            (0, 3),
            (0, 4),  # Connections from the top vertex
            (1, 2),
            (1, 5),  # Connections involving the right vertex
            (2, 3),
            (2, 5),  # Connections involving the front vertex
            (3, 4),
            (3, 5),  # Connections involving the left vertex
            (4, 1),
            (4, 5),  # Connections involving the back vertex
        ]
