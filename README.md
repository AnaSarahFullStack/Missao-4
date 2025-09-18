# Calculadora e Sistema de Gestão de Pessoas em Python 🐍

Este repositório contém os códigos desenvolvidos na **Missão 4 da faculdade**, utilizando Python. O objetivo foi praticar **programação orientada a objetos (POO)**, criando uma **calculadora** e um **sistema de cadastro de pessoas físicas e jurídicas**.

---

## 🛠️ Tecnologias

- Python 3.x

---

## 📁 Estrutura de arquivos

### Calculadora
- `Calculadora.py` – Classe que implementa a calculadora com operações básicas (+, -, *, /), validação e tratamento de erros.
- `main-calculadora.py` – Arquivo principal interativo para testar a calculadora.

### Sistema de Pessoas
- `Pessoa.py` – Classe base para representar uma pessoa.
- `PessoaFisica.py` – Classe derivada para representar pessoa física, com CPF e RG.
- `PessoaJuridica.py` – Classe derivada para representar pessoa jurídica, com CNPJ e data de abertura da empresa.
- `main_pessoa.py` – Arquivo principal para testar a criação e exibição de pessoas físicas e jurídicas.

---

## ⚡ Objetivos da Missão

- Praticar **POO**, incluindo:
  - Herança (`PessoaFisica` e `PessoaJuridica` derivadas de `Pessoa`)  
  - Encapsulamento (uso de getters e setters)
  - Modularização (cada classe em arquivo separado)
- Criar programas que simulam:
  - Uma **calculadora interativa** com validação de operações
  - Um **sistema de cadastro de pessoas**, tanto físicas quanto jurídicas
- Consolidar conceitos de **boas práticas de programação** em Python.

---

## 🚀 Como executar

1. **Calculadora**
```bash
python main-calculadora.py
