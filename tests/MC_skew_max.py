import random
import csv
import subprocess
from math import fabs
import time

import numpy as np
from scipy.stats import skewnorm, skew


def get_sample():
    loc = random.uniform(-10, 10)
    scale = random.uniform(0, 10)
    a = random.uniform(-10, 10)

    samples = skewnorm.rvs(a=a, loc=loc, scale=scale, size=10000)

    return np.mean(samples), np.var(samples), skew(samples), samples


if __name__ == "__main__":

    time_start = time.time()
    rows = []

    for i in range(100):
        row = list(range(9))
        muX, varX, skeX, x = get_sample()
        muY, varY, skeY, y = get_sample()
        result = subprocess.run(
            ['../cmake-build-debug/main', str(muX), str(varX), str(skeX), str(muY), str(varY), str(skeY)],
            stdout=subprocess.PIPE)
        z = np.array([max(a, b) for (a, b) in zip(x, y)])
        c_output = result.stdout.decode().split(' ')
        row[0], row[1], row[2] = np.mean(z), np.var(z), skew(z)
        row[3] = round(float(c_output[0]), 10)
        row[4] = round(float(c_output[1]), 10)
        row[5] = round(float(c_output[2]), 10)
        row[6] = '{:.10%}'.format(fabs((row[0] - row[3]) / row[0]))
        row[7] = '{:.10%}'.format(fabs((row[1] - row[4]) / row[1]))
        row[8] = '{:.10%}'.format(fabs((row[2] - row[5]) / row[2]))
        rows.append(row)

    with open('MC_skew_max.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['MC mean', 'MC variance', 'MC skewness',
                         'mean', 'variance', 'skewness',
                         'mean error', 'variance error', 'skewness error'])
        for row in rows:
            writer.writerow(row)

    time_end = time.time()
    print('time cost', time_end - time_start, 's')
