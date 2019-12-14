import requests
import json

response = requests.get('https://statsapi.web.nhl.com/api/v1/teams')
data = response.json()

with open('nhl.json', 'w') as nhl_file:
	nhl_file.write(json.dumps(data))
print(json.dumps(data['teams'], indent=4))


# How many teams in the NHL
num_teams = len(data['teams'])
print(f'Number of NHL teams: {num_teams}')


# How many teams in eastern conference
team_data = data['teams']
eastern_total = 0

for teams in team_data:
	if 'Eastern' in teams['conference']['name']:
		eastern_total += 1
print(f'Number of teams in eastern conference: {eastern_total}')



# Find the oldest NHL team
team_data = data['teams']
first_year_play = []
for team in team_data:
	first_year_play.append({'first_year': int(team['firstYearOfPlay']), 'name': team['name']}) # List contains dictionaries with team name/year
print(type(first_year_play))

min_year = first_year_play[0]['first_year'] # arbitrarily store first index - to be replaced by for-loop result
min_year_name = first_year_play[0]['name']

for team in first_year_play:
	if team['first_year'] < min_year:
		min_year = team['first_year'] # replace value
		min_year_name = team['name'] # replace value
print(min_year, min_year_name)

# # Alternative approach using sort/lambdas
# sorted_list = sorted(first_year_play, key=lambda x: x['first_year'])
# print(sorted_list[0])



# When did Boston Bruins start playing