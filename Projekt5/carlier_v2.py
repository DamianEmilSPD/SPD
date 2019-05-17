from schrage import *

def h(K):
    r_K = min(K, key=lambda x: x[0])[0]
    q_K = min(K, key=lambda x: x[2])[2]
    p_K = sum([k[1] for k in K])
    return r_K + p_K + q_K

UB = 1000000000000000
best_order = 0

procs = []

for i in range(len(procs)):
   task = job(i, data[i][0], data[i][1], data[i][2])
   newdata.append(procs)


def Carlier(tasks):
    global UB, best_order
    tasks, U = schrage(tasks)
    #print(U)
    if UB > U:
        best_order=copy.deepcopy(tasks)
        UB = U

    b = max(tasks, key=lambda x: x.end + x[2])
    c = None
    for i in range(tasks.index(b), 0, -1):
        #print(order[i-1])
        a = tasks[i - 1]
        #print(a)
        if a[2]< b[2] and c is None:
            c = a
            #print(c)
    #print("b",b)
    #print("a",a)
    #print("c",c)

    if c is None:
        return

    K = tasks[tasks.index(c)+1 : tasks.index(b) +1]

    #for i in range(len(K)):
     #  print(K[i])

    r_K = min(K, key=lambda x: x[0])[0]
    q_K = min(K, key=lambda x: x[2])[2]
    p_K = sum([k[1] for k in K])

    boo_r = c[0]
    c[0] = max(c[0], r_K + p_K)
    foo, LB = schragepmtn(tasks)

    #print(LB)
    #for i in range(len(foo)):
    #   print(foo[i])

    LB = max(LB, h(K), h([*K, c]))
    #print(LB)
    #print(LB, r_K + p_K + q_K, h([*K, c]) )

    if LB < UB:
        Carlier(tasks)
    c[0] = boo_r
        #print(order)

    moo_q = c[2]
    c[2] = max(c[2], q_K + p_K)
    foo, LB = schragepmtn(tasks)
    LB = max(LB, h(K), h([*K, c]))
    #print(LB)
    if LB < UB:
        Carlier(tasks)
    c[2] = moo_q
    return best_order, UB

col, nbj, data = read_from_file("data2.txt")
newdata =[]

for i in range(len(data)):
   task = job(i, data[i][0], data[i][1], data[i][2])
   newdata.append(task)

start = time.time_ns() / 10**6
Carlier(newdata)
stop = time.time_ns() / 10**6 - start
print("Carlier: ")
print("Cmax: ", UB)
print("Czas: ", stop)
print("===================================")
#start1 = time.time_ns() / 10**6
#ord, cma = schragepmtn(newdata)
#stop1 = time.time_ns() / 10**6 - start1
#print("Schragepmtn: ")
#print("Cmax ", cma)
#print("Czas: ",stop1)

#for i in range(len(best_order)):
#   print(best_order[i])


