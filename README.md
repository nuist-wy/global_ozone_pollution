# global_ozone_pollution
Code for "Substantially underestimated global health risks of current ozone pollution"

## Abstract
> Existing assessments might have underappreciated ozone-related health impacts worldwide. Here our study deeply assesses current global ozone pollution using the high-resolution (0.05°) estimation from a geo-ensemble learning model, crucially focusing on population exposure and all-cause mortality burden. Our model demonstrates strong performance, with a mean bias of less than -1.5 parts per billion against in-situ measurements. We estimate that 66.2% of the global population is exposed to excess ozone for short term (> 30 days per year), and 94.2% suffers from long-term exposure. Furthermore, severe ozone exposure levels are observed in Cropland areas, particularly over Asia. Importantly, the all-cause ozone-attributable deaths significantly surpass previous recognition from specific diseases worldwide. Notably, mid-latitude Asia (30°N) and the western United States show high mortality burden, contributing substantially to global ozone-attributable deaths. Our study highlights current significant global ozone-related health risks and may benefit the ozone-exposed population in the future.

## 🧩 Install
```
git clone https://github.com/nuist-wy/global_ozone_pollution.git
```

## 🧩 Environment
 > * Matlab 2023b
 > * Python 3.8

## 🧩 Python libraries
 > * netCDF4 
 > * numpy
 > * scipy
 > * natsort
 > * h5py
 > * lightgbm
 > * xgboost
 > * deep-forest
 > * scikit-learn
 > * shutil
 > * pickle

 ## 🧩 Usage
 ### Validation (SICV)
- **Step I.**  Divide the grids into blocks.
```
matlab -batch "run('div_grid.m')"
```
- **Step II.**  Calculate the global-local relations of blocks.
```
matlab -batch "run('cal_relation.m')"
```
- **Step III.**  Train the GL-CEF model.
```
python fold.py
python site_model.py
```
- **Step IV.**  Validate the model performance.
```
python site_eva.py
```

 ### Validation (TESICV)
- **Step I.**  Divide the grids into blocks.
```
matlab -batch "run('div_grid_t.m')"
```
- **Step II.**  Calculate the global-local relations of blocks.
```
matlab -batch "run('cal_relation_t.m')"
```
- **Step III.**  Train the GL-CEF model.
```
python fold_t.py
python site_model_t.py
```
- **Step IV.**  Validate the model performance.
```
python site_eva_t.py
```

 ### Estimation and visualization
- **Step I.**  Divide the grids into blocks.
```
matlab -batch "run('div_grid_gen.m')"
```
- **Step II.**  Calculate the global-local relations of blocks.
```
matlab -batch "run('cal_relation_gen.m')"
```
- **Step III.**  Train the GL-CEF model.
```
python fit_allmodel.py
python site_model_gen.py
```
- **Step IV.**  Estimate ambient ozone concentrations.
```
python pre_allmodel.py
python site_pre.py
```
- **Step V.**  Visualize the results.
```
matlab -batch "run('getr.m ')"
python convert_to_nc.py 
python map.py
```
