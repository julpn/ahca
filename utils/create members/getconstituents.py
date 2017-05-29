import pandas as pd
#from rep_api.models import Rep

df = pd.read_csv('members.csv')

attributes = [
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
        val = str(row[attribute])
        new_att = attribute
        if attribute == "num_uninsured":
            new_att = "uninsured"
        elif attribute == "num_deaths":
            new_att = "killed"
            val = float(val)
            val = int(round(val, 0))
        if val == 'N':
            val = False
        if val == 'Y':
            val = True
        if val != 'nan':
            args[new_att] = val
    print args
    #r = Rep.objects.create(**args)
