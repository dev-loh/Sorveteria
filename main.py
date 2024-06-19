print('Bem-vindo a Sorveteria da Lorena Muller')
print('--------------------------------------CARDÁPIO-------------------------------------')
print('| Nº DE BOLAS | SABOR TRADICIONAL (tr) | SABOR PREMIUM (pr) | SABOR ESPECIAL (es) |')
print('|     1       |      R$ 6,00           |       R$ 7,00      |        R$ 8,00      |')
print('|     2       |      R$ 10,00          |       R$ 12,00     |        R$ 14,00     |')
print('|     3       |      R$ 14,00          |       R$ 17,00     |        R$ 20,00     |')
print('-----------------------------------------------------------------------------------')
acumulador = 0
while True:
  sabor = input('Digite os sabores de sorvetes desejados (tr/pr/es):')
  if sabor != 'tr' and sabor != 'pr' and sabor != 'es':
    print('Opção Invválida. Digite um sabor correto!') 
    continue #se o usuário digitar um sabor errado, volta para o ínicio

  numero_bolas = input('Digite o número de bolas desejado (1/2/3):')
  if numero_bolas != '1' and numero_bolas != '2' and numero_bolas != '3':
    print('Opção Inválida. Digite o número de bolas de 1 a 3!')
    continue #se o usuário digitar o número de bolas errado, volta para o ínicio

  if numero_bolas == '1' and sabor == 'tr':
    print('Você escolheu o sorvete tradicional, com 1 bola.')
    acumulador = acumulador + 6 #sabor tradicional com 1 bola

  elif numero_bolas == '2' and sabor == 'tr':
    print('Você escolheu o sorvete tradicional, com 2 bolas.')
    acumulador = acumulador + 10 #sabor tradicional com 2 bolas

  elif numero_bolas == '3' and sabor == 'tr':
    print('Você escolheu o sorvete tradicional, com 3 bolas.')
    acumulador = acumulador + 14 #sabor tradicional com 3 bolas

  elif numero_bolas == '1' and sabor == 'pr':
    print('Você escolheu o sorvete premium, com 1 bola.')
    acumulador = acumulador + 7 #sabor premium com 1 bola

  elif numero_bolas == '2' and sabor == 'pr':
    print('Você escolheu o sorvete premium, com 2 bolas.')
    acumulador = acumulador + 12 #sabor premium com 2 bolas

  elif numero_bolas == '3' and sabor == 'pr':
    print('Você escolheu o sorvete premium, com 3 bolas.')
    acumulador = acumulador + 17 #sabor premium com 3 bolas

  elif numero_bolas == '1' and sabor == 'es':
    print('Você escolheu o sorvete especial, com 1 bola.')
    acumulador = acumulador + 8 #sabor especial com 1 bola

  elif numero_bolas == '2' and sabor == 'es':
    print('Você escolheu o sorvete especial, com 2 bolas.')
    acumulador = acumulador + 14 #sabor especial com 2 bolas

  elif numero_bolas == '3' and sabor == 'es':
    print('Você escolheu o sorvete especial, com 3 bolas.')
    acumulador = acumulador + 20 #sabor especial com 3 bolas
    
  pedir_mais = input('Deseja pedir mais algum sorvete (S/N)?') #para realizar com pedidos
  pedir_mais = pedir_mais.upper()
  if pedir_mais == 'S': 
    continue #caso o usuário queira realizar mais pedidos, volta para o ínicio
  else:
    print('O valor total a ser pago: R${:.2f}'.format(acumulador)) #soma total do pedido
    break 
 
