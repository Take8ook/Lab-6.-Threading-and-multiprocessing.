from threading import Thread
from time import time

n = 5000
p = [x for x in range(1, n + 1)]
q = [y for y in range(1, n + 1)]


def filling_matrix(p_vector, q_vector):
    matrix_def = []
    for pi in p_vector:
        for qj in q_vector:
            matrix_def.append(1 / (1 + (qj - pi)**2))
    return matrix_def


t = time()
matrix_A = filling_matrix(p, q)
matrix_B = filling_matrix(p, q)
print("Output time without threads: ", round(time() - t, 4))

t = time()
t1 = Thread(target=filling_matrix, args=(p, q,))
t1.start()
t2 = Thread(target=filling_matrix, args=(p, q,))
t2.start()
t1.join()
t2.join()
print("Output time with threads: ", round(time() - t, 4))
