class Group:
    def __init__(self, bags):
        self.bags = bags
        self.badge = self.badge_item()

    # I want to be physically sick looking at this...
    def badge_item(self) -> int:
        previous_bag_contents = None
        matched_contents = []
        for bag in self.bags:
            if previous_bag_contents is not None:
                for item in bag.contents:
                    if item in previous_bag_contents:
                        matched_contents.append(item)
                previous_bag_contents = matched_contents
                matched_contents = []
            else:
                previous_bag_contents = bag.contents
        return previous_bag_contents[0]


class Bag:
    def __init__(self, content_string: str):
        self.contents = self.convert_content_string(content_string)
        self.first_compartment = self.contents[:int(len(self.contents)/2)]
        self.second_compartment = self.contents[int(len(self.contents)/2):]
        self.duplicated_item = self.find_matching_elements()

    def convert_content_string(self, content_string: str) -> [int]:
        content_numbers = []
        for letter in content_string:
            content_numbers.append(self.convert_letter_to_int(letter))
        return content_numbers

    def find_matching_elements(self) -> int:
        for number in self.first_compartment:
            if number in self.second_compartment:
                return number

    @staticmethod
    def convert_letter_to_int(letter: str) -> int:
        # write a unit test for this where a gives 1, b gives 2, and a capital
        amount_to_subtract = 0
        if letter.isupper():
            amount_to_subtract = 38
        else:
            amount_to_subtract = 96
        return ord(letter) - amount_to_subtract


# Open input file
f = open("input.txt")
content = f.read().split("\n")

# get list of bags
list_of_bags = []
for line in content:
    list_of_bags.append(Bag(line))

# get a list of groups
list_of_groups = []
next_bag_index = 0
while next_bag_index < len(list_of_bags):
    bags = list_of_bags[next_bag_index:next_bag_index+3]
    list_of_groups.append(Group(bags))
    next_bag_index += 3

# get sum of group badges
group_badge_total = 0
for group in list_of_groups:
    print(group.badge)
    group_badge_total += group.badge
print(group_badge_total)
