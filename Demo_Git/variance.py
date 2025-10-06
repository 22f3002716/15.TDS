import json
import statistics

# Read the JSON file (e.g., [12.3, 15.4, 14.8, ...])
with open('q-calculate-variance.json', 'r') as f:
    data = json.load(f)

# Compute sample variance (uses N-1)
sample_variance = statistics.variance(data)

# Round to 2 decimal places
print(round(sample_variance, 2))