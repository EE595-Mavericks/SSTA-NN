import numpy as np
from scipy.stats import skewnorm
import matplotlib.pyplot as plt

if __name__ == "__main__":
    loc = 1
    scale = 1
    a = 1

    fig, ax = plt.subplots(1, 1)
    x = np.linspace(skewnorm.ppf(0.01, a=a, loc=loc, scale=scale),
                    skewnorm.ppf(0.99, a=a, loc=loc, scale=scale), 100)
    ax.plot(x, skewnorm.pdf(x, a=a, loc=loc, scale=scale),
            'r-', lw=5, alpha=0.6, label='skewnorm pdf')

    r = skewnorm.rvs(a=a, loc=loc, scale=scale, size=10000)

    ax.hist(r, density=True, bins='auto', histtype='stepfilled', alpha=0.2)
    ax.set_xlim([x[0], x[-1]])
    ax.legend(loc='best', frameon=False)
    plt.show()
