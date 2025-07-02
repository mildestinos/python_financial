📈 Sistema de Análise de Vendas com Python e Excel

Um projeto de terminal interativo em Python que permite responder automaticamente 10 perguntas de negócio com base em um arquivo Excel de dados de vendas.

Autor: Eric VieiraPropósito: Didático / Corporativo / Automatização de Análises

🌟 Objetivo

Criar uma aplicação simples em Python que:

Leia dados de vendas de um arquivo Excel

Apresente um menu interativo com 10 perguntas estratégicas

Calcule automaticamente as respostas, com números e percentuais

Limpe o terminal a cada execução

Aguarde a interação do usuário para continuar

📁 Estrutura do Projeto

📆 Dash/
┣ 📄 Financial Sample.xlsx
┣ 📄 main.py
┗ 📄 README.md

🧰 Requisitos

Python 3 instalado

VS Code (ou qualquer editor)

Pacotes:

pip install pandas openpyxl

📊 Fonte de Dados

Arquivo: Financial Sample.xlsxConteúdo: dados de vendas por produto, país, cliente e tempo.

🧠 Funcionalidades

Ao executar o script main.py, o sistema:

Lê e prepara os dados do Excel

Mostra um menu com as 10 perguntas abaixo

Calcula e exibe a resposta detalhada (números e %)

Aguarda o usuário pressionar ENTER

Limpa a tela e reinicia o ciclo

📋 Perguntas Respondidas

Qual o total de vendas acumulado no último ano?

Quais os 5 produtos mais vendidos no último ano?

Qual o crescimento percentual das vendas comparado ao ano anterior?

Qual o cliente com maior volume de compras no último ano?

Qual o país com maior faturamento no último ano?

Qual a média de vendas por mês no último ano?

Qual segmento de mercado teve o maior crescimento no último ano?

Quais produtos apresentaram queda de vendas em relação ao ano anterior?

Qual o mês com maior volume de vendas no último ano?

Quantas unidades foram vendidas no total por produto no último ano?

▶️ Como Executar

python main.py

🧠 Aprendizados

Durante o desenvolvimento você aprenderá:

Leitura e tratamento de dados com pandas

Menu interativo via terminal

Agrupamentos e filtros com groupby

Cálculo de percentuais e totais

Limpeza de terminal (os.system)

Boas práticas com funções reutilizáveis

✨ Possíveis Extensões

Exportar as respostas para .txt ou .xlsx

Adicionar gráficos com matplotlib

Criar uma interface gráfica com Tkinter ou PySimpleGUI

Integração com email para envio automático de relatórios

👤 Autor

Eric Vieira

GitHub: github.com/ericvieira

Linkedin: linkedin.com/in/ericvieira

📄 Licença

Uso livre para fins educacionais e corporativos.