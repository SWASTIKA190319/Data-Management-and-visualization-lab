import matplotlib.pyplot as plt

# Example data
x = [1, 2, 3, 4, 5]
bar_values = [10, 15, 7, 12, 9]
scatter_values = [5, 7, 8, 6, 9]

# Create subplots (1 row, 2 columns)
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# First subplot - Bar chart
axs[0].bar(x, bar_values, color='skyblue')
axs[0].set_title("Bar Chart")
axs[0].set_xlabel("X-axis")
axs[0].set_ylabel("Values")
axs[0].grid(axis='y', linestyle='--', alpha=0.7)

# Second subplot - Scatter plot
axs[1].scatter(x, scatter_values, color='green', marker='o')
axs[1].set_title("Scatter Plot")
axs[1].set_xlabel("X-axis")
axs[1].set_ylabel("Values")
axs[1].grid(True)

# Adjust layout
plt.tight_layout()
plt.show()
