from instruction import Instruction


class Grid:
    def __init__(self):
        self.matrix: [[GridCell]] = [[]]

    def execute_instruction(self, instruction: Instruction):
        """
        Takes an instruction and executes it by moving the head and then the tail x number of times
        :param instruction: An instruction with a direction and a distance
        """
        print(f"The instruction is to move {instruction.distance} in the direction {instruction.direction}")
        # get the current head coordinates

        if head_will_go_out_of_matrix():

        # Check that the distance and direction won't lead out of the matrix
        for n in range(instruction.distance):
            # move the head knot
            self.move_knot(knot_type="H", instruction=instruction)
            # move the tail knot
            self.move_knot(knot_type="T", instruction=instruction)


    def get_head_coordinates(self) -> [int, int]:
        for y_index, row in enumerate(self.matrix):
            for x_index, element in enumerate(row):
                if element.status == "H":
                    print()

    def head_will_go_out_of_matrix(self):
        return

    def move_knot(self, knot_type: str, instruction: Instruction):
        # add error handling for if the board isn't the right dimensions
        return

    # add empty row(s) on top
    # add empty row(s) on bottom
    # add empty row(s) to left
    # add empty row(s) on right


class GridCell:
    def __init__(self, status: str = "-", is_start: bool = False):
        self.status = status
        self.is_start = is_start
        self.tail_has_touched = False
