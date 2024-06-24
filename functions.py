############### THIS FILE CONTAINS ALL FUNCTIONS OF THE MASTERMIND  #############
import random

# constants Initialization 
SET_OF_NUMBERS = {1, 2, 3, 4, 5, 6}


## This functions allows to initialize game by generate randomly a combinaison of 04 numbers 
def generate_combinaison():
    
    initial_combinaison = [random.choice(list(SET_OF_NUMBERS)) for _ in range (4)]
    print(initial_combinaison)

    return initial_combinaison

# This function allows to initialize players combinaison
def player_initialize_combinaison():
    
    player_combinaison = []
    for i in range (0,4):
        i = i + 1
        combinaison = int(input(f"Entrée votre combinaison N°{i} \n"))
        if combinaison in SET_OF_NUMBERS:
            player_combinaison.append(combinaison)
        else:
            print("la combinaison choisie n'existe pas dans le champ de possibilité ci-dessus:")
            print(f"{SET_OF_NUMBERS}")
            print("Réssayer à nouveau !!")

            ### IL y'a un problème à ce niveau
            player_initialize_combinaison()
    
    print("*********************************************")
    print(f"votre combinaison est {player_combinaison}  **")
    print("*********************************************")

    return player_combinaison

# This function allows to check the existence of the combinaison of the player and the initial combinaison and return which element is correct,
# check also if it's at the correct position by using the symbol (*) or wrong position by using this symbol(°) 

def check_combinaisons(player_combinaison, initial_combinaison):
    check_combinaison = []
    for position, number in enumerate(player_combinaison):
      
        if number in initial_combinaison:
            ### IL y'a un problème à ce niveau
            if number == initial_combinaison[position]:
                check_combinaison.append(f"{number}*")
                
            else:
                check_combinaison.append(f"{number}°")
                
        else:
            check_combinaison.append(f"{number}")
    return check_combinaison

def turn_manager(initial_combinaison):
    print("Vous avez droit à 10 tentatives\n")
    numbers_of_turns = 0
    while numbers_of_turns < 11:
        print(f"Vous êtes au tour N° {numbers_of_turns + 1} sur 10\n")

        player_combinaison = player_initialize_combinaison()
        check_combinaison = check_combinaisons(player_combinaison, initial_combinaison)
        correct_combinaison = 0

        print(check_combinaison)
        for combinaison in check_combinaison:                    
            if "*" in combinaison:
                correct_combinaison +=1
        if correct_combinaison == 4:
            print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
            print("°                    Vous avez trouvez la combinaison exacte !!                                                         °")
            print(f"°                          {initial_combinaison}                                                              °")
            print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
            break

        numbers_of_turns += 1
        if numbers_of_turns == 10:
            print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°° Vous avez épuisé vos essais °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n")
            print("                                     Vous n'avez pas trouvez la combinaison correct                                    °°")
            print(f"                                 la combinaison correcte est : {initial_combinaison}                                  °°")
            print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
            break


initial_combinaison = generate_combinaison()
turn_manager(initial_combinaison)

