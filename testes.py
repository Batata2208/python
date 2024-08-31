import os
catalogo = []

os.system("cls")

def AdicionarProduto():
	print("Digite o produto para ser cadastrado")
	ProdutoAdicionar = input(str())
	catalogo.append(ProdutoAdicionar)
	print("\nProduto adicionado com sucesso")

def RemoverProduto():
	print("Digite o produto a ser removido \n")
	ProdutoRemover = input(str())
	catalogo.remove(ProdutoRemover)

	print("\nProduto removido com sucesso")

def EditarProduto():
	print("Digite o produto a ser editado\n")
	ProdutoEditar = input(str())
	i = 0
	while catalogo[i] == ProdutoEditar:
		if catalogo[i] == ProdutoEditar:
			catalogo[i] = ProdutoEditar
		
	print("\nProduto editado com sucesso")
	
def lista():
	for i in catalogo:
  		print(i)
		  
AdicionarProduto()

lista()

EditarProduto()

lista()