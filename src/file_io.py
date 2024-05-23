def read_message_from_file(filename):
    with open(filename, 'r') as file:
        return file.read().strip()

def write_message_to_file(filename, message):
    with open(filename, 'w') as file:
        file.write(message)
