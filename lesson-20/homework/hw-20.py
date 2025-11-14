




##-----------------------------------------
##----------------------------------------
# Lesson-20





#Customer Purchases Analysis:
#Find the total amount spent by each customer on purchases (considering invoices).
#Identify the top 5 customers with the highest total purchase amounts.
#Display the customer ID, name, and the total amount spent for the top 5 customers.

import pandas as pd
import sqlite3

conn = sqlite3.connect("chinook.db")

customers = pd.read_sql_query("SELECT CustomerId, FirstName, LastName FROM Customers", conn)
invoices = pd.read_sql_query("SELECT CustomerId, Total FROM Invoices", conn)

# 3. Har bir mijozning jami xarajatini hisoblash
total_spent = invoices.groupby("CustomerId")["Total"].sum().reset_index()

# 4. Mijozlar bilan birlashtirish (ID bo‘yicha)
total_spent = total_spent.merge(customers, on="CustomerId")

# 5. Eng ko'p xarajat qilgan 5 mijozni topish
top5_customers = total_spent.sort_values(by="Total", ascending=False).head(5)

# 6. Natijani ko'rsatish
print(top5_customers[["CustomerId", "FirstName", "LastName", "Total"]])




#Album vs. Individual Track Purchases:
#Determine the percentage of customers who prefer to buy individual tracks instead of full albums.
#A customer is considered to prefer individual tracks if they have purchased only a subset of tracks from an album.
#Provide a summary of the percentage of customers who fall into each category (individual tracks vs. full albums).

import sqlite3
import pandas as pd

# 1. Ma'lumotlar bazasiga ulanish
conn = sqlite3.connect("chinook.db")

# 2. Jadvallarni o'qish
customers = pd.read_sql_query("SELECT CustomerId FROM Customers", conn)
tracks = pd.read_sql_query("SELECT TrackId, AlbumId FROM Tracks", conn)
albums = pd.read_sql_query("SELECT AlbumId, Title FROM Albums", conn)
invoice_lines = pd.read_sql_query("SELECT InvoiceId, TrackId FROM InvoiceLines", conn)
invoices = pd.read_sql_query("SELECT InvoiceId, CustomerId FROM Invoices", conn)

# 3. InvoiceLines va Invoices ni birlashtirish
purchases = invoice_lines.merge(invoices, on="InvoiceId")

# 4. Mijoz-albom-traklar jadvalini yaratish
purchases_album = purchases.merge(tracks, on="TrackId")

# 5. Har bir albomdagi treklar soni
album_track_counts = tracks.groupby("AlbumId")["TrackId"].count().reset_index()
album_track_counts.rename(columns={"TrackId":"TotalTracks"}, inplace=True)

# 6. Har bir mijoz-albomdagi xarid qilingan treklar soni
customer_album_tracks = purchases_album.groupby(["CustomerId","AlbumId"])["TrackId"].count().reset_index()
customer_album_tracks.rename(columns={"TrackId":"PurchasedTracks"}, inplace=True)

# 7. Albumdagi treklar soni bilan solishtirish
customer_album_tracks = customer_album_tracks.merge(album_track_counts, on="AlbumId")

# 8. Har bir mijozning kategoriyasini aniqlash
def preference(row):
    if row["PurchasedTracks"] == row["TotalTracks"]:
        return "Full Album"
    else:
        return "Individual Tracks"

customer_album_tracks["Preference"] = customer_album_tracks.apply(preference, axis=1)

# 9. Har bir mijozni kategoriyalash
# Agar mijoz har qanday albomni faqat trek sifatida sotib olsa → Individual Tracks
# Agar barcha albomlari butun bo‘lsa → Full Album

def overall_pref(df):
    if (df["Preference"] == "Individual Tracks").any():
        return "Individual Tracks"
    else:
        return "Full Album"

customer_pref = customer_album_tracks.groupby("CustomerId").apply(overall_pref).reset_index()
customer_pref.columns = ["CustomerId","Preference"]

# 10. Foiz hisoblash
percentage = customer_pref["Preference"].value_counts(normalize=True) * 100

print(percentage)
