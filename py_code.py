import pandas as pd

netflix_df=pd.read_csv('netflix_data.csv')
print(netflix_df)
#question1
recent_movies_df=netflix_df.loc[
     (netflix_df['type']=='Movie') &
     (netflix_df['release_year']>2025)]
#question2
short_action_movies_df=netflix_df.loc[
        (netflix_df['genre']=='Action') &
        (netflix_df['duration']<90)
     ]
#question3
americans_90s_df=netflix_df.loc[
    (netflix_df["country"]=='United States')&
    ((netflix_df['release_year']<=1990)&(netflix_df['release_year']<=1999))
]
#question 4
long_comedies_df=netflix_df.loc[
    (netflix_df['genre']=='Comedies')&
    (netflix_df['duration'])>120
]
#question5
recent_horror_df=netflix_df.loc[
    (netflix_df['genre']=='horror')&
    ((netflix_df['release_year']>=2010)&(netflix_df['release_year']<=2020))
]
#question 6
action_comedy_df=netflix_df.loc[
    (netflix_df['genre']=='Action')|(netflix_df['genre']=='Comedies')
]
#question7
selected_countries_df=netflix_df.loc[
    (netflix_df['country']=='United States')|(netflix_df['country']=='India')
]
#question8
old_recent_movies=netflix_df.loc[
    (netflix_df['release_year']<1990)| (netflix_df['release_year']>2018)
]
#question 10
recent_action_comedy=netflix_df.loc[
    (netflix_df['release_year']==2010)&
    ((netflix_df['genre']=='Action')|(netflix_df['genre']=='Comedies'))
]
#question 11
long_selected_genres=netflix_df.loc[
    (netflix_df['duration']>120)&
    ((netflix_df['genre']=='Action')|(netflix_df['genre']=='Dramas'))
]
#question14
selected_genres_df=netflix_df.loc[
    (netflix_df['genre'].isin(['Action','Dramas','Comedies']))
]