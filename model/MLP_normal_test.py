import torch
import pandas as pd

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

# Load trained model from file
model = MLP()
model.load_state_dict(torch.load("model.pt"))

# Read CSV file for testing
test_data = pd.read_csv("/Users/yuzhe/Documents/Study/EE595_Software_Design_and_Optimization/Project/Normal-RVs/model/output_v2.csv")

# Split data into input and output
X_test = test_data.iloc[:, :4].values
y_test = test_data.iloc[:, 4:].values

# Test model on testing set
with torch.no_grad():
    y_pred_test = model(torch.tensor(X_test, dtype=torch.float32))
    error_rate = torch.abs(y_pred_test - torch.tensor(y_test, dtype=torch.float32)) / torch.tensor(y_test, dtype=torch.float32)
    error_rate_0 = torch.mean(error_rate[:, 0])
    error_rate_1 = torch.mean(error_rate[:, 1])
    error_rate_2 = torch.mean(error_rate[:, 2])
    print(f"Error rate on testing set for output 0: {error_rate_0.item()}")
    print(f"Error rate on testing set for output 1: {error_rate_1.item()}")
    print(f"Error rate on testing set for output 2: {error_rate_2.item()}")
