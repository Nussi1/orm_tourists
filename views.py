from models import *
from pprint import pprint


with db:
    # Создание таблиц
    # db.create_tables([Inner_flights, Outter_flights])

    # Создание записей в таблицы
    # 1
    # Inner_flights(
    #     from_region='Chui',
    #     to_destination='Bishkek',
    #     company='Air Manas'
    # ).save()
    # 2
    # Inner_flights.create(
    #     from_region='Osh',
    #     to_destination='Karakol',
    #     company='Pegasus',
    #     quantity=80
    # )
    # 3
    # data = [
    #     {'from_country':'Kyrgyzstan1',
    #     'to_country':'Tyrkey1',
    #     'company':'Pegasus1',
    #     'flight_type':Outter_flights.TYPE[0],
    #     'neighbors':7},
    #     {'from_country': 'Franch1',
    #      'to_country': 'Spain1',
    #      'company': 'Boieng1',
    #      'flight_type': Outter_flights.TYPE[1],
    #      'neighbors': 10},
    #     {'from_country': 'Kyrgyzstan2',
    #      'to_country': 'Tyrkey2',
    #      'company': 'Pegasus2',
    #      'flight_type': Outter_flights.TYPE[0],
    #      'neighbors': 7},
    #     {'from_country': 'Franch2',
    #      'to_country': 'Spain2',
    #      'company': 'Boieng2',
    #      'flight_type': Outter_flights.TYPE[1],
    #      'neighbors': 10},
    #     {'from_country': 'Kyrgyzstan2',
    #      'to_country': 'Tyrkey2',
    #      'company': 'Pegasus2',
    #      'flight_type': Outter_flights.TYPE[0],
    #      'neighbors': 7},
    #     {'from_country': 'Franch3',
    #      'to_country': 'Spain3',
    #      'company': 'Boieng3',
    #      'flight_type': Outter_flights.TYPE[1],
    #      'neighbors': 10},
    #     {'from_country': 'Kyrgyzstan2',
    #      'to_country': 'Tyrkey2',
    #      'company': 'Pegasus2',
    #      'flight_type': Outter_flights.TYPE[0],
    #      'neighbors': 7},
    #     {'from_country': 'Franch3',
    #      'to_country': 'Spain3',
    #      'company': 'Boieng3',
    #      'flight_type': Outter_flights.TYPE[1],
    #      'neighbors': 10},
    #     {'from_country': 'Kyrgyzstan4',
    #      'to_country': 'Tyrkey4',
    #      'company': 'Pegasus4',
    #      'flight_type': Outter_flights.TYPE[0],
    #      'neighbors': 7},
    #     {'from_country': 'Franch',
    #      'to_country': 'Spain',
    #      'company': 'Boieng',
    #      'flight_type': Outter_flights.TYPE[1],
    #      'neighbors': 10},
    # ]
    # Outter_flights.insert_many(data).execute()

    # data = [
    #     {'from_region': 'Kyrgyzstan1',
    #      'to_destination': 'Tyrkey1',
    #      'company': 'Pegasus1',
    #      'quantity': 7},
    #     {'from_region': 'Kyrgyzstan2',
    #      'to_destination': 'Tyrkey2',
    #      'company': 'Pegasus1',
    #      'quantity': 70},
    #     {'from_region': 'Kyrgyzstan3',
    #      'to_destination': 'Tyrkey3',
    #      'company': 'Pegasus1',
    #      'quantity': 50},
    #     {'from_region': 'Kyrgyzstan4',
    #      'to_destination': 'Tyrkey4',
    #      'company': 'Pegasus4',
    #      'quantity': 3},
    #     {'from_region': 'Kyrgyzstan5',
    #      'to_destination': 'Tyrkey5',
    #      'company': 'Pegasus1',
    #      'quantity': 200},
    #     {'from_region': 'Kyrgyzstan6',
    #      'to_destination': 'Tyrkey6',
    #      'company': 'Pegasus1',
    #      'quantity': 700},
    #     {'from_region': 'Kyrgyzstan1',
    #      'to_destination': 'Tyrkey1',
    #      'company': 'Pegasus1',
    #      'quantity': 70},
    #     {'from_region': 'Kyrgyzstan1',
    #      'to_destination': 'Tyrkey1',
    #      'company': 'Pegasus1',
    #      'quantity': 500},
    #     {'from_region': 'Kyrgyzstan1',
    #      'to_destination': 'Tyrkey1',
    #      'company': 'Pegasus1',
    #      'quantity': 67},
    #     {'from_region': 'Germany',
    #      'to_destination': 'Spain',
    #      'company': 'Easyflight',
    #      'quantity': 17},
    # ]
    # Inner_flights.insert_many(data).execute()

    # Плучение данных
    # in_fl = Inner_flights.select()
    # print(in_fl)
    # for i_f in in_fl:
    #     print(i_f.id,
    #           i_f.from_region,
    #           i_f.to_destination,
    #           i_f.quantity,
    #           i_f.company)
    # print()
    # print()
    # in_fl = Inner_flights.select().where(Inner_flights.id > 5)
    # i_f = [(i_f.id, i_f.from_region, i_f.company, i_f.quantity, i_f.to_destination) for i_f in in_fl]
    # pprint(i_f)
    # in_fl = Inner_flights.select().where((Inner_flights.to_destination == 'Osh') | (Inner_flights.to_destination == 'Bishkek'))
    # print(in_fl)
    # for i_f in in_fl:
    #     print(i_f.id,
    #           i_f.from_region,
    #           i_f.to_destination,
    #           i_f.quantity,
    #           i_f.company)
    # in_fl = Inner_flights.select().where(Inner_flights.quantity > 150)
    # for i_f in in_fl:
    #     print(i_f.id,
    #           i_f.from_region,
    #           i_f.to_destination,
    #           i_f.quantity,
    #           i_f.company)
    # out_fl = Outter_flights.select(Outter_flights.company).where(Outter_flights.flight_type == "(1, 'Грузовой')")
    # for o_f in out_fl:
    #     print(o_f.company)

    # out_fl = Outter_flights.select().where(Outter_flights.id < 7)
    # for o_f in out_fl:
    #     print(o_f.id,
    #           o_f.company)

    # out_fl = Outter_flights.select().where(Outter_flights.neighbors > 3)
    # for o_f in out_fl:
    #     print(o_f.from_country,
    #           o_f.to_country,
    #           o_f.company,
    #           o_f.flight_type,
    #           o_f.neighbors
    # )
    # out_fl = Outter_flights.select().where((Outter_flights.neighbors < 20) & (Outter_flights.flight_type == "(2, 'Пассажирский')"))
    # for o_f in out_fl:
    #     print(o_f.from_country,
    #           o_f.to_country,
    #           o_f.company,
    #           o_f.flight_type,
    #           o_f.neighbors
    # )
    # out_fl = Outter_flights.select()
    # for o_f in out_fl:
    #     print(o_f.to_country,
    #           o_f.company,
    # )



    # pass








print('Готово')