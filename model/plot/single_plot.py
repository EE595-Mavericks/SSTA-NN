import glob
import os.path
import pandas as pd
import matplotlib.pyplot as plt
import shutil

if __name__ == "__main__":
    # Read all CSV files under folder you choice
    folder_path = '../results/skewness-e1000'

    if os.path.exists(folder_path + "/figures"):
        shutil.rmtree(folder_path + "/figures")
    os.makedirs(folder_path + "/figures")
    file_pattern = '*.csv'

    file_paths = glob.glob(os.path.join(folder_path, file_pattern))

    file_names = [os.path.basename(file_path) for file_path in file_paths]

    for i in range(len(file_paths)):
        df = pd.read_csv(file_paths[i], skiprows=[1, 2])

        epoch = df.iloc[:, 0]
        train_error = df.iloc[:, 1]
        test_error = df.iloc[:, 2]

        # Create a figure and axes
        fig, ax = plt.subplots()

        # Plot the train error and test error on the axes
        ax.plot(epoch, train_error, label='Train Error')
        ax.plot(epoch, test_error, label='Test Error')

        # Add a legend to the axes
        ax.legend()

        # Set the labels for the axes
        ax.set_xlabel('Epoch')
        ax.set_ylabel('Error')

        ax.set_title(file_names[i].split('.csv')[0])

        plt.yscale('log')

        # save figure under where you want
        plt.savefig(folder_path + "/figures/" + file_names[i].split('.csv')[0] + '.png')

        # Show the plo
        # plt.show()
        plt.close()
