from typing import Any

import requests

#
# API att använda: OpenWeatherMap (https://openweathermap.org/api)
# - Skapa ett gratiskonto, hämta din API-nyckel under "API keys" på ditt konto
# - OBS: en nyskapad nyckel kan ta upp till en timme innan den aktiveras
# - Gratis-tier: 60 anrop/minut, 1 000 000 anrop/månad - var ändå försiktig
#   med loopar under utveckling, precis som i din riktiga labb
#
# Relevanta endpoints att utforska i deras dokumentation:
# - Aktuellt väder för en stad:
#   https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric
#
# Testa båda URL:erna i webbläsaren (byt ut {city} och {API_KEY}) för att se
# exakt hur svaret ser ut, INNAN du börjar koda.
#
# Tänk på klassen som ENDAST hanterande funktionalitet - ingen print/input
# här. All interaktion sker i main_weather.py.


class WeatherHandler:
    def __init__(self, filepath: str = "weather_cache.json"):
        """
        Initiera WeatherHandler.

        Ska:
        1. Försöka ladda sparad väderdata från en lokal JSON-fil
           (load_weather_data).
        2. Om ingen fil finns, eller datan är för gammal (fundera på ett
           rimligt tidsintervall - väder ändras snabbare än valutakurser!),
           hämta färsk data (fetch_weather_data).
        3. Spara resultatet i ett lämpligt instansattribut.

        Fundera: till skillnad från din CurrencyHandler, som hämtar ALLA
        valutakurser i ett enda anrop, kräver detta API ett SEPARAT anrop
        PER STAD. Hur vill du hantera det - en lista med städer du bevakar,
        satt vid skapandet? Något annat sätt? Det finns inget facit, men
        du måste bestämma dig för en design.
        """
        pass

    def fetch_weather_data(self, city: str) -> dict[str, Any]:
        """
        Hämta färsk väderdata för EN stad från OpenWeatherMap.

        Ska:
        1. Göra ett GET-anrop mot rätt endpoint.
        2. Hantera requests.exceptions (Timeout, ConnectionError, HTTPError -
           notera att en OGILTIG stad ger ett 404-svar, inte ett Python-fel
           automatiskt - du behöver troligen kolla status_code eller använda
           raise_for_status()).
        3. Returnera den relevanta datan.

        Args:
            city: Namnet på staden, t.ex. "Stockholm".

        Returns:
            Ett dict med väderdata för staden.

        Raises:
            Ditt eget custom exception vid nätverksfel eller ogiltig stad.
        """
        pass

    def get_temperature(self, city: str) -> float:
        """
        Hämta aktuell temperatur (Celsius) för en stad.

        Ska:
        - LBYL: kontrollera att `city` är en giltig, icke-tom sträng.
        - EAFP: slå upp staden i din interna, sparade data.
        - Kasta ett eget exception, t.ex. CityNotFoundError, om staden
          inte finns i den sparade datan (fundera: ska den då försöka
          FETCHA staden automatiskt, eller kräva att man lagt till den
          separat först? Du väljer, motivera för dig själv.)

        Returns:
            Temperaturen i Celsius, som ett flyttal.
        """
        pass

    def convert_temperature(self, value: float, from_unit: str, to_unit: str) -> float:
        """
        Konvertera ett temperaturvärde mellan Celsius, Fahrenheit och Kelvin.
        Detta kräver INGET API-anrop, bara matematik - jämför med hur
        convert_any_currency i din riktiga labb kan lösas med "basic math".

        Args:
            value: Temperaturvärdet att konvertera.
            from_unit: Enheten värdet redan är i ("C", "F" eller "K").
            to_unit: Enheten att konvertera TILL.

        Returns:
            Det konverterade värdet.

        Raises:
            ValueError eller ditt eget exception om from_unit/to_unit
            inte är giltiga enheter.
        """
        pass

    def list_cities(self) -> list[str]:
        """
        Lista alla städer du för närvarande har sparad data för,
        alfabetiskt sorterade.

        Returns:
            En sorterad lista av stadsnamn.
        """
        pass

    def add_city(self, city: str) -> None:
        """
        Lägg till en ny stad att bevaka - hämtar färsk data för den
        och sparar i din interna datastruktur.

        Ska hantera fallet att staden redan finns (uppdatera, eller
        kasta ett eget exception - du väljer och motiverar).

        Raises:
            Ditt eget exception om staden inte kan hittas via API:et.
        """
        pass

    def load_weather_data(self) -> dict[str, Any]:
        """
        Ladda väderdata från cache-filen, eller hämta färsk data om cachen
        saknas, är trasig, eller är för gammal.

        Följ samma cache-mönster du redan övat på:
        1. EAFP: försök läsa filen (FileNotFoundError, json.JSONDecodeError).
        2. Om den lästes OK: kolla tidsstämpeln - för gammal?
        3. Vid behov: hämta färsk data för alla bevakade städer på nytt.

        Returns:
            Ett dict med all sparad väderdata.
        """
        pass

    def get_forecast_trend(self, city: str, days: int) -> list[tuple[str, float]]:
        """
        Hämta en prognos-trend för en stad över ett antal dagar, med hjälp
        av 5-dagars-forecast-endpointen (jämför med hur din riktiga labb
        ber dig lista HISTORISKA kurser - detta är samma idé, fast framåt
        i tiden istället för bakåt, eftersom gratis-tier inte ger historik).

        Args:
            city: Stadens namn.
            days: Antal dagar att inkludera (max 5, eftersom API:et bara
                  ger 5 dagar framåt på gratis-nivå).

        Returns:
            En lista av tuples: (datum, temperatur), sorterad efter datum.

        Raises:
            ValueError eller eget exception om days är ogiltigt (t.ex. >5).
        """
        pass

    def export_to_json(self, filepath: str) -> None:
        """
        Exportera nuvarande väderdata till en JSON-fil.

        Ska hantera fel vid filskrivning (OSError, eller ett eget
        exception som wrappar den).
        """
        pass


# ============================================================
# BONUS (frivilligt, för extra övning på arv):
# Fundera på om det finns anledning att ha olika "typer" av väderrapporter
# - t.ex. en CurrentWeather och en ForecastWeather som ärver från en
# gemensam WeatherReport-basklass. Inte nödvändigt, men bra extraövning
# om du känner för det.
# ============================================================
