alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v",
            "w", "x", "y", "z"]

msg = input("Digite a mensagem que deseja criptografar: ")
key = int(input("Insira a chave(número): "))
cifrada = ""
msg_list = []

for letter in msg:
    newLetter = alfabeto[(alfabeto.index(letter) + key) % len(alfabeto)]
    msg_list.append(letter)
    cifrada = cifrada + newLetter
print(f"A sua palavra quando criptografada vai ser: \033[31m{cifrada}")
