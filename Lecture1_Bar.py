import matplotlib.pyplot as plt

# Data for the bar graph
categories = ['Sachin', 'Virat', 'R.P', 'Me', 'M.S.D' , 'Yuvaraj']
values = [100, 81, 73, 1, 16, 3]

plt.bar(categories, values)

# Adding title and labels
plt.title("Simple Bar Graph")
plt.xlabel("Categories")
plt.ylabel("Values")

# Display the graph
plt.show()

