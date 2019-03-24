import numpy

def read_from_file(filename):
    with open(filename) as f:
        number_of_machines, number_of_jobs = [int(x) for x in next(f).split()]
        p_time = numpy.zeros((number_of_machines, number_of_jobs)) #processing time
        for i in range(number_of_machines):
            p_i = f.readline().split()
            for j in range(number_of_jobs):
                p_time[i][j] = p_i[j]
    return number_of_machines, number_of_jobs, p_time

def sum(index_job, data, nb_machines):
    sum_p = 0
    for i in range(1,nb_machines):
        sum_p += data[i][index_job]
    return sum_p

def order_neh(data, nb_machines, nb_jobs):
    my_seq = []
    for j in range(nb_jobs):
        my_seq.append(j)
    order = sorted(my_seq, key=lambda x: sum(x, data, nb_machines), reverse=True)
    return order

def reorder_array(order, data, nbm, nbj):
    r_data = numpy.zeros((nbm, nbj))
    for j in range(len(order)):
        r_data[:,j] = data[:,order[j]]
    return r_data

def calc_cmax(data, nbm, nbj):
    times = []
    for j in range(0, nbj):
        times.append(0)
    for foo in range(0, nbm):
        times[0] = data[foo, 0] + times[0]
        #print("times moo : ", times[0])
        for moo in range(1, nbj):
            times[moo] = data[foo, moo] + max(times[moo-1], times[moo])
            #print("times moo : ", times[moo])
        print("timespan debug", times)
    return times

nbm, nbj, p_ij = read_from_file("data.txt")
print("Data: \n ", p_ij)
print("Number of Machines:", nbm)
print("Number of jobs:", nbj)
print("Non-increasing order of total processing times:")
order_seq = order_neh(p_ij, nbm, nbj)
print(order_seq)
ordered_data = reorder_array(order_seq, p_ij, nbm, nbj)
print("Ordered data: ")
print(ordered_data)
cmax = calc_cmax(ordered_data, nbm, nbj)
print("cmax ", cmax)
