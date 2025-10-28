
import json
from pathlib import Path

students_file = Path("students.json")

try:
    with students_file.open("r", encoding="utf-8") as f:
        students = json.load(f)
    print(" Students:")
    for s in students:
        print(f"- Name: {s.get('name')} | Age: {s.get('age')} | Grade: {s.get('grade')}")
except FileNotFoundError:
    print("students.json file not found in the current folder.")
except json.JSONDecodeError as e:
    print("Error decoding JSON:", e)





import requests

api_key = input("Enter your OpenWeather API key: ").strip()
city = "Tashkent"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:
    res = requests.get(url, timeout=10)
    data = res.json()
    if res.status_code == 200:
        print(f"City: {data.get('name')}")
        print(f"Temperature: {data['main'].get('temp')} °C")
        print(f"Humidity: {data['main'].get('humidity')} %")
        print(f"Weather: {data['weather'][0].get('description')}")
    else:
        print('Error:', data.get('message', 'Unknown error'), f'(status {res.status_code})')
except requests.RequestException as e:
    print('Network error:', e)







import json
from pathlib import Path

books_file = Path("books.json")

def load_books():
    if not books_file.exists():
        return []
    try:
        return json.loads(books_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print("books.json has invalid JSON. Starting with an empty list.")
        return []

def save_books(books):
    books_file.write_text(json.dumps(books, ensure_ascii=False, indent=4), encoding="utf-8")

def show_books(books):
    if not books:
        print("No books found.")
        return
    for i, b in enumerate(books, 1):
        print(f"{i}. {b.get('title')} — {b.get('author')}")

books = load_books()

while True:
    print("\nBook Manager:\n1) Add book\n2) Update book\n3) Delete book\n4) Show all\n5) Exit")
    choice = input("Choose: ").strip()
    if choice == '1':
        title = input('Title: ').strip()
        author = input('Author: ').strip()
        books.append({"title": title, "author": author})
        save_books(books)
        print('Added.')
    elif choice == '2':
        show_books(books)
        idx = input('Enter number of book to update: ').strip()
        if idx.isdigit() and 1 <= int(idx) <= len(books):
            i = int(idx)-1
            books[i]['title'] = input(f"New title (leave empty to keep '{books[i]['title']}'): ").strip() or books[i]['title']
            books[i]['author'] = input(f"New author (leave empty to keep '{books[i]['author']}'): ").strip() or books[i]['author']
            save_books(books)
            print('Updated.')
        else:
            print('Invalid selection.')
    elif choice == '3':
        show_books(books)
        idx = input('Enter number of book to delete: ').strip()
        if idx.isdigit() and 1 <= int(idx) <= len(books):
            books.pop(int(idx)-1)
            save_books(books)
            print('Deleted.')
        else:
            print('Invalid selection.')
    elif choice == '4':
        show_books(books)
    elif choice == '5':
        break
    else:
        print('Invalid choice')








import requests, random

api_key = input("Enter your OMDB API key: ").strip()
genre = input("Enter desired genre (e.g. Action, Comedy, Drama): ").strip()

# We'll try multiple common keywords to get a wider pool, then filter by genre in the detailed info.
keywords = ['best', 'popular', 'classic', 'new', 'top', 'award']
candidates = []

for q in keywords:
    try:
        r = requests.get(f"http://www.omdbapi.com/?apikey={api_key}&s={q}&type=movie", timeout=10)
        data = r.json()
        if 'Search' in data:
            candidates.extend(data['Search'])
    except requests.RequestException:
        pass

# remove duplicates by imdbID
unique = {m['imdbID']: m for m in candidates}.values()
candidates = list(unique)

# fetch full details for each candidate and filter by genre
filtered = []
for m in candidates:
    try:
        r = requests.get(f"http://www.omdbapi.com/?apikey={api_key}&i={m['imdbID']}", timeout=10)
        d = r.json()
        g = d.get('Genre','')
        if genre.lower() in g.lower():
            filtered.append(d)
    except requests.RequestException:
        pass

if filtered:
    choice = random.choice(filtered)
    print(f"Recommended: {choice.get('Title')} ({choice.get('Year')})\nGenre: {choice.get('Genre')}\nPlot: {choice.get('Plot')}\nIMDB: {choice.get('imdbRating')}")
else:
    print('No matching movie found. Try a broader genre or different API key.')






