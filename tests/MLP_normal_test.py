import torch
from torch.utils.data import DataLoader, TensorDataset
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import csv
import itertools


class MLP(torch.nn.Module):
    def __init__(self, layers, activation):
        super(MLP, self).__init__()
        self.layers = torch.nn.ModuleList()
        for i in range(len(layers) - 1):
            self.layers.append(torch.nn.Linear(layers[i], layers[i + 1]))
            if i == len(layers) - 2:
                break
            if activation == "relu":
                self.layers.append(torch.nn.ReLU())
            elif activation == "tanh":
                self.layers.append(torch.nn.Tanh())
            elif activation == 'sigmoid':
                self.layers.append(torch.nn.Sigmoid())

    def forward(self, x):
        for layer in self.layers:
            x = layer(x)
        return x



if __name__ == "__main__":
    # Read CSV file
    data = pd.read_csv("dataset/normal_rv_test_sample.csv")

    # Split data into input and output
    x_test = data.iloc[:, :4].values.astype(np.float32)
    y_test = data.iloc[:, 4:].values.astype(np.float32)

    # Convert np.ndarray of type numpy.object_ to tensors
    x_test = torch.tensor(x_test, dtype=torch.float32)
    y_test = torch.tensor(y_test, dtype=torch.float32)

    # Set device to GPU if available, else CPU
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # Move the data to the device
    x_test = x_test.to(device)
    y_test = y_test.to(device)

    # Test model on testing set
    with torch.no_grad():
        model = MLP([4, 50, 50, 50, 50, 3], "tanh").to(device)
        model.load_state_dict(torch.load("50-50-50-50-epoch-240.pt"))
        y_pred_test = model(x_test)
        error_rate = torch.abs(y_pred_test - y_test) / y_test
        error_rate_0 = torch.mean(error_rate[:, 0])
        error_rate_1 = torch.mean(error_rate[:, 1])
        error_rate_2 = torch.mean(error_rate[:, 2])
        print(f"Error rate on testing set for mean: {error_rate_0.item()}")
        print(f"Error rate on testing set for variance: {error_rate_1.item()}")
        print(f"Error rate on testing set for skewness: {error_rate_2.item()}")

    # save predict result along with the test data to a csv file
    x_test = x_test.numpy()
    y_test = y_test.numpy()
    y_pred_test = y_pred_test.numpy()

    with open('MLP_test_sample_result.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['mean_x', 'var_x','mean_y', 'var_y','mean_z', 'var_z', 'skewness_z', 'mean_predict', 'var_predict', 'skewness_predict'])
        for i in range(len(y_test)):
            writer.writerow([x_test[i][0], x_test[i][1], x_test[i][2], x_test[i][3],y_test[i][0], y_test[i][1], y_test[i][2], y_pred_test[i][0], y_pred_test[i][1], y_pred_test[i][2]])

    