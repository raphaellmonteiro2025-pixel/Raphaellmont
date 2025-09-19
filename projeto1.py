#MEU PRIMEIRO PROJETO
#COLOCANDO EM PRÁTICA MINHAS AULAS DE PYTHON
print('SEJA BEM VINDO(A) AO MEU PRIMEIRO PROJETO!!')

nome_do_usuario = input('Me diga o seu nome: ')

if nome_do_usuario:
    print(f'Olá {nome_do_usuario}, muito prazer!!'
           ' me chamo Raphaell Monteiro e sou o CEO '
           'deste projeto.')
    vald_p_cont = input('Podemos ' \
'prosseguir com algumas pergu' \
'ntas sobre você? Digite [S] para SIM ' \
'ou [N] para NÃO: ')
if (vald_p_cont == 'S'):
    print(f'Ótimo fico feliz que você'   
        ' desejou continuar!! ')
else:
    print('Muito obrigado(a), '
          'volte sempre!!!')

sobrenome = input('Qual seu ' \
'sobrenome? ')
idade = input('Qual sua idade? ')
altura = float(input('Qual sua altura? '))
peso = float(input('Qual seu peso? '))

result_pe = peso   #peso em kg
vari_peso = 35   #variavel base de taxa regular
imc = peso / (altura * altura) #peso elevado a altura ao quadrado
peso_ideal = (imc * altura * altura)  #ml de água por kg
multi_p = result_pe * vari_peso #multiplicador das variáveis


vald_final = print(f'Você '
                   f'se chama {nome_do_usuario} {sobrenome}'
                   f' tem {idade} anos, possui {altura}mo de altura'
                   f' e tem {peso}kg')
multi_1 = peso * altura

confir_d_diag = input('Com base nas informações'
' que você me passou, irei fazer um diagnostico!!' \
'' \
' Para que possamos processeguir digite [S]' \
' para SIM E [N] para NÃO: ')
if (confir_d_diag == 'S'):
    print('COM BASE NAS INFORMAÇÕES PASSADAS ACIMA VOCÊ!!!'
          
          )
else:
    print('Muito obrigado(a)' \
    ' volte sompre!!')
  
multi_1 = peso * altura

print(f'Seu peso 'f'ideal é de {int(peso_ideal)} '
      f'kg, seu IMC Seu IMC é de {imc:1f}, e você '
      f' deve beber cerca de {multi_p / 1000:.2f}L '
      f' por dia para se manter saudável! ')

print('VOLTE SEMPRE, OBRIGADO(A)!!!')
