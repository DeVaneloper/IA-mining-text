# -*- coding: utf-8 -*-
# """SimpleBotia-Infotexto.ipynb

# Automatically generated by Colaboratory.
# aqui fue donde corrio normal
# Original file is located at 
# https://colab.research.google.com/drive/1Qet_6tr7Xoj7RcJHJYsMy3UYd1EZC9zH 
    
# Simple Text Mining IA Interpretator :V es mas cool que interpretador!!
# Usamos la libreria tranformers

!pip install transformers

# ahora importamos el diccionario de para la tokenizacion es un diccionaio llamado bert en espanol, la equivalecial a nltk (models/spanish.tagger', 'stanford-postagger.jar', encoding='utf8) 
# la diferencia es que esta esta un poco mas orientada a una red neuronal de aprandizaje de pregunta y respuesta temporal

# Importamos el diccionario de datos en espanol esta disponible pero muy sinmple que esta disponible esta un poco incompleto 
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
the_model = 'mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es'
tokenizer = AutoTokenizer.from_pretrained(the_model, do_lower_case=False)
model = AutoModelForQuestionAnswering.from_pretrained(the_model)

# """esto no es necesario para final pero esto es el modelo obtenido"""

# esto no es necesario solo es para verificar que se creo el modelo a partir de la libreria
print(model)

# entonces mediante la tokenizacion permite interpretar el contexto, e realizar el formato de pregunta y respuesta"""

# Ejemplo tokenización, de lka pregunta y respuesta puede simplificar la pregunta o haecrla mas compleja con sus simbolos de interrogacion
contexto = 'soy vanelope'
pregunta = 'cómo me llamo'

encode = tokenizer.encode_plus(pregunta, contexto, return_tensors='pt')
input_ids = encode['input_ids'].tolist()
tokens = tokenizer.convert_ids_to_tokens(input_ids[0])
for id, token in zip(input_ids[0], tokens):
  print('{:<12} {:>6}'.format(token, id))
  print('')

# Ejemplo de inferencia (pregunta-respuesta), asi queda la interpretacion de pregunta y respuesta
nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)
salida = nlp({'question':pregunta, 'context':contexto})
print(salida)

from textwrap import wrap

def pregunta_respuesta(model, contexto, nlp):

  # Imprime el contexto generado a partir del texto no es necesario poner visual pero si quieres ver el texto lo activas
  #print('Contexto:')
  #print('-----------------')
  #print('\n'.join(wrap(contexto)))

  # Loop preguntas-respuestas:
  continuar = True
  while continuar:
    print('\nPregunta:')
    print('-----------------')
    pregunta = str(input())

    continuar = pregunta!=''

    if continuar:
      salida = nlp({'question':pregunta, 'context':contexto})
      print('\nRespuesta:')
      print('-----------------')
      print(salida['answer'])

# puedes usar os creo par importar un archivo de texto directamente te crea la respuestas y todo lo malo es que al terminar 
# pierde lo aprendido durante la sesion de preguntas
contexto = "Los datos que necesitas saber acerca de Kmushicoin: Se trata del primer proyecto de criptomoneda colombiana. La idea surgió en 2019 de la empresa Tierra Viva. Su objetivo es reducir las altas comisiones que generan las exportaciones internacionales. Cuenta con blockchain propia. Utiliza tanto PoW como PoS. Su emisión está limitada a 20 millones de unidades.El primer proyecto de criptomoneda colombiana se llama Kmushicoin (KTV). Su origen, sin duda, resulta muy interesante. Kmushicoin fue concebida por la empresa Tierra Viva, una compañía colombiana, ubicada en la ciudad de Tunja, que cría escarabajos gigantes y produce abono orgánico. Tierra Viva recolecta residuos orgánicos que se generan en hogares, los cuales usa para alimentar y criar a las larvas de escarabajo, y durante dicho proceso se genera el abono.La idea que dio origen a Kmushicoin surge en agosto de 2019, cuando el ingeniero medioambiental Germán Viasus y el programador Carmelo Campos (socios en Tierra Viva) imaginaron una criptomoneda que les permitiera tener un medio de pago propio, de esta forma, evitarían las altas comisiones de los pagos internacionales que generaban sus exportaciones.Al mismo tiempo, la criptomoneda, en línea con la visión medioambiental de Tierra Viva, trataría de reducir su impacto ambiental a través de diversas medidas (que la compañía expone en su página web). Otra aspiración es que, hacia el futuro, Kmushicoin sea utilizada como medio de pago para productos y servicios más allá del entorno de la empresa.  El nombre de la criptomoneda deriva de dos palabras: «kabuto»y «mushi», y su significado es escarabajo de cuernos. En la elección del nombre también influyó el vínculo que la empresa colombiana tiene con Japón, nación asiática a la que exporta este tipo de escarabajos (que son adoptados como mascotas). kmushicoin cryptoconexión Logo de Tierra Viva Escarabajos Al mismo tiempo, la criptomoneda, en línea con la visión medioambiental de Tierra Viva, trataría de reducir su impacto ambiental a través de diversas medidas (que la compañía expone en su página web). Otra aspiración es que, hacia el futuro, Kumshicoin sea utilizada como medio de pago para productos y servicios más allá del entorno de la empresa. El nombre de la criptomoneda deriva de dos palabras: «kabuto»y «mushi», y su significado es escarabajo de cuernos. En la elección del nombre también influyó el vínculo que la empresa colombiana tiene con Japón, nación asiática a la que exporta este tipo de escarabajos (que son adoptados como mascotas).  Kmushicoin, la criptomoneda de los escarabajos cornudos Sustentada en la empresa privada Tierra Viva, que se dedica a criar escarabajos gigantes y a la producción de abono orgánico.Su nombre deriva de dos palabras: «kabuto»y «mushi», que significa escarabajo de cuernos. Breve historia de Kmushicoin Agosto de 2019: nace Kmushicoin como iniciativa de la empresa Tierra Viva. Febrero de 2021: la Superintendencia Financiera del gobierno de Colombia coloca a Kmushicoin en los medios, ya que determina que la idea inicial de la empresa, emitir tokens como si fueran acciones de Tierra Viva (un recurso común para financiar el lanzamiento de una criptomoneda), no se podía hacer sin cumplir ciertos requisitos previos.  Mayo de 2021: se comunica a los inversores que adquirieron kmushicoins que no se trata de acciones, sino de criptoactivos. Septiembre de 2022: se produce el lanzamiento de KmushiPay, una app creada especialmente para los negocios y disponible en algunos países, mediante la cual se puede enviar, recibir y comprar Kmushicoin.Características técnicas Kmushicoin se apoya en una blockchain propia (no usa la de otra criptomoneda). Es una criptodivisa basada en el algoritmo script con sistema híbrido, es decir, utiliza como protocolo de consenso tanto PoS como PoW. Dado que esta criptomoneda busca, como prioridad, la mejora medioambiental, la minería PoW no proporciona recompensas a los mineros. Solo reciben las tasas de las transacciones en espera. La recompensa que obtendrá la validación PoS es de un 16% anual, distribuyéndose la ganancia cada minuto al confirmar un bloque. La emisión de esta criptomoneda está limitada a 20 millones de unidades (KTV).Carteras Kmushicoin cuenta con carteras para diferentes sistemas operativos, como Linux, Windows e IOS . ¿Dónde la consigues? Kmushicoin cuenta con su propio exchange para poder operar la criptomoneda: https://kmushicoin.co/p2p. También puede obtenerse en el exchange txbit.io. Más información Si quieres profundizar en algún tema de esta criptomoneda y su blockchain, puedes hacerlo en su página oficial aquí¿Te gustaría leer el White Paper de Kmushicoin? Consíguelo aquí."
pregunta_respuesta(model, contexto, nlp)

