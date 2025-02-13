class Subsystem:
    """
    Class to store and manage individual ship subsystems
    """

    def __init__(self, power):
        """Constructor to set initial power consumed"""
        if power < 0:
            raise ValueError("Power cannot be negative")
    
        self._power = power

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        if value < 0:
            raise ValueError("Power cannot be negative.")
        self._power = value

    @property
    def online(self):
        return self._power > 0



sys = Subsystem(1)
assert sys.power == 1
sys.power = 3
assert sys.power == 3
try:
    sys.power = -1
except ValueError:
    pass
assert sys.power == 3
assert sys.online == True
sys.power = 0
assert sys.power == 0
assert sys.online == False


class Ship:
    """
    Class to represent a spacecraft
    """

    def __init__(self):
        """
        Constructor

        Initialize subsystems and set initial values
        """
        self._hull = 100
        self._shields = Subsystem(1)
        self._weapons = Subsystem(1)
        self._engines = Subsystem(1)
        self._reactor_output = 5
        self._subsystems = [self._shields, self._weapons, self._engines]

    def shutdown(self):
        """Shutdown all systems"""
        for subsystem in self._subsystems:
            subsystem.power = 0

    def raise_shields_to_maximum(self):
        """Move all power to the shields"""
        self.shutdown()
        self._shields.power = self._reactor_output

    def apply_damage(self, damage):
        """Applies hull damage less current shield level"""
        if self._shields.power >= damage:
            self._shields.power -= damage
        else:
            remaining_damage = damage - self._shields.power
            self._shields.power = 0
            self._hull -= remaining_damage
            if self._hull < 0:
                self._hull = 0

    def get_available_energy(self):
        """
        Return the available ship energy

        This is the reactor output minus energy used by
        subsystems
        """
        return self._reactor_output - sum(subsystem.power for subsystem in self._subsystems)
    
    @property
    def shields(self):
        return self._shields.power

    @shields.setter
    def shields(self, value):
        if value < 0 or value > self.get_available_energy() + self._shields.power:
            raise ValueError("Not enough energy available or invalid value.")
        self._shields.power = value

    @property
    def weapons(self):
        return self._weapons.power

    @weapons.setter
    def weapons(self, value):
        if value < 0 or value > self.get_available_energy() + self._weapons.power:
            raise ValueError("Not enough energy available or invalid value.")
        self._weapons.power = value

    @property
    def engines(self):
        return self._engines.power

    @engines.setter
    def engines(self, value):
        if value < 0 or value > self.get_available_energy() + self._engines.power:
            raise ValueError("Not enough energy available or invalid value.")
        self._engines.power = value


# Tests

s = Ship()
assert s._shields.power == 1
assert s._engines.power == 1
assert s._weapons.power == 1
s.shutdown()
assert s._shields.power == 0
assert s._engines.power == 0
assert s._weapons.power == 0

s = Ship()
assert s._shields.power == 1
s.raise_shields_to_maximum()
assert s._shields.power == 5
assert s._engines.power == 0
assert s._weapons.power == 0

s = Ship()
assert s._hull == 100
s.apply_damage(6)
assert s._hull == 95
s.raise_shields_to_maximum()
s.apply_damage(3)
assert s._hull == 95
s.shutdown()
s.apply_damage(4)
assert s._hull == 91

s = Ship()
assert s.get_available_energy() == 2
s.shutdown()
assert s.get_available_energy() == 5
s.raise_shields_to_maximum()
assert s.get_available_energy() == 0
s.shutdown()

s = Ship()
assert s.shields == 1
s.shields = 2
assert s.shields == 2
s.shields = 3
assert s.shields == 3
try:
    s.shields = 4
except ValueError:
    pass
assert s.shields == 3
try:
    s.shields = -2
except ValueError:
    pass
assert s.shields == 3

s = Ship()
assert s.weapons == 1
s.weapons = 2
assert s.weapons == 2
s.weapons = 3
assert s.weapons == 3
try:
    s.weapons = 4
except ValueError:
    pass
assert s.weapons == 3
try:
    s.weapons = -2
except ValueError:
    pass
assert s.weapons == 3

s = Ship()
assert s.engines == 1
s.engines = 2
assert s.engines == 2
s.engines = 3
assert s.engines == 3
try:
    s.engines = 4
except ValueError:
    pass
assert s.engines == 3
try:
    s.engines = -2
except ValueError:
    pass
assert s.engines == 3