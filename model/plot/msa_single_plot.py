import glob
import os.path
import pandas as pd
import matplotlib.pyplot as plt
import pdb

ACT = "sigmoid"
OPT = "SGD"
LR = "0.01"
BATCH = 100
VER = "" # "-v2" 
EPOCH = 2500

# Read all CSV files under folder you choice 

folder_path = f"../results/var-e1000{VER}/"
file_pattern = "*.csv"
file_pattern = f"*{OPT}-{ACT}-{LR}-{BATCH}-e{EPOCH}.csv"

file_paths = glob.glob(os.path.join(folder_path, file_pattern))
file_paths = [fp for fp in file_paths if 
        fp.split("/")[-1].split("-")[0] in ["50", "250", "500", "750", "1000"]]
sz = [int(fp.split("/")[-1].split("-")[0]) for fp in file_paths]
file_paths = [x for _, x in sorted(zip(sz, file_paths))]

file_names = [os.path.basename(file_path) for file_path in file_paths]
print("\n".join(file_paths))

# Create a figure and axes
fig, ax = plt.subplots(figsize=(16, 8))
ax.set_ylim([0.02, 0.4])
ax.set_xlim([100, 2500])


for i in range(len(file_paths)):

    arch = file_paths[i].split("/")[-1].split(OPT)[0]
    df = pd.read_csv(file_paths[i], skiprows=[1,2])

    epoch = df.iloc[:, 0]
    train_error = df.iloc[:, 1]
    test_error = df.iloc[:, 2]

    
    # Plot the train error and test error on the axes
    # ax.plot(epoch, train_error, label=f"({arch}) E-train")
    ax.plot(epoch, test_error, label=f"({arch}) E-test")

    # Set the labels for the axes
    # ax.set_xlabel('Epoch')
    # ax.set_ylabel('Error')
    # ax.set_title(file_names[i].split('.csv')[0])

    # save figure under where you want
    # plt.tight_layout()
    # plt.savefig('./figures/' + file_names[i].split('.csv')[0] + '.png')

# Add a legend to the axes
ax.legend()
plt.yscale('log')
plt.tight_layout()
plt.savefig('./figures/' + f"2L-{OPT}-{ACT}-{LR}-{BATCH}{VER}.png")

# Show the plot
# plt.show()
plt.close()
