""" 23) Сортировка выбором
Идея - находим минимальный элемент и меняем его местами с самым первым.
Так проделываем для оставшейся части массива,
начиная со второго элемента. Минимум меняем местами уже со вторым.
При дальнейшем поиске минимума не трогаем отсортированную часть!
"""
def choise_sort(array):
    N = len(array)
    for pos in range(0, N - 1): ## pos + 1 - индекс элемента, с которого начинается поиск минимума
        for k in range(pos + 1, N):
            for k in range(pos + 1, N):
                if array[k] < array[pos]:
                    array[k], array[pos] = array[pos], array[k]