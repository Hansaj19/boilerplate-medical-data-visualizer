import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
bmi = df['weight']/((df['height']/100)**2)
df['overweight'] = np.where(bmi>25,1,0)

# 3
df['cholesterol'] = np.where(df['cholesterol']==1,0,1)
df['gluc'] = np.where(df['gluc']==1,0,1)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])



    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'])['value'].count().reset_index(name='total')
    
    # Ensure the order of 'variable' for plotting
    # This is crucial for the test case failure related to x-axis labels
    cat_order = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
    df_cat['variable'] = pd.Categorical(df_cat['variable'], categories=cat_order, ordered=True)
    df_cat = df_cat.sort_values('variable') # Sort by variable to ensure consistent plotting order

    

    # 7

    

    # 8
    fig =sns.catplot(data=df_cat,x='variable',y='total',col='cardio', hue='value',kind='bar',height=5, aspect=1).fig

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) & 
        (df['height'] >= df['height'].quantile(0.025)) & 
        (df['height'] <= df['height'].quantile(0.975)) & 
        (df['weight'] >= df['weight'].quantile(0.025)) & 
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12
    corr =df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr,dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(10,8))
    # 15

    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", cmap='coolwarm', ax=ax)


    # 16
    fig.savefig('heatmap.png')
    return fig