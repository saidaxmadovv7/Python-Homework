#---------------------------------------
#-----------------------------------------
import pandas as pd

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

print(data)

data1 = pd.DataFrame(data)
print(data1)

#Rename
data1 = data1.rename(columns={"First Name":"first_name"})
print(data1)

#Rename
data1 = data1.rename(columns={"Age":"age"})
print(data1)



#dataframe
print(data1[["first_name","age","City"]])

#Top 3
print(data1.head(3))

age = data1["age"]
print(age)

print(age.mean())


data1["Salary"]= [70000, 80000, 90000, 100000]
print(data1)



print(data1.describe())







import pandas as pd

# Ma'lumotlardan DataFrame yaratish
sales_and_expenses = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
})

# DataFrame ni ko‘rsatish
print("Sales and Expenses Data:")
print(sales_and_expenses)

# Maksimum qiymatlar
max_sales = sales_and_expenses['Sales'].max()
max_expenses = sales_and_expenses['Expenses'].max()

# Minimum qiymatlar
min_sales = sales_and_expenses['Sales'].min()
min_expenses = sales_and_expenses['Expenses'].min()

# O‘rtacha qiymatlar
avg_sales = sales_and_expenses['Sales'].mean()
avg_expenses = sales_and_expenses['Expenses'].mean()

# Natijalarni chiqarish
print("\nMaximum Sales:", max_sales)
print("Maximum Expenses:", max_expenses)
print("Minimum Sales:", min_sales)
print("Minimum Expenses:", min_expenses)
print("Average Sales:", round(avg_sales, 2))
print("Average Expenses:", round(avg_expenses, 2))






import pandas as pd

# Ma'lumotlar jadvali
data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

# DataFrame yaratish
expenses = pd.DataFrame(data)

# Category ni index sifatida o‘rnatish
expenses = expenses.set_index('Category')

# DataFrame ni ko‘rsatish
print("Expenses DataFrame:")
print(expenses)

# Maksimum qiymatlar
max_expenses = expenses.max(axis=1)

# Minimum qiymatlar
min_expenses = expenses.min(axis=1)

# O‘rtacha qiymatlar
avg_expenses = expenses.mean(axis=1)

# Natijalarni chiqarish
print("\n Maximum expenses for each category:")
print(max_expenses)

print("\n Minimum expenses for each category:")
print(min_expenses)

print("\n Average expenses for each category:")
print(round(avg_expenses, 2))





