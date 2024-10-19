def beolvas():
    oldal = float(input("Add meg a háromszög oldalát!"))
    return oldal


def hat():
    a = beolvas()
    b = beolvas()
    c = beolvas()

    if (a > 0) and (b > 0) and (c > 0):
        if a < (c+b) and c < (a+b) and b < (c+a):
            print("A háromszög megszerkezthető.")
        else:
            print("A háromszög nem megszerkezthető.")
    else:
        print("HIBA: Nem megfelelő bemenő adatok")
