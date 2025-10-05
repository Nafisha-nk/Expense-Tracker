# Expense-Tracker

# Expense Tracker

A simple command-line expense tracker application to manage your personal finances. Track, categorize, and analyze your expenses with ease.

## Features

### Core Features
- ✅ **Add expenses** with description, amount, and category
- ✅ **Delete expenses** by ID
- ✅ **Update existing expenses**
- ✅ **View all expenses** in a formatted table
- ✅ **Expense summary** - total and monthly views
- ✅ **Monthly filtering** - view expenses for specific months

### Additional Features
- ✅ **Expense categories** with filtering capability
- ✅ **CSV export** - export your expenses to spreadsheet format
- ✅ **Data persistence** - automatically saves to JSON file
- ✅ **Error handling** - validates inputs and handles edge cases

## Installation

### Method 1: Direct Python Execution (Quick Start)
```bash
# Clone or download the expense_tracker.py file
python expense_tracker.py --help
```

### Method 2: Global Installation
```bash
# Make the script executable
chmod +x expense_tracker.py

# Create a symlink (Linux/Mac)
sudo ln -s $(pwd)/expense_tracker.py /usr/local/bin/expense-tracker

# On Windows, you can create a batch file or use Python directly
```

### Method 3: Using Setup Script
```bash
# Run the setup script
chmod +x setup.sh
sudo ./setup.sh
```

## Usage

### Adding Expenses
```bash
# Basic expense
expense-tracker add --description "Lunch" --amount 20

# With category
expense-tracker add --description "Groceries" --amount 85.50 --category "Food"

# Multiple categories example
expense-tracker add --description "Bus ticket" --amount 2.50 --category "Transport"
expense-tracker add --description "Movie" --amount 15 --category "Entertainment"
```

### Viewing Expenses
```bash
# List all expenses
expense-tracker list

# Filter by category
expense-tracker list --category "Food"
expense-tracker list --category "Transport"
```

### Managing Expenses
```bash
# Update an expense
expense-tracker update --id 1 --amount 25 --description "Business Lunch"

# Delete an expense
expense-tracker delete --id 2
```

### Summary and Reports
```bash
# Total summary
expense-tracker summary

# Monthly summary (month as number 1-12)
expense-tracker summary --month 8

# Export to CSV
expense-tracker export --filename my_expenses.csv
```

## Command Reference

| Command | Options | Description |
|---------|---------|-------------|
| `add` | `--description`, `--amount`, `--category` | Add new expense |
| `delete` | `--id` | Delete expense by ID |
| `update` | `--id`, `--description`, `--amount`, `--category` | Update existing expense |
| `list` | `--category` | List all expenses (optionally filtered) |
| `summary` | `--month` | Show expense summary |
| `export` | `--filename` | Export to CSV file |

## Examples

### Complete Workflow
```bash
# Add some expenses
$ expense-tracker add --description "Coffee" --amount 4.50 --category "Food"
Expense added successfully (ID: 1)

$ expense-tracker add --description "Taxi" --amount 12 --category "Transport"
Expense added successfully (ID: 2)

# View all expenses
$ expense-tracker list
ID  Date         Description  Amount     Category
1   2024-08-06   Coffee       $4.50      Food
2   2024-08-06   Taxi         $12.00     Transport

# Get summary
$ expense-tracker summary
Total expenses: $16.50

# Update an expense
$ expense-tracker update --id 1 --amount 5.25
Expense updated successfully

# Export data
$ expense-tracker export --filename august_expenses.csv
Expenses exported to august_expenses.csv successfully
```

## Data Storage

The application stores data in a JSON file (`expenses.json`) with the following structure:
```json
[
  {
    "id": 1,
    "date": "2024-08-06",
    "description": "Lunch",
    "amount": 20.0,
    "category": "Food"
  }
]
```

## Error Handling

The application includes comprehensive error handling for:
- Invalid amounts (must be positive)
- Non-existent expense IDs
- File I/O errors
- Invalid month numbers
- Missing required parameters

## Requirements

- Python 3.6 or higher
- No external dependencies - uses only Python standard library

## File Structure
```
expense-tracker/
├── expense_tracker.py  # Main application
├── expenses.json       # Data file (auto-created)
├── setup.sh           # Installation script
└── README.md          # This file
```

## Common Categories

Suggested expense categories:
- `Food` - Meals, groceries, snacks
- `Transport` - Bus, taxi, fuel, parking
- `Entertainment` - Movies, games, hobbies
- `Bills` - Utilities, rent, subscriptions
- `Shopping` - Clothes, electronics, household
- `Health` - Medicine, doctor visits
- `General` - Default category

## Tips

1. **Use consistent categories** for better filtering and analysis
2. **Export regularly** to backup your data
3. **Use monthly summaries** to track spending patterns
4. **Update descriptions** to make expenses more searchable

## Troubleshooting

**"Command not found" error:**
- Ensure the script is executable: `chmod +x expense_tracker.py`
- Use full path: `python /path/to/expense_tracker.py list`

**Permission errors:**
- Use `sudo` for system-wide installation
- Or install to user directory: `~/bin/`

**Data file issues:**
- Delete `expenses.json` to start fresh
- Check file permissions if saving fails

## License

This is a simple educational project. Feel free to modify and distribute.

## Contributing

Feel free to extend this application with features like:
- Budget setting and alerts
- Data visualization
- Recurring expenses
- Multiple currency support
- Cloud synchronization

https://roadmap.sh/projects/expense-tracker
