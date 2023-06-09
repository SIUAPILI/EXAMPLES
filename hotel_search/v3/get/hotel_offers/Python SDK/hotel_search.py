# Install the Python library from https://pypi.org/project/amadeus
from amadeus import Client, ResponseError

amadeus = Client(
    client_id='YOUR_AMADEUS_API_KEY',
    client_secret='YOUR_AMADEUS_API_SECRET'
)

try:
    # Get list of Hotels by city code
    hotels_by_city = amadeus.shopping.hotel_offers_search.get(
        hotelIds='RTPAR001', adults='2')
except ResponseError as error:
    raise error
