# Application of LightGBM-ALE in Agriculture in the North China Plain
The application of the LightGBM-ALE model in Interpretable Machine Learning for Revealing Main and Interactive Effects of Ozone and Meteorological Factors on Crop Photosynthesis.  
The code folder contains the processes for generating the Figures and Tables within the article.  
The data folder houses the data used in the article, the model folder includes the outcomes of the LightGBM-ALE model training.  
The pic folder contains the original images of the article's figures.  
**Attention** lightgbm==4.1.0; pyale==1.1.3  
  
# Implementation Steps
This repository provides a comprehensive workflow for analyzing wheat datasets using advanced machine learning techniques. Below are the detailed steps to reproduce the results using the provided code and data files.  
## 1. Data Preprocessing  
Import the preprocessed wheat dataset (_wheat.csv_) into the _Split the train and test datasets.py_ script. This will generate two separate files: _train-wheat.csv_ and _test-wheat.csv_.  
## 2. Model Fitting and Hyperparameter Tuning  
Utilize the _train-wheat.csv_ dataset to build a fitting model.  
Import _train-wheat.csv_ into _Search for hyperparameters.py_ to obtain the set of hyperparameters.  
Input the hyperparameters and _train-wheat.csv_ into _Fit the model.py_ to establish the wheat fitting model. This process will produce the model file _bsm-wheat-sif.pkl_ and a 10-fold cross-validation file named _model-wheat-10cv.txt_.  
## 3. ALE Module Interpretation  
Import the _train-wheat.csv_ dataset and the model file _bsm-wheat-sif.pkl_ into the ALE module scripts _1d-ALE.py_ and _2d-ALE.py_. This will generate first-order and second-order ALE plots and data.  
## 4. Image Optimization  
Import the ALE data (in CSV format) generated from the ALE module into _Process ALEeff.py_. This script will extract the extreme values of first-order and second-order ALE effects, resulting in the files _wheat-1d.csv_ and _wheat-2d.csv_.  
Feed the extracted results into _Extract ALE range.py_ to obtain the ALE Range values. This will provide the main effect values of first-order ALE and the interaction effect values of second-order ALE for each factor.  
Using the ALE main effect and interaction effect values, import them into _1D/2D bar charts.py_ to create bar charts. This visualization will facilitate an intuitive display of the effect values for each factor.  
Import the ALE main effect and interaction effect values into _Calculate the comparison of two effects.py_ for comparative analysis. Subsequently, input the results into _Draw comparison heatmaps.py_ to generate heatmaps. This will enable an intuitive comparison of the main and interaction effects for wheat crops.  
By following these steps, users can effectively utilize the provided code and data to analyze wheat datasets and visualize the results through ALE plots, bar charts, and heatmaps.  
