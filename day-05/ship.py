from crate import Crate


class Ship:
    def __init__(self, crates):
        self.crates = crates

    def move(self, number_of_crates_to_move: int, from_stack: int, to_stack: int):
        print(number_of_crates_to_move)
        print(from_stack)
        print(to_stack)
        for _ in range(number_of_crates_to_move):
            print(self.crates)
            crate = self.crates[from_stack-1].pop()
            self.crates[to_stack-1].append(crate)

    def get_top_crate_letters(self) -> str:
        final_string = ""
        for section in self.crates:
            final_string += section[-1].letter
        return final_string
