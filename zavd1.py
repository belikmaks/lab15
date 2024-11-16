import pandas as pd

data = {
    'Country': ['Ukraine', 'Ukraine', 'Poland', 'Poland', 'Germany', 'Germany'],
    'Category': ['Groceries', 'Electronics', 'Groceries', 'Electronics', 'Groceries', 'Electronics'],
    'Sales': [2000, 3500, 1800, 4000, 2200, 5000],
    'Quantity': [150, 70, 120, 80, 130, 90]
}

df = pd.DataFrame(data)

aggregated_data = df.groupby(['Country', 'Category']).agg({
    'Sales': 'sum',
    'Quantity': 'sum'
}).reset_index()

print("Початкові дані:")
print(df)
print("\nАгреговані дані:")
print(aggregated_data)
