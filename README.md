# A Pong Game with Reinforced Q-Learning

This repository contains a simple implementation of the classic Pong game using the Q-learning algorithm for reinforcement learning. In this game, the left paddle is controlled by a computer player using random actions, while the right paddle is controlled by a model using a Q-learning algorithm.

**Note** The Q-learning model gets more precise as more game states are iterated through.

## Background

Pong is a two-player sports game that simulates table tennis. Players control paddles on either side of the screen, and they use the paddles to strike a ball back and forth. The goal is to score points by making the ball pass the opponent's paddle, or in this cae, past the player's line of bounds.
<p align="center">
  <img src="https://github.com/pmoraless/pong-reinforced/blob/29fa1631bae724e1b1ebee99d924c88e0eda0179/docs/pong.gif"/>
</p>
<p>
    <em>Working Pong version. Left paddle: randomized computer Right paddle: Q-table algorithm model, Dec 2023 </em>
</p>

## Q-Learning Algorithm

The Q-learning algorithm is a reinforcement learning algorithm. In the context of this Pong game, the Q-table is initialized with random values and is updated every time the ball is hit. The state is represented by a tuple of five variables: ball x-coordinate, ball y-coordinate, paddle 1 y-coordinate, paddle 2 y-coordinate, and ball direction (dx and dy).

The reward is calculated as the difference between the scores of the two players and is used to update the Q-table using the following formula:

```python
q_table[current_state][chosen_action] += learning_rate * (reward + discount_factor * max(q_table[new_state]) - q_table[current_state][chosen_action])
```

where:

`current_state` is the snapshot of the environment at a specific point in time during the execution of the Pong game. Holds all relevant information about the positions, velocities, and other relevant attributes of the game elements, such as paddles and the ball.

`chosen_action` is the decision made by the reinforcement learning model from the set of available actions in the current state. Actions in the game include moving the paddle up, down, or taking no action.

`new_state` is the result of the environment's response to the chosen action. It represents the updated configuration of the game elements after the agent has taken a specific action in the current state.

`learning_rate` is a hyperparameter that determines the extent to which the Q-values are updated during the Q-table learning process. It controls the balance between retaining past knowledge of the states and integrating new information for the game elements.

`discount_factor` is a parameter that determines the importance of future rewards in the model's decision-making process. It discounts the value of future rewards to make them less significant than immediate rewards.

## Game Logic

- The left paddle (controlled by the computer) moves randomly up or down.
- The right paddle (controlled by the Q-learning model) chooses actions based on the Q-values.
- The ball bounces off the top and bottom walls.
- The ball reflects when it hits the left paddle, increasing the score for the left player.
- The ball reflects when it hits the right paddle, increasing the score for the right player.
- If the ball goes out of bounds on the left or right, the scores are updated, and a new round begins, as indicated via the score on the upper display.
- The game continues indefinitely until the player exits the PyGame window.

## Running the Game

To run the game, make sure you have Python and Pygame installed. 

```pip3 install pygame```
```pip3 install python3```
 
Execute the provided Python script game.py in your desired terminal. 

```python3 game.py```

**Note** Setup was tested using a Unix-based system. As such, I do not guarantee it working on another based system. 

Adjust the parameters and hyperparameters in the script to observe different behaviors of the Q-learning model.