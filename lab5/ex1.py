class MealyAutomaton:
    def __init__(self):
        self.state = "S0"
        self.transitions = {
            ("S0", (0, 0)): ("S0", 0),
            ("S0", (0, 1)): ("S1", 1),
            ("S0", (1, 0)): ("S0", 0),
            ("S0", (1, 1)): ("S1", 1),
            ("S1", (0, 0)): ("S0", 0),
            ("S1", (0, 1)): ("S1", 1),
            ("S1", (1, 0)): ("S1", 1),
            ("S1", (1, 1)): ("S0", 0),
        }

    def process(self, inputs):
        for inp in inputs:
            self.state, output = self.transitions[(self.state, inp)]
            print(f"Input: {inp}, State: {self.state}, Output: {output}")

mealy = MealyAutomaton()
inputs = [(0, 1), (1, 0), (1, 1)]
mealy.process(inputs)
