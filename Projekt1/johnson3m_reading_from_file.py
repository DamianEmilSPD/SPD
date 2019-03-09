with open('ta000.txt') as f:
    number_of_jobs, number_of_machines = [int(x) for x in next(f).split()] #czytanie pierwszej linii instancji
    data_1 = []
    for line in f:
        data_1.append([int(x) for x in line.split()])
print(data_1)

#tworzenie wirtualnych maszyn
data_2 = []
for i in range(0, number_of_jobs):
    array = [data_1[i][0] + data_1[i][1], data_1[i][1] + data_1[i][2]]
    data_2.append(array)
print("Podgląd danych dla wirtualnych maszyn: ")
print(data_2)

#sortowanie danych od najmniejszego do największego

data_2.sort(key=lambda x: min((x[0], x[1])))
data_2.reverse() #odwrócenie kolejności

print("Podgląd danych po posortowaniu dla 3 maszyn")
print(data_2)

def Johnson3m(data_array):

    tasks = []
    for i in range(0,len(data_array)):
        if data_array[i][0]>data_array[i][1]:
           tasks.append(data_array[i])
        else:
           tasks.insert(0, data_array[i])
    return tasks

print("Kolejnosc według algorytmy Johnson'a dla 3 maszyn:")
data = Johnson3m(data_2)
print(data)