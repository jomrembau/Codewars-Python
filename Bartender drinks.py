def get_drink_by_profession(param):
    param = param.lower()

    match param:
        case "jabroni":
            return "Patron Tequila"
        case "school counselor":
            return "Anything with Alcohol"
        case "programmer":
            return "Hipster Craft Beer"
        case "bike gang member":
            return 	"Moonshine"
        case "politician":
            return 	"Your tax dollars"
        case "rapper":
            return "Cristal"
        case _:
            return "Beer"

print(get_drink_by_profession("School Counselor"))