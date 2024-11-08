# global_ozone_pollution
Code for "Substantially underestimated global health risks of current ozone pollution"

## Abstract
> Global ozone (O₃) pollution was increasing, posing serious threats to human health and the ecological environment. Existing assessments might have underappreciated O₃-related health impacts worldwide due to their reliance on partial conditions (e.g., specific diseases, limited countries, or single O₃ source) and coarse-resolution holistic models. Here our study deeply assessed current global O₃ pollution using a geo-ensemble learning model (GL-CEF), with key focuses on population exposure and all-cause mortality burden. The GL-CEF model demonstrated strong performance in estimating global daily seamless ambient O₃ concentrations at high resolution (0.05°), achieving a mean bias of less than -1.5 ppb. We estimated that 66.2% of the global population was exposed to excess ambient O₃ for short term (> 30 days per year), and 94.2% suffered from long-term O₃ exposure. Notably, severe short- and long-term O₃ exposure levels were observed in Cropland areas, particularly over Asia. Importantly, 0.177 million (95% confidence interval [CI]: 0.139, 0.214) and 1.407 million (95% CI: 0.909, 1.896) all-cause deaths per year were attributed to short- and long-term O₃ exposure worldwide, respectively, significantly surpassing previous recognition from specific diseases. Furthermore, mid-latitude Asia (30°N) and the western United States showed high mortality burden due to O₃ exposure, contributing substantially to global O₃-attributable deaths. Our study highlighted current significant global O₃-related health risks and may effectively benefit the population exposed to O₃ pollution in the future.

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
 ### Validation (SICV or TESICV)
- **Step I.**  Divide the grids into blocks.
```
matlab -batch "run('div_grid.m')"
or
matlab -batch "run('div_grid_t.m')"
```
- **Step II.**  Calculate the global-local relations of blocks.
```
matlab -batch "run('cal_relation.m')"
or
matlab -batch "run('cal_relation_t.m')"
```
- **Step III.**  Train the GL-CEF model.
```
python fold.py
or
python fold_t.py
```
```
python site_model.py
or
python site_model_t.py
```
- **Step IV.**  Validate the model performance.
```
python site_eva.py
or
python site_eva_t.py
```

 ### Estimation and visualization
- **Step I.**  Divide the grids into blocks.
```
run div_grid_gen.m
```
- **Step II.**  Calculate the global-local relations of blocks.
```
run cal_relation_gen.m
```
- **Step III.**  Train the GL-CEF model.
```
run fit_allmodel.py
run site_model_gen.py
```
- **Step IV.**  Estimate ambient ozone concentrations.
```
run pre_allmodel.py
run site_pre.py
```
- **Step V.**  Visualize the results.
```
run getr.m 
run convert_to_nc.py 
run map.py
```
