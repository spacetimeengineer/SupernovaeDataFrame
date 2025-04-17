# Cosmic Expansion Dataset

This script provides an embedded dataset of redshift and comoving distance measurements from Type Ia supernovae and a minimal Python class to load and parse the data in memory.

These measurements can be used for studying cosmic expansion, Hubble's law, and dark energy models.

---

## 🚀 Overview

The dataset is embedded directly in the script as a multi-line string using CSV format. The class `CosmologicalExpansionAnalyzer` reads and parses this data on instantiation.

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

After installing the package, simply type the following command in your terminal:

```bash
cosmoexp
```

This will automatically load the dataset and display a Hubble diagram, showcasing the relationship between redshift and comoving distance.

No additional setup or coding is required except anything that you might contribute.

