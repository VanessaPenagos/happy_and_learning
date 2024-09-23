# -*- coding: utf-8 -*-


countries  = {
  'colombia': 49,
  'mexico': 122,
  'argentina': 49,
  'chile':18,
  'peru': 31
}

while True:
    country = str(raw_input('Enter the name of a country: ')).lower();
    try:
        print('The population of {} is: {} millions'.format(country, countries[country]))
    except KeyError:
        print('We do not have the data for the population of {}'.format(country))
