# ввод плейлиста
def input_playlist():
    number_of_songs = int(input('Сколько песен выбрать? '))
    list = [input(f'Название {i+1}-й песни: ') for i in range(number_of_songs)]
    return list

# считаем время
def time_playlist(pl):
    count_time = 0
    violator_songs = [['s1', 4.86], ['s2', 4.43], ['s3', 4.56], ['s4', 4.9], ['s5', 6.07],
    ['s6', 4.20], ['s7', 4.76], ['s8', 4.29], ['s9', 5.83]]

    for song_number in range(len(pl)):
        for song_time in range(len(violator_songs)):
            if pl[song_number] in violator_songs[song_time][0]:
                count_time += float(violator_songs[song_time][1])
    return count_time

play_list = input_playlist()
time = time_playlist(play_list)

print(f'Общее время звучания песен: {round(time, 2)} минуты')
