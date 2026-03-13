# Bookstore Inventory and Analytics System

## Project Overview

The **Bookstore Inventory and Analytics System** is a Python-based application that helps manage bookstore inventory and analyze sales data.
It uses **Object-Oriented Programming (OOP)** along with **NumPy, Pandas, Matplotlib, and Seaborn** for data analysis and visualization.

The system allows users to add books, update inventory, record sales, and generate analytical reports from CSV data.

---

# Features

* Menu-driven user interface
* Add, update, and remove books from inventory
* Record book sales
* Load and clean data from CSV files
* Perform sales analysis using **NumPy & Pandas**
* Visualize data using **Matplotlib & Seaborn**

---

# Technologies Used

* **Python**
* **NumPy**
* **Pandas**
* **Matplotlib**
* **Seaborn**

---

# Project Structure

```
bookstore-project/
│
├── bookstore_system.py   # Main Python program
├── inventory.csv         # Inventory dataset
├── sales.csv             # Sales dataset
└── README.md             # Project documentation
```

---

# CSV File Format

## inventory.csv

```
Title,Author,Genre,Price,Quantity
Python Basics,John,Programming,500,10
Data Science 101,Jane Smith,Analytics,700,5
```

## sales.csv

```
Title,Quantity Sold,Total Revenue,Date
Python Basics,2,1000,2026-01-05
Data Science 101,1,700,2026-01-10
```

---

# How to Run the Project

1. Install required libraries:

```
pip install numpy pandas matplotlib seaborn
```

2. Run the program:

```
python bookstore_system.py
```

3. Use the menu options to manage inventory and analyze sales.

---

# Data Visualization

The program generates the following charts:

* **Bar Chart** → Total sales by book
* **Line Chart** → Monthly sales trend
* **Pie Chart** → Revenue share by genre
* **Heatmap** → Correlation between price and quantity

---

# Learning Outcomes

This project demonstrates:

* Object-Oriented Programming in Python
* Data analysis using Pandas & NumPy
* Data visualization using Matplotlib & Seaborn
* CSV data handling and cleaning
* Menu-driven Python applications

---

# Author

**Dhyani Gandhi**

