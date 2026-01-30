import pandas as pd

raw = {
    "product": ["Widget A", "Widget B", "Widget C"],
    "price": ["$1,234.50", "$567.89", "$2,345.00"],
    "quantity": [10, 5, None],
}

df = pd.DataFrame(raw)

# 1 Clean price column
df['price'] = df['price'].apply(lambda x: float(x.replace('$', '').replace(',', '')))

# 2 Fill missing quantity values with 0
df['quantity'] = df['quantity'].fillna(0)

# 3 Create total column by multiplying price and quantity
df['total'] = df['price'] * df['quantity']

# 4 Add price_category column, low / med / high
df['price_category'] = df['price'].apply(
    lambda x: 'low' if x < 1000 else ('high' if x > 2000 else 'med'))

print(df)