# Notater fra StatQuest

## Confusion matrix

This is an example of a 2x2 confusion matric
The values on the top are values that are true, while the values on the side is the value that that is predicted

|                  | Has obesity     | Has not obesity |
| ---------------- | --------------- | --------------- |
| Has obesity      | True Positives  | False Positives |
| Has not obersity | False Negatives | True Negatives  |

## Sensitivity

Calculating sensitivity goes as follows:

$$ 
Sensitivity = {True Positives \over 
True Positives + False negatives}
$$

With the example in the 2x2 matrix above, the sensetivity tells us what percentage of patients with hearth disease where correctly indentified

## Specificity

Calculating specificity goes as follows:

$$
Specificity = {True Negatives \over
True Negatives + False Positives}
$$

With the example in the 2x2 matrix above, the specificity tells us what percentage of patients without hearth disease where correctly indentified

## Sensitivity and Specifisity

If one model is better at Sensitivity we use the model if it is more important to (in the example above) identify patients with hearth disease.

And vise versa if another model is better at Specifisity we use this model if it is more important to correctly identify patoents without heart disease.

## Sensitivity and Specifisity on bigger matrixes

If there are three ore more collumns/rows in the confusion matrix, we need to calculate both Sensitivity and Specifisity for each category.