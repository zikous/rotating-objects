import pygame
from Model.Model import *  # Import the updated Model class
from Model.ModelExamples import *

# Define a dictionary of available 3D model types
MODEL_CLASSES = {
    "Cube": Cube,
    "Tetrahedron": Tetrahedron,
    "Pyramid": Pyramid,
    "Octahedron": Octahedron,
    # Easily add more models here
}


def display_menu(screen, model_names, selected_index):
    """
    Displays the menu where the user can select a 3D model.

    Args:
        screen: Pygame screen object.
        model_names: List of model names.
        selected_index: Index of the currently selected model.
    """
    font = pygame.font.Font(None, 36)  # Set font for text

    # Menu text lines, including instructions
    menu_text = [
        "Select a model to view:",
        *[f"Press {i+1} for {name}" for i, name in enumerate(model_names)],
        "Press ESC to quit",
    ]

    screen.fill((255, 255, 255))  # Clear the screen with a white background

    # Render each menu line, highlighting the selected option
    for i, line in enumerate(menu_text):
        color = (0, 0, 0)  # Default text color: black
        if i == selected_index + 1:  # Highlight selected option
            color = (255, 0, 0)  # Highlight color: red
        text_surface = font.render(line, True, color)
        screen.blit(text_surface, (20, 30 + i * 40))  # Position menu text

    pygame.display.flip()  # Update the display


def main():
    """
    Main function for running the 3D model visualization program.
    """
    # Initialize Pygame
    pygame.init()

    # Screen dimensions and settings
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("3D Model Visualization")

    # Model settings
    SIZE = 200  # Size of the models
    ROTATION_SPEED = 0.03  # Speed of rotation for models

    # Variables for program state
    model = None  # Current model object
    model_names = list(MODEL_CLASSES.keys())  # List of model names
    selected_index = 0  # Index of the currently selected model
    in_menu = True  # Flag for whether the menu is active

    # Pygame clock to control frame rate
    clock = pygame.time.Clock()
    running = True  # Main loop control variable

    # Main program loop
    while running:
        clock.tick(60)  # Limit frame rate to 60 FPS

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Quit program
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Quit on ESC
                    running = False

                if in_menu:
                    # Navigate menu with arrow keys
                    if event.key == pygame.K_UP:  # Move up
                        selected_index = (selected_index - 1) % len(model_names)
                    if event.key == pygame.K_DOWN:  # Move down
                        selected_index = (selected_index + 1) % len(model_names)
                    if event.key == pygame.K_RETURN:  # Select model
                        model = MODEL_CLASSES[model_names[selected_index]](SIZE)
                        in_menu = False  # Switch to 3D view
                else:
                    # Handle back-to-menu input in 3D view
                    if event.key == pygame.K_b:
                        in_menu = True
                        model = None  # Reset model

        if in_menu:
            # Display the menu when active
            display_menu(screen, model_names, selected_index)
        else:
            # Handle model rotation with key presses
            keys = pygame.key.get_pressed()
            if keys[pygame.K_z] or keys[pygame.K_UP]:
                model.apply_rotation(ROTATION_SPEED, 0, 0)
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                model.apply_rotation(-ROTATION_SPEED, 0, 0)
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                model.apply_rotation(0, ROTATION_SPEED, 0)
            if keys[pygame.K_q] or keys[pygame.K_LEFT]:
                model.apply_rotation(0, -ROTATION_SPEED, 0)

            # Render the model
            screen.fill((255, 255, 255))  # Clear screen
            model.draw(screen)  # Draw the model

            # Display instructions for returning to menu
            font = pygame.font.Font(None, 36)
            back_text = font.render("Press 'B' to go back to menu", True, (0, 0, 0))
            screen.blit(back_text, (20, HEIGHT - 50))

        # Update the display
        pygame.display.flip()

    # Quit Pygame when loop exits
    pygame.quit()


if __name__ == "__main__":
    main()
