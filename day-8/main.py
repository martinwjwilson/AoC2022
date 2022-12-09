from tree import Tree


# Anything north of the tree is North, and the Y will be -1 of the
# When the y is +1 it will always be south
# East and west the Y coordinate will match and the x coordinate will be either < or >
def is_tree_visible(forest: [Tree], current_tree: Tree) -> bool:
    north_visible = True
    east_visible = True
    south_visible = True
    west_visible = True
    for comparison_tree in forest:
        # North
        if (comparison_tree.y < current_tree.y) and (comparison_tree.x == current_tree.x):
            if comparison_tree.height >= current_tree.height:
                north_visible = False
        # West
        if (comparison_tree.y == current_tree.y) and (comparison_tree.x < current_tree.x):
            if comparison_tree.height >= current_tree.height:
                west_visible = False
        # East
        if (comparison_tree.y == current_tree.y) and (comparison_tree.x > current_tree.x):
            if comparison_tree.height >= current_tree.height:
                east_visible = False
        # South
        if (comparison_tree.y > current_tree.y) and (comparison_tree.x == current_tree.x):
            if comparison_tree.height >= current_tree.height:
                south_visible = False
    if north_visible or east_visible or south_visible or west_visible:
        print(True)
        return True
    print(False)
    return False


def calculate_border_count(last_tree):
    return (last_tree.x + last_tree.y) * 2


def calculate_number_of_visible_trees(forest):
    total_number_of_visible_trees = 0
    # calculate number of trees on border as they're all visible
    total_number_of_visible_trees += calculate_border_count(forest[-1])
    maximum_x = forest[-1].x
    maximum_y = forest[-1].y
    tree_counter = 0
    for tree in forest:
        if (tree.x != 0) and (tree.y != 0) and (tree.x != maximum_x) and (tree.y != maximum_y):
            if is_tree_visible(forest, tree):
                tree_counter += 1
    print(f"There are {total_number_of_visible_trees + tree_counter} visible trees")


if __name__ == '__main__':
    f = open("input.txt")
    content = f.read().splitlines()
    print(content)

    forest = []
    y_coordinate = 0
    for row in content:
        x_coordinate = 0
        for element in row:
            # create a tree and give it coordinates
            forest.append(Tree(int(element), x_coordinate, y_coordinate))
            x_coordinate += 1
        y_coordinate += 1

    test_tree = forest[9]
    print(f"The height of the tree at ({test_tree.x},{test_tree.y}) = {test_tree.height}")

    calculate_number_of_visible_trees(forest)
