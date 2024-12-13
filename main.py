import pygame
from Model import *  # Make sure to import the updated Model class

# Define a list of model types
MODEL_CLASSES = {
    "Cube": Cube,
    "Tetrahedron": Tetrahedron,
    "Pyramid": Pyramid,
    "Octahedron": Octahedron,
    # You can easily add new models here
}


def display_menu(screen, model_names, selected_index):
    font = pygame.font.Font(None, 36)
    menu_text = [
        "Select a model to view:",
        *[f"Press {i+1} for {name}" for i, name in enumerate(model_names)],
        "Press ESC to quit",
    ]

    screen.fill((255, 255, 255))  # Fill screen with white background

    # Highlight the selected model
    for i, line in enumerate(menu_text):
        color = (0, 0, 0)
        if i == selected_index + 1:  # Highlight the selected option
            color = (255, 0, 0)  # Red color for the selected option
        text_surface = font.render(line, True, color)
        screen.blit(text_surface, (20, 30 + i * 40))

    pygame.display.flip()


def main():
    pygame.init()

    WIDTH = 800
    HEIGHT = 600
    screen_size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("3D Model Visualization")

    SIZE = 200
    ROTATION_SPEED = 0.03
    model = None  # Start with no model
    model_names = list(MODEL_CLASSES.keys())  # Get the names of the models
    selected_index = 0  # Initially, the first model is selected

    clock = pygame.time.Clock()
    running = True
    in_menu = True  # Flag to check if we are in the menu or viewing the model

    while running:
        clock.tick(60)  # Limit the frame rate to 60 FPS

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                # Handle model selection using arrow keys
                if in_menu:
                    if event.key == pygame.K_UP:  # Move up in the menu
                        selected_index = (selected_index - 1) % len(model_names)
                    if event.key == pygame.K_DOWN:  # Move down in the menu
                        selected_index = (selected_index + 1) % len(model_names)
                    # Handle Enter key for model selection
                    if event.key == pygame.K_RETURN:
                        model = MODEL_CLASSES[model_names[selected_index]](SIZE)
                        in_menu = False  # Switch to 3D view
                else:  # Handle rotation and back to menu when viewing the model
                    if event.key == pygame.K_b:  # Back to menu
                        in_menu = True
                        model = None  # Reset model

        if in_menu:
            display_menu(
                screen, model_names, selected_index
            )  # Show the menu if no model is selected
        else:
            # Handle continuous key press for rotation
            keys = pygame.key.get_pressed()
            if keys[pygame.K_z] or keys[pygame.K_UP]:
                model.apply_rotation(ROTATION_SPEED, 0, 0)
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                model.apply_rotation(-ROTATION_SPEED, 0, 0)
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                model.apply_rotation(0, ROTATION_SPEED, 0)
            if keys[pygame.K_q] or keys[pygame.K_LEFT]:
                model.apply_rotation(0, -ROTATION_SPEED, 0)

            # Draw the model
            screen.fill((255, 255, 255))  # Fill screen with white background
            model.draw(screen)

            # Display a "Back to Menu" instruction
            font = pygame.font.Font(None, 36)
            back_text = font.render("Press 'B' to go back to menu", True, (0, 0, 0))
            screen.blit(back_text, (20, HEIGHT - 50))

        pygame.display.flip()  # Update the display

    pygame.quit()


if __name__ == "__main__":
    main()
