# tee ratkaisu tänne
def luvuista_suurin(numero1,numero2,numero3):
    if numero1 >= numero2 and numero1 >= numero3:
        return numero1
    elif numero2 >= numero1 and numero2 >= numero3:
        return numero2
    elif numero3 >= numero1 and numero3 >= numero2:
        return numero3
    else:
        return 0