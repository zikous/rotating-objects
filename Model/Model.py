from abc import ABC, abstractmethod
import pygame
from Model.utils import rotation_x, rotation_y, rotation_z, matrix_product


class Model(ABC):
    """
    Abstract base class representing a 3D geometric model.
    """

    def __init__(self, size):
        """
        Initialize the model with a given size and calculate its vertices and connections.

        Args:
            size (float): The size of the model.
        """
        self.size = size
        self.points = self.create()  # Create the vertices of the model
        self.connections = (
            self.link()
        )  # Define the connections (edges) between vertices
        self.center_gravity()  # Center the model based on its center of gravity

    @abstractmethod
    def create(self):
        """
        Abstract method to define the vertices of the model.

        Returns:
            list: A list of 3x1 matrices representing the vertices.
        """
        pass

    @abstractmethod
    def link(self):
        """
        Abstract method to define the edges of the model.

        Returns:
            list: A list of tuples, where each tuple represents an edge connecting two vertices.
        """
        pass

    def gravity_center(self):
        """
        Calculate the center of gravity of the model.

        Returns:
            list: A 3x1 matrix representing the center of gravity [x, y, z].
        """
        n = len(self.points)
        sum_x, sum_y, sum_z = 0, 0, 0
        for point in self.points:
            sum_x += point[0][0]  # Extract x from [[x], [y], [z]]
            sum_y += point[1][0]  # Extract y
            sum_z += point[2][0]  # Extract z
        return [[sum_x / n], [sum_y / n], [sum_z / n]]

    def apply_translation(self, dx, dy, dz):
        """
        Translate the model by a given offset in x, y, and z directions.

        Args:
            dx (float): Offset in the x-direction.
            dy (float): Offset in the y-direction.
            dz (float): Offset in the z-direction.
        """
        for point in self.points:
            point[0][0] += dx
            point[1][0] += dy
            point[2][0] += dz

    def center_gravity(self):
        """
        Adjust the model so that its center of gravity is at the origin (0, 0, 0).
        """
        gx, gy, gz = self.gravity_center()
        self.apply_translation(-gx[0], -gy[0], -gz[0])

    def draw(self, screen):
        """
        Draw the model on a given Pygame screen.

        Args:
            screen (pygame.Surface): The Pygame surface to draw the model on.
        """
        # Get the center of the screen
        screen_width, screen_height = screen.get_size()
        center_x, center_y = screen_width / 2, screen_height / 2

        # Draw the vertices as circles
        for point in self.points:
            pygame.draw.circle(
                screen,
                (0, 0, 0),  # Black color
                (
                    int(center_x + point[0][0]),  # Adjust x with screen center
                    int(center_y + point[1][0]),  # Adjust y with screen center
                ),
                5,  # Radius of the point
            )

        # Draw the edges as lines
        for i, j in self.connections:
            pygame.draw.line(
                screen,
                (0, 0, 0),  # Black color
                (
                    int(center_x + self.points[i][0][0]),  # Adjust x for vertex i
                    int(center_y + self.points[i][1][0]),  # Adjust y for vertex i
                ),
                (
                    int(center_x + self.points[j][0][0]),  # Adjust x for vertex j
                    int(center_y + self.points[j][1][0]),  # Adjust y for vertex j
                ),
                2,  # Thickness of the line
            )

    def apply_rotation(self, dx, dy, dz):
        """
        Apply rotation to the model around the x, y, and z axes.

        Args:
            dx (float): Rotation angle around the x-axis in radians.
            dy (float): Rotation angle around the y-axis in radians.
            dz (float): Rotation angle around the z-axis in radians.
        """
        r_x = rotation_x(dx)
        r_y = rotation_y(dy)
        r_z = rotation_z(dz)

        for i in range(len(self.points)):
            self.points[i] = matrix_product(r_x, self.points[i])  # Rotate around x-axis
            self.points[i] = matrix_product(r_y, self.points[i])  # Rotate around y-axis
            self.points[i] = matrix_product(r_z, self.points[i])  # Rotate around z-axis
