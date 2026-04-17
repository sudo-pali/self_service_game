# Função principal
def main():


	# Menu de comidas
	menu = ['arroz', 'tutu', 'carne', 'batata frita', 'salada', 'farofa']


	# Menu de sobremesas
	sobremesas = ['quindim', 'bolo', 'torta', 'pudim', 'cupcake']


	# Apresentação do game
	print("\nSelf Service Game!!\n\nmonte seu prato e escolha suas sobremesas sem repetições!\n")


	# Prato feito a ser montado
	prato_feito = []


	# Sobremesa a ser montada
	sobremesa_pronta = []


	# Loop do prato feito
	while True:


		# Print de comidas disponíveis
		print(f"Comidas dispoíveis: {menu}")


		# Escolha do jogador
		escolha = input('\nEscolha um alimento sem repetições ou pressione "Enter" para sair: ').strip().lower()

		
		# Ifs e elses
		if escolha == "":
			break


		if escolha in menu:

			if escolha in prato_feito:
				print('\n\n\nAlimento já selecionado\n\n\n')
		

			else:
				prato_feito.append(escolha)
				print('\n\n\nAdicionado com sucesso\n\n\n')

		else:

			print('\n\n\nAlimento não disponível\n\n\n')


	# Prato feito
	print(f'\n\n\nSeu prato feito: {prato_feito}\n\n\n')


	# Loop da sobremesa pronta
	while True:


		# Print de sobremesas disponíveis
		print(f"Sobremesas dispoíveis: {sobremesas}")


		# Escolha do jogador
		escolha2 = input('\nEscolha uma sobremesa sem repetições ou pressione "Enter" para sair: ').strip().lower()


		# Ifs e elses
		if escolha2 == "":
			break

		if escolha2 in sobremesas:

			if escolha2 in sobremesa_pronta:
				print('\n\n\nSobremesa já selecionada\n\n\n')


			else:
				sobremesa_pronta.append(escolha2)
				print('\n\n\nAdicionado com sucesso\n\n\n')

		else:
			print('\n\n\nSobremesa não disponível\n\n\n')


	# Sobremesa pronta
	print(f'\n\n\nSua sobremesa pronta: {sobremesa_pronta}\n\n\n')


# Chamando a função
if __name__ == "__main__":
    main()
