import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r'C:\Users\dell\Downloads\Personal_Finance_Dataset.csv')

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# Total Income vs Expense
summary = df.groupby('Type')['Amount'].sum()
print("Total Income vs Expense:")
print(summary)

# Expenses by Category
expenses = df[df['Type'] == 'Expense'].groupby('Category')['Amount'].sum().sort_values(ascending=False)
print("\nExpenses by Category:")
print(expenses)

# Bar chart - Expenses by Category
plt.figure(figsize=(10, 6))
sns.barplot(x=expenses.values, y=expenses.index, palette='Reds_r')
plt.title('Total Expenses by Category (2020-2024)')
plt.xlabel('Total Amount ($)')
plt.ylabel('Category')
plt.tight_layout()
plt.savefig(r'C:\Users\dell\Desktop\expenses_by_category.png')
plt.show()
print("Chart saved to Desktop!")

# Line chart - Income vs Expense by Year
yearly = df.groupby(['Year', 'Type'])['Amount'].sum().unstack()
plt.figure(figsize=(10, 6))
plt.plot(yearly.index, yearly['Expense'], marker='o', color='red', label='Expense')
plt.plot(yearly.index, yearly['Income'], marker='o', color='green', label='Income')
plt.title('Income vs Expense Trend (2020-2024)')
plt.xlabel('Year')
plt.ylabel('Total Amount ($)')
plt.legend()
plt.tight_layout()
plt.savefig(r'C:\Users\dell\Desktop\income_vs_expense_trend.png')
plt.show()
print("Trend chart saved!")