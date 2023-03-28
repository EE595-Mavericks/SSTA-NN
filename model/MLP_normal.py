import torch
import pandas as pd
from sklearn.model_selection import train_test_split
import csv
import itertools


class MLP(torch.nn.Module):
    def __init__(self, layers, activation):
        super().__init__()
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


def test_module(layers, activation, epoch_num, opt, learning_rate):
    # Read CSV file
    data = pd.read_csv("dataset/normal_rv_dataset.csv")

    # Split data into input and output
    x = data.iloc[:, :4].values
    y = data.iloc[:, 4:].values

    # Split data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # Define MLP model with fully connected layers

    # Initialize MLP model
    model = MLP(layers, activation)

    # Define loss function and optimizer
    criterion = torch.nn.MSELoss()
    if opt == 'Adam':
        optimizer = torch.optim.Adam(model.parameters(), learning_rate)
    elif opt == 'SGD':
        optimizer = torch.optim.SGD(model.parameters(), learning_rate)

    # Train model
    for epoch in range(epoch_num):
        # Forward pass
        y_pred = model(torch.tensor(x_train, dtype=torch.float32))
        loss = criterion(y_pred, torch.tensor(y_train, dtype=torch.float32))

        # Backward pass
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # Print training progress
        if epoch % 1000 == 0:
            print(f"Epoch {epoch}: loss = {loss.item()}")

    torch.save(model.state_dict(), "model.pt")

    # Test model on testing set
    with torch.no_grad():
        y_pred_test = model(torch.tensor(x_test, dtype=torch.float32))
        error_rate = torch.abs(y_pred_test - torch.tensor(y_test, dtype=torch.float32)) / torch.tensor(y_test,
                                                                                                       dtype=torch.float32)
        error_rate_0 = torch.mean(error_rate[:, 0])
        error_rate_1 = torch.mean(error_rate[:, 1])
        error_rate_2 = torch.mean(error_rate[:, 2])
        print(f"Error rate on testing set for output 0: {error_rate_0.item()}")
        print(f"Error rate on testing set for output 1: {error_rate_1.item()}")
        print(f"Error rate on testing set for output 2: {error_rate_2.item()}")
        return [error_rate_0.item(), error_rate_1.item(), error_rate_0.item()]


if __name__ == "__main__":
    neurons_list = [[4, 6, 8, 16, 8, 3]]
    act_list = ['tanh']
    epoch_list = [1000, 5000, 10000]
    opt_list = ['Adam']
    lr_list = [0.001, 0.005]

    parameters = [neurons_list, act_list, epoch_list, opt_list, lr_list]
    models = list(itertools.product(*parameters))

    header = ['Neurons', 'Activation function', 'Number of EPOCHs', 'Optimization algorithm', 'learning rate',
              'Error rate of mean', 'Error rate of variance', 'Error rate of skewness']

    with open("MLP_result.csv", 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for [layers, activation, epoch_num, opt, learning_rate] in models:
            errors = test_module(layers, activation, epoch_num, opt, learning_rate)
            writer.writerow(
                [layers] + [activation] + [epoch_num] + [opt] + [learning_rate] + [errors[0]] + [errors[1]] + [
                    errors[2]])

        f.close()
