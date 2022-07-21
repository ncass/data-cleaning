from numpy import where
import pandas as pd

'''script to read in a csv and convert it to a pandas dataframe to clean'''
f = open('C:/Users/Nick/Downloads/archive/anime.csv', 'r', encoding="utf-8")
x = pd.read_csv(f)
x.rename(columns={'anime_id': 'ID', 'name': 'Name', 'genre': 'Genre', 'type': 'TV/Movie', 'episodes': 'Episode Count', 'rating': 'User Rating', 'members': 'Members'}, inplace=True)

# criteria for separate excel sheets
tv = x.where((x['User Rating'] > 5) & (x['Genre'] != 'Hentai') & (x['TV/Movie'] == 'TV'))
movie = x.where((x['User Rating'] > 5) & (x['Genre'] != 'Hentai') & (x['TV/Movie'] == 'Movie')) 
ova = x.where((x['User Rating'] > 5) & (x['Genre'] != 'Hentai') & (x['TV/Movie'] == 'OVA'))  

#drop unnecessary columns
tv.drop(['Members', 'ID'], axis=1, inplace=True)
movie.drop(['Members', 'ID'], axis=1, inplace=True)
ova.drop(['Members', 'ID'], axis=1, inplace=True)

# remove null rows
tv.dropna(inplace=True)
movie.dropna(inplace=True)
ova.dropna(inplace=True)

#write to separate excel sheets for same doc
with pd.ExcelWriter('C:/Users/Nick/Downloads/archive/refined_list.xlsx') as writer:
    tv.to_excel(writer, sheet_name='tv', float_format='%.2f', index='true')
    movie.to_excel(writer, sheet_name='movie', float_format='%.2f', index='true')
    ova.to_excel(writer, sheet_name='ova', float_format='%.2f', index='true')

