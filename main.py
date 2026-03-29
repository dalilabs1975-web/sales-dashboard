import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Charger le CSV
df = pd.read_csv("Sales.csv")

# Nettoyer noms de colonnes
df.columns = df.columns.str.strip().str.replace(' ', '_')

# Colonnes numériques
colonnes_num = ['Units_Sold', 'Manufacturing_Price', 'Sale_Price',
                'Gross_Sales', 'Discounts', 'Sales', 'COGS', 'Profit']

# Nettoyer et convertir en float
for col in colonnes_num:
    df[col] = df[col].astype(str).str.replace('[\$,]', '', regex=True)
    df[col] = pd.to_numeric(df[col], errors='coerce')

# ============================
# 1. Profit par pays
# ============================
profit_par_pays = df.groupby("Country")["Profit"].sum()

plt.figure()
plt.bar(profit_par_pays.index, profit_par_pays.values)
plt.xticks(rotation=45)
plt.title("Profit par pays")
plt.xlabel("Pays")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()
plt.savefig("Country.png")

# ============================
# 2. Ventes par mois
# ============================
ventes_par_mois = df.groupby("Month_Name")["Sales"].sum()

# ordre des mois
ordre_mois = ['January','February','March','April','May','June',
              'July','August','September','October','November','December']

ventes_par_mois = ventes_par_mois.reindex(ordre_mois)

plt.figure()
plt.bar(ventes_par_mois.index, ventes_par_mois.values)
plt.xticks(rotation=45)
plt.title("Ventes par mois")
plt.xlabel("Mois")
plt.ylabel("Ventes")
plt.tight_layout()
plt.show()
plt.savefig("mois.png")

# ============================
# 3. Pertes (Profit < 0)
# ============================
pertes = df[df["Profit"] < 0]
pertes_par_pays = pertes.groupby("Country")["Profit"].sum()

plt.figure()
plt.bar(pertes_par_pays.index, pertes_par_pays.values)
plt.xticks(rotation=45)
plt.title("Pertes par pays")
plt.xlabel("Pays")
plt.ylabel("Profit négatif")
plt.tight_layout()
plt.show()
plt.savefig("Pertes.png")

# ============================
#  4. Top 3 produits
# ============================
top_produits = df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(3)

plt.figure()
plt.bar(top_produits.index, top_produits.values)
plt.title("Top 3 produits par ventes")
plt.xlabel("Produit")
plt.ylabel("Ventes")
plt.tight_layout()
plt.show()
# Sauvegarde image
plt.savefig("Top Produit.png")


