#
# César Rodas
# 16776
##

from gl import Render, color, V2, V3
from obj import Obj, Texture
from shaders import *

r = Render()
r.glCreateWindow(1280,720)

#
# Se carga el fondo de pantalla
# imagen: fondo.bmp
#
print('Se va a cargar una escena, esta operación puede tardar unos minutos...\n')
print('Cargando fondo de la escena...')
fondo = Texture('./models/fondo.bmp')
r.pixels = fondo.pixels
print('Fondo cargado...')

#
# se agrega la camara
# se setea la posición inicial de los modelos respecto a la cámara
#
posModel = V3( 0, 0, 200)
r.lookAt(posModel, V3(0,0,5)) #5,5,0


#
# Se agrega el modelo de la torre de agua con textura y shader.
# obj:      water_tower.bmp
# textura:  water_tower.obj
# shader:   static_matix
#
print('Cargando modelo torre de agua...')
r.active_texture = Texture('./models/water_tower.bmp')
r.active_shader = static_matrix
r.glLoadModel('./models/water_tower.obj', V3( 0, -10, 450), V3(1,1,1), V3(0,0,0))
print('Torre de agua cargada...')


#
# Se agrega el modelo de los soldados con textura y shader.
# Primer soldado:
# obj:      soldier.bmp
# textura:  soldier.obj
# shader:   negative
#
print('Cargando modelo de soldados...')
r.active_texture = Texture('./models/soldier.bmp')
r.active_shader = negative
r.glLoadModel('./models/soldier.obj', V3( -12, -9, 40), V3(2,2,2), V3(0,0,0))
#
# Segundo soldado:
# shader:   gourad
#
r.active_shader = gourad
r.glLoadModel('./models/soldier.obj', V3( -17, -10, 40), V3(2,2,2), V3(0,0,0))
print('Soldados cargados...')


#
# Se agrega el modelo de los soldados con textura y shader.
# Primer soldado:
# obj:      soldier.bmp
# textura:  soldier.obj
# shader:   negative
#
print('Cargando modelo de hunvee...')
r.active_texture = Texture('./models/humvee.bmp')  
r.active_shader = toon
r.glLoadModel('./models/humvee.obj', V3( -15, 0, 23), V3(1,1,1), V3(0,0,0))
print('Hunvee cargado...')


#
# Se agrega el modelo de los barriles con textura y shader.
# Primer barril:
# obj:      barril.bmp
# textura:  barril2.obj
# shader:   phong
#
print('Cargando modelos de barriles...')
r.active_texture = Texture('./models/barril.bmp')
r.active_shader = phong
r.glLoadModel('./models/barril2.obj',V3(2.8,-1.5,17), V3(1,1.1,1), V3(0,0,0))
#
# Segundo soldado:
# shader:   greyScale
#
r.active_shader = greyScale
r.glLoadModel('./models/barril2.obj',V3(4.1,-1.5,17), V3(1,1.2,1), V3(0,0,0))
#
# Tercer soldado:
# shader:   phong
#
r.active_shader = phong
r.glLoadModel('./models/barril2.obj',V3(5.4,-1.5,17), V3(1,1.2,1), V3(0,0,0))
#
# Cuarto soldado:
# shader:   greyScale
#
r.active_shader = greyScale
r.glLoadModel('./models/barril2.obj',V3(6.8,-1.5,17), V3(1,1,1), V3(0,0,0))
print('Barriles cargados...')


#
# Se agrega el modelo del carro viejo con textura y shader.
# obj:      rusted_car.bmp
# textura:  rusted_car.obj
# shader:   phong
#
print('Cargando modelo de carro viejo...')
r.light= V3(0,0,1)
r.active_texture = Texture('./models/rusted_car.bmp')
r.active_shader = phong
r.glLoadModel('./models/rusted_car.obj',V3(10,-14,31), V3(1,1,1), V3(30,0,0))
print('Carro viejo cargada...')

#
# finaliza la escena y se crea el archivo
##
print('\nEscena creada, grabando archivo...\n')
r.glFinish('escena.bmp')