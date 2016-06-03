import variaveis as var

def casdastrarProduto():
	produto=[]
	print("◄ CɅDɅSTRɅR PRθDƲTθ")
	codigo=int(input("CθDIGθ: "))
	#consultar o codigo do produto para saber se ele já existe
	indice_produto_existe = recuperarProdutoPorCodigo(codigo)	
	if(indice_produto_existe != None):
		print("Já existe um produto atribuido a este código")
	else:
		nome_produto=str.upper(input( "NθMΣ: "))
		quantidade=int(input( "QUANTIDADΣ: "))
		preco=float(input(       "VALOR DO PRODUTO:R$ "))		
		produto=[nome_produto,quantidade,preco,codigo]
	return produto

def apagarProduto():
	print("◄ DELETAR PRθDƲTθ")
	codigo=int(input("PESQUISE O PRODUTO POR CÓDIGO: "))
	indice_produto = recuperarProdutoPorCodigo(codigo)
	if(indice_produto != None):
		opcao=str.upper(input(" Você tem certeza que deseja remover o produto? [s,n]"))		
		if opcao == "S":
			var.produtos.pop(indice_produto)
			print("Produto removido com sucesso.")
		else:
			print("Produto não removido.")
	else:
		print("Produto não encontrado")

def recuperarProdutoPorCodigo(codigo):	
	ret_indice = None
	encontrado=False
	indice = 0
	for produto in var.produtos:
		if(produto[3] == codigo):			
			ret_indice = indice
			break
		indice +=1
	return ret_indice

def consultarProdutoPorCodigo():
	print("◄ CONSULTAR PRθDƲTθS")
	codigo=int(input("PESQUISE O PRODUTO POR CÓDIGO: "))
	indice_produto = recuperarProdutoPorCodigo(codigo)
	if(indice_produto != None):
		print('{cod}  {nome}   {qtd}  {preco}'.format(cod=var.produtos[indice_produto][3], nome=var.produtos[indice_produto][0], qtd=var.produtos[indice_produto][1], preco=var.produtos[indice_produto][2])) 		
	else:
		print("Produto não existe")
	
		
def alterarProdutoPorCodigo():
	print("◄ ALTERAR PRθDƲTθ")
	codigo=int(input("DIGITE O CÓDIGO DO PRODUTO QUE DESEJA ALTERAR: "))
	indice_produto = recuperarProdutoPorCodigo(codigo)
	if(indice_produto != None):
		novo_produto=[]
		
		nome_produto=str.upper(input( "NOVO NθMΣ: "))
		quantidade=int(input( "NOVA QUANTIDADΣ: "))
		preco=float(input("NOVO VALOR DO PRODUTO:R$ "))
		novo_produto=[nome_produto,quantidade,preco,codigo]
		var.produtos[indice_produto] = novo_produto		
	else:
		print("Produto não existe")		

def listarTodosProdutos():
	print("◄ LISTAR ESTOQUE DE PRθDUTθS")
	if(len(var.produtos) > 0):
		for produto in var.produtos:
			print('{cod}  {nome}   {qtd}  {preco}'.format(cod=produto[3], nome=produto[0], qtd=produto[1], preco=produto[2]))
	else:
		print("Nenhum produto foi cadastrado ainda.")
		
	
	