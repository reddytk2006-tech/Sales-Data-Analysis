import pandas as pd

data = {
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Laptop', 'Mobile'],
    'Sales': [50000, 30000, 15000, 45000, 25000]
}

df = pd.DataFrame(data)

print("Sales Data:")
print(df)

print("\nTotal Sales:", df['Sales'].sum())
print("Average Sales:", df['Sales'].mean())
print("Highest Sale:", df['Sales'].max())
