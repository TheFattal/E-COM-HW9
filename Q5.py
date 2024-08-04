# 5:
cities = ["Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]
print("The cities list is:", cities)

# a:
cities.sort(key=lambda city: len(city))
print("Sorted by length:", cities)

# b:
cities.sort(key=lambda city: city[-1])
print("Sorted by last letter:", cities)

# c:
cities.sort(key=lambda city: city[::-1])
print("Sorted reversed:", cities)

