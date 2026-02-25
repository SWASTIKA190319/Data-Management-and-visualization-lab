import matplotlib.pyplot as plt

# Number of data values
n = int(input("Enter number of data values: "))

data = []

print("Enter the values:")
for i in range(n):
    value = float(input(f"Value {i+1}: "))
    data.append(value)

# Number of bins
bins = int(input("Enter number of bins: "))

# Plot histogram
plt.hist(data, bins=bins, edgecolor='black')

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram from User Input")
plt.grid(axis='y')

plt.show()
