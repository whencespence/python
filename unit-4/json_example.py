import json

# person = {'Name': 'Christina', 'Job': 'Developer', 'City': 'Toronto'}
# print(type(person))


with open('cohort.json', 'r') as cohort_file:
	cohort = json.load(cohort_file) # store dictionary in cohort variable

# 'json.dumps' takes a dictionary and turns it into a string - accepts a paramater 'indent=2'
print(json.dumps(cohort, indent=2))
