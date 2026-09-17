from weatherhandler import WeatherHandler
from text import text as t

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
    """
    weather_handler = WeatherHandler()

    while True:
        print(t["main_menu"]["menu"])

        choice = input(t["common"]["empty_input"])

        if choice == "q":
            print(t["main_menu"]["exit"])
            break

        try:
            choice = int(choice)
        except ValueError:
            print(t["main_menu"]["invalid_choice"])
            return

        if choice == 0:
            pass

        elif choice == 1:
            pass

        elif choice == 2:
            pass

        elif choice == 3:
            pass

        elif choice == 4:
            pass

        elif choice == 5:
            pass

        elif choice == 6:
            pass
        else:
            print(t["main_menu"]["invalid_choice"])


if __name__ == "__main__":
    # Only run main() if this file is executed directly (not when imported)
    main()
