from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40)
    code = models.IntegerField()


class Student(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()


class Profesor(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    profession = models.CharField(max_length=40)


class Homework(models.Model):
    name = models.CharField(max_length=40)
    due_date = models.DateField()
    is_delivered = models.BooleanField()

class Categoria(models.Model):
    name = models.CharField(max_length=40)
    code = models.IntegerField()

class Entrenador(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    disciplina = models.CharField(max_length=40)

class Deportista(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    disciplina = models.CharField(max_length=40)   

class Entrenamiento(models.Model):
    name = models.CharField(max_length=40)
    due_date = models.DateField()
    is_delivered = models.BooleanField()    