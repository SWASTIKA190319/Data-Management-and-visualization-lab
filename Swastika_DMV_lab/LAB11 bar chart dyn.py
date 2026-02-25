import matplotlib.pyplot as plt

# Number of categories
n = int(input("Enter number of categories: "))

categories = []
values = []

# Input category names and values
for i in range(n):
    category = input(f"Enter name of category {i+1}: ")
    value = float(input(f"Enter value for {category}: "))
    categories.append(category)
    values.append(value)

# Create bar chart
plt.bar(categories, values, color='skyblue')

plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Chart from User Input")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
