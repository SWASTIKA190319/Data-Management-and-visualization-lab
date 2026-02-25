import matplotlib.pyplot as plt

# Number of points
n = int(input("Enter number of data points: "))

x = []
y = []

# Input X values
print("Enter X values:")
for i in range(n):
    value = float(input(f"X[{i+1}]: "))
    x.append(value)

# Input Y values
print("Enter Y values:")
for i in range(n):
    value = float(input(f"Y[{i+1}]: "))
    y.append(value)

# Plot line graph
plt.plot(x, y, marker='o', linestyle='-', color='blue')

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Graph from User Input")
plt.grid(True)

plt.show()
