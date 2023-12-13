# A Pong Game with Reinforced Q-Learning

This repository contains a simple implementation of the classic Pong game using the Q-learning algorithm for reinforcement learning. In this game, the left paddle is controlled by a computer player using random actions, while the right paddle is controlled by a model using a Q-learning algorithm.

**Note** The Q-learning model gets more precise as more game states are iterated through.

## Background

Pong is a two-player sports game that simulates table tennis. Players control paddles on either side of the screen, and they use the paddles to strike a ball back and forth. The goal is to score points by making the ball pass the opponent's paddle, or in this cae, past the player's line of bounds.

## Q-Learning Algorithm

The Q-learning algorithm is a model-free reinforcement learning algorithm. In the context of this Pong game, the Q-table is initialized with random values and is updated every time the ball is hit. The state is represented by a tuple of five variables: ball x-coordinate, ball y-coordinate, paddle 1 y-coordinate, paddle 2 y-coordinate, and ball direction (dx and dy).

The reward is calculated as the difference between the scores of the two players and is used to update the Q-table using the following formula:

```python
Q(s, a) += alpha * (reward + gamma * max(Q(s', a')) - Q(s, a))

where:

's' is the current state
'a' is the action taken
's'' is the new state after taking the action
'alpha' is the learning rate
'gamma' is the discount factor