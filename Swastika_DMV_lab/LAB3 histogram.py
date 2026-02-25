import matplotlib.pyplot as plt

# Already provided input data
data = [12, 15, 13, 10, 18, 20, 17, 15, 14, 16, 19, 11, 14]

# Create histogram
plt.hist(data, bins=5, edgecolor='black')

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram Chart")
plt.grid(axis='y')

plt.show()
