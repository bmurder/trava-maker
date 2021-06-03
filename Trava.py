import webbrowser
import os
import time
os.system('clear')

print('criador de travas')

trava = input("digite a sequência de caracteres: ")
repetição = input("quantas vezes irá se repetir?: ")
iniciar = input('iniciar s/n: ')
if (iniciar=='s'):
   print(trava*300)
elif (iniciar=='n'):
  print('compreensivel tenha um bom dia')
  
else: 
  print('vc está brincando com a minha cara?')
  
  time.sleep(3)
  webbrowser.open('https://youtu.be/dQw4w9WgXcQ')
  