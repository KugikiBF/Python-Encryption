# Projeto: Cifras Clássicas em Python (César e Vigenère)

Este é um script Python de linha de comando (CLI) que implementa duas cifras criptográficas clássicas: a Cifra de César (ROT13) e a Cifra de Vigenère.

O objetivo principal é demonstrar a aplicação de lógica de programação, manipulação de strings e algoritmos fundamentais em Python.

---

## 📖 Sobre o Projeto

O script é dividido em duas funcionalidades principais:

1.  **`caesar(text, key=13)`**: Uma função que aplica a Cifra de César. Ela desloca cada letra do alfabeto por um número (chave), tratando corretamente caracteres não alfanuméricos e o "wrap-around" no final do alfabeto usando aritmética modular.
2.  **`vigenere(key='python')`**: Uma aplicação de console interativa que implementa a Cifra de Vigenère. Esta cifra utiliza uma palavra-chave para aplicar diferentes deslocamentos da Cifra de César a cada letra do texto, tornando-a mais robusta.

---

## 🛠️ Funcionalidades Principais

* **Cifra de César:** Implementação de uma cifra de substituição simples (padrão ROT13).
* **Cifra de Vigenère:** Implementação de uma cifra polialfabética mais complexa.
* **Interatividade (CLI):** O menu principal (`vigenere`) permite ao usuário:
    * Digitar o texto a ser processado.
    * Escolher entre **criptografar** ou **descriptografar** o texto.
    * Continuar executando o programa em loop.
* **Tratamento de Erros:** Validação simples de entrada do usuário (S/N).
* **Manipulação de Strings:** O código demonstra o uso de `.find()`, `.strip()`, `.isalnum()` e aritmética modular (`%`) para mapear caracteres entre o texto e o alfabeto da cifra.
* **Alfabeto Customizado:** A cifra de Vigenère utiliza um alfabeto que inclui letras maiúsculas, minúsculas e números.

---

## 💻 Tecnologias Utilizadas

* **Python 3**
* Módulo Padrão: **`time`** (para a função `sleep()`)

---

## 🚀 Como Executar

Este script é projetado para ser executado diretamente em um terminal.

1.  Clone este repositório:
    ```bash
    git clone [https://github.com/KugikiBF/nome-do-seu-repositorio.git](https://github.com/KugikiBF/nome-do-seu-repositorio.git)
    ```

2.  Navegue até o diretório do projeto:
    ```bash
    cd nome-do-seu-repositorio
    ```

3.  Salve o código como um arquivo (ex: `ciphers.py`).

4.  **Importante:** Para executar o menu interativo, adicione o seguinte "ponto de entrada" (entry point) ao final do seu arquivo `.py`:
    ```python
    if __name__ == "__main__":
        vigenere()
    ```

5.  Execute o script:
    ```bash
    python ciphers.py
    ```

6.  Siga as instruções apresentadas no terminal para criptografar ou descriptografar mensagens.

---

## 👨‍💻 Autor

**Bruno Felipe Mafra Lacerda**

* LinkedIn: [https://www.linkedin.com/in/bruno-felipe-7956bb351/](https://www.linkedin.com/in/bruno-felipe-7956bb351/)
* GitHub: [https://github.com/KugikiBF](https://github.com/KugikiBF)
