import pandas as pd
from utils.constants import MARKET_PROFILE_PATH

# File paths to be cleaned
input_path = MARKET_PROFILE_PATH

# Output file paths for cleaned files
output_path = MARKET_PROFILE_PATH

# Define the headers
headers = ['Club', 'Age', 'player_id', 'MarketValueAmount', 'Currency', 'Date', 'HighestMarketValue', 'HighestMarketValueDate', 'LastChangeDate']

# Load the data into a pandas DataFrame, adding the headers
df = pd.read_csv(input_path, header=None, names=headers)

# # Convert all date columns to datetime and remove the time component
for column in ['Date', 'HighestMarketValueDate', 'LastChangeDate']:
    df[column] = pd.to_datetime(df[column], errors='coerce').dt.date.replace(pd.NaT, None)

# Write the cleaned data to a new CSV file
df.to_csv(output_path, index=False)