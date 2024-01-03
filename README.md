# AI Snake Game
## Teach AI to play Snake Game using deep Q-Learning


# Snake Game AI with Deep Q-Network (DQN)

## Overview

This repository contains a Snake game-playing agent implemented using a Deep Q-Network (DQN) reinforcement learning approach. The agent learns to play the Snake game by training on the game environment and updating its Q-network.

## Getting Started



### Prerequisites

- Python 3.x
- PyTorch (install via `pip install torch`)
- Conda 

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/kunalarora0930/snake-game-ai.git
   cd snake-game-ai
   ```

2. Install dependencies:
    Create conda environment from backup
   ```bash
    conda env create -f environment_snake.yml
   ```

## Usage
1. Activate ```snake``` virtual environment
    ```bash
    conda activate snake
    ```
2. Run the agent:

   ```bash
   python agent.py
   ```

   This will start the loop for the Snake game playing agent.

2. Monitor the training progress and results in the console output.

## Project Structure

- `train.py`: Main script for training the Snake game-playing agent.
- `game.py`: Custom module containing the Snake game logic.
- `model.py`: Custom module defining the Q-network and training process.
- `helper.py`: Custom module with helper functions, including plotting.
- `bestscore.txt`: Text file storing the best score achieved by the agent.
- `model/`: Directory to store saved models.

## Training

The training script (`train.py`) implements the main training loop. The agent collects experiences, updates its Q-network, and saves the best model.

## Results

- The best score achieved by the agent is stored in `bestscore.txt`.
- Models with the highest scores are saved in the `model/` directory.

