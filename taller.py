import pandas as pd

data = {
    "ID": [1,2,3,4,5,6,7,8,9,10],
    "Producto": ["Laptop", "Monitor", "Teclado", "Laptop", "Tablet", "Impresora", "Smartphone", "Mouse", "Monitor", "Tablet"],
    "Categoría": ["Electrónica", "Computación", "Accesorios", "Electrónica", "Computación", "Oficina", "Electrónica", "Accesorios", "Computación", "Computación"],
    "Ventas": [15, 8, 25, 10, 20, 5, 30, 40, 12, 18],
    "Precio Unitario": [1200, 500, 50, 1100, 700, 400, 800, 20, 450, 750],
    "Total Ventas": [18000, 4000, 1250, 11000, 14000, 2000, 24000, 800, 5400, 13500],
    "Región": ["Norte", "Sur", "Norte", "Este", "Oeste", "Norte", "Sur", "Este", "Oeste", "Norte"]
}

print(data)

df = pd.DataFrame(data)

print(df)

#cantidad total de productos vendidos
print(df['Ventas'].sum())

print(df['Ventas'].mean())
print(df['Ventas'].std())
print(df.describe())
categoriaMasVendida = df.groupby('Categoría')['Ventas'].sum().idxmax()
print(categoriaMasVendida)

productosMayores = df[df['Precio Unitario']>500]

print(productosMayores)

df['ValorMasIVA'] = df['Precio Unitario'] * 1.19

print(df)

print(df[['Producto','Precio Unitario','ValorMasIVA']])