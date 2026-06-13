# Importando as bibliotecas
import os
from time import sleep
from InquirerPy import inquirer


# Função limpa tela
def limpar_tela():
	os.system('cls' if os.name == 'nt' else 'clear')


# Função principal
def main():


	# Menu de comidas
	menu_escolhas = ['arroz', 'tutu', 'carne', 'batata frita', 'salada', 'farofa', 'salpicão', 'maionese', 'sair']


	# Menu de bebidas
	bebidas_escolha = ['coca cola', 'suco', 'água', 'água c/ gás', 'pepsi', 'vinho', 'caipirinha', 'sair']


	# Menu de sobremesas
	sobremesas_escolha = ['quindim', 'bolo', 'torta', 'pudim', 'cupcake', 'pavê', 'gelatina', 'sair']


	# Apresentação do game
	print("""\n           
	   			=======================================
								
	   				Self Service Game!!
	   
					monte seu prato,
					acompanhe bebidas 
					e escolha suas sobremesas
					sem repetições!
	   
	   			========================================
				\n""")
	

	# Prato feito a ser montado
	prato_feito = []


	# Drink a ser montado
	drink_pronto = []


	# Sobremesa a ser montada
	sobremesa_pronta = []


	# Inicio
	input('Pressione [Enter] para iniciar: ')


	# Loop do prato feito
	while True:


		# Limpar tela
		limpar_tela()


		# Mostrar prato
		texto_prato = f" Prato atual: {prato_feito if prato_feito else 'Vazio'}"
		tamanho_barra = len(texto_prato) + 2


		print("=" * tamanho_barra)
		print(texto_prato)
		print("=" * tamanho_barra + "\n")


		# Escolha do jogador (prato feito)
		escolha = inquirer.select(
			qmark='',
			amark='',
			message='- Escolha um alimento ou pressione [sair] para escolher bebida\n',
			choices=menu_escolhas,
			show_cursor=False
		).execute()


		# If's e else (prato feito)
		if escolha == 'sair':
			break


		if escolha not in prato_feito:
				
			prato_feito.append(escolha)
			print('''\n\n\n 
		  			===============================
		  			Alimento adicionado com sucesso
		  			===============================\n\n\n''')
			sleep(1.5)


		else:
			print('''\n\n\n 
		  			=======================
		  			Alimento já selecionado
		  			=======================\n\n\n''')
			sleep(1.5)


	# Loop do drink pronto
	while True:


		# Limpar tela
		limpar_tela()


		# Mostrar drink
		texto_drink = f" Drink atual: {drink_pronto if drink_pronto else 'Vazio'}"
		tamanho_barra = len(texto_drink) + 2


		print("=" * tamanho_barra)
		print(texto_drink)
		print("=" * tamanho_barra + "\n")


		# Escolha do jogador 2 (drink pronto)
		escolha2 = inquirer.select(
			qmark='',
			amark='',
			message='- Escolha uma bebida ou pressione [sair] para escolher sobremesa\n',
			choices=bebidas_escolha,
			show_cursor=False
		).execute()


		# If's e else 2 (drink pronto)
		if escolha2 == 'sair':
			break


		if escolha2 not in drink_pronto:

			drink_pronto.append(escolha2)
			print('''\n\n\n					
		  			=============================
		  			Bebida adicionada com sucesso
		  			=============================\n\n\n''')
			sleep(1.5)



		else:

			print('''\n\n\n				  	
		  			=====================	
		  			Bebida já selecionada
		  			=====================\n\n\n''')
			sleep(1.5)


	# Loop da sobremesa pronta
	while True:


		# Limpar tela
		limpar_tela()


		# Mostrar prato
		texto_sobremesa = f" Sobremesa atual: {sobremesa_pronta if sobremesa_pronta else 'Vazio'}"
		tamanho_barra = len(texto_sobremesa) + 2


		print("=" * tamanho_barra)
		print(texto_sobremesa)
		print("=" * tamanho_barra + "\n")


		# Escolha do jogador 3 (sobremesa pronta)
		escolha3 = inquirer.select(
			qmark='',
			amark='',
			message='- Escolha uma sobremesa ou pressione [sair] para finalizar\n',
			choices=sobremesas_escolha,
			show_cursor=False
		).execute()


		# If's e else 3 (sobremesa pronta)
		if escolha3 == 'sair':
			break


		if escolha3 not in sobremesa_pronta:

			sobremesa_pronta.append(escolha3)
			print('''\n\n\n					
		  			======================
		  			Adicionado com sucesso
		  			======================\n\n\n''')
			sleep(1.5)


		else:

			print('''\n\n\n					
		  			========================
		  			Sobremesa já selecionada
		  			========================\n\n\n''')
			sleep(1.5)


	# Total de refeições
	print(f"""\n\n					
                                        ===================
                                        No total você comeu
                                        ===================
	   

	   
                                        {prato_feito}
					   
										
                                        de refeição

										
                                        acompanhado de 

										
                                        {drink_pronto}

						
                                        	e 
			
                                        {sobremesa_pronta}

										
                                        de sobremesa.""")


# Chamando a função
if __name__ == "__main__":
    main()