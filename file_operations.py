# file_operations.py - Handle CSV file operations
import csv
import os
from config import FILE_NAME

def initialize_file():
    """Create CSV file with headers if it doesn't exist"""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category", "Description"])
        print("📁 New expenses.csv file created!")
        return True
    return False

def save_expense(expense_data):
    """Save a single expense to CSV file"""
    try:
        with open(FILE_NAME, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                expense_data['date'],
                expense_data['amount'],
                expense_data['category'],
                expense_data['description']
            ])
        return True
    except Exception as e:
        print(f"Error saving expense: {e}")
        return False

def load_all_expenses():
    """Load all expenses from CSV file"""
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except Exception as e:
        print(f"Error loading expenses: {e}")
        return []

def delete_all_expenses():
    """Delete all expenses (reset the file)"""
    initialize_file()
    print("🗑️ All expenses deleted!")