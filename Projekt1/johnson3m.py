#przykład danych z intrukcji

data_1 = [
    [5,5,3],
    [4,5,2],
    [4,4,5],
    [3,5,7],
]

#tworzenie wirtualnych maszyn

data = [
    [data_1[0][0] + data_1[0][1], data_1[0][1] + data_1[0][2]],
    [data_1[1][0] + data_1[1][1], data_1[1][1] + data_1[1][2]],
    [data_1[2][0] + data_1[2][1], data_1[2][1] + data_1[2][2]],
    [data_1[3][0] + data_1[3][1], data_1[3][1] + data_1[3][2]],
]

print(data)

#sortowanie od najmniejszego do największego

data.sort(key=lambda x: min((x[0], x[1],)))
data.reverse() #odwrócenie kolejności

print("Podglad danych po posortowaniu")
print(data)

def Johnson(data_array):

    tasks = []
    for i in range(0,len(data_array)):
        if data_array[i][0]>data_array[i][1]:
           tasks.append(data_array[i])
        else:
           tasks.insert(0, data_array[i])
    return tasks

print("Kolejnosc według algorytmy Johnson'a:")
data = Johnson(data)
print(data)
