from time import time
import pandas as pd
import matplotlib.pyplot as plt


def run_loop_a(n):
    summ = 0
    for i in range(n + 1):
        for j in range(i, 10001):
            summ += j


def run_loop_b(n):
    summ = 0
    for i in range(n + 1):
        for j in range(i, n + 1):
            summ += j


if __name__ == '__main__':
    summary = pd.DataFrame(columns=['Loop A', 'Loop B'], index=range(1, 100))

    for n in range(0, 15000, 70):
        t0 = time()
        run_loop_a(n)
        time_a = time() - t0

        t0 = time()
        run_loop_b(n)
        time_b = time() - t0

        summary.loc[n, 'Loop A'] = time_a
        summary.loc[n, 'Loop B'] = time_b

        if n % 350 == 0:
            print(n, end=' ')

    summary.plot()
    plt.title('Running time of two loops')
    plt.xlabel('Iterations n')
    plt.ylabel('Time (s)')
    plt.savefig('loops.png')
    plt.show()
