from mestre import Mestre
mestre = Mestre()

print('Adventure of Rusty Axe Tavern')
print('Bem Vindo jogador')
print('Escolha o se personagem')
print('1. Borin o Bárbaro')
print('2. Mirah a Barda')
print('3. Osric o Clérigo')
print('4. Fenric o Druida')
print('5. Lorik o Guerreiro')
print('6. Silas o Ladino')
print('7. Cyria a Maga')
print('8. Kyan o monge')
print('9. Edras o paladino')
print('10. Korvin o patrulheiro')
print('11. Zethrin o Feiticero')
print('12. Drazel o Bruxo')



mensagem = mestre.mensagem('Começar Aventura')
print(mensagem)

def dialogo(npc, acao):
    resposta_ia = Mestre.mensagem(f'O jogador começa um dialogo com o {npc}: {acao}')
    while resposta_ia != 'Dialogo encerrado':
        print(resposta_ia)
        acao = input(f'nome do personagem do jogador: ')
        resposta_ia = Mestre.mensagem(f'Ação do jogador: {acao}')

def inventario():
    resposta_ia = Mestre.mensagem('O jogador quer verificar oq ele tem dentro da sua mochila: Responda com uma lista de todos os itens que o jogador tem')
    print(resposta_ia)
    acao = input('')
    return  acao


def combate(inimigos):
    contador = 1
    resosta_ia = Mestre.mensagem(f'O jogador inicia o combate com {inimigos}:')
    print(resosta_ia)
    while combate == True:
        print(f'Rodada {contador}')
        acao = input('')
        resposta_ia =  resosta_ia = Mestre.mensagem(f'Ação do jogador: {acao}')
        print(resposta_ia)
        contador += 1






continuar = True

while continuar != False:
    acao = input('')
    mensagem = mestre.mensagem(acao)
    print(mensagem)