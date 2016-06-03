import variaveis as var
import crud_produtos as func_produtos

def menu():
	print("_____________________________________________________________")
	print("╳                     ✳   ŠHɅDΣ    ✳                       ╳")
	print("╳            ◄ ( 1 ) CɅDɅSTRɅR PRθDUTθ                     ╳")
	print("╳            ◄ ( 2 ) CONSULTAR PRθDUTθ                     ╳")
	print("╳            ◄ ( 3 ) ALTERAR PRθDUTθ                       ╳")
	print("╳            ◄ ( 4 ) REMOVER PRθDUTθ                       ╳")
	print("╳            ◄ ( 5 ) LISTAR ESTOQUE DE PRθDUTθS            ╳")
	print("╳            ◄ ( 9 ) SAIR                                  ╳")
	print("____________________________________________________________")

	continuar=True
	while continuar:
		opcao=int(input(">> DIGITE SUA OPÇÃO:"))
		if (opcao==1):			
			var.produtos.append(func_produtos.casdastrarProduto())		
		elif (opcao==2):			
			func_produtos.consultarProdutoPorCodigo()
		elif (opcao==3):			
			func_produtos.alterarProdutoPorCodigo()
		elif (opcao==4):
			func_produtos.apagarProduto()
		elif (opcao==5):
			func_produtos.listarTodosProdutos()
		elif (opcao==9):
			print("Volte sempre!")
			continuar=False
			
menu()
