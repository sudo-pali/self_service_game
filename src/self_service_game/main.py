# Importando a biblioteca
from InquirerPy import inquirer


# Função principal
def main():


	# Menu de comidas
	menu = ['arroz', 'tutu', 'carne', 'batata frita', 'salada', 'farofa', 'salpicão', 'maionese']
	menu_escolhas = ['arroz', 'tutu', 'carne', 'batata frita', 'salada', 'farofa', 'salpicão', 'maionese', 'sair']


	# Menu de bebidas
	bebidas = ['coca cola', 'suco', 'água', 'água c/ gás', 'pepsi', 'vinho', 'caipirinha']
	bebidas_escolha = ['coca cola', 'suco', 'água', 'água c/ gás', 'pepsi', 'vinho', 'caipirinha', 'sair']


	# Menu de sobremesas
	sobremesas = ['quindim', 'bolo', 'torta', 'pudim', 'cupcake', 'pavê', 'gelatina']
	sobremesas_escolha = ['quindim', 'bolo', 'torta', 'pudim', 'cupcake', 'pavê', 'gelatina', 'sair']


	# Escolhas
	escolhas = ['S', 'N']


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


	# Loop do prato feito
	while True:


		# Print de comidas disponíveis
		print(f"""\n\n       
					Comidas dispoíveis: 
		
			{menu}
					\n\n""")


		# Escolha do jogador (prato feito)
		escolha = inquirer.select(
			qmark='',
			amark='',
			message='- Deseja escolher alimento? Pressione "N" para escolher bebida',
			choices=escolhas,
			show_cursor=False
		).execute()


		# If's e else (prato feito)
		if escolha == 'N':
			break


		if escolha == 'S':
			escolha_alimento = inquirer.select(
				qmark='',
				amark='',
				message='Escolha um alimento ou pressione "sair" para avançar',
				choices=menu_escolhas,
				show_cursor=False
			).execute()
	

		if escolha_alimento == 'sair':
			break


		if escolha_alimento not in prato_feito:
				
			prato_feito.append(escolha_alimento)
			print('''\n\n\n 
		  			===============================
		  			Alimento adicionado com sucesso
		  			===============================\n\n\n''')
			

		else:
			print('''\n\n\n 
		  			=======================
		  			Alimento já selecionado
		  			=======================\n\n\n''')


	# Prato feito
	print(f"""\n\n\n					Comida selecionada: 
	   
	   			{prato_feito}\n""")


	# Loop do drink pronto
	while True:


		# Print de bebidas disponíveis
		print(f"""\n\n       
					Bebidas dispoíveis:
		 
			{bebidas}
					\n\n""")


		# Escolha do jogador 2 (drink pronto)
		escolha2 = inquirer.select(
			qmark='',
			amark='',
			message='- Deseja escolher bebida? Pressione "N" para escolher sobremesa',
			choices=escolhas,
			show_cursor=False
		).execute()


		# If's e else 2 (drink pronto)
		if escolha2 == 'N':
			break

		
		if escolha2 == 'S':
			escolha_bebida = inquirer.select(
				qmark='',
				amark='',
				message='Escolha uma bebida ou pressione "sair" para avançar',
				choices=bebidas_escolha,
				show_cursor=False
			).execute()


		if escolha_bebida == 'sair':
			break


		if escolha_bebida not in drink_pronto:

			drink_pronto.append(escolha_bebida)
			print('''\n\n\n					
		  			=============================
		  			Bebida adicionada com sucesso
		  			=============================\n\n\n''')


		else:

			print('''\n\n\n				  	
		  			=====================	
		  			Bebida já selecionada
		  			=====================\n\n\n''')


	# Drink pronto
	print(f"""\n\n\n				    	Bebida selecionada: 
	   
	   			{drink_pronto}\n""")


	# Loop da sobremesa pronta
	while True:


		# Print de sobremesas disponíveis
		print(f"""\n\n					Sobremesas dispoíveis:

				{sobremesas}\n\n""")


		# Escolha do jogador 3 (sobremesa pronta)
		escolha3 = inquirer.select(
			qmark='',
			amark='',
			message='- Deseja escolher sobremesa? Pressione "N" para encerrar',
			choices=escolhas,
			show_cursor=False
		).execute()


		# If's e else 3 (sobremesa pronta)
		if escolha3 == 'N':
			break


		if escolha3 == 'S':
			escolha_sobremesa = inquirer.select(
				qmark='',
				amark='',
				message='Escolha uma sobremesa ou pressione "sair" para finalizar',
				choices=sobremesas_escolha,
				show_cursor=False
			).execute()

		
		if escolha_sobremesa == 'sair':
			break


		if escolha_sobremesa not in sobremesa_pronta:

			sobremesa_pronta.append(escolha_sobremesa)
			print('''\n\n\n					
		  			======================
		  			Adicionado com sucesso
		  			======================\n\n\n''')
			
		else:

			print('''\n\n\n					
		  			========================
		  			Sobremesa já selecionada
		  			========================\n\n\n''')


	# Sobremesa pronta
	print(f'''\n\n\n					Sua sobremesa pronta:
	   
	   				{sobremesa_pronta}\n\n\n''')


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
