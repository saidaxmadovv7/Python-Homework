##-----------------------------------------
##-----------------------------------------

# Circle Class
#Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius
# Example usage:
circle = Circle(5)
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())

# Person Class
class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def age(self):
        today = datetime.date.today()
        age = today.year - self.date_of_birth.year
        if today.month < self.date_of_birth.month or (today.month == self.date_of_birth.month and today.day < self.date_of_birth.day):
            age -= 1
        return age
import datetime
# Example usage:
person = Person("Alice", "USA", datetime.date(1990, 5,
15))
print("Name:", person.name)
print("Country:", person.country)
print("Date of Birth:", person.date_of_birth)
print("Age:", person.age())

#Calculator Class
#Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error! Division by zero."
# Example usage:
calc = Calculator()
print("Addition:", calc.add(10, 5))
print("Subtraction:", calc.subtract(10, 5))
print("Multiplication:", calc.multiply(10, 5))
print("Division:", calc.divide(10, 5))

#Shape and Subclasses
#Write a Python program to create a class that represents a shape. 
#Include methods to calculate its area and perimeter. Implement subclasses for different shapes like Circle, Triangle, and Square.
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c
# Example usage:
circle = Circle(5)
square = Square(4)
triangle = Triangle(3, 4, 5)
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())
print("Square Area:", square.area())
print("Square Perimeter:", square.perimeter())
print("Triangle Area:", triangle.area())
print("Triangle Perimeter:", triangle.perimeter())


# Binary Search Tree Class
#Write a Python program to create a class representing a binary search tree.
# Include methods for inserting and searching for elements in the binary tree.
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_rec(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_rec(node.right, key)

    def search(self, key):
        return self._search_rec(self.root, key)

    def _search_rec(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search_rec(node.left, key)
        return self._search_rec(node.right, key)
# Example usage:
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
found_node = bst.search(5)
if found_node:
    print("Node found:", found_node.val)
else:
    print("Node not found")



#Stack Data Structure
#Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
# Example usage:
stack = Stack()
stack.push(10)
stack.push(20)
print("Top element:", stack.peek())
print("Stack size:", stack.size())
print("Popped element:", stack.pop())
print("Stack size after pop:", stack.size())


# Linked List Data Structure
#Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting, and deleting nodes.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
# Example usage:
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()
ll.delete(20)
ll.display()
# Example usage:
ll.insert(40)
ll.display()



# Shopping Cart Class
#Write a Python program to create a class representing a shopping cart.
# Include methods for adding and removing items, and calculating the total price.

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price, quantity=1):
        if item in self.items:
            self.items[item]['quantity'] += quantity
        else:
            self.items[item] = {'price': price, 'quantity': quantity}

    def remove_item(self, item, quantity=1):
        if item in self.items:
            if self.items[item]['quantity'] > quantity:
                self.items[item]['quantity'] -= quantity
            else:
                del self.items[item]

    def total_price(self):
        total = 0
        for item in self.items.values():
            total += item['price'] * item['quantity']
        return total
# Example usage:
cart = ShoppingCart()
cart.add_item("Apple", 1.5, 3)
cart.add_item("Banana", 0.5, 5)
print("Total Price:", cart.total_price())
cart.remove_item("Apple", 1)
print("Total Price after removing an Apple:", cart.total_price())
# Example usage:
cart.add_item("Orange", 0.8, 2)
print("Total Price after adding Oranges:", cart.total_price())




 #Stack with Display
#Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping, and displaying elements.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        if not self.is_empty():
            print("Stack elements:")
            for item in reversed(self.items):
                print(item)
        else:
            print("Stack is empty")

# Example usage:
stack = Stack()
stack.push(10)
stack.push(20)
stack.display()
print("Top element:", stack.peek())
print("Stack size:", stack.size())
print("Popped element:", stack.pop())
print("Stack size after pop:", stack.size())



#Queue Data Structure
#Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "Queue is empty"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        if not self.is_empty():
            print("Queue elements:")
            for item in self.items:
                print(item)
        else:
            print("Queue is empty")

# Example usage:
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.display()
print("Dequeued element:", queue.dequeue())
print("Queue size after dequeue:", queue.size())
print("Front element:", queue.items[0] if not queue.is_empty() else "Queue is empty")



 #Bank Class
#Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited: {amount}. New Balance: {self.balance}"
        return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew: {amount}. New Balance: {self.balance}"
        return "Insufficient funds or invalid withdrawal amount."

    def get_balance(self):
        return self.balance
# Example usage:
account = BankAccount("123456", "John Doe", 1000)
print(account.deposit(500)) 
print(account.withdraw(200))
print("Current Balance:", account.get_balance())
print(account.withdraw(2000))
