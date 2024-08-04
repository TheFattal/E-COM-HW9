# 3:
import random

random_list = [random.randint(-50, 50) for _ in range(20)]
print("The random list is:\n", random_list)

# a:
print('Elements power 3 are:\n', list(map(lambda x: x ** 3, random_list)))

# b:
print('Elements ones digit:\n', list(map(lambda x: x % 10 if x > 0 else x * (-1) % 10, random_list)))

# c:
print('Elements in Fahrenheit are:\n', list(map(lambda x: f"{x * 1.8 + 32:.2f}", random_list)))

# d:
print('Do elements are positive or negative?\n', list(map(lambda x: "Positive" if x > 0 else "Negative", random_list)))

# e:
max_num = max(random_list)
min_num = min(random_list)
update_list = list(map(lambda x: "Max" if x == max_num else "Min" if x == min_num else x, random_list))
print('MIN or MAX?\n', update_list)

# g:
update_list = list(map(lambda x: x * (-1) if x < 0 else x, random_list))
print('ABS list is:\n', update_list)
