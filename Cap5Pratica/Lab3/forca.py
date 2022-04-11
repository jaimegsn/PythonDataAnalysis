import os
import random


class Boneco():
    def __init__(self):
        self.vida = 0
        self.estados = [
            "     |\n     |\n     |\n     |\n ________",
            " O   |\n     |\n     |\n     |\n ________",
            " O   |\n |   |\n     |\n     |\n ________",
            " O   |\n/|   |\n     |\n     |\n ________",
            " O   |\n/|\  |\n     |\n     |\n ________",
            " O   |\n/|\  |\n/    |\n     |\n ________",
            " O   |\n/|\  |\n/ \  |\n     |\n ________"
        ]
        self.bonecoDesenho = self.estados[self.vida]

    def __str__(self):
        print(" +---+")
        return(self.bonecoDesenho)

    def __len__(self):
        return self.vida

    def errou(self):
        self.vida += 1
        self.bonecoDesenho = self.estados[self.vida]


with open('Cap5Pratica/Lab3/data.txt', 'r') as data:
    palavras = data.read()
listaPalavras = palavras.split(',')

b1 = Boneco()
palavra = random.choice(listaPalavras)
letrasDigitadasCertas = ""
todasLetrasDigitadas = ""


def letrasDescobertas(ld, pl):
    Word = list(pl)
    Mask = ""
    for x in Word:
        if x in ld:
            Mask += x
            continue
        Mask += "-"
    return Mask


while True:
    print("\n\n__________________________________\n")
    if(b1.vida == 6):
        print(b1)
        print("VOCÊ PERDEU !!")
        break
    else:
        print(b1)
        print("\n\nPalavra: %s\n\n" %
              (letrasDescobertas(letrasDigitadasCertas, palavra)))

        print("\nLetras Digitadas: %s\n" % (todasLetrasDigitadas))

        if(letrasDescobertas(letrasDigitadasCertas, palavra) == palavra):
            print("VOCÊ GANHOU !!")
            break
        else:
            letra = input("Digite uma Letra: ")
            todasLetrasDigitadas += letra

            if((letra in palavra) & (letra not in letrasDigitadasCertas)):
                letrasDigitadasCertas += letra
                continue
            else:
                b1.errou()
                continue
