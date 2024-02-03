# Importing necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Load the dataset and find the most common gender and birth country
nobel_data = pd.read_csv('nobel.csv')

# Extracting the top values from sex and birth_country columns
top_gender = nobel_data['sex'].value_counts().index[0]
top_country = nobel_data['birth_country'].value_counts().index[0]
print("\n The gender with the most Nobel laureates is :", top_gender)
print(" The most common birth country of Nobel laureates is :", top_country)

# Step 2: Identify the decade with the highest proportion of US-born winners
# Create the US-born winners column
nobel_data['usa_born_winner'] = nobel_data['birth_country'] == 'United States of America'

# Create the decade column 
nobel_data['decade'] = (np.floor(nobel_data['year'] / 10) * 10).astype(int)

# Print to show modifications
print("\n After adding 'usa_born_winner' and 'decade' columns:")
print(nobel_data.head())

# Finding the proportion
prop_usa_winners = nobel_data.groupby('decade', as_index=False)['usa_born_winner'].mean()

# Print to show modifications
print("\n Proportion of USA-born winners by decade:")
print(prop_usa_winners)

# Identify the decade with the highest proportion of US-born winners
max_decade_usa = prop_usa_winners.loc[prop_usa_winners['usa_born_winner'].idxmax(), 'decade']

# Plotting USA born winners
plt.figure(figsize=(10, 6))
sns.lineplot(x='decade', y='usa_born_winner', data=prop_usa_winners, marker='o')
plt.title('Proportion of US-Born Nobel Prize Winners Over Decades')
plt.xlabel('Decade')
plt.ylabel('Proportion')
plt.show()

# Step 3: Find the decade and category with the highest proportion of female laureates
# Calculate the proportion of female laureates per decade and category
prop_female_winners = nobel_data[nobel_data['sex'] == 'Female'].groupby(['decade', 'category'], as_index=False)['sex'].count()

# Print to show modifications
print("\n Proportion of Female Nobel Prize Winners by Decade and Category:")
print(prop_female_winners)

# Find the decade and category with the highest female winners
max_female_decade_category = prop_female_winners.loc[prop_female_winners['sex'].idxmax(), ['decade', 'category']]

# Create a DataFrame for better visualization
plt.figure(figsize=(8, 6))
sns.lineplot(x='decade', y='sex', hue='category', data=prop_female_winners, marker='v')
plt.title('Proportion of Female Nobel Prize Winners Over Decades by Category')
plt.xlabel('Decade')
plt.ylabel('Count')
plt.legend(title='Category', bbox_to_anchor=(0, 1), loc='upper left')
plt.show()

# Step 4: Find the first woman to win a Nobel Prize
first_woman_data = nobel_data[nobel_data['sex'] == 'Female'].sort_values(by='year').iloc[0]
first_woman_name = first_woman_data['full_name']
first_woman_category = first_woman_data['category']
print(f"\n The first woman to win a Nobel Prize was {first_woman_name}, in the category of {first_woman_category}.")

# Step 5: Determine repeat winners
repeat_list = nobel_data['full_name'].value_counts()[nobel_data['full_name'].value_counts() >= 2].index.tolist()
print("\n The repeat winners are :", repeat_list)
