mariana = 2 # dona da casa
renato = 4
larissa = 2
rafael = 5
augusto = 1
rafaela = 3

dedos = {mariana, renato, larissa, rafael, augusto, rafaela}
participantes = 6 #quantidade de participantes
somaDedos = 17 #soma dos valores de cada dedo
dedoapontadopara = 0
for x in range(somaDedos):
  if dedoapontadopara > participantes:
     dedoapontadopara = 0
  dedoapontadopara += 1
dedos = list(dedos)  #converter dedos para arquivo tipo 'list'
print('No final o dedo foi apontado para {}.'.format(dedos[dedoapontadopara]))