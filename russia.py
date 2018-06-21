import pandas as pd
from okrug import oblast

rus_all = pd.read_csv('rus_all_ip.csv')
rus_2017 = pd.read_csv('rus_2017_ip.csv')

#rus_all.columns = ['country', 'region', 'all_ip']
#rus_2017.columns = ['country', 'region', 'all_ip']

rus_all = rus_all.set_index('country')
rus_2017 = rus_2017.set_index('country')

rus_all.to_csv('rus_all_ip.csv')
rus_2017.to_csv('rus_2017_ip.csv')

rus_obl_all = pd.merge(rus_all, oblast, on='region')
rus_obl_2017 = pd.merge(rus_2017, oblast, on='region')

#print(rus_obl_all)
#print(rus_obl_2017)

del rus_obl_all['Unnamed: 0']
del rus_obl_2017['Unnamed: 0']

rus_obl_all = rus_obl_all.set_index('Avtonom')
rus_obl_2017 = rus_obl_2017.set_index('Avtonom')

rus_obl_all = rus_obl_all.groupby(['Avtonom', 'region'])['all_ip'].sum(asending = True)
rus_obl_2017 = rus_obl_2017.groupby(['Avtonom', 'region'])['all_ip'].sum()

rus_obl_all.to_csv('sort_avtonom_ocrug__all.csv')
rus_obl_2017.to_csv('sort_avtonom_ocrug_2017.csv')

#rus_obl_all = rus_obl_all.groupby('country').sum()
#rus_obl_2017 = rus_obl_2017.groupby('country').sum()

rus_obl_all.columns = ['country', 'region', 'all_ip']
rus_obl_2017.columns = ['country', 'region', 'all_ip']

rus_obl_all = rus_obl_all.groupby(['Avtonom']).sum()
rus_obl_2017 = rus_obl_2017.groupby(['Avtonom']).sum()

rus_obl_all = rus_obl_all.sort_values(ascending=False)
rus_obl_2017 = rus_obl_2017.sort_values(ascending=False)

rus_obl_all.to_csv('avtonom_ocrug_all.csv')
rus_obl_2017.to_csv('avtonom_ocrug_2017.csv')

print(rus_obl_all)
print(rus_obl_2017)






#rus_all.columns = ['country', 'region', 'all_ip']
#rus_2017.columns = ['country', 'region', 'all_ip']

#rus_obl_all = rus_obl_all.groupby(['Avtonom', 'region'])['all_ip'].sum()
#rus_obl_2017 = rus_obl_2017.groupby(['Avtonom', 'region'])['all_ip'].sum()

#rus_obl_all = rus_obl_all.sort_values(['all_ip'], ascending=False)
#rus_obl_2017 = rus_obl_2017.sort_values(['all_ip'], ascending=False)

#rus_obl_all = rus_obl_all.sort_values(by = "all_ip", ascending = False)

#rus_obl_all = rus_obl_all.set_index()

#print(rus_obl_all)
#print(rus_obl_2017)