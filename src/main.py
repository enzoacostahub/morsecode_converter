from file_io import read_message_from_file, write_message_to_file
from converter import text_to_morse, morse_to_text
from morse_tree import build_morse_tree

def main():
    morse_tree = build_morse_tree()

    while True:
        print("Escolha uma opção:")
        print("1. Texto para Morse (entrada do arquivo)")
        print("2. Texto para Morse (entrada manual)")
        print("3. Morse para Texto (entrada do arquivo)")
        print("4. Morse para Texto (entrada manual)")
        print("5. Sair")
        choice = input("Digite o número da opção: ")

        if choice == '1':
            normal_message = read_message_from_file('../data/normal_message.txt')
            morse_message = text_to_morse(normal_message)
            write_message_to_file('../data/morse_message.txt', morse_message)
            print(f"Mensagem em Morse: {morse_message}")

        elif choice == '2':
            normal_message = input("Digite a mensagem em texto normal: ")
            morse_message = text_to_morse(normal_message)
            write_message_to_file('../data/morse_message.txt', morse_message)
            print(f"Mensagem em Morse: {morse_message}")

        elif choice == '3':
            morse_message = read_message_from_file('../data/morse_message.txt')
            decoded_message = morse_to_text(morse_message, morse_tree)
            print(f"Mensagem decodificada: {decoded_message}")

        elif choice == '4':
            morse_message = input("Digite a mensagem em Morse: ")
            decoded_message = morse_to_text(morse_message, morse_tree)
            print(f"Mensagem decodificada: {decoded_message}")

        elif choice == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
