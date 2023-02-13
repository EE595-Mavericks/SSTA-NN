import math
import sys
import numpy as np
from scipy.stats import skew

if __name__ == "__main__":
    mean_x = float(sys.argv[1])
    std_x = math.sqrt(float(sys.argv[2]))
    mean_y = float(sys.argv[3])
    std_y = math.sqrt(float(sys.argv[4]))

    x = np.random.normal(mean_x, std_x, size=1000000)
    y = np.random.normal(mean_y, std_y, size=1000000)

    # Find the maximum of each sample pair
    max_xy = np.maximum(x, y)

    # Calculate the mean of the maximum
    mean_max_xy = np.mean(max_xy)
    variance = np.var(max_xy)
    # skewness = np.mean(((max_xy - mean_max_xy) / variance) ** 3)
    skewness = skew(max_xy)

    print("Mean of max(X, Y): {:.5f}".format(mean_max_xy))
    print("Variance of max(X, Y): {:.5f}".format(variance))
    print("Skewness of max(X, Y): {:.5f}".format(skewness))

    with open("result_MC.txt", "a") as f:
        f.write(f"{format(mean_x, '.5f')} {format(float(sys.argv[2]), '.5f')} {format(mean_y, '.5f')} {format(float(sys.argv[4]), '.5f')} {format(mean_max_xy, '.5f')} {format(variance, '.5f')} {format(skewness, '.5f')}\n")
