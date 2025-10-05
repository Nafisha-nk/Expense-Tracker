#!/usr/bin/env python3
"""
Simple Expense Tracker Application
"""

import argparse
import json
import csv
import os
from datetime import datetime
from typing import List, Dict, Optional

# Data file to store expenses
DATA_FILE = "expenses.json"

class ExpenseTracker:
    def __init__(self, data_file: str = DATA_FILE):
        self.data_file = data_file
        self.expenses = self.load_expenses()
    
    def load_expenses(self) -> List[Dict]:
        """Load expenses from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return []
        return []
    
    def save_expenses(self):
        """Save expenses to JSON file"""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.expenses, f, indent=2)
        except IOError as e:
            print(f"Error saving expenses: {e}")
    
    def get_next_id(self) -> int:
        """Get next available expense ID"""
        if not self.expenses:
            return 1
        return max(expense['id'] for expense in self.expenses) + 1
    
    def add_expense(self, description: str, amount: float, category: str = "General") -> int:
        """Add a new expense"""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        expense = {
            'id': self.get_next_id(),
            'date': datetime.now().strftime("%Y-%m-%d"),
            'description': description,
            'amount': amount,
            'category': category
        }
        
        self.expenses.append(expense)
        self.save_expenses()
        return expense['id']
    
    def delete_expense(self, expense_id: int) -> bool:
        """Delete an expense by ID"""
        for i, expense in enumerate(self.expenses):
            if expense['id'] == expense_id:
                del self.expenses[i]
                self.save_expenses()
                return True
        return False
    
    def update_expense(self, expense_id: int, description: str = None, 
                    amount: float = None, category: str = None) -> bool:
        """Update an existing expense"""
        for expense in self.expenses:
            if expense['id'] == expense_id:
                if description is not None:
                    expense['description'] = description
                if amount is not None:
                    if amount <= 0:
                        raise ValueError("Amount must be positive")
                    expense['amount'] = amount
                if category is not None:
                    expense['category'] = category
                self.save_expenses()
                return True
        return False
    
    def list_expenses(self, category: str = None):
        """List all expenses, optionally filtered by category"""
        filtered_expenses = self.expenses
        
        if category:
            filtered_expenses = [e for e in self.expenses if e['category'].lower() == category.lower()]
        
        if not filtered_expenses:
            print("No expenses found.")
            return
        
        print(f"{'ID':<4} {'Date':<12} {'Description':<20} {'Amount':<10} {'Category':<15}")
        print("-" * 65)
        
        for expense in filtered_expenses:
            print(f"{expense['id']:<4} {expense['date']:<12} {expense['description']:<20} "
                f"${expense['amount']:<9.2f} {expense['category']:<15}")
    
    def get_summary(self, month: int = None) -> float:
        """Get total expenses, optionally for a specific month"""
        if month:
            current_year = datetime.now().year
            monthly_expenses = [
                e for e in self.expenses 
                if datetime.strptime(e['date'], "%Y-%m-%d").month == month
                and datetime.strptime(e['date'], "%Y-%m-%d").year == current_year
            ]
            total = sum(e['amount'] for e in monthly_expenses)
        else:
            total = sum(e['amount'] for e in self.expenses)
        
        return total
    
    def export_to_csv(self, filename: str = "expenses_export.csv"):
        """Export expenses to CSV file"""
        try:
            with open(filename, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['id', 'date', 'description', 'amount', 'category'])
                writer.writeheader()
                writer.writerows(self.expenses)
            return True
        except IOError as e:
            print(f"Error exporting to CSV: {e}")
            return False

def main():
    tracker = ExpenseTracker()
    
    parser = argparse.ArgumentParser(description="Simple Expense Tracker")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new expense')
    add_parser.add_argument('--description', required=True, help='Expense description')
    add_parser.add_argument('--amount', type=float, required=True, help='Expense amount')
    add_parser.add_argument('--category', default='General', help='Expense category')
    
    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete an expense')
    delete_parser.add_argument('--id', type=int, required=True, help='Expense ID to delete')
    
    # Update command
    update_parser = subparsers.add_parser('update', help='Update an expense')
    update_parser.add_argument('--id', type=int, required=True, help='Expense ID to update')
    update_parser.add_argument('--description', help='New description')
    update_parser.add_argument('--amount', type=float, help='New amount')
    update_parser.add_argument('--category', help='New category')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List all expenses')
    list_parser.add_argument('--category', help='Filter by category')
    
    # Summary command
    summary_parser = subparsers.add_parser('summary', help='Show expense summary')
    summary_parser.add_argument('--month', type=int, help='Month number (1-12)')
    
    # Export command
    export_parser = subparsers.add_parser('export', help='Export expenses to CSV')
    export_parser.add_argument('--filename', default='expenses_export.csv', help='Output filename')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    try:
        if args.command == 'add':
            expense_id = tracker.add_expense(args.description, args.amount, args.category)
            print(f"Expense added successfully (ID: {expense_id})")
        
        elif args.command == 'delete':
            if tracker.delete_expense(args.id):
                print("Expense deleted successfully")
            else:
                print(f"Error: Expense with ID {args.id} not found")
        
        elif args.command == 'update':
            if tracker.update_expense(args.id, args.description, args.amount, args.category):
                print("Expense updated successfully")
            else:
                print(f"Error: Expense with ID {args.id} not found")
        
        elif args.command == 'list':
            tracker.list_expenses(args.category)
        
        elif args.command == 'summary':
            total = tracker.get_summary(args.month)
            if args.month:
                month_name = datetime(2024, args.month, 1).strftime("%B")
                print(f"Total expenses for {month_name}: ${total:.2f}")
            else:
                print(f"Total expenses: ${total:.2f}")
        
        elif args.command == 'export':
            if tracker.export_to_csv(args.filename):
                print(f"Expenses exported to {args.filename} successfully")
            else:
                print("Error exporting expenses")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()