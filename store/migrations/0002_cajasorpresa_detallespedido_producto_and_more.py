# Generated by Django 5.0.6 on 2024-07-07 22:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CajaSorpresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DetallesPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='ame',
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caja_sorpresa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.cajasorpresa')),
            ],
        ),
        migrations.CreateModel(
            name='PedidoDetalles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalles_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.detallespedido')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.pedido')),
            ],
        ),
        migrations.AddField(
            model_name='detallespedido',
            name='producto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.producto'),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caja_sorpresa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.cajasorpresa')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.usuario'),
        ),
    ]
