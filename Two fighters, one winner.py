def declare_winner(fighter1, fighter2, first_attacker):
    if first_attacker in fighter1:
        first_blood = list(fighter1)
        second_blood = list(fighter2)
    else:
        first_blood = list(fighter2)
        second_blood = list(fighter1)

    while True:
        second_blood[1] -= first_blood[2]
        if second_blood[1] <= 0:
            return first_blood[0]

        first_blood[1] -= second_blood[2]
        if first_blood[1] <= 0:
            return second_blood[0]


print(declare_winner(("Lew", 10, 2),("Harry", 5, 4), "Lew"))
