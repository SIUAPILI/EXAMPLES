// How to install the library at https://github.com/amadeus4dev/amadeus-java

import com.amadeus.Amadeus;
import com.amadeus.Params;
import com.amadeus.exceptions.ResponseException;
import com.amadeus.resources.HotelOfferSearch;

public class HotelSearch {

  public static void main(String[] args) throws ResponseException {
    Amadeus amadeus = Amadeus
      .builder("YOUR_AMADEUS_API_KEY", "YOUR_AMADEUS_API_SECRET")
      .build();

    HotelOfferSearch[] offers = amadeus.shopping.hotelOffersSearch.get(
      Params.with("hotelIds", "RTPAR001")
        .and("adults", 2)
    );

    if (offers[0].getResponse().getStatusCode() != 200) {
      System.out.println("Wrong status code: " + offers[0].getResponse().getStatusCode());
      System.exit(-1);
    }

    System.out.println(offers[0]);
  }
}