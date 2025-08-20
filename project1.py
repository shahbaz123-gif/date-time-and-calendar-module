import calendar

# Get all month names
months = list(calendar.month_name)[1:]  # Remove empty first element

print("Months of the year:")
for i, month in enumerate(months, 1):
    print(f"{i:2d}. {month}")