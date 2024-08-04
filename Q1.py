# 1:
import random
import statistics

random_numbers = [random.randint(1, 100) for _ in range(50)]
print(f"The random list is: \n{random_numbers}")

# a:
filtered_numbers = list(filter(lambda x: x > 50, random_numbers))
print(f"Numbers greater than 50 are:\n{filtered_numbers}")

# b:
filtered_numbers = list(filter(lambda x: x % 7 == 0, random_numbers))
print(f"Numbers Divisible by 7 without a remainder:\n{filtered_numbers}")

# c:
filtered_numbers = list(filter(lambda x: 10 < x < 99, random_numbers))
print(f"Only double digit numbers:\n{filtered_numbers}")

# d:
filtered_numbers = list(filter(lambda x: x // 10 == x % 10, random_numbers))
print(f"Only two-digit numbers whose ones digit is equal to its tens digit:\n{filtered_numbers}")

# e:
filtered_numbers = list(filter(lambda x: x // 10 + x % 10 == 9, random_numbers))
print(f"Only two-digit numbers whose ones digit plus the tens digit equal 9:\n{filtered_numbers}")

# f:
avg: float = sum(random_numbers) / len(random_numbers)
filtered_numbers = list(filter(lambda x: x > avg, random_numbers))
print(f"Numbers greater than the average {avg}:\n{filtered_numbers}")

# g:
max_in_list: int = max(random_numbers)
filtered_numbers = list(filter(lambda x: x > max_in_list * 0.5, random_numbers))
print(f"Numbers greater than half of the max number {max_in_list}:\n{filtered_numbers}")

# h:
sorted_numbers = sorted(random_numbers)
median = statistics.median(sorted_numbers)
greater_than_median = list(filter(lambda x: x > median, random_numbers))
print(f"Numbers greater than the median ({median}):\n{greater_than_median}")

# i:
numbers_input = list(map(int, input("Enter 5 integers separated by spaces: ").split()))
print("Input list is:", numbers_input)
updated_list = [item for item in random_numbers if item not in numbers_input]
print("Updated list:", updated_list)
