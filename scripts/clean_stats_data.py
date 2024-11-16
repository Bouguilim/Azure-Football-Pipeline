import pandas as pd
from utils.constants import STATS_PROFILE_PATH

# File paths to be cleaned
input_path = STATS_PROFILE_PATH

# Output file paths for cleaned files
output_path = STATS_PROFILE_PATH

df = pd.read_csv(input_path)

# Step 1: Remove rows where the 'Season' column is empty
df = df.dropna(subset=['Season'])

# Step 2: Group by 'Player ID' and 'Season' and sum the remaining columns
columns_to_sum = ['Appearances', 'Goals', 'Assists', 'Yellow Cards', 'Second Yellow Cards', 'Red Cards', 'Minutes']
cleaned_df = df.groupby(['Player ID', 'Season'], as_index=False)[columns_to_sum].sum()

cleaned_df.to_csv(output_path, index=False)