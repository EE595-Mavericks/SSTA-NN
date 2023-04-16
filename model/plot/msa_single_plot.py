import glob
import os.path
import pandas as pd
import matplotlib.pyplot as plt
import pdb

ACT = "sigmoid"


# Read all CSV files under folder you choice 

folder_path = '../results/var-e1000/'
file_pattern = '*.csv'
file_pattern = f"*SGD-{ACT}-0.01-50-e1000.csv"

file_paths = glob.glob(os.path.join(folder_path, file_pattern))
file_paths = [fp for fp in file_paths if 
        fp.split("/")[-1].split("-")[0] in ["25", "50","100","150"]]
sz = [int(fp.split("/")[-1].split("-")[0]) for fp in file_paths]
file_paths = [x for _, x in sorted(zip(sz, file_paths))]

file_names = [os.path.basename(file_path) for file_path in file_paths]
print("\n".join(file_paths))


# Create a figure and axes
fig, ax = plt.subplots(figsize=(16, 8))


for i in range(len(file_paths)):

    arch = file_paths[i].split("/")[-1].split("-Adam")[0]
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
plt.savefig('./figures/' + f"2L-SGD-{ACT}-0.005-50-v0.png")

# Show the plo
# plt.show()
plt.close()
