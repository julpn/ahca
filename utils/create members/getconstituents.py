import pandas as pd
#import Rep model

df = pd.read_csv('members.csv')

attributes =[
    'first_name',
    'last_name',
    'state',
    'district',
    'gender',
    'population',
    'num_uninsured',
    'num_deaths',
    'medicaid_expansion_state',
    'swing_left_district',
    'freedom_caucus_member',
    'percent_vote_2016',
    'percent_vote_clinton',
    'percent_vote_trump',
    'president_vote_margin',
    'twitter_link',
    'facebook_link',
    'twitter_handle',
    'phone_number',
]

for index, row in df.iterrows():
    args = {}
    for attribute in attributes:
        args[attribute] = row[attribute]
    continue
    #r = Rep.objects.create(**args)
