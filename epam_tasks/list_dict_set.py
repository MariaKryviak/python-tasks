# Number
print("___Task Number___")
a = 1
b = 2
print((12 * a + 25 * b) / (1 + a ** (2 ** b)))
print("______\n")

# String
print("___Task String___")


def get_numerator(a):
    return int(str(a).split('/')[0])


def get_denominator(a):
    return int(str(a).split('/')[1])


def calculate_numerator(a, b):
    return sum([a, b])


def find_number_to_reduce(numerator, denominator):
    if numerator % denominator == 0:
        return denominator
    return int(numerator % denominator)


def get_reduced_value(reduce, numb_):
    return int(numb_ / reduce)


def print_fractions(numerator, denominator):
    print(f"{numerator}/{denominator}")


def get_fractions(a_b, c_b):
    denominator = get_denominator(a_b)
    a = get_numerator(a_b)
    b = get_numerator(c_b)
    numerator = calculate_numerator(a, b)
    reduce = find_number_to_reduce(numerator, denominator)
    numerator = get_reduced_value(reduce, numerator)
    denominator = get_reduced_value(reduce, denominator)
    print_fractions(numerator, denominator)


a_b = '1/3'
c_b = '5/3'
get_fractions(a_b, c_b)
print("______\n")

# List
print("___Task List___")
colors = ('red', 'white', 'black', 'red', 'green', 'black')
print(set(colors))
non_repeating_colors = []
for color in colors:
    if colors.count(color) == 1:
        non_repeating_colors.append(color)
print("Non-repeating colors:\n", non_repeating_colors, "\n______\n")

# Tuple
print("___Task Tuple___")


def get_tuple(a):
    return tuple([int(x) for x in str(a)])


print(get_tuple(87178291199), "\n______\n")

# Dictionaries
print("___Task Dictionaries___")
input_ = 'Oh, it is python'
input_ = input_.lower()
output_ = dict()
for i in input_:
    y = input_.count(i)
    output_.update({i: input_.count(i)})
    input_.replace(i, '')
print(output_, "\n______\n")

print("____Task Final___")
diction_val = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
               {"VIII": "S007"}]
all_values_set = set()
for map_ in diction_val:
    for value in map_.values():
        all_values_set.add(value)
print(all_values_set)

# Print only non-repeating values
all_values = []
non_repeating_values = set()
for map_ in diction_val:
    for key, value in map_.items():
        all_values.append(value)
for value in all_values:
    if all_values.count(value) == 1:
        non_repeating_values.add(value)
print("Non-repeating values:\n", non_repeating_values, "\n______\n")

# Task Function
print("___Task Function___")


def generate_squares(range_):
    nums_dict = dict()
    for x in range(1, range_ + 1):
        nums_dict.update({x: x * x})
    return nums_dict


num = 5
# print(*f"Squares of {num} is {generate_squares(num)}\n______\n", sep=" ")
print(f"Squares of {num} is {generate_squares(num)}\n______\n")


# Task # 2
def odd_n(a) -> dict:
    odd_list = []
    for k in a.keys():
        if k % 2 == 0:
            odd_list.append(k)
    return {tuple(odd_list): sum(odd_list)}


a = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7}
print(odd_n(a))


def get_pairs(list_n):
    new_list = []
    for x in list_n:
        index_of_el = list_n.index(x)
        if index_of_el != 0:
            new_list.append(tuple((list_n[index_of_el - 1], list_n[index_of_el])))
    return new_list


print(get_pairs(['need', 'to', 'sleep', 'more']))
