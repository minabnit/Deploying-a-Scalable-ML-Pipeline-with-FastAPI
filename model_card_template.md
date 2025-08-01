# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

-Developed by Mark Inabnit
-Model Date: 8/1/25
-Model Version 1.0.0
-Model Type: ADABoost Classifier

## Intended Use

This model is intended to be used to predict whether a person earns more than
$50,000 per year based on their personal, educational, and employment demographics.

## Training Data

This model uses the census.csv dataset.  

It is designed for educational purposes to demonstrate how to 
deploy an ML Pipeline using Fast API.

Preprocessing steps include recoding categorical data using 
Scikitlearn's OneHotEncoder and label binarizier.

Training data uses 80% of the dataset.

## Evaluation Data

This model uses the census.csv dataset.  

It is designed for educational purposes to demonstrate how to 
deploy an ML Pipeline using Fast API.

Preprocessing steps include recoding categorical data using 
Scikitlearn's OneHotEncoder and label binarizier.

Testing Data uses 20% of the dataset.  

## Metrics

The model had a Precision Score of .7593, a Recall Score of .5961, 
and an F1 score of .6678.  Please see the file "slice_output.txt" for
performance on individual slices.

## Ethical Considerations

The original dataset contains information that may be sensitive in nature,
and thus the model may expose disparities based on racial or gender inequalities. 

## Caveats and Recommendations

This model was trained using only one set of hyperparameters.  Performance may
improve with additional hyperparameter tuning.   