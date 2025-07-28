'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt

# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 
def scatterplot_predictions_by_charge(pred_with_felony):
    sns.lmplot(data=pred_with_felony,
               x='prediction_felony',
               y='prediction_nonfelony',
               hue='has_felony_charge',
               fit_reg=False)
    plt.title('Felony vs Non-Felony Predictions, Hue by Current Felony Charge')
    plt.xlabel('Prediction for Felony Rearrest')
    plt.ylabel('Prediction for Non-Felony Rearrest')
    plt.savefig('data/part5_plots/felony_vs_nonfelony_by_charge.png', bbox_inches='tight')
    plt.clf()
    
# In a print statement, answer the following question: What can you say about the group of dots on the right side of the plot?
print("Part 5 Question 1 Answer:")
print("The cluster of dots on the right side likely represents individuals with high predicted felony rearrest risk.")

# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.
def scatterplot_felony_prediction_vs_outcome(pred_with_felony):
    sns.stripplot(data=pred_with_felony,
                  x='prediction_felony',
                  y='label_felony',
                  jitter=True,
                  alpha=0.4)
    plt.title('Prediction vs Actual Felony Rearrest')
    plt.xlabel('Prediction for Felony Rearrest')
    plt.ylabel('Actual Felony Rearrest (0 = No, 1 = Yes)')
    plt.savefig('data/part5_plots/felony_prediction_vs_actual.png', bbox_inches='tight')
    plt.clf()
    
# In a print statement, answer the following question: Would you say based off of this plot if the model is calibrated or not?
print("Part 5 Question 2 Answer:")
print("The model may be overestimating risk for some individuals, since if it were well calibrated, ")
print("higher predicted probabilities would correspond with more 1s on the y-axis, suggesting it is not perfectly calibrated.")