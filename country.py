import pandas as pd

country_all = pd.read_csv('country_all_ip.csv', index_col='country')
country_2017 = pd.read_csv('country_2017_ip.csv', index_col='country')

del country_all['Unnamed: 0']
del country_2017['Unnamed: 0']

del country_2017['region']
country_2017 = country_2017.sort_values(['all_ip'], ascending=False)



country_2017 = country_2017.groupby('country').sum()
country_2017 = country_2017.sort_values(['all_ip'], ascending=False)
print(country_2017)
country_2017.to_csv('country_2017.csv')



#del country_all['region']
#country_all = country_all.sort_values(['all_ip'], ascending=False)




#country_all.columns = ['country', 'region', 'all_ip']
#country_2017.columns = ['country', 'region', 'all_ip']

#country_all.to_csv('country_all_ip.csv')
#country_2017.to_csv('country_2017_ip.csv')



#country_all = country_all.groupby(['country'])['all_ip'].count()
#country_all = country_all.sort_value(ascending=True)
#discipline.sort_values(['Red Cards', 'Yellow Cards'], ascending = False)


#print(country_all)


#country_all.to_csv('country_all.csv')

#country_all.sort_values[]
#country_all = country_all.groupby(['country'])['all_ip'].count()


#rtr = ru_stat_all.groupby(['country', 'region'])['last_ip'].count()
#rtr = rtr.sort_values(ascending=False)
#rtr.to_csv('rus_all.csv')



#print(country_all)
#print(country_2017)



#country_all = country_all.groupby(['country'])['last_ip'].count()
#rtr = rtr.sort_values(ascending=False)
#print(country_all)
#rtr.to_csv('rusregions_all.csv')

#rtr = ru_stat_2017.groupby(['country', 'region'])['last_ip'].count()
#rtr = rtr.sort_values(ascending=False)
#print(rtr)
#rtr.to_csv('rusregions_2017.csv')