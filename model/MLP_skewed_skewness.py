import torch
from torch.utils.data import DataLoader, TensorDataset
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import csv
import itertools
import time
import sys
import pdb


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


def test_module(layers, activation, epoch_num, opt, learning_rate, batch_size):
    model = MLP(layers, activation).to(device)
    dataset = TensorDataset(x_train, y_train)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    # Define loss function and optimizer
    criterion = torch.nn.MSELoss().to(device)
    if opt == 'Adam':
        optimizer = torch.optim.Adam(model.parameters(), learning_rate)
    elif opt == 'SGD':
        optimizer = torch.optim.SGD(model.parameters(), learning_rate, momentum=0.9)

    # Train model
    res = list()
    for epoch in range(1, epoch_num + 1):
        for i, (batch_x, batch_y) in enumerate(dataloader):
            # V2: set the gradient to zero
            # optimizer.zero_grad()

            # Move the data to the device
            batch_x = batch_x.to(device)
            batch_y = batch_y.to(device)

            # Forward pass
            y_pred = model(batch_x)
            loss = criterion(y_pred, batch_y)

            # Backward pass
            # V0 default code: zero grad used to be here
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        # Print training progress
        # if epoch % 10 == 0:
        #     print(f"Epoch {epoch}: loss = {loss.item()}")

        if epoch % 10 == 0:
            # print(f"\t Epoch {epoch}/{epoch_num} completed")
            with torch.no_grad():
                y_pred_train = model(x_train)
                error_rate_train = torch.abs(y_pred_train - y_train) / torch.abs(y_train)
                y_pred_test = model(x_test)
                error_rate_test = torch.abs(y_pred_test - y_test) / torch.abs(y_test)
                tmp = [epoch]
                tmp += [torch.mean(error_rate_train[:, i]).item() for i in range(1)]
                tmp += [torch.mean(error_rate_test[:, i]).item() for i in range(1)]
                res.append(tmp)

    torch.save(model.state_dict(), f"{name}-skew.pt")

    # Test model on testing set
    with torch.no_grad():
        y_pred_test = model(x_test)
        error_rate = torch.abs(y_pred_test - y_test) / y_test
        error_rate_0 = torch.mean(error_rate[:, 0])
        # error_rate_1 = torch.mean(error_rate[:, 1])
        # error_rate_2 = torch.mean(error_rate[:, 2])
        print(f"Error rate on testing set for skewness: {error_rate_0.item()}")
        return res


if __name__ == "__main__":
    # Read CSV file
    data = pd.read_csv("dataset/skewed_rv_dataset.csv")
    print(f"Dataset is loaded, size is {data.shape}")

    # Split data into input and output
    x = data.iloc[:, 1:6].values
    y = data.iloc[:, 8].values
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    x_train = torch.tensor(x_train, dtype=torch.float32)
    x_test = torch.tensor(x_test, dtype=torch.float32)
    y_train = torch.tensor(y_train, dtype=torch.float32).unsqueeze(1)
    y_test = torch.tensor(y_test, dtype=torch.float32).unsqueeze(1)

    # Set device to GPU if available, else CPU
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # Move the data to the device
    x_train = x_train.to(device)
    y_train = y_train.to(device)
    x_test = x_test.to(device)
    y_test = y_test.to(device)

    # neurons_list = [
    #     [10, 10, 10],
    #     [15, 15, 15],
    #     [20, 20, 20],
    #     [25, 25, 25],
    #     [50, 50, 50],
    #     [100, 100, 100],
    #     [150, 150, 150],
    #     [200, 200, 200],
    #     [250, 250, 250]
    # ]
    neurons_list = [
        [10, 10],
        [15, 15],
        [20, 20],
        [25, 25],
        [50, 50],
        [100, 100],
        [150, 150],
        [200, 200],
        [250, 250],
        [500, 500],
        [750, 750],
        [1000, 1000]
    ]
    if len(sys.argv) > 1:
        neurons_list = neurons_list[int(sys.argv[1]):int(sys.argv[2])]
        print(f"Training these neural nets in this process:\n\t{neurons_list}")
    for arr in neurons_list:
        arr.insert(0, 5)
        arr.append(1)
    act_list = ['tanh', 'relu']
    epoch = 10000
    opt_list = ['SGD']
    lr_list = [0.001]
    batch_sizes = [50]

    parameters = [act_list, opt_list, lr_list, batch_sizes]
    models = list(itertools.product(*parameters))

    header = ['Epoch', 'train error mean', 'test error mean']
    para_names = ['activation', 'optimization', 'learning rate', 'batch size']

    for [activation, opt, learning_rate, batch_size] in models:
        for layers in neurons_list:
            structure = '-'.join(str(x) for x in layers[1:-1])
            name = f"{structure}-{opt}-{activation}-{learning_rate}-{batch_size}-e{epoch}"
            t_s = time.time()
            print(f"Starting with training model {name}")
            with open(f"{name}.csv", 'w') as f:
                writer = csv.writer(f)
                writer.writerow(header)
                writer.writerow(para_names)
                writer.writerow([activation, opt, learning_rate, batch_size])
                res = test_module(layers, activation, epoch, opt, learning_rate, batch_size)
                for row in res:
                    writer.writerow(row)
                f.close()
            print(f"\t... training completed {time.time() - t_s}")
