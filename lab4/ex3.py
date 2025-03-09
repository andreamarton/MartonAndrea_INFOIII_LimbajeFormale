class MealyMachine:
    def __init__(self):
        self.transitions = {
            ("Q1", "X"): ("Q2", "O1"),
            ("Q1", "Y"): ("Q1", "O2"),
            ("Q2", "X"): ("Q2", "O1"),
            ("Q2", "Y"): ("Q2", "O2"),
        }
        self.current_state = "Q1"

    def process(self, inputs):
        for i in inputs:
            new_state, output = self.transitions.get((self.current_state, i), (self.current_state, ""))
            print(f"Input: {i}, New State: {new_state}, Output: {output}")
            self.current_state = new_state

mealy = MealyMachine()
mealy.process("XYXXY")
