from random import choice

# lists of movies and shows
options = [['Good Will Hunting', 'drama', 'movie'], ['How to Lose a Guy in 10 Days', 'goofy', 'movie'],
    ['The Godfather', 'nostalgic', 'movie'], ['Gilmore Girls', 'drama', 'show'], ['The Office', 'goofy', 'show'],
    ['How I Met Your Mother', 'nostalgic', 'show']]

# input mood/genre
print('do you want to watch a show or a movie?')
vidType = input()

print('what mood are you in?')
mood = input()

# loop through options to find one that fits the categories
for item in options:
    if item[2] == vidType and item[1] == mood:
        print('chosen ' + vidType + ': ' + item[0])

# print randomly selected movie or show
# print(choice(options))
