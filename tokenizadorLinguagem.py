
# coding: utf-8

# In[24]:

import re
from collections import namedtuple


# In[54]:

#LISTA DE TUPLAS

regex_map = [    
    ('NUMBER', r'[0-9]+(\.[0-9]*)?'),
    ('NAME' , r'[a-zA-Z_][a-zA-Z_0-9]*'),
    ('OP' , r'\+|\-|\*|\/'),
    ('LPAR' , r'\('),
    ('RPAR' , r'\)'),
    ('EQ',r'\='),
    ('NEWLINE',r'\n'),
    ('SPACE' , r'\s+'),
    ('ANYTHING' , r'.+'),
]

test1 = 'pi = 3.141516'
test2 = '1/n + (42 * x)'
test3 = 'pi = 3,14'


# In[8]:


#criando lista de grupos
"""
groups = [
    template.format(name = 'NUMBER', regex = NUMBER),
    template.format(name = 'NAME', regex = NAME)
]
"""


# In[55]:

#REGEX PARA COMBINAR TODOS OS TOKENS 

template = r'(?P<{name}>{regex})'

#UNIR TODAS AS REGEX

REGEX_ALL = '|'.join(
    template.format(name=name, regex=regex)
    for (name,regex) in regex_map
)

re_all = re.compile(REGEX_ALL)


# In[46]:

m, *rest = list(re_all.finditer(test1))


# In[60]:

#CLASSE PORCA - TUPLA
Token = namedtuple('Token',['type','data','lineno']) # Função que retorna uma classe com nome Token

#Pode acessar como struct ou como tupla
tk = Token('NUMBER', '3.14','lineno')


# In[32]:

"""converter objeto do tipo match em token
def token_from_match(m):
    sada"""


# In[61]:

source = test1

def lexer(source):
    lineno = 1
    for m in re_all.finditer(source):    
        #extrair tipo
        type_ = m.lastgroup
        if type_ == 'SPACE':
            continue
        elif type == 'NEWLINE':
            lineno+= 1
            continue
        #pegar os indices
        i,j = m.span()
        data = m.string[i:j]
        #yield : Semelhante ao return mas retorna controle para o que chamou a função e se chamada novamente
        #retorna de onde havia parado
        yield Token(type_,data,lineno)
        
list(lexer(source))

