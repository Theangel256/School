'''
Este código revias una lista de chunks
y se queda con el que tenga mayor puntuación
cuando se traslapan
'''
chunks=[[0, 5, .9], [6, 12, .8], [9, 15, .85], [10, 14, .7]]
resultado_de_traslape = []
filtrado_de_chunks = []

print('''
  TAREA 7 - Desempaquetado de chunks
      
      Chunks de entrada:
      ''')
print(chunks)
for chunk in chunks: #se recorren los chunks uno por uno
    if len(filtrado_de_chunks)==0: #este if pone el primer chunk por que la lista esta vacía
        filtrado_de_chunks.append(chunk) 
    else:
        ultimo = filtrado_de_chunks[-1] #aqui agarro el ultimo chunk que se guardo
        if chunk[0]<=ultimo[1]: #aqui se checa si se traslapan
            if chunk[2]>ultimo[2]: #al checar si se traslapan, checa su puntuación
                filtrado_de_chunks[-1]=chunk #si hay mayor puntuación, se traslapa
        else:
            filtrado_de_chunks.append(chunk) #si no se traslapa, se guarda

#dejo los chunks en un filtrado
chunks = filtrado_de_chunks

#aqui junta los chunks que se traslapan
for traslape in chunks:
    if len(resultado_de_traslape)==0: #si esta vacio, meto el primero
        resultado_de_traslape.append(traslape)
    else:
        ultimo_chunk=resultado_de_traslape[-1] #se agarra el ultimo chunk colocado
        if traslape[0]<=ultimo_chunk[1]: #aqui se checa si se traslapa
            resultado_de_traslape[-1]=[ultimo_chunk[0], traslape[1]]
        else:
            resultado_de_traslape.append(traslape) #si no se traslapa, se coloca el traslape guardado
#imprime el traslape
print("""
      Chunks de salida:
      """)
print(resultado_de_traslape)