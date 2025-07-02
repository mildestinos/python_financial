import pandas as pd
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Carrega e prepara os dados
df = pd.read_excel("Financial Sample.xlsx")
df.columns = df.columns.str.strip()
df['Date'] = pd.to_datetime(df['Date'])

# Funções analíticas
def total_vendas_ultimo_ano():
    ano = df['Year'].max()
    total = df[df['Year'] == ano]['Sales'].sum()
    return f"Total de vendas no último ano ({ano}): ${total:,.2f}"

def top_5_produtos_mais_vendidos():
    ano = df['Year'].max()
    top = df[df['Year'] == ano].groupby("Product")["Units Sold"].sum().sort_values(ascending=False).head(5)
    return f"Top 5 produtos mais vendidos no ano {ano} (quantidade de unidades):\n{top.to_string()}"

def crescimento_percentual_vendas():
    anos = sorted(df['Year'].unique())
    vendas = df.groupby("Year")["Sales"].sum()
    anterior = vendas.iloc[-2]
    atual = vendas.iloc[-1]
    crescimento = ((atual - anterior) / anterior) * 100
    return (f"Vendas {anos[-2]}: ${anterior:,.2f}\n"
            f"Vendas {anos[-1]}: ${atual:,.2f}\n"
            f"Crescimento: {crescimento:.2f}%")

def cliente_maior_venda():
    ano = df['Year'].max()
    grupo = df[df['Year'] == ano].groupby("Country")["Sales"].sum()
    pais = grupo.idxmax()
    valor = grupo.max()
    return f"Cliente com maior volume de compras no ano {ano}: {pais} - ${valor:,.2f}"

def pais_maior_faturamento():
    ano = df['Year'].max()
    pais = df[df['Year'] == ano].groupby("Country")["Sales"].sum().sort_values(ascending=False).head(1)
    return f"País com maior faturamento em {ano}:\n{pais.to_string()}"

def media_vendas_por_mes():
    ano = df['Year'].max()
    mensal = df[df['Year'] == ano].groupby("Month Number")["Sales"].sum()
    media = mensal.mean()
    return f"Média mensal de vendas no ano {ano}: ${media:,.2f}"

def segmento_maior_crescimento():
    anos = sorted(df['Year'].unique())
    vendas = df.groupby(["Segment", "Year"])["Sales"].sum().unstack()
    vendas["Crescimento %"] = ((vendas[anos[-1]] - vendas[anos[-2]]) / vendas[anos[-2]]) * 100
    vendas["Variação $"] = vendas[anos[-1]] - vendas[anos[-2]]
    top = vendas["Crescimento %"].idxmax()
    percentual = vendas.loc[top, "Crescimento %"]
    valor = vendas.loc[top, "Variação $"]
    return (f"Segmento com maior crescimento de {anos[-2]} para {anos[-1]}:\n"
            f"{top}: ${valor:,.2f} | {percentual:.2f}%")

def produtos_com_queda_vendas():
    anos = sorted(df['Year'].unique())
    vendas = df.groupby(["Product", "Year"])["Sales"].sum().unstack()
    vendas['Crescimento %'] = ((vendas[anos[-1]] - vendas[anos[-2]]) / vendas[anos[-2]]) * 100
    queda = vendas[vendas['Crescimento %'] < 0]
    return (f"Produtos com queda de vendas ({anos[-2]} → {anos[-1]}):\n"
            f"{queda[[anos[-2], anos[-1], 'Crescimento %']].round(2).to_string()}")

def mes_maior_volume_vendas():
    ano = df['Year'].max()
    total_mes = df[df['Year'] == ano].groupby("Month Name")["Sales"].sum()
    mes = total_mes.idxmax()
    valor = total_mes.max()
    return f"Mês com maior volume de vendas em {ano}: {mes} - ${valor:,.2f}"

def unidades_vendidas_por_produto():
    ano = df['Year'].max()
    unidades = df[df['Year'] == ano].groupby("Product")["Units Sold"].sum().sort_values(ascending=False)
    return f"Total de unidades vendidas por produto em {ano}:\n{unidades.to_string()}"

# Mapeamento das funções
funcoes = {
    "1": total_vendas_ultimo_ano,
    "2": top_5_produtos_mais_vendidos,
    "3": crescimento_percentual_vendas,
    "4": cliente_maior_venda,
    "5": pais_maior_faturamento,
    "6": media_vendas_por_mes,
    "7": segmento_maior_crescimento,
    "8": produtos_com_queda_vendas,
    "9": mes_maior_volume_vendas,
    "10": unidades_vendidas_por_produto,
}

# Menu
def exibir_menu():
    print("\n=== MENU DE PERGUNTAS ===")
    print("1. Qual o total de vendas acumulado no último ano?")
    print("2. Quais os 5 produtos mais vendidos no último ano?")
    print("3. Qual o crescimento percentual das vendas comparado ao ano anterior?")
    print("4. Qual o cliente com maior volume de compras no último ano?")
    print("5. Qual o país com maior faturamento no último ano?")
    print("6. Qual a média de vendas por mês no último ano?")
    print("7. Qual segmento de mercado teve o maior crescimento no último ano?")
    print("8. Quais produtos apresentaram queda de vendas em relação ao ano anterior?")
    print("9. Qual o mês com maior volume de vendas no último ano?")
    print("10. Quantas unidades foram vendidas no total por produto no último ano?")
    print("0. Sair")

# Execução
def main():
    while True:
        limpar_tela()
        exibir_menu()
        escolha = input("Digite o número da opção desejada: ")

        if escolha == "0":
            print("Saindo...")
            break
        elif escolha in funcoes:
            print("\nResposta:")
            print(funcoes[escolha]())
            input("\nPressione Enter para continuar...")
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
