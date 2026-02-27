import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sensor_log.csv")

print(df.head())

plt.plot(df["light"], label="light")
plt.plot(df["sound"], label="sound")
plt.plot(df["temperature"], label="temperature")

plt.legend()
plt.show()
