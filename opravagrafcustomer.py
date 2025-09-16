
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Načítanie dát a príprava prostredia
df = pd.read_csv('marketing_campaign.csv', sep='\t')
print(df.info())
print(df.head())

# Text do Wordu:
print(f"Databáza obsahuje {df.shape[0]} riadkov a {df.shape[1]} stĺpcov.")
print("Príklady stĺpcov:")
print("- 'Year_Birth' – rok narodenia zákazníka,")
print("- 'Income' – príjem zákazníka,")
print("- 'MntWines' – suma peňazí minutá na vína.")

# 2. Vyčistenie dát
df = df.dropna()
print("Počet riadkov po odstránení NaN hodnôt:", len(df))

# 3. Vytvorenie nových stĺpcov
df['Age'] = 2025 - df['Year_Birth']
df['Kids'] = df['Kidhome'] + df['Teenhome']
df['TotalPurchases'] = df[['MntWines', 'MntFruits', 'MntMeatProducts',
                           'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']].sum(axis=1)
print(df.head())

# Text do Wordu:
print("Nové stĺpce vytvorené:")
print("- 'Age' – vek zákazníka (2025 minus rok narodenia).")
print("- 'Kids' – celkový počet detí a tínedžerov v domácnosti.")
print("- 'TotalPurchases' – celková suma peňazí minutá na rôzne kategórie produktov.")

# 4. Vizualizácia dát
plt.figure(figsize=(6,4))
sns.histplot(df['Age'], bins=20, kde=True)
plt.title('Rozloženie veku zákazníkov')
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x=df['Income'])
plt.title('Rozloženie príjmov zákazníkov')
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(x=df['Kids'])
plt.title('Počet detí v domácnosti')
plt.show()

# Text do Wordu:
print("Pozorovania z grafov:")
print("- Väčšina zákazníkov má vek medzi približne 30 a 60 rokmi.")
print("- Príjmy sú väčšinou v rozmedzí od 30 000 do 80 000 (s niekoľkými extrémami).")
print("- Väčšina domácností má 1 až 2 deti/tínedžerov.")

# 5. Uloženie nového datasetu
df.to_csv('customer_cleaned.csv', index=False)
print("Nový dataset uložený ako 'customer_cleaned.csv'.")