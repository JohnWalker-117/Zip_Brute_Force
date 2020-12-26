import os
from zipfile import ZipFile
import string
import multiprocessing as mp
import gc
import itertools

threadList = ["TH1", "TH2", "TH3", "TH4"]
threads = []


def generate(ch, maxChar, limite):

    while True:
        for s in itertools.product(ch, repeat=maxChar):
            i = "".join(s)
            yield i
        print(f"Teste {maxChar} caracter terminado")
        maxChar += 1
        print(f"Teste {maxChar} caracter começando")
        if maxChar > limite:
            os.sys.exit()


def crack(file, ch, maxChar, limite):

    with ZipFile(file) as zf:
        for i in generate(ch, maxChar, limite):
            try:
                zf.extractall(pwd=bytes(i, "utf-8"))
                print("Finalizado")

            except:
                pass

            else:
                print(f"A senha é: {i}")
                os.sys.exit()


def setup():
    print("Definindo informações.")

    file = input("Caminho para o arquivo (Ex: C:\\Users\\Desktop\\Arquivo.zip): ")

    maxChar = int(input("Número de caracteres mínimo: "))

    limite = int(input("Número de caracteres máximo: "))

    tipo = input(
        "Tipo de combinação: \n"
        " Letras (1) \n"
        " Números (2) \n"
        " Letras e Números (3) \n"
        " Letras, Números e Símbolos (4) \n"
    )

    if tipo == "1":
        ch = string.ascii_letters + "ç" + "Ç"

    elif tipo == "2":
        ch = string.digits

    elif tipo == "3":
        ch = string.ascii_letters + string.digits + "ç" + "Ç"

    elif tipo == "4":
        ch = string.ascii_letters + string.digits + string.punctuation + "ç" + "Ç"

    return ch, maxChar, limite, file


def main():
    print("Iniciando... \n")

    ch, maxChar, limite, file = setup()

    while True:

        for tName in threadList:
            thread = mp.Process(target=crack(file, ch, maxChar, limite))
            thread.start()
            threads.append(thread)

        for t in threads:
            t.join()

        gc.collect()


if __name__ == "__main__":
    main()
