# import pandas as pd

# def load_players(file_path):
#     pass

# def load_matches(file_path):
#     pass

# def merge_players_matches(players_df, matches_df):
#    pass

# def total_runs_per_team(merged_df):
#    pass

# def calculate_strike_rate(merged_df):
#     pass

# def runs_agg_per_player(merged_df):
#    pass

# def avg_age_by_role(players_df):
#    pass
# def total_matches_per_player(matches_df):
#    pass

#     # Step 1: Get counts (index: PlayerID, column: count)
    
#     # Step 2: Rename columns explicitly and cleanly
   

#     # Ensure columns are in correct order
   
#     return 



# def top_wicket_takers(merged_df):
#     pass
# def avg_strike_rate_per_team(merged_df):
#      pass

# def catch_to_match_ratio(merged_df):
#      pass

import pandas as pd
import numpy as np

def load_players(file_path):
    return pd.read_csv('C:\\Users\\Ascendion\\Downloads\\cricket_players_analysis\\data\\players.csv')

def load_matches(file_path):
    return pd.read_csv('C:\\Users\\Ascendion\\Downloads\\cricket_players_analysis\\data\\matches.csv')

def merge_players_matches(players_df, matches_df):
    merged = pd.merge(matches_df, players_df, on='PlayerID')
    expected_order = ['PlayerID', 'Name', 'Team', 'Role', 'Age',
                      'MatchID', 'Runs', 'Balls', 'Fours', 'Sixes', 'Wickets', 'Catches', 'Date']
    return merged[expected_order]


def total_runs_per_team(merged_df):
    runs_by_team = merged_df.groupby('Team')['Runs'].sum().sort_values(ascending=False)
    return runs_by_team.reset_index()

def calculate_strike_rate(merged_df):
    merged_df['StrikeRate'] = (merged_df['Runs'] / merged_df['Balls']) * 100
    return merged_df[['PlayerID', 'Name', 'Runs', 'Balls', 'StrikeRate']]


def runs_agg_per_player(merged_df):
    agg_df = merged_df.groupby(['PlayerID', 'Name'])['Runs'].agg(['mean', 'max', 'min']).reset_index()
    return agg_df


def avg_age_by_role(players_df):
    avg_age = players_df.groupby('Role')['Age'].mean().round(2).reset_index()
    return avg_age


def total_matches_per_player(matches_df):
    match_counts = matches_df.groupby('PlayerID')['MatchID'].nunique().reset_index()
    match_counts.columns = ['PlayerID', 'MatchCount']
    return match_counts


def top_wicket_takers(merged_df, top_n=3):
    wickets_df = merged_df.groupby(['PlayerID', 'Name'])['Wickets'].sum().reset_index()
    return wickets_df.sort_values(by='Wickets', ascending=False).head(top_n)


def avg_strike_rate_per_team(merged_df):
    merged_df['StrikeRate'] = (merged_df['Runs'] / merged_df['Balls']) * 100
    return merged_df.groupby('Team')['StrikeRate'].mean().round(2).reset_index()


def catch_to_match_ratio(merged_df):
    catches_df = merged_df.groupby('PlayerID')[['Catches', 'MatchID']].agg({
        'Catches': 'sum',
        'MatchID': 'nunique'
    }).reset_index()
    catches_df['CatchToMatchRatio'] = (catches_df['Catches'] / catches_df['MatchID'])
    return catches_df[['PlayerID', 'CatchToMatchRatio']].sort_values(by='CatchToMatchRatio', ascending=False)

