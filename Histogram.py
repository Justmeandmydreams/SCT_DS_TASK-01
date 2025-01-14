import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate a sample population data
np.random.seed(42)
ages = np.random.randint(0, 100, 1000)  # Generate 1000 random ages between 0 and 99

# Save the data to a CSV file
data = pd.DataFrame({'Age': ages})
data.to_csv('population_data.csv', index=False)  # Save to CSV

# Create an advanced histogram
plt.figure(figsize=(12, 8))
sns.histplot(data['Age'], bins=20, kde=True, color='teal', edgecolor='black', alpha=0.7)

# Overlay KDE shading
sns.kdeplot(data['Age'], color='blue', fill=True, alpha=0.3, linewidth=2)

# Customize the plot
plt.title("Advanced Age Distribution of Population", fontsize=16, fontweight='bold')
plt.xlabel("Age", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', alpha=0.4, linestyle='--')

# Ensure x-axis starts from 0
plt.xlim(0, 100)

# Annotate bar heights
for p in sns.histplot(data['Age'], bins=20, kde=False, color='teal', edgecolor='black', alpha=0.7).patches:
    plt.annotate(
        format(int(p.get_height()), ","),
        (p.get_x() + p.get_width() / 2., p.get_height()),
        ha='center', va='center',
        xytext=(0, 8),
        textcoords='offset points',
        fontsize=10,
        color='black'
    )

plt.tight_layout()
plt.show()
