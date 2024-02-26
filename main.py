import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear_screen()
    idade = input("Digite sua idade: ")
    
    if idade.isdigit():
        if int(idade) >= 18:
            print("Maior de Idade")
            break
        else:
            print("Menor de idade")
            break
    else:
        print("Você digitou um valor irregular.")
        verificar = input("Deseja continuar no sistema (S/N)? ").upper()
        if verificar == "N":
            break
