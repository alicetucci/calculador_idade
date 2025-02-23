from datetime import datetime

data_nascimento_usuario = input("Informe sua data de nascimento (dd/mm/aaaa): ")
data_nascimento_usuario = datetime.strptime(data_nascimento_usuario, "%d/%m/%Y")

data_atual = datetime.now()

idade = data_atual.year - data_nascimento_usuario.year

mes_atual = data_atual.month 
dia_atual = data_atual.day

mes_nascimento = data_nascimento_usuario.month 
dia_nascimento = data_nascimento_usuario.day

# se o mês e dia atual for menor que o mês e dia de nascimento, ainda não fez aniversário
# por exemplo, se nasceu em 05/07/2000 e hoje é 04/07/2023, ainda não fez aniversário
if mes_nascimento > mes_atual:
    idade -= 1
elif mes_nascimento == mes_atual and dia_nascimento > dia_atual:
    idade -= 1

print(f"Sua idade é {idade} anos.") 