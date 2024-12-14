# Rotating Objects

This project involves creating and rendering 3D models with rotation functionality using Python and the Pygame library. The models include basic geometric shapes like cubes, tetrahedrons, pyramids, and octahedrons. The program allows for rotating these models around the x, y, and z axes and centers them on the screen for better visualization.

## Features

- **3D Models**: Includes cubes, tetrahedrons, pyramids, and octahedrons.
- **Rotation**: Models can be rotated along the x, y, and z axes.
- **Centering**: Models are centered on the screen for better visualization.
- **Gravity Center Calculation**: The gravity center is computed and models are centered based on it before transformations are applied.
- **2D Projection**: Projects 3D points to 2D for rendering on the screen.
- **UI**: Simple menu-based UI for selecting models and interacting with the 3D visualization using keyboard inputs.

## Requirements

- Python 3.x
- Pygame library

You can install Pygame with pip:

```bash
pip install pygame
```

## How to Run

1. Clone or download the repository.
2. Install the required dependencies (`Pygame`).
3. Run the application by executing `main.py`:

```bash
python main.py
```

4. The models will be rendered, and you can rotate them using the controls (e.g., keyboard arrows and keys).

### Controls

- **Arrow keys**: Rotate the model along different axes.
- **'B' key**: Go back to the main menu for selecting a new model.
- **'Enter'**: Select the currently highlighted model from the menu.
- **'Esc'**: Exit the program.
