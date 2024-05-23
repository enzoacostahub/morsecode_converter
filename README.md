
# Morse Code Converter

Este projeto é uma aplicação Python que converte mensagens entre texto normal e código Morse utilizando uma árvore binária para representar o alfabeto Morse. 

## Estrutura do Projeto

```
morse_code_converter/
├── data/
│   ├── normal_message.txt
│   └── morse_message.txt
├── src/
│   ├── tree_node.py
│   ├── morse_tree.py
│   ├── converter.py
│   ├── file_io.py
│   └── main.py
├── README.md
└── requirements.txt
```

## Configuração do Ambiente

1. **Clone o repositório:**

```sh
   git clone git@github.com:enzoacostahub/morsecode_converter.git

   cd morse_code_converter
```


## Executando o Programa

Para executar o programa, navegue até o diretório \`src\` e execute o script \`main.py\`:

```sh
cd src

python main.py
```

## Uso

Ao executar o programa, você verá um menu com as seguintes opções:

```
Escolha uma opção:
1. Texto para Morse (entrada do arquivo)
2. Texto para Morse (entrada manual)
3. Morse para Texto (entrada do arquivo)
4. Morse para Texto (entrada manual)
5. Sair
```

### Opção 1: Texto para Morse (entrada do arquivo)

- **Descrição:** Converte uma mensagem em texto normal lida do arquivo \`data/normal_message.txt\` para código Morse e salva a saída em \`data/morse_message.txt\`.
- **Exemplo de Entrada:** 
  - \`data/normal_message.txt\`: 
```
    EP1 ESTRUTURA DE DADOS E ANALISE DE ALGORITMOS /IPT
```
- **Exemplo de Saída:** 
  - \`data/morse_message.txt\`:
```
    . .--. .---- / . ... - .-. ..- - ..- .-. .- / -.. . / -.. .- -.. --- ... / . / .- -. .- .-.. .. ... . / -.. . / .- .-.. --. --- .-. .. - -- --- ... / / .. .--. -
```

### Opção 2: Texto para Morse (entrada manual)

- **Descrição:** Solicita ao usuário que insira uma mensagem em texto normal, converte para código Morse e salva a saída em \`data/morse_message.txt\`.
- **Exemplo de Entrada:**
```
  DIGITE A MENSAGEM EM TEXTO NORMAL: EXEMPLO DE TESTE
```
- **Exemplo de Saída:**
  - \`data/morse_message.txt\`:
```
    . -..- . -- .--. .-.. --- / -.. . / - . ... - . 
```
  - **Saída no console:**
```
    Mensagem em Morse: . -..- . -- .--. .-.. --- / -.. . / - . ... - . 
```

### Opção 3: Morse para Texto (entrada do arquivo)

- **Descrição:** Converte uma mensagem em código Morse lida do arquivo \`data/morse_message.txt\` para texto normal e exibe a mensagem decodificada.
- **Exemplo de Entrada:** 
  - \`data/morse_message.txt\`:
```
    .. ... ... --- / . .... / ..- -- / . -..- . -- .--. .-.. ---
```
- **Exemplo de Saída:**
  - **Saída no console:**
```
    Mensagem decodificada: ISSO EH UM EXEMPLO
```

### Opção 4: Morse para Texto (entrada manual)

- **Descrição:** Solicita ao usuário que insira uma mensagem em código Morse, converte para texto normal e exibe a mensagem decodificada.
- **Exemplo de Entrada:**
```
  DIGITE A MENSAGEM EM MORSE: . -..- . -- .--. .-.. --- / -.. . / - . ... - .
```
- **Exemplo de Saída:**
  - **Saída no console:**
```
    Mensagem decodificada: EXEMPLO DE TESTE
```

### Opção 5: Sair

- **Descrição:** Sai do programa.

---
