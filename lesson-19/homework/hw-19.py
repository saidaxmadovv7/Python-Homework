##-------------------------------
##-------------------------------

import pandas as pd

# CSV faylni o'qish
sales_df = pd.read_csv("https://raw.githubusercontent.com/IslomovSH/python-homework/refs/heads/main/lesson-19/homework/task/sales_data.csv")


category_stats = sales_df.groupby('Category').agg({
    'Quantity': ['sum', 'max'],
    'Price': 'mean'
}).reset_index()
category_stats.columns = ['Category', 'Total_Quantity', 'Max_Quantity', 'Average_Price']
print(category_stats)


top_products = sales_df.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()
top_products = top_products.loc[top_products.groupby('Category')['Quantity'].idxmax()]
print(top_products)


sales_df['Total_Sales'] = sales_df['Quantity'] * sales_df['Price']
top_date = sales_df.groupby('Date')['Total_Sales'].sum().idxmax()
print("Date with highest sales:", top_date)




orders_df = pd.read_csv("https://raw.githubusercontent.com/IslomovSH/python-homework/refs/heads/main/lesson-19/homework/task/customer_orders.csv")

# 1 Customers with >=20 orders
customer_counts = orders_df.groupby('CustomerID')['OrderID'].count()
customers_20plus = customer_counts[customer_counts >= 20].index
filtered_orders = orders_df[orders_df['CustomerID'].isin(customers_20plus)]
print(filtered_orders)

# 2 Customers who ordered products with average price > 120
avg_price = orders_df.groupby('Product')['Price'].mean()
expensive_products = avg_price[avg_price > 120].index
customers_expensive = orders_df[orders_df['Product'].isin(expensive_products)]['CustomerID'].unique()
print(customers_expensive)

# 3 Total quantity and total price per product
product_totals = orders_df.groupby('Product').agg({
    'Quantity': 'sum',
    'Price': lambda x: (x * orders_df.loc[x.index, 'Quantity']).sum()  # total revenue
}).reset_index()
product_totals = product_totals[product_totals['Quantity'] >= 5]
print(product_totals)



import requests

url = "https://raw.githubusercontent.com/username/repo/main/population.db"
r = requests.get(url)

with open("population.db", "wb") as f:
    f.write(r.content)




import sqlite3
import pandas as pd

conn = sqlite3.connect("population.db")  # endi to‘g‘ri fayl
# verify file looks like a SQLite DB before querying
try:
    with open("population.db", "rb") as _f:
        header = _f.read(16)
    if not header.startswith(b"SQLite format 3"):
        raise sqlite3.DatabaseError("population.db is not a valid SQLite database (bad header)")

    population_df = pd.read_sql_query("SELECT * FROM population", conn)

except (sqlite3.DatabaseError, pd.io.sql.DatabaseError) as e:
    print("Failed to read SQLite database:", e)
    # fallback attempts: try loading as CSV, otherwise create empty DataFrame
    try:
        population_df = pd.read_csv("population.db")
        print("Loaded population.db as CSV fallback.")
    except Exception as e2:
        print("CSV fallback failed:", e2)
        population_df = pd.DataFrame()
        print("Using empty DataFrame as fallback.")
conn.close()
print(population_df.head())






from io import BytesIO

url = "https://github.com/IslomovSH/python-homework/blob/main/lesson-19/homework/task/population_salary_analysis.xlsx"
# prefer the raw.githubusercontent URL and add timeout/handling
raw_url = url.replace("github.com/", "raw.githubusercontent.com/").replace("/blob/", "/")
try:
    r = requests.get(raw_url, timeout=10)
    if r.status_code != 200:
        # fallback to the original URL if raw failed
        r = requests.get(url, timeout=10)
except requests.RequestException as e:
    print("Download failed:", e)
    r = requests.Response()
    r.status_code = 0
    r._content = b''
if r.status_code == 200:
    salary_bands = pd.read_excel(BytesIO(r.content))
else:
    # Try GitHub raw URL fallback
    raw_url = url.replace("github.com/", "raw.githubusercontent.com/").replace("/blob/", "/")
    r2 = requests.get(raw_url)
    if r2.status_code == 200:
        salary_bands = pd.read_excel(BytesIO(r2.content))
    else:
        print("Failed to download Excel file:", r.status_code, r2.status_code)
        salary_bands = pd.DataFrame()






import requests
from io import BytesIO

url = "https://raw.githubusercontent.com/IslomovSH/python-homework/main/lesson-19/homework/task/population_salary_analysis.xlsx"
r = requests.get(url)
salary_bands = pd.read_excel(BytesIO(r.content))
print(salary_bands)



import requests

url = "https://raw.githubusercontent.com/IslomovSH/python-homework/main/lesson-19/homework/task/population.db"
r = requests.get(url)
with open("population.db", "wb") as f:
    f.write(r.content)



import sqlite3
import pandas as pd

# lokalga saqlangan population.db faylni ulash
conn = sqlite3.connect("population.db")

# population jadvalidan barcha ma'lumotlarni olish
population_df = pd.read_sql("SELECT * FROM population", conn)
conn.close()

print(population_df.head())
print(population_df.columns)  # ustun nomlarini tekshirish uchun




print(salary_bands.head())
print(salary_bands.columns)



# Salary Band ajratish
def assign_band(salary):
    if salary < 30000:
        return 'Low'
    elif salary < 70000:
        return 'Medium'
    elif salary < 120000:
        return 'High'
    else:
        return 'Very High'

population_df['Salary_Band'] = population_df['salary'].apply(assign_band)  # kichik harf

# Hisoblash
band_count = population_df.groupby('Salary_Band').size()
band_avg = population_df.groupby('Salary_Band')['salary'].mean()
band_median = population_df.groupby('Salary_Band')['salary'].median()
band_percent = (band_count / band_count.sum()) * 100

salary_summary = pd.DataFrame({
    'Count': band_count,
    'Average_Salary': band_avg,
    'Median_Salary': band_median,
    'Percentage': band_percent
})

print(salary_summary)



# State bo‘yicha hisoblash
state_summary = population_df.groupby(['state', 'Salary_Band']).agg(
    Count=('salary', 'count'),        # kichik harf bilan 'salary'
    Average_Salary=('salary', 'mean'),
    Median_Salary=('salary', 'median')
).reset_index()

# Foiz hisoblash
state_totals = state_summary.groupby('state')['Count'].transform('sum')
state_summary['Percentage'] = (state_summary['Count'] / state_totals) * 100

print(state_summary)


