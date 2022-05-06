from peewee import *

db = SqliteDatabase('tourist.db')

class BaseClass(Model):
    id = PrimaryKeyField(
        unique=True,
        index=True
    )
    company = CharField(
        max_length=255,
        help_text='Выберите один из компаний'
    )

class Inner_flights(BaseClass):
    from_region = CharField(
        max_length=255,
        index=True,
        default='Aiport',
        help_text='Сюда укажите место вылета' # comment
    )
    to_destination = CharField(
        max_length=255,
        index=True,
        default='Aiport',
        help_text='Сюда укажите место прилета'
    )
    quantity = IntegerField(
        null=True,
        constraints=[Check('quantity >= 0')],
        help_text='Укажите количество пассажиров'
    )

    class Meta:
        database = db
        order_by = 'id'
        table_db = 'Вылет внутрений'


class Outter_flights(BaseClass):
    from_country = CharField(
        max_length=255,
        index=True,
        default='Страна',
        help_text='Сюда укажите страну вылета'
    )
    to_country = CharField(
        max_length=255,
        index=True,
        default='Страна',
        help_text='Сюда укажите страну прилета'
    )
    TYPE = (
        (1, "Грузовой"),
        (2, "Пассажирский"),
    )
    flight_type = CharField(
        max_length=255,
        choices=TYPE,
        help_text='Выберите тип'
    )
    neighbors = IntegerField(
        null=True,
        help_text='Укажите количество стран над которыми вы пролетите'
    )

    class Meta:
        database = db
        order_by = 'id'
        table_db = 'Вылет внешний'