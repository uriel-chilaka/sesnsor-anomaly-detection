import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

#load features
X = pd.read_csv("features.csv")

#normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
joblib.dump(scaler, "scaler.joblib")

data = torch.tensor(X_scaled, dtype=torch.float32)

#autoencoder model

class AutoEncoder(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(dim, 8),
            nn.ReLU(),
            nn.Linear(8, 3)
        )
        self.decoder = nn.Sequential(
            nn.Linear(3, 8),
            nn.ReLU(),
            nn.Linear(8, dim)
        )
        
    def forward(self, x):
        z = self.encoder(x)
        return self.decoder(z)
    
model = AutoEncoder(data.shape[1])
optimizer = optim.Adam(model.parameters(), lr=1e-3)
loss_fn = nn.MSELoss()

#train loop
for epoch in range(300):
    optimizer.zero_grad()
    out = model(data)
    loss = loss_fn(out, data)
    loss.backward()
    optimizer.step()
    
    if epoch % 50 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.6f}")
    
torch.save(model.state_dict(), "autoendcoder.pt")
print("Saved autoencoder.pt")