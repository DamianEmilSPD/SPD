#przykład danych z intrukcji

data = [
    [6,4],
    [10,8],
    [4,9],
    [7,2],
    [6,3],
    [5,6],
]

#sortowanie danych od najmniejszego do największego

data.sort(key=lambda x: min((x[0], x[1])))
data.reverse() #odwrócenie kolejności

print("Podglad danych po posortowaniu")
print(data)

def Johnson(data_array):
    tasks = []
    for i in range(0,len(data_array)):
        if data_array[i][0]>data_array[i][1]:
            tasks.append(data_array[i]) #umieszczenie na końcu listy
        else:
                tasks.insert(0, data_array[i]) #umieszczenie na początku listy
    return tasks

print("Kolejnosc według algorytmy Johnson'a:")
data = Johnson(data)
print(data)
