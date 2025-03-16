class MooreAutomaton:
    def __init__(self):
        self.state = "S0"
        self.transitions = {
            ("S0", (0, 0)): "S0",
            ("S0", (0, 1)): "S1",
            ("S0", (1, 0)): "S0",
            ("S0", (1, 1)): "S1",
            ("S1", (0, 0)): "S0",
            ("S1", (0, 1)): "S1",
            ("S1", (1, 0)): "S1",
            ("S1", (1, 1)): "S0",
        }
        self.outputs = {
            "S0": 0,
            "S1": 1,
        }
    def process(self, inputs):
        for inp in inputs:
            print(f"State: {self.state}, Output: {self.outputs[self.state]}")
            self.state = self.transitions[(self.state, inp)]
        print(f"Final State: {self.state}, Output: {self.outputs[self.state]}")  # Ultima ieșire
moore = MooreAutomaton()
inputs = [(0, 1), (1, 0), (1, 1)]
moore.process(inputs)
