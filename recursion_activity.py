
def recursive_sum(numbers):
    if len(numbers) == 0:
        return 0

    return numbers[0] + recursive_sum(numbers[1:])


def find_largest(numbers):
    if len(numbers) == 0:
        raise ValueError("Array must not be empty")

    if len(numbers) == 1:
        return numbers[0]

    largest_rest = find_largest(numbers[1:])

    if numbers[0] > largest_rest:
        return numbers[0]
    else:
        return largest_rest


def count_number(numbers, target):
    if len(numbers) == 0:
        return 0

    if numbers[0] == target:
        return 1 + count_number(numbers[1:], target)
    else:
        return count_number(numbers[1:], target)


print("1. Sum the Array")
print(recursive_sum([]))
print(recursive_sum([10]))
print(recursive_sum([5, 10, 15]))
print(recursive_sum([5, -2, 10, -3]))

print("\n2. Find the Largest Number")
print(find_largest([10]))
print(find_largest([20, 5, 10]))
print(find_largest([5, 10, 20]))
print(find_largest([-5, -2, -10]))

print("\n3. Count a Chosen Number")
print(count_number([], 5))
print(count_number([5, 2, 5, 3, 5], 5))
print(count_number([1, 2, 3, 4], 5))
