#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt


# In[2]:


df = pd.read_csv('Pokemon.csv')


# In[3]:


df.info()


# In[4]:


df.head()


# Seaborn's plotting functions.
# One of Seaborn's greatest strengths is its diversity of plotting functions. For instance, making a scatter plot is just one line of code using the lmplot() function.
# 
# There are two ways you can do so.
# 
# The first way (recommended) is to pass your DataFrame to the data= argument, while passing column names to the axes arguments, x= and y=.
# The second way is to directly pass in Series of data to the axes arguments.
# Comparing the Attack and Defense stats for our Pokémon:

# In[5]:


sns.lmplot(x='Attack', y='Defense', data=df)


# In[6]:


# Scatterplot arguments
sns.lmplot(x='Attack', y='Defense', data=df,
           fit_reg=False, # No regression line
           hue='Stage')   # Color by evolution stage


# Seaborn is a high-level interface to Matplotlib. From our experience, Seaborn will get you most of the way there, but you'll sometimes need to bring in Matplotlib.
# 
# Setting your axes limits is one of those times, but the process is pretty simple:
# 
# First, invoke your Seaborn plotting function as normal.
# Then, invoke Matplotlib's customization functions. In this case, we'll use its ylim() and xlim() functions.

# In[15]:


from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize'] = [10, 5]


# In[16]:


# Plot using Seaborn
sns.lmplot(x='Attack', y='Defense', data=df,
           fit_reg=False, 
           hue='Stage')
 
# Tweak using Matplotlib
plt.ylim(0, None)
plt.xlim(0, None)


# In[17]:


# Boxplot
sns.boxplot(data=df)


# In[18]:


# Pre-format DataFrame
stats_df = df.drop(['Total', 'Stage', 'Legendary'], axis=1)
 
# New boxplot using stats_df
sns.boxplot(data=stats_df)


# In[19]:


# Set theme
sns.set_style('whitegrid')
 
# Violin plot
sns.violinplot(x='Type 1', y='Attack', data=df)


# Color palettes.
# Fortunately, Seaborn allows us to set custom color palettes. We can simply create an ordered Python list of color hex values.
# 
# using Bulbapedia to help us create a new color palette:

# In[21]:


pkmn_type_colors = ['#78C850',  # Grass
                    '#F08030',  # Fire
                    '#6890F0',  # Water
                    '#A8B820',  # Bug
                    '#A8A878',  # Normal
                    '#A040A0',  # Poison
                    '#F8D030',  # Electric
                    '#E0C068',  # Ground
                    '#EE99AC',  # Fairy
                    '#C03028',  # Fighting
                    '#F85888',  # Psychic
                    '#B8A038',  # Rock
                    '#705898',  # Ghost
                    '#98D8D8',  # Ice
                    '#7038F8',  # Dragon
                   ]


# In[22]:


# Violin plot with Pokemon color palette
sns.violinplot(x='Type 1', y='Attack', data=df, 
               palette=pkmn_type_colors) # Set color palette


# In[23]:


# Swarm plot with Pokemon color palette
sns.swarmplot(x='Type 1', y='Attack', data=df, 
              palette=pkmn_type_colors)


# In[24]:


# Set figure size with matplotlib
plt.figure(figsize=(10,6))
 
# Create plot
sns.violinplot(x='Type 1',
               y='Attack', 
               data=df, 
               inner=None, # Remove the bars inside the violins
               palette=pkmn_type_colors)
 
sns.swarmplot(x='Type 1', 
              y='Attack', 
              data=df, 
              color='k', # Make points black
              alpha=0.7) # and slightly transparent
 
# Set title with matplotlib
plt.title('Attack by Type')


# In[25]:


stats_df.head()


# In[26]:


# Melt DataFrame
melted_df = pd.melt(stats_df, 
                    id_vars=["Name", "Type 1", "Type 2"], # Variables to keep
                    var_name="Stat") # Name of melted variable
melted_df.head()


# In[27]:


print( stats_df.shape )
print( melted_df.shape )
# (151, 9)
# (906, 5)


# In[28]:


# Swarmplot with melted_df
sns.swarmplot(x='Stat', y='value', data=melted_df, 
              hue='Type 1')


# In[30]:


sns.swarmplot(x='Stat', y='value', data=melted_df, 
              hue='Type 1')
plt.rcParams['figure.figsize'] = [15, 7]


# making a few final tweaks for a more readable chart:
# 
# Enlarge the plot.
# Separate points by hue using the argument split=True .
# Use our custom Pokemon color palette.
# Adjust the y-axis limits to end at 0.
# Place the legend to the right.

# In[31]:


plt.figure(figsize=(10,6))
 
sns.swarmplot(x='Stat', 
              y='value', 
              data=melted_df, 
              hue='Type 1', 
              split=True, # 2. Separate points by hue
              palette=pkmn_type_colors) # 3. Use Pokemon palette
 
# 4. Adjust the y-axis
plt.ylim(0, 260)
 
# 5. Place legend to the right
plt.legend(bbox_to_anchor=(1, 1), loc=2)


# In[32]:


# Calculate correlations
corr = stats_df.corr()
 
# Heatmap
sns.heatmap(corr)


# In[33]:


# Distribution Plot (a.k.a. Histogram)
sns.distplot(df.Attack)


# In[34]:


# Count Plot (a.k.a. Bar Plot)
sns.countplot(x='Type 1', data=df, palette=pkmn_type_colors)
 
# Rotate x-labels
plt.xticks(rotation=-45)


# In[35]:


# Factor Plot
g = sns.factorplot(x='Type 1', 
                   y='Attack', 
                   data=df, 
                   hue='Stage',  # Color by stage
                   col='Stage',  # Separate by stage
                   kind='swarm') # Swarmplot
 
# Rotate x-axis labels
g.set_xticklabels(rotation=-45)
 
# Doesn't work because only rotates last plot
# plt.xticks(rotation=-45)


# In[36]:


# Density Plot
sns.kdeplot(df.Attack, df.Defense)


# Joint Distribution Plot
# Joint distribution plots combine information from scatter plots and histograms to give you detailed information for bi-variate distributions.

# In[38]:


# Joint Distribution Plot
sns.jointplot(x='Attack', y='Defense', data=df)


# In[ ]:




