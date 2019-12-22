s = [i for i in range(2, 30)]


def l_search(mass, arg):
    for i in range(len(mass)):
        if mass[i] == arg:
            return i

