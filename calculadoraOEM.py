
pi = 3.14159265
c = 3*(10**8)

# (Não esqueça de indicar as unidades)

# Entra com o valor de f, retorna: λ, k, ω
def casoF(f):
  lam = c/f
  omega = f * (2*pi)
  k = omega/c

  print(f"\033[34m \nlam: {lam} \nomega: {omega} \nk: {k}\n \033[m")
  

#Entre com o valor de λ, retorna: f, k, ω
def casoLam(lam):
  f = c/lam
  k = (2*pi)/lam
  omega = (2*pi)*f

  print(f"\033[34m \nf: {f}\nk: {k}\nomega: {omega}\n \033[m")

  
# Entre com o valor de k, retorna: f, λ, ω
def casoK(k):
  lam = (2*pi) / k
  f = c / lam
  omega = (2*pi) / f

  print(f"\033[34m \nlam: {lam}\nf: {f}\nomega: {omega}\n \033[m")
  

# Entra com o valor de ω, retorna: f, λ, k
def casoOmega(omega):
  f = omega / (2*pi)
  lam = c / f
  k = (2*pi) / lam

  print(f"\033[34m \nf: {f}\nlambda: {lam}\nk: {k}\n \033[m")
  

# Entra com o valor de do campo Bm, retorna Em.
def bmToEm(bm):
  print(f"\033[34m {c * bm} \033[34m")
  

# Usuário entra com Em, retorna Bm.
def emToBm(em):
  print(f"\033[34m {em / c} \033[34m")

  
# FAZER CONVERSORES
#  7 - conversoes e tal
#  micro -6 to m
#  nm -9 to m
#  segundos 
#  hz 
#  grau - rad
  
def conversores():
  print("vazio")

  
# MENU
  
def menu():
  while True:
    print("---------- MENU -----------")
    print("1 - Insira o valor da frequencia (f)")
    print("2 - Insira o comprimento de onda (lambda)")
    print("3 - Insira o número de onda (k)")
    print("4 - Insira o valor da frequencia angular (omega)")
    print("5 - Insira o valor de do campo magnético (Bm)")
    print("6 - Insira o valor do campo elétrico (Em)")
    print("7 - Conversores")
    #ZERO PARA FINALIZAR O PROGRAMA
    # NÃO IMPLEMENTADO

    opc = int(input("\nEscolha uma das opções: "))

    if opc == 1:
      num = float(input("Insira o valor de f: "))
      casoF(num)
    elif opc == 2:
      num = float(input("Insira o valor de lambda: "))
      casoLam(num)
    elif opc == 3:
      num = float(input("Insira o valor de k: "))
      casoK(num)
    elif opc == 4:
      num = float(input("Insira o valor de omega: "))
      casoOmega(num)
    elif opc == 5:
      num = float(input("Insira o valor de do campo Bm: "))
      bmToEm(num)
    elif opc == 6:
      num = float(input("Insira o valor do campo Em: "))
      emToBm(num)
    elif opc == 7:
      conversores()
    elif (opc >= 8 or opc <= -1):
      print("Opção inválida\n")
    
menu()