
import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('Life Expectancy Data.csv')
print(df.columns)

# Dicionários de mapeamento para cada coluna
status_map = {'Developing': 0, 'Developed': 1}
Country_map = {
    'Afghanistan': 0, 'Albania': 1, 'Algeria': 2, 'Angola': 3,
    'Antigua and Barbuda': 4, 'Argentina': 5, 'Armenia': 6, 'Australia': 7,
    'Austria': 8, 'Azerbaijan': 9, 'Bahamas': 10, 'Bahrain': 11,
    'Bangladesh': 12, 'Barbados': 13, 'Belarus': 14, 'Belgium': 15,
    'Belize': 16, 'Benin': 17, 'Bhutan': 18, 'Bolivia (Plurinational State of)': 19,
    'Bosnia and Herzegovina': 20, 'Botswana': 21, 'Brazil': 22, 'Brunei Darussalam': 23,
    'Bulgaria': 24, 'Burkina Faso': 25, 'Burundi': 26, 'Cabo Verde': 27,
    'Cambodia': 28, 'Cameroon': 29, 'Canada': 30, 'Central African Republic': 31,
    'Chad': 32, 'Chile': 33, 'China': 34, 'Colombia': 35,
    'Comoros': 36, 'Congo': 37, 'Costa Rica': 38, 'Croatia': 39,
    'Cuba': 40, 'Cyprus': 41, 'Denmark': 42, 'Djibouti': 43,
    'Dominica': 44, 'Dominican Republic': 45, 'Ecuador': 46, 'El Salvador': 47,
    'Equatorial Guinea': 48, 'Eritrea': 49, 'Estonia': 50, 'Ethiopia': 51,
    'Fiji': 52, 'Finland': 53, 'France': 54, 'Gabon': 55,
    'Georgia': 56, 'Germany': 57, 'Ghana': 58, 'Greece': 59,
    'Grenada': 60, 'Guatemala': 61, 'Guinea': 62, 'Guinea-Bissau': 63,
    'Guyana': 64, 'Haiti': 65, 'Honduras': 66, 'Hungary': 67,
    'Iceland': 68, 'India': 69, 'Indonesia': 70, 'Iran (Islamic Republic of)': 71,
    'Iraq': 72, 'Ireland': 73, 'Israel': 74, 'Italy': 75,
    'Jamaica': 76, 'Japan': 77, 'Jordan': 78, 'Kazakhstan': 79,
    'Kenya': 80, 'Kiribati': 81, 'Kuwait': 82, 'Latvia': 83,
    'Lebanon': 84, 'Lesotho': 85, 'Liberia': 86, 'Libya': 87,
    'Lithuania': 88, 'Luxembourg': 89, 'Madagascar': 90, 'Malawi': 91,
    'Malaysia': 92, 'Mali': 93, 'Malta': 94, 'Mauritania': 95,
    'Mexico': 96, 'Mongolia': 97, 'Montenegro': 98, 'Morocco': 99,
    'Mozambique': 100, 'Myanmar': 101, 'Namibia': 102, 'Nepal': 103,
    'Netherlands': 104, 'Nicaragua': 105, 'Niger': 106, 'Nigeria': 107,
    'Niue': 108, 'Norway': 109, 'Pakistan': 110, 'Palau': 111,
    'Panama': 112, 'Papua New Guinea': 113, 'Paraguay': 114, 'Peru': 115,
    'Philippines': 116, 'Poland': 117, 'Portugal': 118, 'Qatar': 119,
    'Republic of Korea': 120, 'Republic of Moldova': 121, 'Romania': 122, 'Russian Federation': 123,
    'Rwanda': 124, 'Saint Kitts and Nevis': 125, 'Saint Lucia': 126, 'Saint Vincent and the Grenadines': 127,
    'Samoa': 128, 'San Marino': 129, 'Sao Tome and Principe': 130, 'Saudi Arabia': 131,
    'Senegal': 132, 'Serbia': 133, 'Seychelles': 134, 'Sierra Leone': 135,
    'Singapore': 136, 'Slovakia': 137, 'Solomon Islands': 138, 'Somalia': 139,
    'South Africa': 140, 'South Sudan': 141, 'Spain': 142, 'Sri Lanka': 143,
    'Sudan': 144, 'Suriname': 145, 'Swaziland': 146, 'Sweden': 147,
    'Switzerland': 148, 'Syrian Arab Republic': 149, 'Tajikistan': 150, 'Thailand': 151,
    'The former Yugoslav republic of Macedonia': 152, 'Timor-Leste': 153, 'Togo': 154, 'Tonga': 155,
    'Trinidad and Tobago': 156, 'Tunisia': 157, 'Turkey': 158, 'Turkmenistan': 159,
    'Tuvalu': 160, 'Uganda': 161, 'Ukraine': 162, 'United Arab Emirates': 163,
    'United Kingdom of Great Britain and Northern Ireland': 164, 'United Republic of Tanzania': 165,
    'United States of America': 166, 'Uruguay': 167, 'Uzbekistan': 168, 'Vanuatu': 169,
    'Venezuela (Bolivarian Republic of)': 170, 'Viet Nam': 171, 'Yemen': 172, 'Zambia': 173,
    'Zimbabwe': 174
}

# Aplicar o mapeamento para cada coluna relevante
df['Country'] = df['Country'].map(Country_map)
df['Status'] = df['Status'].map(status_map)

# remove todas linhas que tem pelo menos um valor faltante
df = df.dropna()

# Salvar as alterações em um novo arquivo CSV ou sobrescrever o existente
df.to_csv('LifeExpectancyData_Alterada.csv', index=False)

