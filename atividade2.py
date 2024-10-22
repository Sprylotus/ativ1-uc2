import pandas as pd 


import os

os.system('cls')


roupas = ['Camiseta', 'Calça', 'Jaqueta', 'Vestido', 'Boné']
quant_estoque = 50, 30, 15, 10, 25

estoque = pd.Series (quant_estoque, index=roupas)

print('Série Estoque de Roupas:')
print(estoque)

estoque.loc ['Saia'] = None 
print('\nAdicionada roupa fora de estoque:')
print(estoque)

print('\nRoupas com mais de 20 em estoque:')
print(estoque[estoque > 20])

precos = pd.Series ([3500, 2500, 1200, 900, 1500], index=roupas)
print('\nPreços das roupas em estoque:')
print(precos)

print('\nValor total do estoque por roupa (preço * quantidade):')
print(precos * estoque)