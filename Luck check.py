def luck_check(st):
    st = [int(x) for x in st]
    half = int((len(st) / 2))
    if len(st) % 2 == 1:
        st.remove(st[half])
    if sum(st[half:]) == sum(st[:half]):
        return True
    else:
        return False


print(luck_check("62953"))