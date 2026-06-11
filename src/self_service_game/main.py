# Função principal
def main():


	# Menu de comidas
	menu = ['arroz', 'tutu', 'carne', 'batata frita', 'salada', 'farofa', 'salpicão', 'maionese']


	# Menu de bebidas
	bebidas = ['coca cola', 'suco', 'água', 'água c/ gás', 'pepsi', 'vinho', 'caipirinha']


	# Menu de sobremesas
	sobremesas = ['quindim', 'bolo', 'torta', 'pudim', 'cupcake', 'pavê', 'gelatina']


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
		escolha = input('''\n  - Escolha um alimento sem repetições ou pressione "Enter" para sair: 
				  
> ''').strip().lower()


		# If's e else's (prato feito)
		if escolha == "":
			break


		if escolha in menu:

			if escolha in prato_feito:	
				print('''\n\n\n 
		  			=======================
		  			Alimento já selecionado
		  			=======================\n\n\n''')
		

			else:
				prato_feito.append(escolha)
				print('''\n\n\n 
		  			===============================
		  			Alimento adicionado com sucesso
		  			===============================\n\n\n''')

		else:
			print('''\n\n\n	
		 			=======================		
		 			Alimento não disponível
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
		escolha2 = input('''\n  - Escolha uma bebida sem repetições ou pressione "Enter" para sair:
				   
> ''').strip().lower()


		# If's e else's 2 (drink pronto)
		if escolha2 == "":
			break


		if escolha2 in bebidas:

			if escolha2 in drink_pronto:
				print('''\n\n\n				  	
		  			=====================	
		  			Bebida já selecionada
		  			=====================\n\n\n''')


			else:
				drink_pronto.append(escolha2)
				print('''\n\n\n					
		  			=============================
		  			Bebida adicionada com sucesso
		  			=============================\n\n\n''')

		else:
			print('''\n\n\n				 	
		 			=====================
		 			Bebida não disponível
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
		escolha3 = input('''\n  - Escolha uma sobremesa sem repetições ou pressione "Enter" para sair: 

> ''').strip().lower()


		# If's e else's 3 (sobremesa pronta)
		if escolha3 == "":
			break


		if escolha3 in sobremesas:

			if escolha3 in sobremesa_pronta:
				print('''\n\n\n					
		  			========================
		  			Sobremesa já selecionada
		  			========================\n\n\n''')


			else:
				sobremesa_pronta.append(escolha3)
				print('''\n\n\n					
		  			======================
		  			Adicionado com sucesso
		  			======================\n\n\n''')

		else:
			print('''\n\n\n					
		 			========================
		 			Sobremesa não disponível
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
