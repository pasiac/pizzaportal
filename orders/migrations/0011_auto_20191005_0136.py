# Generated by Django 2.2.5 on 2019-10-04 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20190925_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(blank=True, choices=[('Peperoni', 'Peperoni'), ('None', 'None'), ('Sausage', 'Sausage'), ('Mushrooms', 'Mushrooms'), ('Onions', 'Onions'), ('Canadian Bacon', 'Canadian Bacon'), ('Pineapple', 'Pineapple'), ('Eggplant', 'Eggplant'), ('Tomato & Basil', 'Tomato & Basil'), ('Green Peppers', 'Green Peppers'), ('Hamburger', 'Hamburger'), ('Spinach', 'Spinach'), ('Zucchini', 'Zucchini'), ('Ham', 'Ham'), ('Fresh Garlic', 'Fresh Garlic'), ('Artichoke', 'Artichoke'), ('Buffalo Chicken', 'Buffalo Chicken'), ('Barbecue Chicken', 'Barbecue Chicken'), ('Anchovies', 'Anchovies'), ('Black Olives', 'Black Olives')], max_length=32, null=True)),
                ('choice2', models.CharField(blank=True, choices=[('Peperoni', 'Peperoni'), ('None', 'None'), ('Sausage', 'Sausage'), ('Mushrooms', 'Mushrooms'), ('Onions', 'Onions'), ('Canadian Bacon', 'Canadian Bacon'), ('Pineapple', 'Pineapple'), ('Eggplant', 'Eggplant'), ('Tomato & Basil', 'Tomato & Basil'), ('Green Peppers', 'Green Peppers'), ('Hamburger', 'Hamburger'), ('Spinach', 'Spinach'), ('Zucchini', 'Zucchini'), ('Ham', 'Ham'), ('Fresh Garlic', 'Fresh Garlic'), ('Artichoke', 'Artichoke'), ('Buffalo Chicken', 'Buffalo Chicken'), ('Barbecue Chicken', 'Barbecue Chicken'), ('Anchovies', 'Anchovies'), ('Black Olives', 'Black Olives')], max_length=32, null=True)),
                ('choice3', models.CharField(blank=True, choices=[('Peperoni', 'Peperoni'), ('None', 'None'), ('Sausage', 'Sausage'), ('Mushrooms', 'Mushrooms'), ('Onions', 'Onions'), ('Canadian Bacon', 'Canadian Bacon'), ('Pineapple', 'Pineapple'), ('Eggplant', 'Eggplant'), ('Tomato & Basil', 'Tomato & Basil'), ('Green Peppers', 'Green Peppers'), ('Hamburger', 'Hamburger'), ('Spinach', 'Spinach'), ('Zucchini', 'Zucchini'), ('Ham', 'Ham'), ('Fresh Garlic', 'Fresh Garlic'), ('Artichoke', 'Artichoke'), ('Buffalo Chicken', 'Buffalo Chicken'), ('Barbecue Chicken', 'Barbecue Chicken'), ('Anchovies', 'Anchovies'), ('Black Olives', 'Black Olives')], max_length=32, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='orderitem',
            name='addon',
            field=models.ManyToManyField(to='orders.Addon'),
        ),
    ]