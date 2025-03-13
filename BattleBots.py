import random
import time

class Action:
    """An action selected by a bot"""
    pass

class Attack(Action):
    def __init__(self, x, y, damage):
        self.x = x
        self.y = y
        self.damage = damage

class Move(Action):
    def __init__(self, direction):
        self.direction = direction

class BattleBot:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.hp = 10
        self.facing = "north"

    def get_possible_moves(self):
        return ["north", "south", "east", "west"]

    def get_attacks(self):
        """ Returns all Attacks for this bot """
        return []

    def get_actions(self, obstacles=[], bots=[]):
        """
        Returns a list of `Actions` to perform in one simulation step

        :param obstacles: List of (x, y) tuples that are not pathable
        :param bots: List of all bots in the simulation
        :return: List of `Actions` to perform

        This implementation is a simple AI to move randomly
        """
        return [Move(random.choice(self.get_possible_moves()))]

class ZapBot(BattleBot):
    def get_attacks(self):
        directions = [
            (1, 1), (1, 0), (1, -1),
            (0, 1), (0, -1),
            (-1, 1), (-1, 0), (-1, -1)
        ]
        
        return [Attack(self.x + dx, self.y + dy, 1) for dx, dy in directions]

class SmashBot(BattleBot):
    def get_attacks(self):
        directions = {
            "north": (0, -1),
            "south": (0, 1),
            "east": (1, 0),
            "west": (-1, 0)
        }
        
        dx, dy = directions.get(self.facing, (0, 0))
        
        return [Attack(self.x + dx, self.y + dy, 5)]

class FlameBot(BattleBot):
    def get_attacks(self):
        directions = {
            "north": (0, -1),
            "south": (0, 1),
            "east": (1, 0),
            "west": (-1, 0)
        }
        
        dx, dy = directions.get(self.facing, (0, 0))
        
        return [Attack(self.x + dx * i, self.y + dy * i, 3) for i in range(1, 4)]

class SuperBot(ZapBot, SmashBot, FlameBot, BattleBot):
    def get_attacks(self):
        return ZapBot.get_attacks(self) + SmashBot.get_attacks(self) + FlameBot.get_attacks(self)

class AngryBot(SuperBot):
    def get_actions(self, obstacles=[], bots=[]):
        """Always attack"""
        return self.get_attacks()
    
class MyBot(SuperBot):
    pass

class BattleArena:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.bots = []
        self.obstacles = set()
        self._create_borders()

    def _create_borders(self):
        """Create arena borders"""
        for x in range(self.width):
            self.add_obstacle(x, 0)
            self.add_obstacle(x, self.height - 1)
        for y in range(1, self.height - 1):
            self.add_obstacle(0, y)
            self.add_obstacle(self.width - 1, y)

    def add_obstacle(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.obstacles.add((x, y))

    def is_valid_position(self, x, y):
        return (x, y) not in self.obstacles

    def render(self, attacks):
        """Text-based display"""
        grid = [[" " for _ in range(self.width)] for _ in range(self.height)]

        # Add obstacles
        for x, y in self.obstacles:
            grid[y][x] = "#"

        # Add attacks
        for attack in attacks:
            grid[attack.y][attack.x] = "x"

        # Add bots
        for bot in self.bots:
            if 0 <= bot.x < self.width and 0 <= bot.y < self.height:
                grid[bot.y][bot.x] = bot.name

        # Print grid with borders
        for row in grid:
            print("".join(row))

    def run_simulation(self):
        """Main game loop"""
        round_num = 1

        while any(bot.hp > 0 for bot in self.bots):
            print(f"\nRound {round_num}:")
            for bot in self.bots:
                print(f"{bot.name} HP: {bot.hp}")
            if any(b.hp <= 0 for b in self.bots):
                break

            attacks = []
            # Process each bot's turn
            for bot in self.bots:
                actions = bot.get_actions(self.obstacles, self.bots)
                has_moved = False

                # Execute a single valid move
                for action in actions:
                    if isinstance(action, Move) and has_moved == False:
                        dxdy_map = {
                            "north": (0, -1),
                            "south": (0, +1),
                            "east": (+1, -0),
                            "west": (-1, +0),
                        }
                        dx, dy = dxdy_map[action.direction]
                        new_x = bot.x + dx
                        new_y = bot.y + dy

                        if self.is_valid_position(new_x, new_y):
                            bot.x = new_x
                            bot.y = new_y
                            bot.facing = action.direction
                            has_moved = True

                if has_moved == False:
                    for action in actions:
                        if isinstance(action, Attack):
                            attacks.append(action)
                            for bot in self.bots:
                                if bot.x == action.x and bot.y == action.y:
                                    bot.hp -= action.damage

            self.render(attacks)

            time.sleep(0.2)
            round_num += 1

print("Testing Move...")
m = Move("north")
assert isinstance(m, Action)
assert m.direction == "north"
m = Move("east")
assert m.direction == "east"

print("Testing Attack...")
a = Attack(1, 2, 3)
assert isinstance(a, Action)
assert a.x == 1
assert a.y == 2
assert a.damage == 3
a = Attack(4, 5, 6)
assert a.x == 4
assert a.y == 5
assert a.damage == 6

print("Testing ZapBot...")
z = ZapBot("Test", 2, 2)
assert isinstance(z, BattleBot)
assert isinstance(z.get_attacks(), list)
assert len(z.get_attacks()) == 8
assert isinstance(z.get_attacks()[0], Attack)
attacks = set((a.x, a.y, a.damage) for a in z.get_attacks())
expected = {
    (1, 2, 1),
    (2, 1, 1),
    (3, 3, 1),
    (1, 3, 1),
    (3, 1, 1),
    (3, 2, 1),
    (2, 3, 1),
    (1, 1, 1),
}
assert attacks == expected

print("Testing SmashBot...")
s = SmashBot("Test", 2, 2)
assert isinstance(s, BattleBot)
assert isinstance(s.get_attacks(), list)
assert len(s.get_attacks()) == 1
assert isinstance(s.get_attacks()[0], Attack)
assert s.get_attacks()[0].x == 2
assert s.get_attacks()[0].y == 1
assert s.get_attacks()[0].damage == 5
s.facing = "east"
assert s.get_attacks()[0].x == 3
assert s.get_attacks()[0].y == 2
assert s.get_attacks()[0].damage == 5
s.facing = "west"
assert s.get_attacks()[0].x == 1
assert s.get_attacks()[0].y == 2
assert s.get_attacks()[0].damage == 5
s.facing = "south"
assert s.get_attacks()[0].x == 2
assert s.get_attacks()[0].y == 3
assert s.get_attacks()[0].damage == 5


print("Testing FlameBot...")
f = FlameBot("Test", 2, 2)
assert isinstance(f, BattleBot)
assert isinstance(f.get_attacks(), list)
assert len(f.get_attacks()) == 3
assert isinstance(f.get_attacks()[0], Attack)
attacks = set((a.x, a.y, a.damage) for a in f.get_attacks())
assert attacks == {(2, 0, 3), (2, 1, 3), (2, -1, 3)}
f.facing = "east"
attacks = set((a.x, a.y, a.damage) for a in f.get_attacks())
assert attacks == {(4, 2, 3), (3, 2, 3), (5, 2, 3)}
f.facing = "west"
attacks = set((a.x, a.y, a.damage) for a in f.get_attacks())
assert attacks == {(-1, 2, 3), (1, 2, 3), (0, 2, 3)}
f.facing = "south"
attacks = set((a.x, a.y, a.damage) for a in f.get_attacks())
assert attacks == {(2, 5, 3), (2, 3, 3), (2, 4, 3)}


print("Testing SuperBot")

b = SuperBot("Test", 2, 2)
assert isinstance(b, ZapBot)
assert isinstance(b, SmashBot)
assert isinstance(b, FlameBot)
assert b.get_attacks()
assert len(b.get_attacks()) == 12
attacks = set((a.x, a.y, a.damage) for a in b.get_attacks())
expected = {
    (1, 2, 1),
    (2, 1, 1),
    (3, 3, 1),
    (2, -1, 3),
    (1, 3, 1),
    (3, 1, 1),
    (2, 1, 3),
    (3, 2, 1),
    (2, 1, 5),
    (2, 3, 1),
    (2, 0, 3),
    (1, 1, 1),
}
assert attacks == expected


if __name__ == "__main__":
    arena = BattleArena(8, 8)

    # Add obstacles
    for _ in range(2):
        arena.add_obstacle(random.randint(3, 6), random.randint(3, 6))
        arena.add_obstacle(random.randint(1, 3), random.randint(3, 6))
        arena.add_obstacle(random.randint(3, 6), random.randint(1, 3))

    arena.bots = [MyBot("B", 1, 1), AngryBot("A", 2, 2)]

    try:
        arena.run_simulation()
    except KeyboardInterrupt:
        print("\nSimulation stopped by user")
