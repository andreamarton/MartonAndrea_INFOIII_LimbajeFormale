class MooreMachine:
    def __init__(self):
        self.states = {"S1": "O1", "S2": "O2"}
        self.transitions = {
            ("S1", "A"): "S1",
            ("S1", "B"): "S2",
            ("S2", "A"): "S1",
            ("S2", "B"): "S2",
        }
        self.current_state = "S1"

    def process(self, inputs):
        for i in inputs:
            self.current_state = self.transitions.get((self.current_state, i), self.current_state)
            print(f"Input: {i}, New State: {self.current_state}, Output: {self.states[self.current_state]}")

moore = MooreMachine()
moore.process("AABAB")
