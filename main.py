 import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# -----------------------------
# 1. Load dataset
# -----------------------------
planets = sns.load_dataset("planets")
features = ["mass", "distance", "orbital_period", "year"]
data = planets[features].dropna()
data = data[(data["mass"] > 0) & (data["distance"] > 0) & (data["orbital_period"] > 0)]

# -----------------------------
# 2. Set theme and colors
# -----------------------------
plt.style.use('default')  # רקע לבן
pink_green_cmap = sns.diverging_palette(300, 150, s=100, l=50, n=9, center="light", as_cmap=True)
star_color = "yellow"  # צבע פנימי של כוכבים
edge_color = "black"   # מסגרת הכוכבים

# -----------------------------
# 3. Histograms
# -----------------------------
plt.figure(figsize=(12, 8))
for i, col in enumerate(["mass", "distance", "orbital_period"]):
    plt.subplot(2, 2, i+1)
    sns.histplot(
        data[col],
        bins=40,
        color="#FF69B4",  #ורוד 
        edgecolor="#32CD32",  # ירוק למסגרות
        alpha=0.8
    )
    plt.title(f"{col} Distribution", fontsize=14)
plt.tight_layout()
plt.savefig("histograms.png", dpi=300, facecolor='white')
plt.show()
plt.close()

# -----------------------------
# 4. Scatter plot — Mass vs Distance
# -----------------------------
plt.figure(figsize=(10, 6))
plt.scatter(
    data['distance'],
    data['mass'],
    s=60,
    marker='*',
    c=star_color,
    edgecolors=edge_color,
    linewidths=1.1,
    alpha=0.8
)
plt.xscale('log')
plt.yscale('log')
plt.title("Mass vs Distance", fontsize=18, color="#FF00AA")
plt.xlabel("Distance")
plt.ylabel("Mass")
plt.grid(True, alpha=0.2)
plt.tight_layout()
plt.savefig("scatter_mass_distance.png", dpi=300, facecolor='white')
plt.show()
plt.close()

# -----------------------------
# 5. Scatter plot — Orbital Period vs Mass
# -----------------------------
plt.figure(figsize=(10, 6))
plt.scatter(
    data['orbital_period'],
    data['mass'],
    s=60,
    marker='*',
    c=star_color,
    edgecolors=edge_color,
    linewidths=1.1,
    alpha=0.8
)
plt.xscale('log')
plt.yscale('log')
plt.title("Orbital Period vs Mass", fontsize=18, color="#FF00AA")
plt.xlabel("Orbital Period")
plt.ylabel("Mass")
plt.grid(True, alpha=0.2)
plt.tight_layout()
plt.savefig("scatter_period_mass.png", dpi=300, facecolor='white')
plt.show()
plt.close()

# -----------------------------
# 6. Correlation Heatmap
# -----------------------------
plt.figure(figsize=(8,6))
sns.heatmap(
    data.corr(),
    annot=True,
    cmap=pink_green_cmap,
    linewidths=0.5,
    fmt=".2f",
    vmin=-1, vmax=1
)
plt.title("Correlation Heatmap — Planets Dataset", color="black", fontsize=16)
plt.tight_layout()
plt.savefig("correlation.png", dpi=300, facecolor='white')
plt.show()
plt.close()
