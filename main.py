# main.py - Main program with user interface
from datetime import datetime
from config import CATEGORIES, DATE_FORMAT
from file_operations import initialize_file, save_expense, load_all_expenses, delete_all_expenses
from calculations import calculate_total, calculate_category_totals, calculate_percentage
from validators import validate_amount, validate_category, validate_description

def add_expense():
    """Add a new expense"""
    print("\n" + "=" * 40)
    print("   💰 ADD NEW EXPENSE")
    print("=" * 40)
    
    # Get amount
    while True:
        amount_input = input("💰 Amount (in ₹): ")
        is_valid, result = validate_amount(amount_input)
        if is_valid:
            amount = result
            break
        print(f"❌ {result}")
    
    # Get category
    print(f"\n📂 Available categories: {', '.join(CATEGORIES)}")
    while True:
        category_input = input("📌 Category: ")
        is_valid, result = validate_category(category_input)
        if is_valid:
            category = result
            break
        print(f"❌ {result}")
    
    # Get description
    while True:
        description_input = input("📝 Description: ")
        is_valid, result = validate_description(description_input)
        if is_valid:
            description = result
            break
        print(f"❌ {result}")
    
    # Get current date
    date = datetime.now().strftime(DATE_FORMAT)
    
    # Save expense
    expense_data = {
        'date': date,
        'amount': amount,
        'category': category,
        'description': description
    }
    
    if save_expense(expense_data):
        print(f"\n✅ Expense added successfully!")
        print(f"   📅 {date} | ₹{amount} | {category} | {description}")
    else:
        print("\n❌ Failed to save expense!")

def show_summary():
    """Display expense summary"""
    print("\n" + "=" * 40)
    print("   📊 EXPENSE SUMMARY")
    print("=" * 40)
    
    expenses = load_all_expenses()
    
    if not expenses:
        print("\n📭 No expenses recorded yet!")
        print("   Add some expenses using option 1 first.")
        return
    
    # Display all expenses
    print("\n📋 All Expenses:")
    print("-" * 70)
    print(f"{'Date':<12} {'Amount':<12} {'Category':<15} {'Description'}")
    print("-" * 70)
    
    for exp in expenses:
        print(f"{exp['Date']:<12} ₹{float(exp['Amount']):<10.2f} {exp['Category']:<15} {exp['Description']}")
    
    print("-" * 70)
    
    # Calculate totals
    total = calculate_total(expenses)
    category_totals = calculate_category_totals(expenses)
    
    print(f"\n💵 GRAND TOTAL: ₹{total:.2f}")
    
    # Show category breakdown
    print("\n📊 CATEGORY WISE BREAKDOWN:")
    print("-" * 40)
    for cat, amt in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
        percentage = calculate_percentage(amt, total)
        bar_length = int(percentage / 2)
        bar = "█" * bar_length
        print(f"  {cat:<15} : ₹{amt:>8.2f}  ({percentage:>5.1f}%) {bar}")

def view_all_expenses():
    """Display raw expenses from CSV"""
    print("\n" + "=" * 40)
    print("   📋 ALL EXPENSES")
    print("=" * 40)
    
    expenses = load_all_expenses()
    
    if not expenses:
        print("\n📭 No expenses recorded yet!")
        return
    
    print(f"\n{'Date':<12} {'Amount':<10} {'Category':<15} {'Description'}")
    print("-" * 60)
    
    for exp in expenses:
        print(f"{exp['Date']:<12} ₹{float(exp['Amount']):<9.2f} {exp['Category']:<15} {exp['Description']}")
    
    print(f"\n📊 Total expenses: {len(expenses)}")

def main():
    """Main program loop"""
    print("\n" + "=" * 50)
    print("   💰 PERSONAL EXPENSE TRACKER")
    print("   Multi-File Professional Edition")
    print("=" * 50)
    
    # Initialize CSV file
    initialize_file()
    
    while True:
        print("\n" + "=" * 40)
        print("📱 MAIN MENU")
        print("=" * 40)
        print("1. 💰 Add Expense")
        print("2. 📊 Show Summary (with charts)")
        print("3. 📋 View All Expenses")
        print("4. 🗑️  Delete All Data")
        print("5. 🚪 Exit")
        print("=" * 40)
        
        choice = input("👉 Enter your choice (1-5): ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            view_all_expenses()
        elif choice == "4":
            confirm = input("⚠️  Delete ALL expenses? This cannot be undone! (yes/no): ")
            if confirm.lower() == "yes":
                delete_all_expenses()
            else:
                print("✅ Deletion cancelled")
        elif choice == "5":
            print("\n👋 Thank you for using Expense Tracker!")
            print("📁 Your data is saved in 'expenses.csv'")
            print("   You can open this file in Excel!")
            break
        else:
            print("❌ Invalid choice! Please enter 1-5")

if __name__ == "__main__":
    main()