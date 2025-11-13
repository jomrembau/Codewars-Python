def read(tape, head, moves):
    final_list = []

    for x in moves:
        final_list.append(tape[head])
        if x == ">":
            head += 1
        if x == "<":
            head -= 1

    return "".join(final_list)

print(read('011010', 3, ">><<"))