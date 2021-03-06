#przykład danych z intrukcji

data_1 = [
    [5,5,3],
    [4,5,2],
    [4,4,5],
    [3,5,7],
]

#tworzenie wirtualnych maszyn
data = []
for i in range(0, len(data_1)):
    array = [data_1[i][0] + data_1[i][1], data_1[i][1] + data_1[i][2]]
    data.append(array)
print("Podgląd danych dla wirtualnych maszyn: ")
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
