import pandas as pd
from pandas.io.parsers import read_csv
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
df['overweight'] = True

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    dataframe = pd.melt('cholesterol' , 'gluc', 'smoke', 'alco', 'active', 'overweight')
    dataframe.savefig("Dataframe.csv")
    df_cat = Image.open("Figure_1.png")
    


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    np.split(column = 'Cardio')
    df_cat = Image.open("Figure_2.png")

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(read_csv("medical_examination.csv"))

    return df_cat


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = sns.heatmap(read_csv("medical_examination.csv"))

    # Calculate the correlation matrix
    corr = np.corrcoef(read_csv("medical_examination.csv"))

    # Generate a mask for the upper triangle
    mask = np.ma.masked_where(read_csv("medical_examination.csv"))

    return df_heat
    return corr
    return mask


    # Set up the matplotlib figure
    fig, ax = plt.figure("Age", "Height", "Gender", "Systolic blood pressure", "Diatolic blood pressure", "Cholestrol", "Glucose", "Samoking", "Alcohol intake", "Physical activity", "Presence or absence of cardiovascular disease")

    # Draw the heatmap with 'sns.heatmap()'
    heatmap = sns.heatmap(read_csv("medical_examination.csv"))



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
