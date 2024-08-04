# 1:
games = ["Fortnite", "Grand Theft Auto V", "The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch"]

# a:
filtered_games = list(filter(lambda x: len(x) > 8, games))
print(f"Games that have more than 8 letters:\n{filtered_games}")

# b:
filtered_games = list(filter(lambda x: x.startswith('F'), games))
print(f"Games that start with F letter are:\n{filtered_games}")

# c:
filtered_games = list(filter(lambda x: len(x.split()) == 2, games))
print(f"Games that have exactly 2 words are:\n{filtered_games}")

# d:
filtered_games = list(filter(lambda x: 'V' in x, games))
print(f"Games that have letter V in them:\n{filtered_games}")

# g:
special_characters = set('@#!$%^&*()_+[]{}|;:,.<>?/~`')
filtered_games = list(filter(lambda game: any(char in special_characters for char in game), games))
print(f"Games that have special characters in them are:\n{filtered_games}")
