import pandas as pd

#load data
df = pd.read_csv("sensor_log.csv")

#drop time stap
df = df.drop(columns=["timestamp"])

WINDOW = 10

features = []

for i in range(len(df) - WINDOW):
    w = df.iloc[i:i+WINDOW]
    
    
    feat = {
        "light_mean": w["light"].mean(),
        "light_std": w["light"].std(),
        "sound_mean": w["sound"].mean(),
        "sound_std": w["sound"].std(),
        "temp_mean": w["temperature"].mean(),
        "temp_std": w["temperature"].std(),
    }
    features.append(feat)
    
X = pd.DataFrame(features)
print(X.head())

X.to_csv("features.csv", index=False)
print("features.csv has been saved.")