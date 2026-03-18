def chromosome_check(chromosome):
    if "Y" in chromosome:
        return "Congratulations! You're going to have a son."
    else:
        return "Congratulations! You're going to have a daughter."

print(chromosome_check("XX"))

