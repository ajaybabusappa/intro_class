import matplotlib.pyplot as plt

# Data for the pie chart
labels = ['M.B', 'P.S.P.K', 'N.T.R', 'Prabhas']
sizes = [25, 25, 25, 25]  # Corresponding values for each label
colors = ['red', 'yellow', 'pink', 'brown']  # Colors for each segment

# Creating the pie chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Adding title
plt.title("Heroes Distribution")

# Display the pie chart
plt.show()
