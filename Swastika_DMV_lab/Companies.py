#1)PIE CHART
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('"D:\Ishita_DMV_Lab\first_20_companies.csv"')

# Count companies year-wise
year_counts = df['years'].value_counts()

# Create pie chart
plt.figure()
plt.pie(year_counts, labels=year_counts.index, autopct='%1.1f%%')

# Title
plt.title('Companies Distribution Year Wise')

# Show chart
plt.show()

#2) FUNNEL CHART
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('first_20_companies.csv')

# Sort by review_count (descending)
df_sorted = df.sort_values(by='review_count', ascending=False)

# Take top companies (optional but recommended for funnel clarity)
df_top = df_sorted.head(10)

# Reverse for funnel shape (largest at top)
df_top = df_top[::-1]

# Plot horizontal bar chart (funnel style)
plt.figure()

plt.barh(df_top['name'], df_top['review_count'])

# Labels and title
plt.xlabel('Review Count')
plt.ylabel('Company Name')
plt.title('Funnel Chart - Companies Review Wise')

# Show plot
plt.show()


#3)HEADQUATERS
import pandas as pd

df = pd.read_csv('first_20_companies.csv')

# Remove metadata like "+276 more"
df['hq'] = df['hq'].str.split('+').str[0].str.strip()

# Now get first 10 companies with cleaned HQ
result = df[['name', 'hq']].head(10)

print(result)

#4)BAR CHART
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('first_20_companies.csv')

# Sort by ratings
df_sorted = df.sort_values(by='ratings', ascending=False)

# Plot bar chart
plt.figure()
plt.bar(df_sorted['name'], df_sorted['ratings'])

# Labels
plt.xlabel('Company Name')
plt.ylabel('Ratings')
plt.title('Companies Rating Wise')

# Rotate names for readability
plt.xticks(rotation=45)

plt.show()


#5) LINE CHART
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('first_20_companies.csv')

# Sort by employees (important for line chart)
df_sorted = df.sort_values(by='employees')

# Plot line chart
plt.figure()
plt.plot(df_sorted['name'], df_sorted['employees'], marker='o')

# Labels
plt.xlabel('Company Name')
plt.ylabel('Number of Employees')
plt.title('Companies Employees Count Wise')

# Rotate names
plt.xticks(rotation=45)

plt.show()