from abc import ABC, abstractmethod
import pygame
from matrix_operations import *
from matrix_rotation import *


class Model(ABC):

    def __init__(self, size):
        self.size = size
        self.points = self.create()
        self.connections = self.link()
        self.center_gravity()

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def link(self):
        pass

    def gravity_center(self):
        n = len(self.points)
        sum_x, sum_y, sum_z = 0, 0, 0
        for point in self.points:
            sum_x += point[0][0]  # Extract x from [[x], [y], [z]]
            sum_y += point[1][0]  # Extract y
            sum_z += point[2][0]  # Extract z
        return [[sum_x / n], [sum_y / n], [sum_z / n]]

    def apply_translation(self, dx, dy, dz):
        for point in self.points:
            point[0][0] += dx
            point[1][0] += dy
            point[2][0] += dz

    def center_gravity(self):
        # Calculate the gravity center of the model
        gx, gy, gz = self.gravity_center()
        # Translate all points so the gravity center is at the origin (0, 0, 0)
        self.apply_translation(-gx[0], -gy[0], -gz[0])

    def draw(self, screen):
        # Get the center of the screen
        screen_width, screen_height = screen.get_size()
        center_x, center_y = screen_width / 2, screen_height / 2

        # Draw the points
        for point in self.points:
            pygame.draw.circle(
                screen,
                (0, 0, 0),
                (
                    int(
                        center_x + point[0][0]
                    ),  # Adjust x by adding the screen center offset
                    int(
                        center_y + point[1][0]
                    ),  # Adjust y by adding the screen center offset
                ),
                5,
            )

        # Draw the connections
        for i, j in self.connections:
            pygame.draw.line(
                screen,
                (0, 0, 0),
                (
                    int(center_x + self.points[i][0][0]),  # Adjust x for point i
                    int(center_y + self.points[i][1][0]),  # Adjust y for point i
                ),
                (
                    int(center_x + self.points[j][0][0]),  # Adjust x for point j
                    int(center_y + self.points[j][1][0]),  # Adjust y for point j
                ),
                2,
            )

    def apply_rotation(self, dx, dy, dz):
        # Apply the rotations directly on the model
        r_x = rotation_x(dx)
        r_y = rotation_y(dy)
        r_z = rotation_z(dz)
        for i in range(len(self.points)):
            self.points[i] = matrix_product(r_x, self.points[i])
            self.points[i] = matrix_product(r_y, self.points[i])
            self.points[i] = matrix_product(r_z, self.points[i])


class Cube(Model):

    def create(self):
        return [
            [[-self.size / 2], [-self.size / 2], [-self.size / 2]],  # Shift to center
            [[self.size / 2], [-self.size / 2], [-self.size / 2]],
            [[-self.size / 2], [self.size / 2], [-self.size / 2]],
            [[-self.size / 2], [-self.size / 2], [self.size / 2]],
            [[self.size / 2], [-self.size / 2], [self.size / 2]],
            [[-self.size / 2], [self.size / 2], [self.size / 2]],
            [[self.size / 2], [self.size / 2], [-self.size / 2]],
            [[self.size / 2], [self.size / 2], [self.size / 2]],
        ]

    def link(self):
        return [
            (0, 1),
            (0, 2),
            (0, 3),
            (1, 4),
            (1, 6),
            (2, 6),
            (3, 5),
            (3, 4),
            (4, 7),
            (5, 7),
            (6, 7),
            (2, 5),
        ]


class Tetrahedron(Model):

    def create(self):
        return [
            [[-self.size / 2], [-self.size / 2], [-self.size / 2]],  # Shift to center
            [[self.size / 2], [-self.size / 2], [-self.size / 2]],
            [[self.size / 2], [self.size / 2], [-self.size / 2]],
            [[0], [0], [self.size / 2]],  # Apex point, centered
        ]

    def link(self):
        return [
            (0, 1),
            (1, 2),
            (2, 0),
            (0, 3),
            (1, 3),
            (2, 3),
        ]


class Pyramid(Model):

    def create(self):
        return [
            [[-self.size / 2], [-self.size / 2], [0]],  # Base point 1
            [[self.size / 2], [-self.size / 2], [0]],  # Base point 2
            [[self.size / 2], [self.size / 2], [0]],  # Base point 3
            [[-self.size / 2], [self.size / 2], [0]],  # Base point 4
            [[0], [0], [self.size]],  # Apex point, centered
        ]

    def link(self):
        return [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 0),  # Base edges
            (0, 4),
            (1, 4),
            (2, 4),
            (3, 4),  # Sides
        ]


class Octahedron(Model):

    def create(self):
        return [
            [[0], [0], [self.size / 2]],  # Top point
            [[self.size / 2], [0], [0]],  # Right point
            [[0], [self.size / 2], [0]],  # Front point
            [[-self.size / 2], [0], [0]],  # Left point
            [[0], [-self.size / 2], [0]],  # Back point
            [[0], [0], [-self.size / 2]],  # Bottom point
        ]

    def link(self):
        return [
            (0, 1),
            (0, 2),
            (0, 3),
            (0, 4),
            (1, 2),
            (1, 5),
            (2, 3),
            (2, 5),
            (3, 4),
            (3, 5),
            (4, 1),
            (5, 4),  # Connections forming the octahedron structure
        ]
