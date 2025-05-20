# Urchin Foraging on Giant Kelp

This repository contains a final project analyzing how sea urchin size and density affect the consumption of giant kelp (*Macrocystis pyrifera*), using data from the Santa Barbara Coastal Long Term Ecological Research (SBC-LTER) program.

---

## 📂 Repository Structure

```
kelp-urchin-project/
├── Urchin Kelp Analysis.ipynb    # Main analysis notebook
├── load_sbc_lter_data.py         # Reusable function to load and format SBC-LTER data
├── density.csv                   # Experimental data: kelp consumption vs urchin density
├── size.csv                      # Experimental data: kelp consumption vs urchin size
├── README.md                     # Project overview and instructions
├── figures/                      # (Optional) Exported figures
└── .gitignore                    # Exclude unnecessary files from repo
```

---

## Project Summary

This project investigates how:
- Different **size classes** of urchins affect grazing pressure on kelp
- **Urchin density** affects per-individual consumption

Data come from SBC-LTER experiments. Analyses include data cleaning, statistical testing (t-tests), and visualizations (boxplots). Results help interpret dynamics that drive kelp forest collapse into urchin barrens.

---

## How to Run the Project

1. Clone the repository:
```bash
git clone https://github.com/your-username/kelp-urchin-project.git
cd kelp-urchin-project
```

2. Open the notebook in Jupyter:
```bash
jupyter notebook "Urchin Kelp Analysis.ipynb"
```

3. Run all cells in order. This requires Python 3.7+ and the following modules:
```bash
pip install pandas matplotlib seaborn scipy
```

---

## Data Sources

This project uses publicly available data from:
- **Santa Barbara Coastal LTER**
  - [Dataset Metadata](https://pasta.lternet.edu/package/metadata/eml/knb-lter-sbc/145/1)
  - Raw data retrieved via `load_sbc_lter_data.py`

If working offline, you may use the included `density.csv` and `size.csv` files.

---

## Dependencies
- Python 3.7 or higher
- pandas
- matplotlib
- seaborn
- scipy

---

## Acknowledgements

This project is based on data provided by:
- Bartholomew DiFiore, Mae Rennick, Joseph Curtis, Daniel Reed, Adrian Stier (SBC LTER)

Citation:
> DiFiore, B., Rennick, M., Curtis, J., Reed, D., Stier, A. (2021). SBC LTER: Sea urchin foraging rates on giant kelp. Environmental Data Initiative. https://doi.org/10.6073/pasta/6af4cc3b0e63b887baf1ae9201e1cd1d

---

## Future Directions

This analysis can be expanded to consider:
- Kelp nutritional quality (C:N ratios, N content)
- Urchin gonad development and reproductive investment
- Temporal and spatial comparisons across regions

