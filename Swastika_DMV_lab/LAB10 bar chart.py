import matplotlib.pyplot as plt

# Already provided data
categories = ['A', 'B', 'C', 'D']
values = [10, 15, 7, 12]

# Create bar chart
plt.bar(categories, values, color='skyblue')

plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Chart Example")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
