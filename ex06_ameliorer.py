import random

nb_a_deviner = random.randint(1, 100)
tentative1 = tentative2 = tentative3 = 0
hitany_ve = False
user = {"user1": tentative1, "user2": tentative2, "user3": tentative3}
lst_tentative = []

for user_input, tentative in user.items() :
    while tentative < 10:
        user_input = input("Devine un nombre entre à 1 et 100: ")
        tentative_restante = 9 - tentative
        print("Tentative restante : ", tentative_restante)
        if user_input.isdigit() :
            user_input = int(user_input)
            if user_input > nb_a_deviner :
                print("Trop grand")
            elif user_input < nb_a_deviner :
                print("Trop petit")
            else :
                hitany_ve = True
                print("Vous avez reussi")
                print("\n \n")
                lst_tentative.append(tentative_restante)
                break
            tentative += 1
    if not hitany_ve :
        lst_tentative.append(tentative_restante)
        print("Game over")
        print("La reponse est : ", nb_a_deviner)
        print("\n \n")
user["user1"] = lst_tentative[0]
user["user2"] = lst_tentative[1]
user["user3"] = lst_tentative[2]
tentative_min = max(lst_tentative)
if lst_tentative == [0, 0, 0] :
    print("Game Over\n Aucun gagnant\n")
else :
    for k, v in user.items() :
        if v == tentative_min :
            print("La gagnant(e) est : ", k )