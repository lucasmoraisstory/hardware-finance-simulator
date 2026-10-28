# Simulador de Financiamento de Equipamentos de TI

def simular_financiamento():
    print("-" * 50)
    print("💻 SIMULADOR DE FINANCIAMENTO DE HARDWARE 💻")
    print("-" * 50)
    
    try:
        valor_total = float(input("Digite o valor total do computador/notebook (R$): "))
        parcelas = int(input("Digite a quantidade de parcelas desejada (Ex: 12): "))
        
        # Define taxa de juros simples com base no número de parcelas
        if parcelas <= 3:
            taxa_juros = 0.0  # Sem juros para parcelas curtas
        else:
            taxa_juros = 0.025  # 2.5% de juros ao mês para parcelas longas
            
        valor_com_juros = valor_total * (1 + (taxa_juros * parcelas))
        valor_parcela = valor_com_juros / parcelas
        
        # Resultado
        print("\n" + "📊 RESULTADO DA SIMULAÇÃO ".center(40, "="))
        print(f"Valor original do equipamento: R$ {valor_total:.2f}")
        print(f"Plano selecionado: {parcelas}x")
        print(f"Taxa de juros aplicada: {taxa_juros * 100:.1f}% ao mês")
        print(f"Valor de cada parcela: R$ {valor_parcela:.2f}")
        print(f"Valor total final a ser pago: R$ {valor_com_juros:.2f}")
        print("=" * 40)
        
    except ValueError:
        print("\n❌ Erro: Por favor, insira valores numéricos válidos.")

if __name__ == "__main__":
    simular_financiamento()
