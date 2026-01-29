name = input("What's your name? ")

match name:
    case "Aegon" | "Egg" | "Rhaenyra":
        print("Targaryen")
    case "Lyonel" | "Robert": 
        print("Baratheon")
    case _:
        print("Who?")