import torch
import pandas as pd
from sklearn.model_selection import train_test_split

# Read CSV file
data = pd.read_csv("dataset/output.csv")

# Split data into input and output
x = data.iloc[:, :4].values
y = data.iloc[:, 4:].values

# Split data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Define MLP model with fully connected layers
class MLP(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(4, 16)
        self.fc2 = torch.nn.Linear(16, 32)
        self.fc3 = torch.nn.Linear(32, 16)
        self.fc4 = torch.nn.Linear(16, 8)
        self.fc5 = torch.nn.Linear(8, 3)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.relu(self.fc3(x))
        x = torch.relu(self.fc4(x))
        x = self.fc5(x)
        return x

# Initialize MLP model
model = MLP()

# Define loss function and optimizer
criterion = torch.nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters())

# Train model
for epoch in range(10000):
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
    error_rate = torch.abs(y_pred_test - torch.tensor(y_test, dtype=torch.float32)) / torch.tensor(y_test, dtype=torch.float32)
    error_rate_0 = torch.mean(error_rate[:, 0])
    error_rate_1 = torch.mean(error_rate[:, 1])
    error_rate_2 = torch.mean(error_rate[:, 2])
    print(f"Error rate on testing set for output 0: {error_rate_0.item()}")
    print(f"Error rate on testing set for output 1: {error_rate_1.item()}")
    print(f"Error rate on testing set for output 2: {error_rate_2.item()}")
