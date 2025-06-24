import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
df = sns.load_dataset('titanic')

# Basic cleaning: drop rows where 'age' or 'class' is missing
df_clean = df.dropna(subset=['age', 'class'])

# Show the first few rows
print(df_clean.head())


# Group by 'class' and calculate average age
avg_age_by_class = df_clean.groupby('class')['age'].mean()
print(avg_age_by_class)


# Pandas boxplot
df_clean.boxplot(column='age', by='class', grid=False)

# Save and show plot
plt.title('Age Distribution by Class')
plt.suptitle('')  # Suppress default title
plt.xlabel('Class')
plt.ylabel('Age')
plt.savefig('pandas_boxplot_age_class.png')
plt.show()


# Seaborn boxplot
plt.figure(figsize=(8,6))
sns.boxplot(x='class', y='age', data=df_clean)

plt.title('Age Distribution by Passenger Class (Seaborn)')
plt.xlabel('Passenger Class')
plt.ylabel('Age')
plt.savefig('seaborn_boxplot_age_class.png')
plt.show()


# Scatter plot with hue
plt.figure(figsize=(8,6))
sns.scatterplot(x='age', y='fare', hue='survived', data=df_clean)

plt.title('Fare vs. Age Colored by Survival Status')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.savefig('seaborn_scatter_fare_age_survived.png')
plt.show()


# Add hue (sex) and size (class)
plt.figure(figsize=(10,7))
sns.scatterplot(
    x='age', y='fare',
    hue='sex', size='class',
    data=df_clean, sizes=(20, 200), alpha=0.6
)

plt.title('Fare vs. Age with Sex and Class')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.savefig('seaborn_scatter_fare_age_sex_class.png')
plt.show()
