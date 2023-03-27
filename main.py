import matplotlib.pyplot as plt

# Ask the user to enter the sales for each month
sales = []
for month in range(1, 13):
    sales.append(float(input(f"Enter sales for month {month}: ")))

# Define the x-axis and y-axis
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
totals = sales

# Create the graph
plt.plot(months, totals)
plt.title("Total Sales by Month")
plt.xlabel("Month")
plt.ylabel("Total Sales ($)")
plt.show()
