from weatherhandler import WeatherHandler

# ÖVNINGSPROJEKT - se weatherhandler.py för kontext.
#
# Precis som i din riktiga labb: all print/input hör hemma HÄR,
# aldrig inuti WeatherHandler.
#
# Kom ihåg: bygg dina egna exceptions i weatherhandler.py (t.ex.
# WeatherError som bas, CityNotFoundError, InvalidUnitError,
# WeatherDataError) och importera dem här för att kunna fånga dem
# i menyn med try/except.


def main() -> None:
    """
    Huvudfunktionen som kör väder-applikationen.

    Ska:
    1. Skapa en instans av WeatherHandler.
    2. Visa en meny med alternativ.
    3. Hantera användarens val i en loop tills de väljer att avsluta.
    4. Fånga och hantera fel snyggt - användaren ska aldrig se en rå
       Python-traceback, bara ett vänligt felmeddelande.

    Menyalternativ, förslag:
    [0] - List tracked cities
    [1] - Add a new city
    [2] - Get current temperature for a city
    [3] - Convert a temperature value between units
    [4] - Get forecast trend for a city
    [5] - Refresh data (force a new fetch for all cities)
    [6] - Export data to JSON
    [7] - Exit
    """
    weather_handler = WeatherHandler()

    while True:
        print("\nWeather Explorer Menu:")
        print("[0] - List tracked cities")
        print("[1] - Add a new city")
        print("[2] - Get current temperature for a city")
        print("[3] - Convert a temperature value between units")
        print("[4] - Get forecast trend for a city")
        print("[5] - Refresh data")
        print("[6] - Export data to JSON")
        print("[q] - Exit")

        choice = input("Enter your choice (0-7): ")

        if choice == "0":
            pass

        elif choice == "1":
            pass

        elif choice == "2":
            pass

        elif choice == "3":
            pass

        elif choice == "4":
            pass

        elif choice == "5":
            pass

        elif choice == "6":
            pass

        elif choice == "q":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
