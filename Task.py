violator_songs = [
    ['a1', 4.86], 
    ['a2', 4.43],
    ['a3', 4.56],
    ['a4', 4.9],
    ['a5', 6.07],
    ['a6', 4.20],
    ['a7', 4.76],
    ['a8', 4.29],
    ['a9', 5.83]
]

number_of_songs = int(input('Сколько песен выбрать?'))
list = [input(f'Название {i+1}-й песни:') for i in range(number_of_songs)]
print(list)
# Название 1-й песни: Halo
# Название 2-й песни: Enjoy the Silence
# Название 3-й песни: Clean