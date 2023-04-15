# Visualize single figure for every model

import pandas as pd
from matplotlib import pyplot as plt

# Define the number of rows per file
rows_per_file = 103

# Read the CSV file into a data frame
# filenames = ["10-10-10.csv", "20-20-20.csv", "50-50-50.csv", "50-50-50-50.csv", "50-100-50.csv", "50-100-100-"]
filename = "10-10-10.csv"
data = pd.read_csv(filename)

# Split the data frame and save each group to a separate CSV file

error_list = ["train error mean", "train error variance", "train error skewness", "test error mean", "test error variance" , "test error skewness"]
for i, chunk in enumerate(data.groupby(data.index // rows_per_file)):
    if i == 5:
        break
    structure = filename.split('.')[0]

    act_func = chunk[1].iloc[1]["Epoch"]
    opti = chunk[1].iloc[1]["train error mean"]
    l_rate = chunk[1].iloc[1]["train error variance"]
    bch_size = chunk[1].iloc[1]["train error skewness"]

    head = chunk[1].head
    epoch = chunk[1]["Epoch"][2:102].astype(int)

    fig, ax = plt.subplots()

    name = structure + '-' + opti + '-' + act_func + '-' + l_rate + '-' + bch_size

    for a in range(6):
        y_value = chunk[1][error_list[a]].iloc[2:102].astype(float)
        ax.plot(epoch, y_value, label=error_list[a])

    ax.set_title(name)
    ax.legend()
    plt.savefig(name + '.png')


    # print(head)
    # filename = "file_" + str(i) + ".csv"
    # chunk[1].to_csv(name + '.csv', index=False)
