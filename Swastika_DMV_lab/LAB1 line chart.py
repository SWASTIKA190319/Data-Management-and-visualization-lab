import matplotlib.pyplot as plt

# Example: already provided inputs
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 17, 20]

plt.plot(x, y, marker='o')
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Line Chart")
plt.grid(True)
plt.show()
