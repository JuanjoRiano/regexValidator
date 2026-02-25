import re

class Validacion: 

	def validar_placa(placa):
		patron = r'^[A-Z]{3}[0-9]{3}$'
		return bool(re.match(patron, placa.strip()))

	def validar_correo(correo):
		patron = r'^[\w.+\-]+@[\w\-]+\.[a-zA-Z]{2,}$'
		return bool(re.match(patron, correo.strip()))

	def validar_cedula(cedula):
		patron = r'^[0-9]{7,10}$'
		return bool(re.match(patron, cedula.strip()))

	def validar_marca(marca):
		patron = r'^[a-zA-Z]+$'
		return bool(re.match(patron, marca.strip()))		

	def validar_modelo(modelo):
		patron = r'^(19[0-9]{2}|200[0-9]|201[0-9]|202[0-6])$'
		return bool(re.match(patron, modelo.strip()))

	def validar_color(color):
		patron = r'^[a-zA-Z ]+$'
		return bool(re.match(patron, color.strip()))

	def validar_chasis(chasis):
		patron = r'^[a-zA-Z0-9]{17}$'
		return bool(re.match(patron, chasis.strip()))

	def validar_noMotor(noMotor):
		patron = r'^[a-zA-Z0-9]+$'
		return bool(re.match(patron, noMotor.strip()))		

	def validar_nombre(nombre):
		patron = r'^[a-zA-Z ]+$'
		return bool(re.match(patron, nombre.strip()))	

	def validar_telefono(telefono):
		patron = r'^[0-9]{10}$'	
		return bool(re.match(patron, telefono.strip()))	









