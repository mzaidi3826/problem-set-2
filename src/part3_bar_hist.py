'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Using the pre_universe data frame, create a bar plot for the fta column.
def barplot_fta(pred_universe):
    sns.countplot(data=pred_universe, x='fta')
    plt.title('FTA Count')
    plt.xlabel('FTA (Failure to Appear)')
    plt.ylabel('Count')
    plt.savefig('data/part3_plots/barplot_fta.png', bbox_inches='tight')
    plt.clf()

# 2. Hue the previous barplot by sex
def barplot_fta_by_sex(pred_universe):
    sns.countplot(data=pred_universe, x='fta', hue='sex')
    plt.title('FTA Count by Sex')
    plt.xlabel('FTA (Failure to Appear)')
    plt.ylabel('Count')
    plt.savefig('data/part3_plots/barplot_fta_by_sex.png', bbox_inches='tight')
    plt.clf()

# 3. Plot a histogram of age_at_arrest
def histogram_age(pred_universe):
    sns.histplot(data=pred_universe, x='age_at_arrest', bins=20)
    plt.title('Age at Arrest Distribution')
    plt.xlabel('Age at Arrest')
    plt.ylabel('Frequency')
    plt.savefig('data/part3_plots/histogram_age.png', bbox_inches='tight')
    plt.clf()
    
# 4. Plot the same histogram, but create bins that represent the following age groups 
def histogram_age_groups(pred_universe):
    bins = [18, 21, 30, 40, 100]
    labels = ['18–21', '21–30', '30–40', '40+']
    pred_universe['age_group'] = pd.cut(pred_universe['age_at_arrest'], bins=bins, labels=labels, right=False)

    sns.countplot(data=pred_universe, x='age_group', order=labels)
    plt.title('Age Group Distribution at Arrest')
    plt.xlabel('Age Group')
    plt.ylabel('Count')
    plt.savefig('data/part3_plots/histogram_age_groups.png', bbox_inches='tight')
    plt.clf()