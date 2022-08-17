import collections
import random
from typing import List


class SnakeGame:
    """
        Design a Snake game that is played on a device with screen size height x width. Play the game online if you are not familiar with the game.

        The snake is initially positioned at the top left corner (0, 0) with a length of 1 unit.

        You are given an array food where food[i] = (ri, ci) is the row and column position of a piece of food that the snake can eat. When a snake eats a piece of food, its length and the game's score both increase by 1.

        Each piece of food appears one by one on the screen, meaning the second piece of food will not appear until the snake eats the first piece of food.

        When a piece of food appears on the screen, it is guaranteed that it will not appear on a block occupied by the snake.

        The game is over if the snake goes out of bounds (hits a wall) or if its head occupies a space that its body occupies after moving (i.e. a snake of length 4 cannot run into itself).

        Implement the SnakeGame class:

        SnakeGame(int width, int height, int[][] food) Initializes the object with a screen of size height x width and the positions of the food.
        int move(String direction) Returns the score of the game after applying one direction move by the snake. If the game is over, return -1.

        Example 1:

        Input
        ["SnakeGame", "move", "move", "move", "move", "move", "move"]
        [[3, 2, [[1, 2], [0, 1]]], ["R"], ["D"], ["R"], ["U"], ["L"], ["U"]]
        Output
        [null, 0, 0, 1, 1, 2, -1]

        Explanation
        SnakeGame snakeGame = new SnakeGame(3, 2, [[1, 2], [0, 1]]);
        snakeGame.move("R"); // return 0
        snakeGame.move("D"); // return 0
        snakeGame.move("R"); // return 1, snake eats the first piece of food. The second piece of food appears at (0, 1).
        snakeGame.move("U"); // return 1
        snakeGame.move("L"); // return 2, snake eats the second food. No more food appears.
        snakeGame.move("U"); // return -1, game over because snake collides with border

        Constraints:

        1 <= width, height <= 104
        1 <= food.length <= 50
        food[i].length == 2
        0 <= ri < height
        0 <= ci < width
        direction.length == 1
        direction is 'U', 'D', 'L', or 'R'.
        At most 104 calls will be made to move.
    """
    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.snake = collections.deque([(0,0)])    # snake head is at the front
        self.snakeSet = {(0,0) : 1}
        self.width = width
        self.height = height
        self.food = food
        self.foodIndex = 0
        self.directions = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        """

        newHead = (self.snake[0][0] + self.directions[direction][0],
                   self.snake[0][1] + self.directions[direction][1])

        # Boundary conditions.
        crossRowBoundary1 = newHead[0] < 0 or newHead[0] >= self.height
        crossColumnBoundary2 = newHead[1] < 0 or newHead[1] >= self.width

        # Checking if the snake bites itself.
        biteItself = newHead in self.snakeSet and newHead != self.snake[-1]

        # If any of the terminal conditions are satisfied, then we exit with rcode -1.
        if crossRowBoundary1 or crossColumnBoundary2 or biteItself:
            return -1

        # Note the food list could be empty at this point.
        nextFoodItem = self.food[self.foodIndex] if self.foodIndex < len(self.food) else None

        # If there's an available food item and it is on the cell occupied by the snake after the move, eat it
        if self.foodIndex < len(self.food) and \
                nextFoodItem[0] == newHead[0] and \
                nextFoodItem[1] == newHead[1]:  # eat food
            self.foodIndex += 1
        else:    # not eating food: delete tail
            tail = self.snake.pop()
            del self.snakeSet[tail]

        # A new head always gets added
        self.snake.appendleft(newHead)

        # Also add the head to the set
        self.snakeSet[newHead] = 1

        return len(self.snake) - 1




