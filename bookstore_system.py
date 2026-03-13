# Bookstore Inventory and Analytics System

# Features:
# - User Input (Menu-driven)
# - Inventory Management (Add, Update, Remove)
# - Bookstore Class (OOP)
# - Data Loading & Cleaning from CSV
# - Sales Analysis (NumPy & Pandas)
# - Data Visualization (Matplotlib & Seaborn)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

inventory = []  # list of dictionaries

# -------------------------------
# Inventory Management Functions
# -------------------------------
class Bookstore:
    def __init__(self):
        self.sales=[]

    def add_book(self, title, author, genre, price, quantity):
        """Add a new book to inventory with user input."""
        if price<=0 or quantity<0:
            print("Invalid input: Price must be > 0 and Quantity >=0 ")
            return
        inventory.append({
            "Title": title,
            "Author": author,
            "Genre": genre,
            "Price": price,
            "Quantity": quantity
        })
        print(f"Book '{title}' added successfully!")

    def update_inventory(self, title, quantity):
        """Updates the stock of a book."""
        for book in inventory:
            if book["Title"] == title:
                if quantity >= 0:
                    book["Quantity"] = quantity
                    print(f"Updated '{title}' quantity to {quantity}")
                else:
                    print("Quantity must be non-negative")
                return
        print("Book not found in inventory")
    
    def record_sale(self, title, quantity):
        """Deducts sold books and updates sales data."""
        for book in inventory:
            if book["Title"] == title:
                if book["Quantity"] >= quantity:
                    book["Quantity"] -= quantity
                    revenue = book["Price"] * quantity
                    self.sales.append({
                        "Title": title,
                        "Quantity Sold": quantity,
                        "Total Revenue": revenue,
                        "Date": pd.Timestamp.today().strftime("%Y-%m-%d")
                    })
                    print(f"Sale recorded: {quantity} copies of '{title}'")
                else:
                    print("Not enough stock!")
                return
        print("Book not found!")

    def generate_report(self):
        """Summarizes inventory and sales metrics."""
        print("\nInventory Report")
        for book in inventory:
            print(f"{book['Title']} - {book['Quantity']} copies left")

        print("\nSales Report")
        total_revenue = sum(sale["Total Revenue"] for sale in self.sales)
        print(f"Total Revenue: rs.{total_revenue}")

# -------------------------------
# Remove Book Function
# -------------------------------

def remove_book():
    """Remove a book from inventory using user input."""
    title = input("Enter book title to remove: ")
    for book in inventory:
        if book["Title"] == title:
            inventory.remove(book)
            print(f"Book '{title}' removed successfully!")
            return
    print("Book not found in inventory")

# -------------------------------
# Data Loading & Cleaning
# -------------------------------

def load_data(inventory_file, sales_file):
    """Load and clean data from CSV files."""
    try:
        inv_df = pd.read_csv(inventory_file)
        sales_df = pd.read_csv(sales_file)

        # Handle missing values
        inv_df.fillna({"Quantity": 0, "Price": 0}, inplace=True)
        sales_df.dropna(subset=["Title", "Quantity Sold", "Total Revenue"], inplace=True)

        print("Data loaded and cleaned successfully!")
        return inv_df, sales_df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None, None
    
# -------------------------------
# Sales Analysis (NumPy & Pandas)
# -------------------------------

def sales_analysis():
    """Perform analysis using Pandas & NumPy."""
    sales_df = pd.read_csv("practical_test/sales.csv")
    inv_df = pd.read_csv("practical_test/inventory.csv")

    if sales_df.empty or inv_df.empty:
        print("No data available for analysis.")
        return None, None

    total_revenue = np.sum(sales_df["Total Revenue"])
    avg_price = np.mean(inv_df["Price"])
    print(f"\nTotal Revenue:rs.{total_revenue}")
    print(f"Average Book Price:rs.{avg_price}")

    best_seller = sales_df.groupby("Title")["Quantity Sold"].sum().idxmax()
    print(f"Best-Selling Book: {best_seller}")

    return sales_df, inv_df

def detailed_sales_analysis():
    """Analyze sales trends by book, genre, and author using Pandas."""
    sales_df = pd.read_csv("practical_test/sales.csv")
    inv_df = pd.read_csv("practical_test/inventory.csv")
    
    if sales_df.empty or inv_df.empty:
        print("No data available for analysis.")
        return None

    merged_df = pd.merge(sales_df, inv_df, on="Title", how="left")

    print("\nSales Trends by Book")
    print(merged_df.groupby("Title")["Quantity Sold"].sum())

    print("\nSales Trends by Genre")
    print(merged_df.groupby("Genre")["Quantity Sold"].sum())

    print("\nSales Trends by Author")
    print(merged_df.groupby("Author")["Quantity Sold"].sum())

    return merged_df

# -------------------------------
# Data Visualization
# -------------------------------

def visualize_data(sales_df, inv_df):
    """Generate charts for insights."""
    if sales_df is None or inv_df is None:
        print("No data to visualize.")
        return

    sales_by_book = sales_df.groupby("Title")["Quantity Sold"].sum()
    sales_by_book.plot(kind="bar", color="skyblue")
    plt.title("Total Sales by Book")
    plt.xlabel("Book Title")
    plt.ylabel("Quantity Sold")
    plt.show()
    # This Bar chart shows Total Sales of Book by book Title.

    sales_df["Date"] = pd.to_datetime(sales_df["Date"])
    monthly_sales = sales_df.groupby(sales_df["Date"].dt.to_period("M"))["Quantity Sold"].sum()
    monthly_sales.plot(kind="line", marker="o")
    plt.title("Monthly Sales Trends")
    plt.ylabel("Books Sold")
    plt.show()
    # This Line chart shows Monthly Sales Trends.

    genre_revenue = inv_df.groupby("Genre")["Price"].sum()
    genre_revenue.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Revenue Share by Genre")
    plt.show()
    # This Pie chart shows Revenue Share of Book by its Genre.

    corr = inv_df[["Price","Quantity"]].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlation: Price vs Quantity")
    plt.show()
    # This Heatmap shows Correlation between Price and Quantity.

# -------------------------------
# Menu-driven Program
# -------------------------------

def main():
    store = Bookstore()
    while True:
        print("\n--- Bookstore Menu ---")
        print("1. Add Book")
        print("2. Update Inventory")
        print("3. Record Sale")
        print("4. Generate Report")
        print("5. Remove Book")
        print("6. Load & Clean Data from CSV")
        print("7. Sales Analysis (Basic)")
        print("8. Detailed Sales Trends (Book/Genre/Author)")
        print("9. Visualize Data")
        print("10. Exit")
        
        choice = input("Enter choice (1-10): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            genre = input("Enter genre: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            store.add_book(title, author, genre, price, quantity)

        elif choice == "2":
            title = input("Enter book title to update: ")
            quantity = int(input("Enter new quantity: "))
            store.update_inventory(title, quantity)

        elif choice == "3":
            title = input("Enter book title sold: ")
            quantity = int(input("Enter quantity sold: "))
            store.record_sale(title, quantity)

        elif choice == "4":
            store.generate_report()

        elif choice == "5":
            remove_book()
        
        elif choice == "6":
            inv_df, sales_df = load_data("practical_test/inventory.csv", "practical_test/sales.csv")
            if inv_df is not None and sales_df is not None:
                print("inventory.csv")
                print(inv_df.head())
                print("-----"*20)
                print("sales.csv")
                print(sales_df.head())
                print("-----"*20)

        elif choice == "7":
            sales_df, inv_df = sales_analysis()

        elif choice == "8":
            detailed_sales_analysis()

        elif choice == "9":
            sales_df, inv_df = sales_analysis()
            visualize_data(sales_df, inv_df)
            
        elif choice == "10":
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
