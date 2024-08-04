# 4:
fruits = ["Apple", "Banana", "Orange", "Mango", "Strawberry", "Pineapple", "Grapes", "Watermelon"]
print("Fruits list is\n", fruits)
# a:
print('List letters backwards is:\n', list(map(lambda x: x[::-1], fruits)))

# b:
print('First letter of every element is:\n', list(map(lambda x: x[0], fruits)))

# c:
print('List in upper letters is:\n', list(map(lambda x: x.upper(), fruits)))

# d:
print('Letters length are:\n', list(map(lambda x: len(x), fruits)))

# e:
print('Adding ! to words ending s:\n', list(map(lambda x: x + "!" if x[-1] == "s" else x, fruits)))
