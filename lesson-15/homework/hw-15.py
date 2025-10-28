#---------------------------------------------------
#---------------------------------------------------
# Create a new database with a table named Roster that has three fields: Name, Species, and Age. The Name and Species columns should be text fields, and the Age column should be an integer field.

import sqlite3

with sqlite3.connect("example.db") as conn:
    cursor = conn.cursor()
    
    # Jadvalni yaratish (agar hali yaratilmagan bo‘lsa)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Roster (
        Name TEXT,
        Species TEXT,
        Age INTEGER
    )
    """)
    
    # Ma'lumotlarni kiritish
    data = [
        ("Benjamin Sisko", "Human", 40),
        ("Jadzia Dax", "Trill", 300),
        ("Kira Nerys", "Bajoran", 29)
    ]
    
    cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", data)
    conn.commit()





import sqlite3

with sqlite3.connect("example.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Roster")
    rows = cursor.fetchall()    # Barcha natijalarni olish uchun ishlatilinadi

    for i in rows:
        print(rows)




# Update the Name of Jadzia Dax to be Ezri Dax

import sqlite3

with sqlite3.connect("example.db") as conn:
    cursor = conn.cursor()
    cursor.execute("UPDATE Roster SET name =? WHERE name=?",("Jadzia Dax","Ezri Dax"))




# Display the Name and Age of everyone in the table classified as Bajoran.

with sqlite3.connect("example.db") as conn:
    cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
    print(cursor.fetchall())




with sqlite3.connect("company1.db") as conn:
    cursor.execute ("SELECT*FROM Roster")
    print(cursor.fetchall())
