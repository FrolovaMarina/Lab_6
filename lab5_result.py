import numpy as np
from numpy import linalg as la
import time
try:
    K = 2
    #int(input("Введите число K = "))
    N = 10
    #int(input("Введите положительное число N = "))
    while N <= 0:
        print("Число N не подходит заданному условию. Пожалуйста, введите N ещё раз.")
        N = int(input("Введите положительное число N = "))
    start = time.time()
    A = np.random.randint(-10, 10, (N, N))
    if N % 2 == 0:
        B = A[0:(N // 2), 0:(N // 2)].copy()
        C = A[0:(N // 2), (N // 2):N].copy()
    else:
        B = A[0:(N // 2), 0:(N // 2)].copy()
        C = A[0:(N // 2), (N // 2)+1:N].copy()
    b2 = []
    for index, i in enumerate(B[:len(B) // 2]):
        if index == 0:
            b2.append(i)
        else:
            b2.append(i[index:-index])
    b3 = []
    for index, i in enumerate(B):
        if index < len(B) // 2:
            b3.append(i[-index - 1:])
        else:
            b3.append(i[index:])
    G = []
    for index, i in enumerate(A[(N // 2):N, 0:N]):
        if N % 2 == 0:
            if index == 0:
                G.append(i[N // 2 - 1:N // 2 + 1])
            else:
                G.append(i[(N // 2 - index - 1):(N // 2 + index + 1)])
        else:
            if index == 0:
                G.append([i[N // 2]])
            else:
                G.append(i[(N // 2 - index):(N // 2 + index + 1)])
    count = 0
    simple_numbers = [2, 3, 5, 7]
    for index, i in enumerate(b2):
        if index % 2 == 0:
            i = i[::2]
        else:
            i = i[1::2]
        for k in simple_numbers:
            count += np.count_nonzero(i == k)
    multiplication = 1
    for i in b3:
        if len(i) == 1:
            multiplication *= i[0]
        else:
            multiplication *= i[0] * i[-1]
    for index in range(len(B)):
        B[index], C[index] = C[index], np.copy(B[index])
    if count > multiplication:
        B = np.fliplr(B)
        C = np.fliplr(C)
    F = A.copy()
    for i in range(N):
        if i < N // 2:
            if N % 2 == 0:
                F[i] = np.r_[B[i], C[i]]
            else:
                F[i] = np.r_[B[i], A[i][len(B)], C[i]]
    if la.det(A) > np.trace(F):
        result1 = A * A.transpose()
        result2 = K * F
        result3 = np.around(result1-result2, 2)
        print(result3)
    else:
        for i in range(N):
            if i < N // 2:
                G.insert(0, np.zeros(N, dtype=int))
            else:
                len_Gi = np.size(G[i])
                for j in range(N-len_Gi):
                    if j < (N - len_Gi) // 2:
                        G[i] = np.insert(G[i], 0, 0)
                    else:
                        G[i] = np.append(G[i], 0)
        inverse_A = np.around(np.linalg.inv(A), 2)
        result1 = inverse_A + G
        inverse_F = np.around(np.linalg.inv(F), 2)
        result2 = result1 - inverse_F
        result3 = np.around(result2 * K, 2)
        np.set_printoptions(suppress=True)
        print(result3)
    finish = time.time()
    result = finish - start
    #print("Время выполнения программы: " + str(result) + " секунд.")
except ValueError:
    print("Это не число")