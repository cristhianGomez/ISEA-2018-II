# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Area(models.Model):
	_name = 'matriculas.area'

	name = fields.Char(string= "Nombre")
	description = fields.Integer(string= "Descripción")

class Curso(models.Model):
	_name = 'matriculas.curso'

	name = fields.Char(string= "Nombre")
	description = fields.Integer(string= "Descripción")
	area_id= fields.Many2one('matriculas.area', string="Area")
	
class Matricula(models.Model):
	_name = 'matriculas.matricula'

	fecha_matricula = fields.Date(string= "Fecha de Matricula")
	curso_id= fields.Many2one('matriculas.curso', string="Modulo")
	alumno_id= fields.Many2one('matriculas.alumno', string="Alumno")
	
class Alumnos(models.Model):
	_name = 'matriculas.alumno'

	name = fields.Char(string= "Nombres y Apellidos")
	age = fields.Char(string= "Edad")
	correo_e = fields.Char(string= "Correo Electrónico")
	celphone = fields.Char(string= "Celular")
	