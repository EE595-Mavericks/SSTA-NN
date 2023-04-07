import pandas as pd
import matplotlib.pyplot as plt

# Define the number of rows per file
rows_per_file = 103

# Read the CSV file into a data frame
data = pd.read_csv("[4, 10, 3].csv")

# Create a figure and axis object
# fig, ax = plt.subplots()
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(30, 20))

# Select the x series to plot
x_value = data["Epoch"].iloc[2:102]

error_list = ["train error mean", "train error variance", "train error skewness", "test error mean", "test error variance" , "test error skewness"]

# Split the data frame and plot each chunk
for i, chunk in enumerate(data.groupby(data.index // rows_per_file)):
    # Select the y series to plot
    # if i == 5:
    #     break
    act_func = chunk[1].iloc[1]["Epoch"]
    opti = chunk[1].iloc[1]["train error mean"]
    l_rate = chunk[1].iloc[1]["train error variance"]
    bch_size = chunk[1].iloc[1]["train error skewness"]
    if opti == 'SGD':
        continue
    if bch_size == str(100):
        continue
    if l_rate == str(0.005):
        continue
    # name = chunk[1].iloc[1]["train error mean"] + ' ' + chunk[1].iloc[1]["train error variance"] + ' ' + chunk[1].iloc[1]["train error skewness"]
    name = act_func + ' ' + opti + ' ' + l_rate + ' ' + bch_size
    # print(name)
    for a in range(6):
        y_value = chunk[1][error_list[a]].iloc[2:102].astype(float)
        # ax = axes[a%3, a/3]
        b = int(a/3)
        c = int(a%3)
        ax = axes[b, c]
        ax.plot(x_value, y_value, label=name)
        ax.set_ylabel("Y values")
        ax.set_title(error_list[a])
        ax.legend()

    # y_value_1 = chunk[1]["train error variance"].iloc[2:102].astype(float)
    # print(y_value_1)
    # # Plot the y series on the same axis
    # ax.plot(x_value, y_value_1, label=f"Chunk {i+1}")

# Add a legend, title, and axis labels
# ax.legend()
# ax.set_title("Multiple Line Plot")
# ax.set_xlabel("X values")
# ax.set_ylabel("Y values")

# Display the plot
# fig.legend()
plt.show()