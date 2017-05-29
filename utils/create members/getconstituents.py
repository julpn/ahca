import pandas as pd
#from ahca_api.rep_api.models import Rep


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

reps = []
for index, row in df.iterrows():
    args = {}
    for attribute in attributes:
        try:
            val = str(row[attribute])
            new_att = attribute
            if attribute == "num_uninsured":
                new_att = "uninsured"
                val = val.replace(',', '')
            elif attribute == 'population':
                val = val.replace(',', '')
            elif attribute == "num_deaths":
                new_att = "killed"
                val = float(val)
                val = int(round(val, 0))
            elif attribute == 'district':
                try:
                    val = int(float(val))
                except ValueError:
                    continue
        except ValueError:
            continue
        if val == 'N':
            val = False
        if val == 'Y':
            val = True
        if val != 'nan':
            args[new_att] = val
    reps.append(args)

   # r = Rep.objects.create(**args)
print reps
