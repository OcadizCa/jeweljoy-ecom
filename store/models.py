from django.db import models
from django.contrib.auth.models import User 
import datetime

#Categorias de productos 


class CajaSorpresa(models.Model):
    nombre = models.CharField(max_length=100)

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    caja_sorpresa = models.OneToOneField(CajaSorpresa, on_delete=models.CASCADE)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)

class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    caja_sorpresa = models.OneToOneField(CajaSorpresa, on_delete=models.CASCADE)

class DetallesPedido(models.Model):
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

class PedidoDetalles(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    detalles_pedido = models.ForeignKey(DetallesPedido, on_delete=models.CASCADE)




class Category (models.Model):
    ame = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
#Cliente
class Customer (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name}{self.lastname}'

#Todos los productos 
class Product (models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True, null=True)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')


    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField (max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField (default = False)

    def __str__(self):
        return self.product
    
