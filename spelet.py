import random
import json

def spela_ny_omgång():
    nummer = random.randint(1, 100)
    försök = 0

    while True:
        gissning = input("Gissa ett nummer mellan 1 och 100: ")
        försök += 1

        try:
            gissning = int(gissning)
        except ValueError:
            print("Ogiltig inmatning, försök igen.")
            continue

        if gissning < nummer:
            print("För lågt!")
        elif gissning > nummer:
            print("För högt!")
        else:
            print(f"Grattis! Du gissade rätt på {försök} försök.")
            print(" ")
            return försök


def visa_highscore():
    try:
        with open("highscore.json", "r", encoding="UTF-8") as fil:
            highscores = json.load(fil)

            if not highscores:
                print("Ingen highscore tillgänglig.")
                return

            bästa = highscores[0]
            print(f"Highscore: {bästa['namn']} med {bästa['försök']} försök.")

    except (FileNotFoundError, ValueError, IndexError):
        print("Ingen highscore tillgänglig.")


def spara_highscore(försök):
    spelaresnamn = input("Ange ditt namn: ")
    ny_score = {"namn": spelaresnamn, "försök": str(försök)}

    try:
        with open("highscore.json", "r", encoding="UTF-8") as fil:
            highscores = json.load(fil)

            if not isinstance(highscores, list):
                highscores = []

    except (FileNotFoundError, ValueError):
        highscores = []

    highscores.append(ny_score)

    # sortera efter antal försök (lägst först)
    highscores.sort(key=lambda x: int(x["försök"]))

    with open("highscore.json", "w", encoding="UTF-8") as fil:
        json.dump(highscores, fil)

    print("Score sparad!")


while True:
    print("--- HÖGT/LÅGT---")
    print("1. Spela ny omgång")
    print("2. Visa highscore")
    print("3. Avsluta\n")
    val = input("Välj ett alternativ: ")

    if val == "1":
        spara_highscore(spela_ny_omgång())
    elif val == "2":
        visa_highscore()
    elif val == "3":
        print("Tack för att du spelade!")
        break
    else:
        print("Ogiltigt val, försök igen.")