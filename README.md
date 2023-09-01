# Einsteins-Riddle

This repository contains a Python script for solving Einstein's riddle, word association game. The game involves grouping words into categories and establishing relationships between them. The program creates a game tree, allowing players to explore different word associations and solve puzzles.

> Through the code in this project, I was introduced to the concept of trees and gained valuable experience in manipulating and exploring them. My task involved implementing the level-order tree traversal algorithm.
> 
> The script was developed as the [second homework assignment](instructions.pdf) for the "Algorithms and Data Structures" course at the School of Electrical Engineering, University of Belgrade, majoring in Software Engineering. 

## Features

1. **Input Data Gathering**: Users are prompted to input the number of word groups (M) and the number of words in each group (N). They can then input the words for each group.

2. **Word Association Establishment**: Users can establish word associations by entering connections between words in the format 'word1 + word2' (for connected words) or 'word1 - word2' (for disconnected words).

3. **Game Tree Creation**: The program creates a game tree to visualize the relationships between words. The tree is generated using breadth-first traversal and is displayed for users to explore.

4. **Interactive Menu**: Users are presented with an interactive menu that offers various game options, including:
   - **Uparivanje**: Matching words based on associations.
   - **Ispravnost unetih pojmova**: Checking the validity of entered words.
   - **Da li ste na dobrom putu?**: Assessing if the user is on the right track.
   - **Pomoc**: Accessing help or guidance.
   - **Nema resenja?**: Identifying situations where there may be no solution.

5. **Tree Traversal**: The code implements level-order tree traversal to display the game tree, allowing users to see the relationships between words at different depths.

## Requirements

- Python 3.x

No additional external libraries or dependencies are required to run this code. 

## Getting Started

To run the Word Association Game, follow these steps:

1. Clone the repository to your local machine.

2. Run the Python script.

3. Follow the on-screen prompts to input word groups, establish associations, and explore game options through the interactive menu.

## Note

- Some parts of the code, such as the actual game logic and implementations of certain functions, are not provided and may need to be developed further to make the game fully functional.
