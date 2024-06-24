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
        combination = int(input(f"Entrée votre combinaison N°{i} :  "))
        if combination in SET_OF_NUMBERS:
            player_combination.append(combination)
            i += 1 
        else :
            print("la combinaison choisie n'existe pas dans le champ de possibilité ci-dessus:")
            print(f"{SET_OF_NUMBERS}")
            print("Réssayer à nouveau !!\n")
            combination = int(input(f"Entrée votre combinaison N°{i} :  \n"))
            player_combination.append(combination)
            i += 1 

    print("*********************************************")
    print(f"votre combination est {player_combination}  **")
    print("*********************************************")

    return player_combination

# This function allows to check the existence of the combination of the player and the initial combination and return which element is correct,
# check also if it's at the correct position by using the symbol (*) or wrong position by using this symbol(°) 

def check_combinations(player_combination, initial_combination):
    check_combination = []
    count_of_number = 0
    for position, number in enumerate(player_combination):
      
        if number in initial_combination:
            ####### PROBLEME RENCONTRE: Gestion des positionnements 

            ### To count the occurence of a number in the initial list
            count_of_number = initial_combination.count(number)
            while count_of_number >= 0: 
                if number == initial_combination[position]:
                    check_combination.append(f"{number}*")
                    
                else:
                    check_combination.append(f"{number}°")
                    
                count_of_number -=1               
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
            print("°                    Vous avez trouvez la combinaison exacte !!                                                         °")
            print(f"°                          {initial_combination}                                                              °")
            print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
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

    print (" Règles du Jeu : ")
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

