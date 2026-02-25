import matplotlib.pyplot as plt

# Number of categories
n = int(input("Enter number of categories: "))

labels = []
sizes = []

# Input category names and values
for i in range(n):
    label = input(f"Enter label for category {i+1}: ")
    value = float(input(f"Enter value for {label}: "))
    labels.append(label)
    sizes.append(value)

# Create pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.titl5
("Pie Chart from User Input")
plt.axis('equal')  # Make it circular
plt.show()
