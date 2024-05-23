from morse_tree import build_morse_tree

morse_tree = build_morse_tree()

morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/', '/': ' '
}

def text_to_morse(message):
    return ' '.join(morse_code[char.upper()] for char in message)

def morse_to_text(morse_message, morse_tree):
    words = morse_message.split(' / ')
    decoded_message = []

    for word in words:
        letters = word.split()
        decoded_word = []
        for letter in letters:
            current = morse_tree
            for symbol in letter:
                if symbol == '.':
                    current = current.left
                elif symbol == '-':
                    current = current.right
                if current is None:
                    decoded_word.append('?')  
                    break
            if current is not None and current.value is not None:
                decoded_word.append(current.value)
            elif current is None or current.value is None:
                decoded_word.append('?')  
        decoded_message.append(''.join(decoded_word))

    return ' '.join(decoded_message)


# Exemplo de uso
if __name__ == "__main__":
    text_message = "ISSO EH UM EXEMPLO"
    morse_message = text_to_morse(text_message)
    print(f"Mensagem em Morse: {morse_message}")

    decoded_message = morse_to_text(morse_message, morse_tree)
    print(f"Mensagem decodificada: {decoded_message}")
