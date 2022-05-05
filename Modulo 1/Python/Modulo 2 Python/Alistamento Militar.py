from datetime import date
atual = date.today().year
nascimento = int(input("Ano de nascimento? "))
idade = atual - nascimento
print("Quem nasceu em {} tem {} ano em {}.".format(nascimento, idade, atual))
if idade == 18:
    print("Você tem que se alistar IMEDIATAMENTE: ")
elif idade < 18:
    saldo = idade - 18
    print("Voce ainda não tem 18 anos. Ainda falta {} anos para o alistamento:".format(saldo))
    ano = saldo + idade
    print("Seu alistamento será em {} anos".format(ano))
elif idade >18:
    saldo = idade - 18
    print("Você ja deveria ter se alistado a {} anos".format(saldo))
    ano = atual - saldo
    print("Seu alistamento foi em {}".format(ano))