from tree_node import TreeNode

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

def build_morse_tree():
    root = TreeNode()
    for char, morse in morse_code.items():
        current = root
        for symbol in morse:
            if symbol == '.':
                if current.left is None:
                    current.left = TreeNode()
                current = current.left
            elif symbol == '-':
                if current.right is None:
                    current.right = TreeNode()
                current = current.right
        current.value = char
    return root

def print_pre_order(node, path=''):
    if node is not None:
        if node.value is not None:
            print(f"{path} {node.value}")
        print_pre_order(node.left, path + '.')
        print_pre_order(node.right, path + '-')

# Exemplo de uso
if __name__ == "__main__":
    morse_tree = build_morse_tree()
    print_pre_order(morse_tree)
