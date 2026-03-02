# 🎓 Fase1: Programação para Dados - PUCRS

Este repositório contém o projeto desenvolvido para a disciplina de **Programação para Dados** do curso de **Banco de Dados** na **PUCRS**. O objetivo é aplicar técnicas de modularização e análise de dados em Python utilizando uma base de dados real da Steam.

## 👤 Identificação
* **Instituição:** Pontifícia Universidade Católica do Rio Grande do Sul (PUCRS)
* **Curso:** Banco de Dados
* **Disciplina:** Programação para Dados
* **Aluno:** Jeferson Gomes da Silva

## 📂 Organização do Projeto
O projeto foi estruturado de forma modular para garantir a separação de responsabilidades:

```text
programacaoparadados1/
│
├── data/
│   └── steam_games.csv      # Base de dados bruta para análise
│
├── steam/                   # Pacote principal com a lógica do sistema
│   ├── __init__.py          # Inicialização do módulo Python
│   ├── game.py              # Definição das entidades (Classes)
│   ├── repository.py        # Camada de persistência e leitura do CSV
│   ├── analytics.py         # Funções de cálculos e métricas estatísticas
│   └── exceptions.py        # Tratamento de erros personalizados
│
├── README.md                # Documentação do projeto
├── main.py                  # Script principal (Ponto de entrada do sistema)
├── tests_sample.py          # Exemplos de testes unitários
└── conclusoes_analise.txt   # Relatório final com o parecer técnico

## 📝 Resumo da Análise (Insights)

A análise processou uma base de 72.934 jogos, revelando os seguintes pontos:

* Modelos de Negócio: Predominância de jogos pagos (82,61%) vs. gratuitos (17,39%).

* Sazonalidade: 2022 foi identificado como o ano recordista de lançamentos na base.

* Engajamento: Jogos gratuitos retêm usuários por cerca de 13,5% mais tempo (130 min)
do que jogos pagos (114 min), evidenciando a força dos modelos "Live Service".

## 🚀 Como executar
1. Clone o repositório:
   ```bash
!python main.py
