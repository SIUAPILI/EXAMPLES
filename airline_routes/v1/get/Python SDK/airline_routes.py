# Install the Python library from https://pypi.org/project/amadeus
from amadeus import Client, ResponseError

amadeus = Client(
    client_id='YOUR_AMADEUS_API_KEY',
    client_secret='YOUR_AMADEUS_API_SECRET'
)

try:
    '''
    What are the destinations served by the British Airways (BA)?
    '''
    response = amadeus.airline.destinations.get(airlineCode='BA')
    print(response.data)
except ResponseError as error:
    raise error
