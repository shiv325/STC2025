import random

def generate_student_data(n=100):
    majors = ["CS", "Math", "Physics", "Bio"]
    students = []

    for _ in range(n):
        student = {
            "Student_ID": random.randint(1000, 9999),
            "Age": random.randint(18, 25),
            "GPA": round(random.uniform(2.0, 4.0), 2),
            "Major": random.choice(majors)
        }
        students.append(student)
    return students

# Generate data for 100 students
student_data = generate_student_data()

import pandas as pd
import numpy as np

# Convert to DataFrame
df = pd.DataFrame(student_data)

# Remove duplicates (if any)
df.drop_duplicates(subset='Student_ID', inplace=True)

# Check for missing values
print(df.isnull().sum())

# Calculate mean and std of GPA
mean_gpa = np.mean(df['GPA'])
std_gpa = np.std(df['GPA'])
print(f"Mean GPA: {mean_gpa:.2f}, Std Dev: {std_gpa:.2f}")

# Filter students with GPA above mean
above_avg = df[df['GPA'] > mean_gpa]
print(above_avg)

# Add 'Performance' column
def label_performance(gpa):
    if gpa >= 3.5:
        return "Excellent"
    elif gpa >= 3.0:
        return "Good"
    else:
        return "Needs Improvement"

df['Performance'] = df['GPA'].apply(label_performance)

import matplotlib.pyplot as plt
import seaborn as sns

# Histogram of GPAs
plt.figure(figsize=(7, 4))
sns.histplot(df['GPA'], bins=10, kde=True, color='skyblue')
plt.title('GPA Distribution')
plt.xlabel('GPA')
plt.ylabel('Frequency')
plt.savefig('gpa_histogram.png')
plt.show()

# Bar chart: Average GPA per Major
plt.figure(figsize=(7, 4))
sns.barplot(x='Major', y='GPA', data=df, estimator=np.mean, palette='viridis')
plt.title('Average GPA by Major')
plt.ylabel('Average GPA')
plt.savefig('avg_gpa_by_major.png')
plt.show()

# Boxplot: GPA by Performance
plt.figure(figsize=(7, 4))
sns.boxplot(x='Performance', y='GPA', data=df, palette='Set2')
plt.title('GPA Distribution by Performance')
plt.savefig('gpa_boxplot_performance.png')
plt.show()

# Scatter Plot: Age vs GPA colored by Major
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Age', y='GPA', hue='Major', data=df, palette='deep')
plt.title('Age vs GPA by Major')
plt.savefig('age_vs_gpa_scatter.png')
plt.show()