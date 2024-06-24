############### THIS FILE CONTAINS ALL FUNCTIONS OF THE MASTERMIND  #############
import random

# constants Initialization
### Initialization of set combination 
SET_OF_NUMBERS = set(random.randint(1, 10) for _ in range(6))


## This functions allows to initialize game by generate randomly a combination of 04 numbers 
def generate_combination():
    
    initial_combination = [random.choice(list(SET_OF_NUMBERS)) for _ in range (4)]
    print(initial_combination)
    display_game_rules()
    return initial_combination

# This function allows to initialize players combination
def player_initialize_combination():    
    player_combination = []
    i = 1
    while i < 5:   
        while True:
            try:
                combination = int(input(f"Entrée votre combinaison N°{i} :  "))
                if combination in SET_OF_NUMBERS:
                    player_combination.append(combination)
                    i += 1
                    break
                else:
                    print("La combinaison choisie n'existe pas dans le champ de possibilité ci-dessous:")
                    print(f"{SET_OF_NUMBERS}")
                    print("Réessayez à nouveau !!\n")
            except ValueError:
                print("Entrez un nombre entier.\n")

    print("************************************************")
    print(f"*  votre combination est {player_combination}               *")
    print("************************************************")

    return player_combination

# This function allows to check the existence of the combination of the player and the initial combination and return which element is correct,
# check also if it's at the correct position by using the symbol (*) or wrong position by using this symbol(°) 

def check_combinations(player_combination, initial_combination):
    check_combination = []
    matched_positions = [False] * len(initial_combination)  # Track matched positions to avoid double counting
    
    for position, number in enumerate(player_combination):
        if number in initial_combination:
            if number == initial_combination[position] and not matched_positions[position]:
                check_combination.append(f"{number}*")
                matched_positions[position] = True  # Mark this position as matched
            else:
                # Find the next unmatched position for the current number
                found_match = False
                for pos, val in enumerate(initial_combination):
                    if val == number and not matched_positions[pos]:
                        matched_positions[pos] = True  
                        found_match = True
                        break
                if found_match:
                    check_combination.append(f"{number}°")
                else:
                    check_combination.append(f"{number}")
        else:
            check_combination.append(f"{number}")
    
    return check_combination

# This function allows to manage player's turns game which is 10 turns
def turn_manager(initial_combination):
    print("Vous avez droit à 10 tentatives\n")
    numbers_of_turns = 0
    while numbers_of_turns < 11:
        print(f"Vous êtes au tour N° {numbers_of_turns + 1} sur 10\n")

        player_combination = player_initialize_combination()
        check_combination = check_combinations(player_combination, initial_combination)
        correct_combination = 0

        print(check_combination)
        for combination in check_combination:                    
            if "*" in combination:
                correct_combination +=1
        if correct_combination == 4:
            print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
            print("°                    Vous avez trouvez la combinaison exacte !!                           °")
            print(f"°                          {initial_combination}                                         °")
            print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
            break

        numbers_of_turns += 1
        if numbers_of_turns == 10:
            print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°° Vous avez épuisé vos essais °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n")
            print("                                     Vous n'avez pas trouvez la combinaison correct                                    °°")
            print(f"                                 la combinaison correcte est : {initial_combination}                                  °°")
            print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
            break

### Faire une fonction pour l'affichage des règles du jeu
def display_game_rules():
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    print("     ---------------------------------------------------------------------------------------------------------------")
    print("             ----------------------------------------------- MASTERMIND -----------------------------------              ")
    print("     ---------------------------------------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------------------------------------------------------------")

    print (" REGLES DU JEU : ")
    print("""
            Le jeu de Mastermind consiste à deviner une combinaison secrète de 04 nombres. Voici comment cela fonctionne de manière simple et fun :

            1. Devine la combinaison secrète de nombres.
            2. Pour chaque nombre deviné :
            - '*' signifie que le chiffre est correct et bien placé.
            - '°' signifie que le chiffre est correct mais mal placé.
            - Pas de symbole signifie que le chiffre est incorrect.
            3. Utilise ces indices pour affiner ta prochaine tentative.

            Prêt à défier ton esprit logique et ton sens de la déduction ? Que la partie commence !
""")




initial_combination = generate_combination()
turn_manager(initial_combination)

# Example input
input_value = 42

# Check if the input is an integer
if isinstance(input_value, int):
    print("The input is an integer.")
else:
    print("The input is not an integer.")
