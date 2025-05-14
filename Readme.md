# Flappy Bird Clone

This is a game create following this tutorial 
https://www.youtube.com/watch?v=POelpwwqxek&list=PLI8CnIMh7oBFN3cx8k_GsBYIRovhKi2gz

## Installation

1. Make sure you have Python installed. You can download it from [python.org](https://www.python.org/).
2. Install Pygame by running the following command:

    ```sh
    pip install pygame
    ```

## How to Start Game

Run the game by executing the index.py file:

```sh
python index.py
```

## Game Command

1. Use the `UP` arrow key to make the bird fly.
2. Avoid the pipes and try to get the highest score possible.
3. Use `Space` for restart game
3. Press `ESC` to quit the game.

## Code Overview

- index.py: The main game file containing the game logic and functions.
- `img/`: Directory containing the images used in the game.

## Functions

- inizializza(): Initializes the game state.
- draw_object(): Draws the game objects on the screen.
- refresh(): Refreshes the game screen.
- looser(): Handles the game over state.

## Classes

- pipe_class: Represents a pipe in the game. Contains methods for pipe movement and collision detection.
