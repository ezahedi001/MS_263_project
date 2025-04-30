import numpy as np

def percent_grazed_by_size(test_diameter_mm, a=0.05, b=2.1):
    test_diameter_mm = np.asarray(test_diameter_mm)
    percent = a * (test_diameter_mm ** b)
    return percent

def nitrate_uptake_rate(nitrate_uM, kelp_biomass_g, vmax=1.2, km=1.5):
    nitrate_uM = np.asarray(nitrate_uM)
    kelp_biomass_g = np.asarray(kelp_biomass_g)
    uptake_per_gram = (vmax * nitrate_uM) / (km + nitrate_uM)
    total_uptake = uptake_per_gram * kelp_biomass_g
    return total_uptake


