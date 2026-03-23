def main():

	menu = ['arroz', 'tutu', 'carne', 'batata frita', 'salada', 'farofa']

	print(menu)



	prato_feito = []



	while True:


		escolha = input('Escolha um alimento sem repetições ou pressione "Enter" para sair: ').strip().lower()


		

		if escolha == "":

			break


		if escolha in menu:

			if escolha in prato_feito:
			
				print('Alimento já selecionado')
		

			else:

				prato_feito.append(escolha)

				print('Adicionado com sucesso')


		else:

			print('Alimento não disponível')


	print(f'Seu prato feito: {prato_feito}')


if __name__ == "__main__":
    main()
