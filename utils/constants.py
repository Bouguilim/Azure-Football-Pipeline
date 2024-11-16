import configparser
import os

parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__), '../config/config.conf'))

# paths
PLAYER_PROFILE_PATH = parser.get('paths', 'PLAYER_PROFILE_PATH')
PROCESSED_PLAYER_URLS_PATH = parser.get('paths', 'PROCESSED_PLAYER_URLS_PATH')
MARKET_PROFILE_PATH = parser.get('paths', 'MARKET_PROFILE_PATH')
PROCESSED_MARKET_IDS_PATH = parser.get('paths', 'PROCESSED_MARKET_IDS_PATH')
STATS_PROFILE_PATH = parser.get('paths', 'STATS_PROFILE_PATH')
PROCESSED_STATS_URLS_PATH = parser.get('paths', 'PROCESSED_STATS_URLS_PATH')