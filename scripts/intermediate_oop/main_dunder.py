from dunder import ReverseView

numbers = [2, 1, 3, 4, 7, 11]
reverse_numbers = ReverseView(numbers)

print(list(reverse_numbers))
# [11, 7, 4, 3, 1, 2]

print(str(reverse_numbers))
# '[11, 7, 4, 3, 1, 2]'

print(reverse_numbers[0])
# 11

print(reverse_numbers[-1])
# 2

print(len(reverse_numbers))
# 6


numbers.append(18)

print(list(reverse_numbers))
# [18, 11, 7, 4, 3, 1, 2]
