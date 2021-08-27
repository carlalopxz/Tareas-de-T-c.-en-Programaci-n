import time

calleRivadavia = {'eo': 'rojo'}
calleJujuy = {'ns':'verde'}

def cambiarLuces(Rivadavia,Jujuy):
  color_calle_R = Rivadavia
  color_calle_J = Jujuy
  rojo = '\033[91m'
  amarillo = '\033[93m'
  verde = '\033[92m'
  blanco = '\033[90m'
  default = '\033[39m'
  semaforo = '▓'*2 
  for i in range(2):
    if color_calle_R == 'rojo' or color_calle_R == rojo:
      print(f'''   {default}Rivadavia\tJujuy
      {rojo}{semaforo} \t {blanco}{semaforo}
      {blanco}{semaforo} \t {blanco}{semaforo}
      {blanco}{semaforo} \t {verde}{semaforo}
      \n''')
      time.sleep(5)
    if color_calle_R == 'rojo' or color_calle_R == rojo:
      print(f'''   {default}Rivadavia\tJujuy
      {rojo}{semaforo} \t {blanco}{semaforo}
      {amarillo}{semaforo} \t {amarillo}{semaforo}
      {blanco}{semaforo} \t {blanco}{semaforo}
      \n''')
      time.sleep(5)
      color_calle_R = verde
    if color_calle_R == verde:
      print(f'''   {default}Rivadavia\tJujuy
      {blanco}{semaforo} \t {rojo}{semaforo}
      {blanco}{semaforo} \t {blanco}{semaforo}
      {verde}{semaforo} \t {blanco}{semaforo}
      \n''')
      time.sleep(5)
    if color_calle_R == verde:
      print(f'''   {default}Rivadavia\tJujuy
      {blanco}{semaforo} \t {rojo}{semaforo}
      {amarillo}{semaforo} \t {amarillo}{semaforo}
      {blanco}{semaforo} \t {blanco}{semaforo}
      \n''')
      color_calle_R = rojo
      time.sleep(5)
    print("\033[H\033[J")
cambiarLuces(calleRivadavia['eo'],calleJujuy['ns'])
