import pandas as pd
import numpy as np

# Load dataset

dataset = pd.read_csv('dataset/president_heights.csv')
print(dataset)

# Preprocess data: save data as numpy array
height = np.array(dataset["height(cm)"])
print(height)

# Summary statistics
print("Mean of heights:",np.mean(height))
print("Standard deviation  of heights:", np.std(height))
print("Max of heights:",np.max(height))
print("Min  of heights:",np.min(height))
print("Median of heights:",np.median(height))
print("25th percentile of heights:",np.percentile(height, 25))
print("75th percentile of heights:",np.percentile(height, 75))

