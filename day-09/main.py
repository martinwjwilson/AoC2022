from instruction import Instruction

if __name__ == '__main__':
    # Parse input into a list of moves
    f = open("test_input.txt")
    content = f.read().splitlines()
    instructions = []
    for line in content:
        split_content = line.split(" ")
        print(split_content)
        instructions.append(Instruction(direction=split_content[0], distance=int(split_content[1])))

    # To start there is a 1x1 grid (list) with the head and the tail on top of each other
    # The grid will take an instruction direction and distance, and if this will exceed the boundaries of the map then
    # Extent the grid in that direction by the required amount (current position + distance
    for instruction in instructions:
        grid.execute_instruction(instruction)
