# validators.py - Input validation functions
from config import CATEGORIES

def validate_amount(amount_str):
    """Validate and convert amount to float"""
    try:
        amount = float(amount_str)
        if amount <= 0:
            return False, "Amount must be greater than zero"
        if amount > 1000000:
            return False, "Amount seems too high! Please check"
        return True, amount
    except ValueError:
        return False, "Please enter a valid number"

def validate_category(category):
    """Validate category exists"""
    if not category:
        return False, "Category cannot be empty"
    category = category.capitalize()
    if category in CATEGORIES:
        return True, category
    else:
        return False, f"Category must be one of: {', '.join(CATEGORIES)}"

def validate_description(description):
    """Validate description"""
    if not description.strip():
        return False, "Description cannot be empty"
    return True, description.strip()