# Install the Python library from https://pypi.org/project/amadeus
from ast import keyword
from amadeus import Client, ResponseError

amadeus = Client(
    client_id='YOUR_AMADEUS_API_KEY',
    client_secret='YOUR_AMADEUS_API_SECRET'
)

try:
    '''
    Hotel name autocomplete for keyword 'PARI' using HOTEL_LEISURE and HOTEL_GDS categories of search
    '''
    response = amadeus.reference_data.locations.hotel.get(keyword='PARI', subType=[Hotel.HOTEL_GDS, Hotel.HOTEL_LEISURE])
    print(response.data)
except ResponseError as error:
    raise error
