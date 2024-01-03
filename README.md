# Snake Game with Reinforcement Learning
## Teach AI to play Snake Game using deep Q-Learning

A Snake game-playing agent implemented using a Deep Q-Network (DQN) reinforcement learning approach. The agent learns to play the Snake game by training on the game environment and updating its Q-network.

## Getting Started

### Prerequisites

- Python 3.x
- PyTorch 
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

3. Monitor the training progress and results in the console output.
4. To play snake game, run ```snake_game_human.py```
   ```bash
   python ./snake_game_human.py
   ```

## Project Structure

- `train.py`: Main script for training the Snake game-playing agent.
- `game.py`: Custom module containing the Snake game logic.
- `model.py`: Custom module defining the Q-network and training process.
- `helper.py`: Custom module with helper functions, including plotting.
- `bestscore.txt`: Text file storing the best score achieved by the agent.
- `model/`: Directory to store saved models.
- `snake_game_human.py`: Snake game 

## Training

The Neural Network is implemented in `train.py`. The agent collects experiences, updates its Q-network, and saves the best model.

## Results

- The best score achieved by the agent is stored in `bestscore.txt`.
- Current and average scores are plotted after each game.
- Models with the highest scores are saved in the `model/` directory.
- Screenshot of trining:
  ![image](https://github.com/kunalarora0930/snake-game-reinforcement-learning/assets/90236283/39429354-2102-48e1-943a-f6c12cc3bb0e)


