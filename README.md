# Urchin Foraging on Giant Kelp

This repository contains a final project analyzing how sea urchin size and density affect the consumption of giant kelp (*Macrocystis pyrifera*), using data from the Santa Barbara Coastal Long Term Ecological Research (SBC-LTER) program.

---

## Repository Structure

```
kelp-urchin-project/
├── Urchin Kelp Analysis.ipynb    # Main analysis notebook
├── load_sbc_lter_data.py         # Reusable function to load and format SBC-LTER data
├── density.csv                   # Experimental data: kelp consumption vs urchin density
├── size.csv                      # Experimental data: kelp consumption vs urchin size
├── README.md                     # Project overview and instructions
└── .gitignore                    # Exclude unnecessary files from repo
```

---

## Project Summary

Kelp forests are among the most productive and ecologically significant marine ecosystems, forming a foundational habitat that supports a diverse array of species across trophic levels. At the heart of these systems is Macrocystis pyrifera, the giant kelp, which is a canopy forming brown alga with rapid growth and high primary productivity that fuels complex food webs and nutrient cycling dynamics. The physiological performance of M. pyrifera is tightly linked to the availability of dissolved inorganic nutrients, particularly nitrate. Nitrogen is a critical macronutrient required for the synthesis of chlorophyll, amino acids, and proteins, and thus directly influences both the growth rate and tissue composition of kelp (Gerard et al. 1987; Wheeler & North 1980). In nutrient limited conditions, even optimal light and temperature regimes may not be sufficient to sustain high kelp productivity (Tegner & Dayton 1987).

This project investigates how:
- Different **size classes** of urchins affect grazing pressure on kelp
- **Urchin density** affects per-individual consumption

This work helps us to better undertsand our changing ecosystems, especially when under the pressure of a changing climate. By conducitng grazing trials in a laboratory setting, we are able to gather data on how urchin consumption may vary. 

Data comes from SBC-LTER experiments. Analyses include data cleaning, statistical testing (ANOVA), and visualizations (boxplots). Results help interpret dynamics that drive kelp forest collapse into urchin barrens.

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

Citations:
> DiFiore, B., Rennick, M., Curtis, J., Reed, D., Stier, A. (2021). SBC LTER: Sea urchin foraging rates on giant kelp. Environmental Data Initiative. https://doi.org/10.6073/pasta/6af4cc3b0e63b887baf1ae9201e1cd1d
> Bracken, M. E. S., Jones, E. & Williams, S. L. 2012. Herbivore-algae interactions across scales: spatial variability and ecosystem consequences. J. Phycol. 48:480–491. https://doi.org/10.1111/j.1529-8817.2012.01168.x
> Filbee-Dexter, K. & Scheibling, R. E. 2014. Sea urchin barrens as alternative stable states of collapsed kelp ecosystems. Mar. Ecol. Prog. Ser. 495:1–25. https://doi.org/10.3354/meps10573
> Fram, J. P., Stewart, H. L., Brzezinski, M. A., Gaylord, B., Reed, D. C., Williams, S. L. & MacIntyre, S. 2008. Physical pathways and utilization of nitrate supply to the giant kelp, Macrocystis pyrifera. Limnol. Oceanogr. 53:1589–1603. https://doi.org/10.4319/lo.2008.53.4.1589
> Gerard, V. A., DuBois, K. R. & North, W. J. 1987. Growth, nutrient uptake, and nutrient content of Macrocystis pyrifera(Phaeophyceae) from different populations in California. J. Phycol. 23:77–83. https://doi.org/10.1111/j.1529-8817.1987.tb04119.x
> Hurd, C. L., Harrison, P. J., Bischof, K. & Lobban, C. S. 2014. Seaweed Ecology and Physiology, 2nd ed. Cambridge University Press, Cambridge, UK, 551 pp.
> Okamoto, D. K. 2014. Resource limitation affects the strength of size-dependent competition in sea urchins. Ecology95:3083–3096. https://doi.org/10.1890/13-1576.1
> Spindel, N. B., Carr, M. H. & Baskett, M. L. 2021. Grazing pressure and environmental variability interact to shape kelp forest resilience. Ecol. Appl. 31:e02391. https://doi.org/10.1002/eap.2391
> Tegner, M. J. & Dayton, P. K. 1987. El Niño effects on southern California kelp forest communities. Adv. Ecol. Res.17:243–279. https://doi.org/10.1016/S0065-2504(08)60247-0
> Wheeler, W. N. & North, W. J. 1980. Effect of nitrogen supply on growth and nitrogen content of Macrocystis pyrifera(Phaeophyta) in culture. J. Phycol. 16:418–422. https://doi.org/10.1111/j.1529-8817.1980.tb03058.x

---

## Future Directions

This analysis can be expanded to consider:
- Kelp nutritional quality (C:N ratios, N content)
- Urchin gonad development and reproductive investment
- Temporal and spatial comparisons across regions
Future research outline:
The goal of this research is to investigate how geographic variability in nitrate availability, driven by natural landmarks and upwelling dynamics, affects Macrocystis pyrifera tissue composition and how these variabilities affect Strongylocentrotus purpuratus feeding, growth, and reproductive investment. By integrating field measurements, laboratory experiments, and comparisons across spatial and thermal gradients, this study seeks to clarify the mechanistic links between nutrient delivery, primary producer quality, and herbivore performance. It begins by examining how nitrate availability varies across Monterey Bay and how these differences are reflected in kelp tissue traits such as carbon to nitrogen ratios and chlorophyll content (Fram et al. 2008). These site specific differences in kelp nutrient quality are then used to test how resource variability influences urchin consumption rates, test growth, and gonadal development. Laboratory experiments based on values from field collections allow direct linkage between environmental nutrient variability and grazer performance metrics. The study also investigates how these nutrient effects are modulated by temperature, a key environmental driver of metabolic demand, to determine whether nutrient limitation exacerbates or mitigates the physiological impacts of warming (Hurd et al. 2014). Finally, a broader comparative framework will assess how landmark-driven variation in algal nutrient content and herbivore reproductive investment compares between temperate and tropical ecosystems, helping to determine whether consistent trophic responses to nutrient supply variation emerge across diverse marine environments.
Taken together, this study will advance our understanding of how foundational species like kelp respond to physical and chemical variability in coastal environments, and how such responses cascade up to affect herbivore populations. In doing so, it addresses a pressing ecological question: How will the foundational interactions between producers and consumers in marine ecosystems be changed in a rapidly changing climate? Given kelp’s critical and urchins in the structure and stability of temperate reef systems, highlighting these dynamics is essential for predicting and potentially managing the resilience of these ecosystems in a changing world.


