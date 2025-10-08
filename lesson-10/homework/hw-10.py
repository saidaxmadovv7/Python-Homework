##-----------------------------------------
##-----------------------------------------
# Homework 1 - ToDo List Application

class Task:
    def __init__(self, title, description, due_date, status="Incomplete"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def mark_complete(self):
        self.status = "Complete"

    def display(self):
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Due Date: {self.due_date}")
        print(f"Status: {self.status}")
        print("-" * 30)


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date):
        task = Task(title, description, due_date)
        self.tasks.append(task)
        print("Task added successfully!")

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                task.display()

    def list_incomplete_tasks(self):
        incomplete = [task for task in self.tasks if task.status == "Incomplete"]
        if not incomplete:
            print("All tasks are complete!")
        else:
            for task in incomplete:
                task.display()

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                task.mark_complete()
                print(f"Task '{title}' marked as complete.")
                return
        print("Task not found.")


def main():
    todo = ToDoList()

    while True:
        print("\n=== ToDo List Menu ===")
        print("1. Add Task")
        print("2. List All Tasks")
        print("3. List Incomplete Tasks")
        print("4. Mark Task Complete")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due Date: ")
            todo.add_task(title, description, due_date)

        elif choice == "2":
            todo.list_all_tasks()

        elif choice == "3":
            todo.list_incomplete_tasks()

        elif choice == "4":
            title = input("Enter task title to mark complete: ")
            todo.mark_task_complete(title)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

# A simple command-line ToDo list application
##-----------------------------------------


##-----------------------------------------
##-----------------------------------------


# Homework 2 - Simple Blog System

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Content: {self.content}")
        print("-" * 40)


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, title, content, author):
        post = Post(title, content, author)
        self.posts.append(post)
        print("Post added successfully!")

    def list_all_posts(self):
        if not self.posts:
            print("No posts available.")
        else:
            for post in self.posts:
                post.display()

    def display_by_author(self, author):
        found = [p for p in self.posts if p.author.lower() == author.lower()]
        if not found:
            print("No posts by this author.")
        else:
            for post in found:
                post.display()

    def delete_post(self, title):
        for post in self.posts:
            if post.title.lower() == title.lower():
                self.posts.remove(post)
                print(f"Post '{title}' deleted.")
                return
        print("Post not found.")

    def edit_post(self, title, new_content):
        for post in self.posts:
            if post.title.lower() == title.lower():
                post.content = new_content
                print("Post updated successfully!")
                return
        print("Post not found.")

    def display_latest_posts(self, count=3):
        print(f"=== Latest {count} Posts ===")
        for post in self.posts[-count:]:
            post.display()


def main():
    blog = Blog()

    while True:
        print("\n=== Blog Menu ===")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. Show Latest Posts")
        print("7. Exit")

        choice = input("Choose (1-7): ")

        if choice == "1":
            title = input("Title: ")
            content = input("Content: ")
            author = input("Author: ")
            blog.add_post(title, content, author)

        elif choice == "2":
            blog.list_all_posts()

        elif choice == "3":
            author = input("Author name: ")
            blog.display_by_author(author)

        elif choice == "4":
            title = input("Title to delete: ")
            blog.delete_post(title)

        elif choice == "5":
            title = input("Title to edit: ")
            new_content = input("New content: ")
            blog.edit_post(title, new_content)

        elif choice == "6":
            blog.display_latest_posts()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()



##-----------------------------------------
##-----------------------------------------


# Homework 3 - Simple Banking System

class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} so'm qo'shildi. Yangi balans: {self.balance}")
        else:
            print("Xato: miqdor musbat bo'lishi kerak!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Xato: miqdor musbat bo'lishi kerak!")
        elif amount > self.balance:
            print("Xato: balansda yetarli mablag' yo'q!")
        else:
            self.balance -= amount
            print(f"{amount} so'm yechildi. Yangi balans: {self.balance}")

    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Balance: {self.balance}")
        print("-" * 30)


class Bank:
    def __init__(self):
        self.accounts = []

    def find_account(self, account_number):
        for acc in self.accounts:
            if acc.account_number == account_number:
                return acc
        return None

    def add_account(self, account_number, holder_name, balance=0):
        if self.find_account(account_number):
            print("Bu hisob raqami allaqachon mavjud!")
        else:
            acc = Account(account_number, holder_name, balance)
            self.accounts.append(acc)
            print("Hisob muvaffaqiyatli qo'shildi!")

    def check_balance(self, account_number):
        acc = self.find_account(account_number)
        if acc:
            print(f"Balans: {acc.balance} so'm")
        else:
            print("Hisob topilmadi.")

    def deposit(self, account_number, amount):
        acc = self.find_account(account_number)
        if acc:
            acc.deposit(amount)
        else:
            print("Hisob topilmadi.")

    def withdraw(self, account_number, amount):
        acc = self.find_account(account_number)
        if acc:
            acc.withdraw(amount)
        else:
            print("Hisob topilmadi.")

    def transfer(self, from_acc, to_acc, amount):
        sender = self.find_account(from_acc)
        receiver = self.find_account(to_acc)
        if not sender or not receiver:
            print("Hisob raqamlardan biri topilmadi!")
            return
        if sender.balance < amount:
            print("Balansda yetarli mablag' yo'q!")
            return
        sender.withdraw(amount)
        receiver.deposit(amount)
        print(f"{amount} so'm {sender.holder_name} dan {receiver.holder_name} ga o'tkazildi.")

    def show_all_accounts(self):
        if not self.accounts:
            print("Bankda hisoblar mavjud emas.")
        else:
            for acc in self.accounts:
                acc.display()


def main():
    bank = Bank()

    while True:
        print("\n=== Banking Menu ===")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer")
        print("6. Show All Accounts")
        print("7. Exit")

        choice = input("Tanlang (1-7): ")

        if choice == "1":
            acc_no = input("Hisob raqami: ")
            name = input("Ism: ")
            balance = float(input("Boshlang'ich balans: "))
            bank.add_account(acc_no, name, balance)

        elif choice == "2":
            acc_no = input("Hisob raqami: ")
            bank.check_balance(acc_no)

        elif choice == "3":
            acc_no = input("Hisob raqami: ")
            amount = float(input("Summani kiriting: "))
            bank.deposit(acc_no, amount)

        elif choice == "4":
            acc_no = input("Hisob raqami: ")
            amount = float(input("Summani kiriting: "))
            bank.withdraw(acc_no, amount)

        elif choice == "5":
            from_acc = input("Jo'natuvchi hisob raqami: ")
            to_acc = input("Qabul qiluvchi hisob raqami: ")
            amount = float(input("Summani kiriting: "))
            bank.transfer(from_acc, to_acc, amount)

        elif choice == "6":
            bank.show_all_accounts()

        elif choice == "7":
            print("Dastur tugadi. Rahmat!")
            break

        else:
            print("Xato tanlov. Qayta urinib ko'ring.")


if __name__ == "__main__":
    main()

