# Cosmic Expansion Dataset

This script provides an embedded dataset of redshift and comoving distance measurements from Type Ia supernovae and a minimal Python class to load and parse the data in memory.

These measurements can be used for studying cosmic expansion, Hubble's law, and dark energy models.

---

## 🚀 Overview

The dataset is embedded directly in the script as a multi-line string using CSV format. The class `CosmicExpansionDataset` reads and parses this data on instantiation.

Each data entry contains:
- `redshift` (z): Dimensionless, derived from supernova light spectra.
- `distance_mpc`: Comoving distance in megaparsecs (Mpc), assuming a cosmological model.

---

## 📦 Features

- **Zero I/O**: Data is embedded in the script—no need for external files.
- **Lightweight**: Pure Python solution with no required dependencies.
- **Ready for analysis**: Converts the dataset into a pandas `DataFrame` for easy manipulation and plotting.

---

## 🧪 Example Usage

```python
from cosmic_expansion import CosmicExpansionDataset

dataset = CosmicExpansionDataset()
df = dataset.df

# Accessing the redshift and distance columns
print(df.head())

# Example: Plotting the Hubble diagram
import matplotlib.pyplot as plt

plt.scatter(df['redshift'], df['distance_mpc'], s=10)
plt.xlabel('Redshift (z)')
plt.ylabel('Distance (Mpc)')
plt.title('Hubble Diagram')
plt.grid(True)
plt.show()
