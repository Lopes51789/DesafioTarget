import json
MAX_INT_VALUE = 999999999999
MIN_INT_VALUE = -1

"""
Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
"""

if __name__ == '__main__':
    f = open('dados.json', 'r')
    dados = json.load(f)#leio os dados do json

    faturas = {}
    for dado in dados:
        faturas[dado['dia']] = dado['valor']

    f.close()

    max_dia = -1
    max_valor = MIN_INT_VALUE
    min_dia = -1
    min_valor = MAX_INT_VALUE
    
    mean_acm = 0
    mean_dias = 0

    for dia in faturas:
        if faturas[dia] != 0:
            mean_acm += faturas[dia]
            mean_dias += 1

        if faturas[dia] > max_valor:
            max_dia = dia
            max_valor = faturas[dia]
        if faturas[dia] < min_valor:
            min_dia = dia
            min_valor = faturas[dia]
        #print(f"{dia}: {faturas[dia]}")

    mean_acm = mean_acm / mean_dias
    dias_validos = 0
    
    for dia in faturas:
        if faturas[dia] > mean_acm:
            dias_validos += 1


    
    print(f"O maior valor foi de R${max_valor:.2f} no dia {max_dia}"
          f"\nO menor valor foi de R${min_valor:.2f} no dia {min_dia}"
          f"\nO valor medio foi de R${mean_acm:.2f}"
          f"\nO numero de dias acima do valor medio foi de {dias_validos}")