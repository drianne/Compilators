import ox #biblioteca do parse -- Só funciona em python3
import  operator as op 

#Criar lexer : Função que recebe string de código e retorna tokens (Recebe lista de tuplas - nome do token e expressão regular)

lexer = ox.make_lexer([
    ('NUMBER', r'\d+(\.\d*)?'), # /d = [0-9]
    ('OP_S', r'[-+]'),    
    ('OP_M', r'[*/]'),
])

# Função recebe o token jogado na funcao func, retorna objeto  que é associado à "átomo"
#Converte string func = float em número par uso posterior

tokens_list = ['NUMBER','OP']
infix = lambda x, op, y : (op, x, y) #Só organiza a ordem dos operadores 
#Lambda define uma funcao simples (lambda argumentos e :retorno)
atom = lambda x: ('atom',float(x)) # Expressão "SEXY ;p" -- função átomo recebe um token e retorna a árvore sintática
parser = ox.make_parser([ 
	('expr : expr OP_S term', infix),
	('expr : term', lambda x : x),
	('term : term OP_M atom', infix),
	('term : atom', lambda x : x),
    ('atom : NUMBER', atom) # Reduz numéro em um átomo
  #  ('expr : atom OP atom', --> (OP x y)) # lisp (lista em python) - Operadores infixo, prefixo, sufixo
], tokens_list)

# ------------------------FUNÇÕES ----------------------------------------------------------------------------

OP_TO_FUNC = {
	'+': lambda x , y : x + y,
	'-': lambda x , y : x - y,
	'*': lambda x , y : x * y,
	'/': lambda x , y : x / y,
}

def eval(ast): # Pega algo que veio de parser e avalia a expressão
	#( incluindo árvores sintáticas)
	head, *tail = ast # "Desestrutura" a lista L = [1,2,3] => x,y,z = L	| x, *y = L (Primeiro elemento da lista vai pra X e o resto pra Y)
	if head == 'atom' :
		return tail[0]
	elif head in {'+','-','*','/'}:
		#Criar dicionário que mapeia cada uma das funcoes OP_TO_FUNC
		func = OP_TO_FUNC[head]
		x , y = map(eval,tail) # Essa fução mapeia os valores da função e retorna pra outra variável (eval do primeiro elemento da calda e do segundo)
		x , y = eval(x), eval(y)
		return func(x,y)
	
#Regra e função que processa a regra
#Simbolo terminal : Não pode ser analisado mais

expr = input('expr:') #Leitura
tokens = lexer(expr)
ast = parser(tokens)
print('tokens : ' ,tokens)
print('AST: ', ast) # ast = arvore abstrata sintática
print('eval: ', eval (ast))
