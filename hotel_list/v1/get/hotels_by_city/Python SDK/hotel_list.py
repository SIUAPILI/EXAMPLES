# Install the Python library from https://pypi.org/project/amadeus
from amadeus import ResponseError, Client

amadeus = Client(
    client_id='YOUR_AMADEUS_API_KEY',
    client_secret='YOUR_AMADEUS_API_SECRET'
)

try:
    '''
    Get list of hotels by city code
    '''
    response = amadeus.reference_data.locations.hotels.by_city.get(cityCode='PAR')

    print(response.data)
except ResponseError as error:
    raise error