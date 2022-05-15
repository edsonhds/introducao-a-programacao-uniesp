# 1.Um dicionário Python pode ser usado para modelar um dicionário de verdade. 
# No entanto, para evitar confusão, chame este dicionário de glossário.

# A) Pense em cinco palavras relacionada à programação que você conheceu nesta disciplina. 
# Use estas palavras como chaves em seu glossário e armazene seus significados como valores.

# B) Mostre cada palavra e seu significado em uma saída, formate a saída de uma forma bem elegante. 
# Por exemplo: você pode exibir a palavra seguida de dois-pontos e depois o seu significado, 
# ou apresentar a palavra em uma linha e então exibir seu significado indentado em uma segunda linha. 
# Utilize o caractere de quebra de linha (\n) para inserir uma linha em branco entre cada palavra-significado em sua saída.

# C) Sugestões de termos: Algoritmos, Python, Webscraping, Lógica de Programação, Google Colab, Visual Studio Code.

glossario = {
    'Nº 1 \n             - Algoritmo:': 'ém matemática e ciência da computação é uma sequência finita de ações executáveis que visam obter uma solução para um determinado tipo de problema',
    'Nº 2 \n             - Python:': 'é uma linguagem de programação de alto nível,interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte',
    'Nº 3 \n             - Web scraping ou raspagem web:': 'é uma ferramenta muito utilizada em estratégias de transformação digital e também para automatizar processos de coleta e consulta de dados e informações públicas, para diversos fins',
    'Nº 4 \n             - Google Colab, ou Google Collaboratory:': 'é um serviço de armazenamento em nuvem de notebooks voltados à criação e execução de códigos em Python diretamente em um navegador, sem a necessidade de nenhum tipo de instalação de software em uma máquina',
    'Nº 5 \n             - Visual Studio Code (VS Code)': 'é um editor de código de código aberto desenvolvido pela Microsoft. A saber, ele está disponível para Windows, Mac e Linux. É criado com Electron, ferramenta criada pelo GitHub que permite a criação de softwares Desktop com HTML, CSS e JavaScript',
    }

for i in glossario:
    print(f'\n\033[1mGlossario {i}\033[0m {glossario[i]}.')
