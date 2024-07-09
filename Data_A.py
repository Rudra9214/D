import pandas as pd

df = pd.read_csv("EASY_IPL.csv")

# Filter the data for the year 2008 and the winner being the team batting first
matches_batting_first_won_2008 = df[(df['Year'] == 2008) & (df['Winning_Team'] == 'FirstBatting')]
matches_batting_second_won_2008 = df[(df['Year'] == 2008) & (df['Winning_Team'] == 'Chasing')]

total_matches = df[df['Year']==2008].shape[0]
# Count the number of such matches
number_of_matches_batting_first_won_2008 = matches_batting_first_won_2008.shape[0]
number_of_matches_batting_second_won_2008 = matches_batting_second_won_2008.shape[0]


print(df)
print(number_of_matches_batting_first_won_2008)
print(number_of_matches_batting_second_won_2008)
print(total_matches)


#Q1
result = df.groupby('Year').agg(
    Total_no_of_matches=('Match_Number', 'count'),
    Number_of_matches_Team_Batting_first_won=('Winning_Team', lambda x: (x == 'FirstBatting').sum()),
    Number_of_Matches_team_chasing_won=('Winning_Team', lambda x: (x == 'Chasing').sum()),
    Number_of_Times_match_tied=('Winning_Team', lambda x: (x == 'Match Tied').sum())
).reset_index()

print('\n\n\n\n\n')
print(result)


#Q2

result2 = df.groupby('Venue').agg(
    Total_no_of_matches_2 = ('Match_Number','count')
)
most_common_venue = result2.idxmax()
number_of_matches = result2.max()

# Create a DataFrame 
result3 = pd.DataFrame({
    'Most_Common_Venue': [df['Venue'].value_counts().idxmax()],
    'Number_of_Matches': [df['Venue'].value_counts().max()]
})


print('\n\n\n\n\n')
#print(result2)
print(result3)

#Q3

result4 = df.loc[df['Bat_First_Run_Rate'].idxmax()]

result5 = pd.DataFrame({
    'Match_Number': [result4['Match_Number']],
    'Team_Batting_First': [result4['Team_Batting_First']],
    'Runs_Scored' : [result4['Bat_First_Runs_Scored']],
    'No-of-overs' : [result4['Bat_First_Overs_Consumed']]
})

print('\n\n\n\n\n')
print(result4)
print(result5)
