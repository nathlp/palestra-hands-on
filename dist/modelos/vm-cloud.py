import graphviz 
 
#criar o modelo de grafo direcionado 
modelo = graphviz.Digraph(name='vm-cloud', directory='modelos/') 

# Especifica caracteristicas para o grafo e passa as principais informaçoes do grafo
# (tempo total, numero de ciclos, tamanho do batch, numero maximo de entidades,
# tipo do modelo, warmup, tamanho warmup, semente)
modelo.attr(rankdir='LR', comment=' 2000 0 0 0 True False 0 10 ')

# Especifica as caracteristicas dos centros de serviço
# (tipo do node, tipo da distribuição de chegada, tipo da distribuição de serviço,
# média das chegadas, média de serviço)
modelo.node('0', 'Source', image='Rsource.gif', shape='plaintext', labelloc='t', comment='1')

modelo.node('1', 'Front', image='R1x1.gif', shape='plaintext', labelloc='t', comment=' 2 1 1 1 0.1 ') 

modelo.node('2', 'Load', image='R1x1.gif', shape='plaintext', labelloc='t', comment=' 2 None 1 None 0.05 ') 


modelo.node('3', 'VM1', image='R1x1.gif', shape='plaintext', labelloc='t', comment=' 2 None 1 None 0.325 ') 
modelo.node('4', 'VM2', image='R1x1.gif', shape='plaintext', labelloc='t', comment=' 2 None 1 None 0.325 ')
modelo.node('5', 'VM3', image='R1x1.gif', shape='plaintext', labelloc='t', comment=' 2 None 1 None 0.325 ')
modelo.node('6', 'VM4', image='R1x1.gif', shape='plaintext', labelloc='t', comment=' 2 None 1 None 0.325 ')

modelo.node('7', 'Destination', image='REnd.gif', shape='plaintext', labelloc='t', comment='3')

# Especifica as caracteristicas dos ligações 
#(node de origem, node de destino e probabilidade)
modelo.edge('0', '1', comment='100')

modelo.edge('1', '2', comment='100') 

modelo.edge('2', '3', comment='25')
modelo.edge('2', '4', comment='25')
modelo.edge('2', '5', comment='25')
modelo.edge('2', '6', comment='25')

modelo.edge('3', '7', comment='100')
modelo.edge('4', '7', comment='100')
modelo.edge('5', '7', comment='100')
modelo.edge('6', '7', comment='100')

modelo.render(format='png')