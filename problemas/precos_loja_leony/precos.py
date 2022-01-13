'''
*************************************************************************************************************************************************
* Considere uma loja que, antes de cada venda, checa manualmente o preço do item a ser vendido e, a partir dessa checagem, realiza a cobrança.  *
* O dono dessa loja, Leony, encomenda um programa que checa os preços cobrados pelos itens vendidos no dia e informa quantos erros aconteceram. *
*                                                                                                                                               *
* Myke Leony dos Santos Amorim. 12 de janeiro de 2021.                                                                                          *                                                                              *
*************************************************************************************************************************************************
'''

def checa_precos(produtos, precos, vendidos, precos_vendidos):
    erros = 0

    for i,v in enumerate(vendidos):
        valor_correto = 0

        for j,p in enumerate(produtos):
            if v == p:
                try: valor_correto = precos[j]
                except: return len(vendidos)   # Lista de preços dos produtos vazia. Todos os itens vendidos são potenciais erros.

                break

        try:
            if precos_vendidos[i] != valor_correto:
                erros += 1

        except:
            return len(vendidos)    # Lista de preços dos produtos vendidos vazia. Todos os itens vendidos são potenciais erros.

    return erros
  
