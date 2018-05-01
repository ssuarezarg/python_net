#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
#ans=True

def clear():
  os.system('clear')

def anykey():
  any=raw_input("...Presione ENTER para continuar...")

def menumain():
    print ("Selecciona una opción")
    print ("\t1 - primera opción")
    print ("\t2 - Lista de host")
    print ("\t3 - tercera opción")
    print ("\t9 - salir")
    ans=raw_input("Seleccione la tarea que desea realizar? ")
    return ans

def menuHost():
    clear()
    print ("Opciones de host")
    print ("\t1 - Ver lista de host")
    print ("\t2 - Agregar un host")
    print ("\t3 - Eliminar un host")
    print ("\t9 - Atras")
    ans=raw_input("Seleccione la tarea que desea realizar? ")
    return ans

def functions():


def main():
  ans=True
  while ans:
      clear()
      ans=menumain()

      if ans=="1":
        print("\nStudent Added")
      elif ans=="2":
        menuHost()
      elif ans=="3":
        print("\n Student Record Found")
      elif ans=="9":
        print("\n Goodbye") 
        ans = None
      else:
         print("\n Not Valid Choice Try again")
      anykey()

if __name__ == "__main__":    #No se xq pero todos lo ponen :(
    main()

