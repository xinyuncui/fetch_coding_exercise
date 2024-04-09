import random

class Game:
    def __init__(self, fake_position):
        """
        Initialize the game with the position of the fake gold bar and setup initial variables.
        """
        self.fake_position = fake_position
        self.weights = [1] * 9
        self.weights[self.fake_position] = 0
        self.left_bowl = []
        self.right_bowl = []
        self.weighing_list = []

    def fill_bowls(self, left, right):  
        """
        Fill the left and right bowls with the specified gold bar numbers.
        """ 
        self.left_bowl = left
        self.right_bowl = right
   
    def reset (self):
        """
        Reset the bowls to empty for the next weighing.
        """
        self.left_bowl = []
        self.right_bowl = []
    
    def weigh(self):
        """
        Weigh the gold bars on the scale and determine if the left side is heavier, lighter, or equal to the right side.
        """
        left_weights, right_weights = 0 , 0
        for i in self.left_bowl:
            left_weights += self.weights[i]
        for i in self.right_bowl:
            right_weights += self.weights[i]

        if left_weights > right_weights:
            res = ">"    
        elif left_weights < right_weights:
            res = "<"
        else:
            res = "="
        self.weighing_list.append(str(self.left_bowl)+ " " + res + " " + str(self.right_bowl))
        return res
    
    def get_weighing_list(self):
        """
        Output the list of weighings made during the game.
        """
        for i, weighning in enumerate(self.weighing_list):
            print(str(i+1) + " " + weighning)

    def click_gold_bar(self, number):
        """
        Check if the clicked gold bar number matches the fake gold bar position.
        """
        if number == self.fake_position:
            print("Yay! You found it!")
        else:
            print("Oops! Try Again!")


def find_fake_position(game):
    """
    Implement the binary search algorithm to find the fake gold bar position.
    """
    low = 0
    high = 8
    while low < high:
        mid = (low + high + 1) // 2
        game.fill_bowls( [i for i in range(low, mid)], [i for i in range(mid, high + 1)])
        res = game.weigh()
        if res == ">" or res == "=":
            low = mid 
        else:
            high = mid - 1
        game.get_weighing_list()
        game.reset()
    game.click_gold_bar(high)
    return


if __name__ == "__main__":
    # Generate a random position for the fake gold bar
    fake_position = random.randint(0,8)
    print("A test case for fake gold bar at position: " + str(fake_position))
    # Initialize the game with the fake gold bar position
    game = Game(fake_position)
    # Find the position of the fake gold bar using the binary search algorithm
    find_fake_position(game)
  