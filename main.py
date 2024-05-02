from random import choice
import string

def gerar (tamanho, inc_letras=True, inc_numeros=True, inc_esp=True):
    caracteres = ''

    if inc_esp:
        caracteres += string.punctuation

    if inc_letras:
        caracteres += string.ascii_letters

    if inc_numeros:
        caracteres += string.digits

    if not caracteres:
        raise ValueError("É preciso incluir algum tipo de caractere na senha")

    senha = ''
    for i in range(tamanho):
        senha += choice(caracteres)
    return senha

def salvar (senha):

    salvar = input("Deseja salvar esta senha? [s/N]: ").strip().upper()

    if salvar == 'S':

        with open("senhas.txt", "a") as f:
            f.write(senha + "\n")
        print("Senha salva com sucesso no arquivo 'senhas.txt'.")
    else:
        print("Senha não foi salva.")

def main():

    tamanho = int(input("Quantos caracteres a senha deverá ter? "))

    inc_letras = input("A senha deverá ter letras? [S/n]").strip().lower() == 's'
    inc_numeros = input("A senha deverá ter numeros? [S/n]").strip().lower() == 's'
    inc_esp = input("A senha deverá ter caracteres epeciais e de pontuacao? [S/n]").strip().lower() == 's'

    try:
        senha = gerar(tamanho, inc_letras, inc_numeros, inc_esp)
        print("A seguinte senha foi gerada: ", senha)
        salvar(senha)
    except ValueError as e:
        print("Deu merda:", e)

if __name__ == "__main__":
    main()
