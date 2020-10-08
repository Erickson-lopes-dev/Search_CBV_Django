from django.db import models


class BaseRegister(models.Model):
    created_date = models.DateField('Data da Criação', auto_now=True)
    created_hours = models.TimeField('Horario de criação', auto_now=True)

    modified_date = models.DateField('Data de modificação', auto_now_add=True)
    modified_hours = models.TimeField('Horario de modificação', auto_now_add=True)

    active = models.BooleanField('Ativado ?', default=True)


class Category(BaseRegister):
    name_category = models.CharField('Nome da Categoria', max_length=50)

    def __str__(self):
        return self.name_category


class Person(BaseRegister):
    name = models.CharField('Nome', max_length=100)
    last_name = models.CharField('Sobrenome', max_length=100)

    email = models.EmailField('E-mail')
    categoria = models.ManyToManyField(Category)

    birth_time = models.TimeField('Horario de nascimento', auto_now=False, auto_now_add=False)
    date_birth = models.DateField('Data de nascimento')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} {self.last_name}'
