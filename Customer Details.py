import csv
import os

def add_customer():
    name = input("Enter customer name: ")
    phone = input("Enter customer phone number: ")
    item = input("Enter purchased item: ")
    quantity = int(input("Enter quantity purchased: "))
    price = float(input("Enter price per item: "))
    total = quantity * price

    file_exists = os.path.isfile('customer_records.csv')

    with open('customer_records.csv', 'a', newline='') as file:
        fieldnames = ['Name', 'Phone', 'Item', 'Quantity', 'Price', 'Total']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({'Name': name, 'Phone': phone, 'Item': item, 'Quantity': quantity, 'Price': price, 'Total': total})

def display_records():
    with open('customer_records.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def main():
    while True:
        print("\n1. Add Customer\n2. Display Records\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_customer()
        elif choice == '2':
            display_records()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter again.")

if __name__ == "__main__":
    main()