import os, route

#TODO: Receber o nome do arquivo como parâmetro do programa (https://www.tutorialspoint.com/python/python_command_line_arguments.htm)
fileName = 'input-routes.csv'

with open (fileName, 'r') as file :
    fileContent = file.read()

print(fileContent)

#TODO: Popular os valores abaixo com o conteúdo do arquivo
graph = route.Graph([
    ("GRU","BRC",10),  ("BRC","SCL",5),  ("GRU","CDG",75), ("GRU","SCL",20),
    ("GRU","ORL",56), ("ORL","CDG",5), ("SCL","ORL",20)])

#TODO: Receber os parâmetros de origem e destino informados pelo usuários
print(graph.dijkstra("GRU", "CDG"))