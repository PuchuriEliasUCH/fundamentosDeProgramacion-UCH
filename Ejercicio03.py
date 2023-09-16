# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 22:08:11 2023

@author: User
"""

CA = float (input ("Ingresa la medida del cateto adyacente del triángulo : "))
CO = float (input ("Ingresa la medida del cateto opuesto del triángulo : "))


H = (((CA*CA) + (CO*CO))**0.5);


print ("El valor de la Hipotenusa es : ",  H )
