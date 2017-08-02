from Carro import Carro
from Hibrido import Hibrido

def main():

    carro1 = Carro("Preto", "Ford Fiesta", 2003)
    hibrido1 = Hibrido("Cinza", "Fiat Uno", 2007)

    print(carro1)
    print(hibrido1)

    carro1.Acelerar()
    carro1.Freiar()

    hibrido1.Acelerar()
    hibrido1.Freiar()
    hibrido1.CarregarBateria()

if (__name__ == "__main__"):
    main()
