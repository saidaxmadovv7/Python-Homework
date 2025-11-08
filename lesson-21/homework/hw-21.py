import pandas as pd
import matplotlib.pyplot as plt

# =========================
#  DataFrame 1: Student Grades
# =========================
data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}
df1 = pd.DataFrame(data1)

# Exercise 1: Calculate average grade for each student
df1['Average'] = df1[['Math', 'English', 'Science']].mean(axis=1)

# Exercise 2: Student with highest average grade
top_student = df1.loc[df1['Average'].idxmax()]

# Exercise 3: Create 'Total' column
df1['Total'] = df1[['Math', 'English', 'Science']].sum(axis=1)

# Exercise 4: Bar chart for average grades in each subject
subjects = ['Math', 'English', 'Science']
avg_subjects = df1[subjects].mean()

plt.figure(figsize=(6,4))
avg_subjects.plot(kind='bar')
plt.title('Average Grades by Subject')
plt.ylabel('Average Grade')
plt.show()

print("Top student with highest average grade:")
print(top_student)

# =========================
# DataFrame 2: Sales Data
# =========================
data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}
df2 = pd.DataFrame(data2)

# Exercise 1: Total sales for each product
total_sales = df2[['Product_A', 'Product_B', 'Product_C']].sum()
print("\nTotal Sales for each product:")
print(total_sales)

# Exercise 2: Date with highest total sales
df2['Total_Sales'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)
best_day = df2.loc[df2['Total_Sales'].idxmax(), 'Date']
print(f"\nDate with highest total sales: {best_day}")

# Exercise 3: Percentage change in sales for each product
pct_change = df2[['Product_A', 'Product_B', 'Product_C']].pct_change() * 100
print("\nPercentage change in sales:\n", pct_change)

# Exercise 4: Line chart for sales trends
plt.figure(figsize=(8,5))
plt.plot(df2['Date'], df2['Product_A'], label='Product A')
plt.plot(df2['Date'], df2['Product_B'], label='Product B')
plt.plot(df2['Date'], df2['Product_C'], label='Product C')
plt.legend()
plt.title('Sales Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

# =========================
# Dataframe 3
# =========================
data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}
df3 = pd.DataFrame(data3)

# Exercise 1: Average salary for each department
avg_salary = df3.groupby('Department')['Salary'].mean()
print("\nAverage salary per department:\n", avg_salary)

# Exercise 2: Employee with most experience
most_exp = df3.loc[df3['Experience (Years)'].idxmax()]
print("\nEmployee with most experience:\n", most_exp)

# Exercise 3: Salary Increase column
min_salary = df3['Salary'].min()
df3['Salary Increase (%)'] = ((df3['Salary'] - min_salary) / min_salary) * 100

# Exercise 4: Bar chart for employee count by department
dept_count = df3['Department'].value_counts()
plt.figure(figsize=(6,4))
dept_count.plot(kind='bar', color='skyblue')
plt.title('Number of Employees per Department')
plt.xlabel('Department')
plt.ylabel('Count')
plt.show()

# =========================
# DataFrame 4
# =========================
data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}
df4 = pd.DataFrame(data4)

# Exercise 1: Total revenue
total_revenue = df4['Total_Price'].sum()
print(f"\nTotal revenue: ${total_revenue}")

# Exercise 2: Most ordered product
most_ordered = df4['Product'].value_counts().idxmax()
print(f"\nMost ordered product: {most_ordered}")

# Exercise 3: Average quantity
avg_quantity = df4['Quantity'].mean()
print(f"\nAverage quantity ordered: {avg_quantity:.2f}")

# Exercise 4: Pie chart for product sales distribution
sales_by_product = df4.groupby('Product')['Total_Price'].sum()
plt.figure(figsize=(6,6))
sales_by_product.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Sales Distribution by Product')
plt.ylabel('')
plt.show()
