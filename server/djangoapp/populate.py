from .models import CarMake, CarModel

def initiate():
    car_make_data = [
        {"name":"NISSAN", "description":"Great cars. Japanese technology", "headquarters":"Yokohama, Japan", "website":"https://www.nissan-global.com", "country_of_origin":"Japan", "established_year":1933},
        {"name":"Mercedes", "description":"Great cars. German technology", "headquarters":"Stuttgart, Germany", "website":"https://www.mercedes-benz.com", "country_of_origin":"Germany", "established_year":1926},
        {"name":"Audi", "description":"Great cars. German technology", "headquarters":"Ingolstadt, Germany", "website":"https://www.audi.com", "country_of_origin":"Germany", "established_year":1909},
        {"name":"Kia", "description":"Great cars. Korean technology", "headquarters":"Seoul, South Korea", "website":"https://www.kia.com", "country_of_origin":"South Korea", "established_year":1944},
        {"name":"Toyota", "description":"Great cars. Japanese technology", "headquarters":"Toyota City, Japan", "website":"https://www.toyota-global.com", "country_of_origin":"Japan", "established_year":1937},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(CarMake.objects.create(
            name=data['name'],
            description=data['description'],
            headquarters=data['headquarters'],
            website=data['website'],
            country_of_origin=data['country_of_origin'],
            established_year=data['established_year']
        ))

    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
        {"name":"Pathfinder", "type":"SUV", "year": 2023, "car_make":car_make_instances[0], "color":"Red", "price":35000.00, "horsepower":284, "fuel_type":"Gasoline", "transmission":"Automatic"},
        {"name":"Qashqai", "type":"SUV", "year": 2023, "car_make":car_make_instances[0], "color":"Blue", "price":25000.00, "horsepower":141, "fuel_type":"Gasoline", "transmission":"Automatic"},
        {"name":"XTRAIL", "type":"SUV", "year": 2023, "car_make":car_make_instances[0], "color":"Black", "price":30000.00, "horsepower":169, "fuel_type":"Gasoline", "transmission":"Automatic"},
        {"name":"A-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1], "color":"White", "price":40000.00, "horsepower":188, "fuel_type":"Gasoline", "transmission":"Automatic"},
        {"name":"C-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1], "color":"Silver", "price":45000.00, "horsepower":255, "fuel_type":"Gasoline", "transmission":"Automatic"},
        {"name":"E-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1], "color":"Gray", "price":55000.00, "horsepower":362, "fuel_type":"Gasoline", "transmission":"Automatic"},
        {"name":"A4", "type":"SUV", "year": 2023, "car_make":car_make_instances[2], "color":"Red", "price":42000.00, "horsepower":201, "fuel_type":"Gasoline", "transmission":"Automatic"},
        {"name":"A5", "type":"SUV", "year": 2023, "car_make":car_make_instances[2], "color":"Blue", "price":47000.00, "horsepower":261, "fuel_type":"Gasoline", "transmission":"Automatic"},
        {"name":"A6", "type":"SUV", "year": 2023, "car_make":car_make_instances[2], "color":"Black", "price":54000.00, "horsepower":335, "fuel_type":"Gasoline", "transmission":"Automatic"},
        {"name":"Sorrento", "type":"SUV", "year": 2023, "car_make":car_make_instances[3], "color":"White", "price":35000.00, "horsepower":191, "fuel_type":"Gasoline", "transmission":"Automatic"},
        {"name":"Carnival", "type":"SUV", "year": 2023, "car_make":car_make_instances[3], "color":"Silver", "price":32000.00, "horsepower":290, "fuel_type":"Gasoline", "transmission":"Automatic"},
        {"name":"Cerato", "type":"Sedan", "year": 2023, "car_make":car_make_instances[3], "color":"Gray", "price":20000.00, "horsepower":147, "fuel_type":"Gasoline", "transmission":"Automatic"},
        {"name":"Corolla", "type":"Sedan", "year": 2023, "car_make":car_make_instances[4], "color":"Red", "price":21000.00, "horsepower":139, "fuel_type":"Gasoline", "transmission":"Automatic"},
        {"name":"Camry", "type":"Sedan", "year": 2023, "car_make":car_make_instances[4], "color":"Blue", "price":25000.00, "horsepower":203, "fuel_type":"Gasoline", "transmission":"Automatic"},
        {"name":"Kluger", "type":"SUV", "year": 2023, "car_make":car_make_instances[4], "color":"Black", "price":40000.00, "horsepower":295, "fuel_type":"Gasoline", "transmission":"Automatic"},
        {"name":"Altima", "type":"Sedan", "year": 2023, "car_make":car_make_instances[0], "color":"White", "price":24000.00, "horsepower":188, "fuel_type":"Gasoline", "transmission":"Automatic"},
        {"name":"GT-R", "type":"Coupe", "year": 2023, "car_make":car_make_instances[0], "color":"Silver", "price":113540.00, "horsepower":565, "fuel_type":"Gasoline", "transmission":"Automatic"},
        {"name":"GLE", "type":"SUV", "year": 2023, "car_make":car_make_instances[1], "color":"Blue", "price":54000.00, "horsepower":255, "fuel_type":"Gasoline", "transmission":"Automatic"},
        {"name":"Q7", "type":"SUV", "year": 2023, "car_make":car_make_instances[2], "color":"Gray", "price":55000.00, "horsepower":248, "fuel_type":"Gasoline", "transmission":"Automatic"},
        {"name":"Sportage", "type":"SUV", "year": 2023, "car_make":car_make_instances[3], "color":"Red", "price":27000.00, "horsepower":187, "fuel_type":"Gasoline", "transmission":"Automatic"},
        {"name":"RAV4", "type":"SUV", "year": 2023, "car_make":car_make_instances[4], "color":"Green", "price":26000.00, "horsepower":203, "fuel_type":"Gasoline", "transmission":"Automatic"}
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            type=data['type'],
            year=data['year'],
            car_make=data['car_make'],
            color=data['color'],
            price=data['price'],
            horsepower=data['horsepower'],
            fuel_type=data['fuel_type'],
            transmission=data['transmission']
        )