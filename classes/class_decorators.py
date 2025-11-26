import uuid

class Cell:
    def __init__(self, name, x, y):
        self.id = uuid.uuid4()
        self._name = name
        self._x = x
        self._y = y

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Cell name cannot be empty")
        self._name = value

    # -------- PROPERTY (deleter) --------
    @name.deleter
    def name(self):
        print("Deleting cell name!")
        self._name = None

    @classmethod
    def from_line(cls, text):
        """
        Create a Cell from a simple text line.
        Example line:  'A1 10 20'
        """
        name, x, y = text.split()
        return cls(name, int(x), int(y))

    @staticmethod
    def manhattan_distance(c1, c2):
        """
        Static utility method: no access to class or object state.
        """
        return abs(c1._x - c2._x) + abs(c1._y - c2._y)

    def __repr__(self):
        return f"Cell({self._name}, x={self._x}, y={self._y})"



c1 = Cell("A1", 10, 20)

print(c1.name)        # getter
c1.name = "A2"        # setter
del c1.name           # deleter

c2 = Cell.from_line("B3 5 7")

dist = Cell.manhattan_distance(c1, c2)
print("Distance:", dist)
