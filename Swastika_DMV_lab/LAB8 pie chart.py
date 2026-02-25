import matplotlib.pyplot as plt

# Already provided data
labels = ['A', 'B', 'C', 'D']
sizes = [25, 35, 20, 20]

# Create pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

plt.title("Pie Chart")
plt.axis('equal')  # Makes pie circular

plt.show()
