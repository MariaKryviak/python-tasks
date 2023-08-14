# Task 1
# Create a function that takes two parameters of string type which are fractions with the same denominator
# and returns a sum expression of these fractions and the sum result.
# get_fractions('1/3', '5/3') -> str Output: '1/3 + 5/3 = 6/3'
# get_fractions('1/2', '5/3') -> str Output: '1/2 + 5/3 = 13/6'
def get_fractions(a_b, c_b):
    a_b_numerator, a_b_denominator = a_b.split('/')
    c_b_numerator, c_b_denominator = c_b.split('/')
    a_b_denominator = int(a_b_denominator)
    c_b_denominator = int(c_b_denominator)

    denominator = max(a_b_denominator, c_b_denominator)
    while denominator % min(a_b_denominator, c_b_denominator) != 0:
        denominator = denominator * min(a_b_denominator, c_b_denominator)
    a_b_new_numerator = denominator / a_b_denominator * int(a_b_numerator)
    c_b_new_numerator = denominator / c_b_denominator * int(c_b_numerator)
    numerator = int(a_b_new_numerator + c_b_new_numerator)
    print(f"{a_b} + {c_b} = {numerator}/{denominator}")


get_fractions('1/3', '5/3')
get_fractions('1/2', '5/3')
get_fractions('1/8', '5/3')


# Task 2
# Define the sum of dict values which have odd dict key.
# Function should return the list of values and sum of these values.
# odd_n({1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7}) Output: ([2, 4, 6], 12)
def odd_n(a) -> dict:
    odd_list = []
    for k in a.keys():
        if k % 2 != 0:
            odd_list.append(a.get(k))
    return {tuple(odd_list): sum(odd_list)}


a = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7}
print(odd_n(a))


# Task 3
# Implement a function get_pairs(lst: List) -> List[Tuple] which returns a list of tuples containing pairs of elements.
# The pairs should be formed as in the example. If there is only one element in the list, return [] instead.
def get_pairs(list_n):
    new_list = []
    for x in list_n:
        index_of_el = list_n.index(x)
        if index_of_el != 0:
            new_list.append(tuple((list_n[index_of_el - 1], list_n[index_of_el])))
    return new_list


print(get_pairs([1, 2, 3, 8, 9]))
print(get_pairs(['need', 'to', 'sleep', 'more']))
print(get_pairs([1]))
