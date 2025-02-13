import random
import time
from dataclasses import dataclass


def agent(percepts, available_actions, previous_actions, state):
    """Handle one agent turn

    :param percepts: dictionary of current percepts (sensor data)
    :param available_actions: List of valid actions
    :param previous_actions: List of all previous actions (most recent last)
    :param state: Initially empty dictionary that can be used to store
    state between calls to the agent function

    Percept descriptions

    - "obstructed" will be True if the path forward is blocked
    - "facing" will be the current direction as one of ["n", "s", "e", "w"]
    - "temp" will be a value between 1 and 100. It will increase by
    1 on each move and decrease 1 on each rest.

    Action descriptions

    "forward" will move forward 1 space
    "left" will turn to the left
    "right" will turn to the right
    "rest" will do nothing. Temperature will decrease by 1

    Returns exactly one action from list of valid actions
    """
    maxtemp = 90

    if percepts["temp"] >= maxtemp:
        return "rest"


    if percepts["obstructed"]:
        return random.choice(["forward" , "right", "left"])
    elif percepts["obstructed"] == False:
        return random.choice(["forward" , "right", "left"])
    else:
        return "forward"
        
   
    


houses = [
    """
***
*.*
*.*
*.*
*.*
***
""",
    """
****
*..*
*..*
****
""",
    """
*****
*...*
***.*
*...*
*****
""",
    """
*****
*...*
*...*
*...*
*****
""",
    """
*********
*.......*
*.......*
*.......*
*.......*
*********
""",
    """
*********
*...*...*
*...*...*
**.**...*
*.......*
*********
""",
    """
*********
*...*...*
*...*...*
**.**...*
*.......*
*.......*
**.***.**
*.......*
*.......*
*********
""",
    """
*******************
*.*..*....*.......*
*....*....*.......*
*.*..*....*.......*
*.*****.***.......*
*.................*
*...*.....*********
*.........*.......*
*......*..........*
*.........*.......*
***.*******.......*
*.........*****.***
*.........*.......*
*.........*.......*
*******************
""",
]


class Board:
    def __init__(self, definition):
        """Converts string reprentation to 2d list

        >>> Board("***\\n*.*\\n*.*\\n***")
        [['*', '*', '*'], ['*', '.', '*'], ['*', '.', '*'], ['*', '*', '*']]
        """

        self.rows = [list(r) for r in definition.strip().split("\n")]

    def get(self, pos):
        return self.rows[pos[1]][pos[0]]

    def set(self, pos, value):
        self.rows[pos[1]][pos[0]] = value

    def contains(self, char):
        """Returns True if their is dirt in the house

        >>> h = Board("***\\n*.*\\n*.*\\n***")
        >>> h.contains('.')
        True

        >>> h = Board("***\\n* *\\n* *\\n***")
        >>> h.contains('.')
        False
        """

        for row in self.rows:
            for cell in row:
                if cell == char:
                    return True

        return False

    def __repr__(self):
        return str(self.rows)


@dataclass
class Direction:
    """
    >>> Direction('n')
    Direction(name='n')

    >>> d = Direction('n')
    >>> d.turn_cw(90)
    >>> d
    Direction(name='e')

    >>> d = Direction('n')
    >>> d.move((0,0))
    (0, -1)
    """

    name: str

    def turn_cw(self, angle):
        """
        >>> d = Direction('n')
        >>> d.turn_cw(-90)
        >>> d
        Direction(name='w')
        """
        directions = "nesw"

        direction = directions.index(self.name)
        direction = (direction + int(angle / 90)) % 4

        self.name = directions[direction]

    def move(self, pos, dist=1):
        """
        >>> d = Direction('w')
        >>> d.move((3,3), 4)
        (-1, 3)

        >>> d = Direction('s')
        >>> d.move((5,5), -2)
        (5, 3)

        >>> d = Direction('n')
        >>> d.move((5,5), 2)
        (5, 3)
        """

        directions = {
            "n": (0, -1),
            "e": (1, 0),
            "s": (0, 1),
            "w": (-1, 0),
        }

        return (
            pos[0] + dist * directions[self.name][0],
            pos[1] + dist * directions[self.name][1],
        )

    def __str__(self):
        return self.name


def clean_house(house, agent, delay=0.5, limit=100000, allow_useless=True):
    house = Board(house)

    action = None
    pos = (1, 1)
    facing = Direction("s")
    temperature = 25

    house.set(pos, facing.name)

    state = {}
    previous_actions = []

    for i in range(limit):
        if delay > 0:
            print(f"Turn: {i} Temp: {temperature}")
            print(f"Completed action: {action}")
            for row in house.rows:
                print("".join(row))

            time.sleep(delay)

        if not house.contains("."):
            return i

        actions = ["left", "right", "rest"]

        if house.get(facing.move(pos)) != "*":
            actions.insert(0, "forward")

        percepts = {
            "facing": facing.name,
            "obstructed": "forward" not in actions,
            "temp": temperature,
        }

        action = agent(percepts, actions, previous_actions, state)
        previous_actions.append(action)

        all_actions = ["left", "right", "forward", "rest"]
        if action not in all_actions:
            print(f"Selected action '{action}' is not a valid action")
            print(f"Valid actions are: {all_actions}")
            exit(1)

        if not allow_useless:
            assert action in actions
        else:
            if not action in actions:
                continue

        house.set(pos, " ")

        if action == "right":
            facing.turn_cw(90)
            temperature += 1
        elif action == "left":
            facing.turn_cw(-90)
            temperature += 1
        elif action == "forward":
            pos = facing.move(pos)
            temperature += 1
        elif action == "rest":
            temperature = max(temperature - 1, 25)

        if temperature >= 100:
            print("The vacuum is on fire (it should rest to keep temp under 100)")
            return float("inf")

        house.set(pos, facing.name)

    return float("inf")


if __name__ == "__main__":
    for i, house in enumerate(houses):
        results = []

        for attempt in range(100):
            result = clean_house(house, agent, delay=0)
            results.append(result)

            if result > 100000:
                break

        average = sum(results) / len(results)

        if average < 100000:
            print(
                f"Cleaned house {i} in {average:.1f} turns on average (max {max(results)})."
            )
        else:
            clean_house(house, agent, delay=0.5)
            print(f"Took too long to clean house {i} on average")
            break