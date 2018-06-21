import pandas as pd

raw_data = {
    'Avtonom': ['Sibirsky', 'Privolzhskiy', 'Yuzhniy', 'Privolzhskiy', 'Centralniy', 'Privolzhskiy', 'Centralniy',
                'Centralniy', 'Yuzhniy', 'Severo-Zapad', 'Sibirsky', 'Uralskyi', 'Sibirsky', 'Centralniy', 'Centralniy',
                'Privolzhskiy', 'Severo-Zapad', 'Yuzhniy', 'Centralniy', 'Severo-Kavkazskiy', 'Centralniy',
                'Dalnevostochniy', 'Centralniy', 'Severo-Zapad', 'Privolzhskiy', 'Severo-Zapad', 'Severo-Kavkazskiy',
                'Centralniy', 'Privolzhskiy', 'Uralskyi', 'Uralskyi', 'Centralniy',
                'Centralniy', 'Privolzhskiy', 'Centralniy', 'Sibirsky', 'Sibirsky', 'Dalnevostochniy', 'Yuzhniy',
                'Uralskyi', 'Sibirsky', 'Centralniy', 'Severo-Zapad', 'Uralskyi', 'Privolzhskiy', 'Dalnevostochniy',
                'Privolzhskiy', 'Centralniy', 'Dalnevostochniy', 'Centralniy', 'Uralskyi', 'Severo-Zapad',
                'Dalnevostochniy', 'Privolzhskiy', 'Yuzhniy', 'Severo-Zapad', 'Privolzhskiy', 'Centralniy',
                'Privolzhskiy', 'Centralniy', 'Severo-Kavkazskiy', 'Sibirsky', 'Severo-Zapad', 'Severo-Zapad',
                'Dalnevostochniy', 'Privolzhskiy', 'Severo-Kavkazskiy', 'Centralniy', 'Yuzhniy', 'Sibirsky',
                'Sibirsky', 'Privolzhskiy', 'Severo-Zapad', 'Sibirsky', 'Severo-Kavkazskiy', 'Sibirsky',
                'Dalnevostochniy', 'Dalnevostochniy', 'Severo-Kavkazskiy', 'Severo-Kavkazskiy', 'Severo-Zapad',
                'Sibirsky', 'Dalnevostochniy', ''],
    'region': ['Krasnoyarskiy Kray', 'Saratovskaya Oblast\'', 'Rostov', 'Respublika Mariy-El', 'Moscow Oblast',
               'Kirovskaya Oblast\'', 'Tverskaya Oblast\'', 'Orlovskaya Oblast\'', 'Astrakhanskaya Oblast\'',
               'Kaliningradskaya Oblast\'',
               'Altai Krai', 'Chelyabinsk', 'Irkutskaya Oblast\'', 'Vladimirskaya Oblast\'', 'Bryanskaya Oblast\'',
               'Samarskaya Oblast\'', 'Komi Republic', 'Volgogradskaya Oblast\'', 'Tambovskaya Oblast\'',
               'Stavropol\'skiy Kray', 'Kurskaya Oblast\'', 'Amurskaya Oblast\'', 'Moscow',
               'St.-Petersburg', 'Tatarstan', 'Murmansk', 'Karachayevo-Cherkesiya', 'Ivanovskaya Oblast\'',
               'Nizhegorodskaya Oblast\'', 'Sverdlovskaya Oblast\'', 'Tyumenskaya Oblast\'', 'Belgorodskaya Oblast\'',
               'Lipetskaya Oblast\'', 'Penzenskaya Oblast\'', 'Tul\'skaya Oblast\'', 'Respublika Buryatiya', 'Transbaikal Territory',
               'Sakhalinskaya Oblast\'', 'Krasnodarskiy Kray', 'Kurganskaya Oblast\'',
               'Kemerovskaya Oblast\'', 'Kaluzhskaya Oblast\'', 'Vologodskaya Oblast\'',
               'Khanty-Mansiyskiy Avtonomnyy Okrug-Yugra', 'Bashkortostan', 'Kamtchatski Kray',
               'Orenburgskaya Oblast\'', 'Smolenskaya Oblast\'', 'Primorskiy Kray', 'Yaroslavskaya Oblast\'',
               'Yamalo-Nenetskiy Avtonomnyy Okrug', 'Leningrad', 'Respublika Sakha (Yakutiya)', 'Chuvashia',
               'Respublika Adygeya', 'Novgorodskaya Oblast\'', 'Udmurtskaya Respublika', 'Voronezhskaya Oblast\'',
               'Perm Krai', 'Kostromskaya Oblast\'', 'North Ossetia', 'Respublika Khakasiya', 'Arkhangelskaya',
               'Pskovskaya Oblast\'', 'Khabarovsk Krai', 'Ulyanovsk Oblast', 'Kabardino-Balkarskaya Respublika',
               'Ryazanskaya Oblast\'', 'Kalmykiya', 'Tomskaya Oblast\'', 'Novosibirskaya Oblast\'',
               'Respublika Mordoviya', 'Republic of Karelia', 'Respublika Altay', 'Dagestan', 'Omskaya Oblast\'',
               'Magadanskaya Oblast\'', 'Chukotskiy Avtonomnyy Okrug', 'Chechnya', 'Respublika Ingushetiya',
               'Nenetskiy Avtonomnyy Okrug', 'Respublika Tyva', 'Jewish Autonomous Oblast', ''
               ]}
obl = pd.DataFrame(raw_data, columns=['Avtonom', 'region'])
oblast = obl
#print(oblast)
# 'Sibirsky', 'Privolzhskiy', 'Yuzhniy', 'Privolzhskiy', 'Centralniy', 'Privolzhskiy', 'Centralniy', 'Centralniy', 'Yuzhniy', 'Severo-Zapad', 'Sibirsky', 'Uralskyi', 'Sibirsky', 'Centralniy', 'Centralniy', 'Privolzhskiy', 'Severo-Zapad',
# 'Yuzhniy', 'Centralniy', 'Severo-Kavkazskiy', 'Centralniy', 'Dalnevostochniy', 'Centralniy', 'Severo-Zapad', 'Privolzhskiy', 'Severo-Zapad', 'Severo-Kavkazskiy', 'Centralniy', 'Privolzhskiy', 'Uralskyi', 'Uralskyi', 'Centralniy',
# 'Centralniy', 'Privolzhskiy', 'Centralniy', 'Sibirsky', 'Sibirsky', 'Dalnevostochniy', 'Yuzhniy', 'Uralskyi', 'Sibirsky', 'Centralniy', 'Severo-Zapad', 'Uralskyi', 'Privolzhskiy', 'Dalnevostochniy', 'Privolzhskiy', 'Centralniy',
# 'Dalnevostochniy', 'Centralniy', 'Uralskyi', 'Severo-Zapad', 'Dalnevostochniy', 'Privolzhskiy', 'Yuzhniy', 'Severo-Zapad', 'Privolzhskiy', 'Centralniy', 'Privolzhskiy', 'Centralniy', 'Severo-Kavkazskiy', 'Sibirsky'
# 'Severo-Zapad', 'Severo-Zapad', 'Dalnevostochniy', 'Privolzhskiy', 'Severo-Kavkazskiy', 'Centralniy', 'Yuzhniy', 'Sibirsky', 'Sibirsky', 'Privolzhskiy', 'Severo-Zapad', 'Sibirsky', 'Severo-Kavkazskiy', 'Sibirsky',
# 'Dalnevostochniy', 'Dalnevostochniy', 'Severo-Kavkazskiy', 'Severo-Kavkazskiy', 'Severo-Zapad', 'Sibirsky', 'Dalnevostochniy', ''
