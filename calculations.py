# calculations.py - Math and summary calculations

def calculate_total(expenses):
    """Calculate total of all expenses"""
    if not expenses:
        return 0
    return sum(float(e['Amount']) for e in expenses)

def calculate_category_totals(expenses):
    """Calculate totals per category"""
    totals = {}
    for exp in expenses:
        cat = exp['Category']
        totals[cat] = totals.get(cat, 0) + float(exp['Amount'])
    return totals

def calculate_percentage(amount, total):
    """Calculate percentage of total"""
    if total == 0:
        return 0
    return (amount / total) * 100