# flash_card_project
App de Flashcards interativa desenvolvida em Python (Tkinter e Pandas). Utiliza o método de repetição espaçada para ajudar a aprender novas línguas, guardando automaticamente o teu progresso num relatório CSV.

# Flashcard Project 

O **Flashcard Project** é uma aplicação desktop interativa desenvolvida em **Python** para ajudar na memorização de vocabulário e na aprendizagem de novas línguas. Utilizando cartões virtuais (Flashcards), o programa desafia o utilizador a testar o seu conhecimento de forma visual e intuitiva.

##  Funcionalidades

*   **Interface Gráfica Fluida:** Criada com o módulo `tkinter`, simulando cartões reais que mudam de cor e de face após um curto período de tempo.
*   **Viragem Automática (Flip Card):** O cartão exibe uma palavra num idioma (ex: Francês) e, após 3 segundos, vira automaticamente para revelar a tradução (ex: Inglês).
*   **Gestão de Progresso Dinâmica:** O utilizador pode clicar no botão de "Certo" (conhece a palavra) ou "Errado" (precisa de estudar mais).
*   **Base de Dados Inteligente:** As palavras que o utilizador já sabe são removidas da lista de estudo e salvas num ficheiro CSV (`words_to_learn.csv`), garantindo que apenas os termos desconhecidos voltem a aparecer nas próximas sessões.

## Tecnologias Utilizadas

*   **[Python](https://python.org):** Linguagem de programação principal.
*   **Módulo Tkinter:** Para o desenvolvimento de toda a interface gráfica (janelas, botões e canvas).
*   **Biblioteca [Pandas](https://pydata.org):** Para a leitura, manipulação e atualização da base de dados de palavras em formato CSV.

## Estrutura do Repositório

```text
├── main.py                 # Código principal com a lógica da aplicação e interface
├── data/
│   ├── french_words.csv    # Base de dados original (ex: Francês/Inglês)
│   └── words_to_learn.csv  # Ficheiro gerado automaticamente com as palavras em falta
├── images/
│   ├── card_front.png      # Imagem de fundo para a frente do cartão
│   ├── card_back.png       # Imagem de fundo para o verso do cartão
│   ├── right.png           # Ícone do botão "Certo"
│   └── wrong.png           # Ícone do botão "Errado"
└── README.md               # Documentação do projeto
```

## Como Executar o Projeto

### Pré-requisitos
Certifica-te de que tens o Python instalado na tua máquina. Vais precisar também de instalar a biblioteca `pandas`:

```bash
pip install pandas
```

### Clonar o Repositório
```bash
git clone git@github.com:porivaldovidro-afk/flash_card_project.git
cd flashcard_project
```

### Executar a Aplicação
```bash
python main.py
```

## Como Utilizar

1. Assim que a aplicação iniciar, verás a frente de um cartão com uma palavra aleatória no idioma de estudo.
2. Aguarda 3 segundos para que o cartão mude de cor e revele a tradução correspondente.
3. Se já sabias o significado da palavra, clica no botão verde (✓). Ela não voltará a aparecer.
4. Se não sabias, clica no botão vermelho (✗). A palavra continuará na tua lista de estudo para as próximas sessões.

## Licença

Este projeto está sob a licença MIT. Consulta o ficheiro `LICENSE` para obter mais detalhes.
