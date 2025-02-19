from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {"name": "NISSAN",
         "description": "Great cars. Japanese technology",
         "headquarters": "Yokohama, Japan",
         "website": "https://www.nissan-global.com",
         "country_of_origin": "Japan",
         "established_year": 1933},
        {"name": "Mercedes",
         "description": "Great cars. German technology",
         "headquarters": "Stuttgart, Germany",
         "website": "https://www.mercedes-benz.com",
         "country_of_origin": "Germany",
         "established_year": 1926},
        {"name": "Audi",
         "description": "Great cars. German technology",
         "headquarters": "Ingolstadt, Germany",
         "website": "https://www.audi.com",
         "country_of_origin": "Germany",
         "established_year": 1909},
        {"name": "Kia",
         "description": "Great cars. Korean technology",
         "headquarters": "Seoul, South Korea",
         "website": "https://www.kia.com",
         "country_of_origin": "South Korea",
         "established_year": 1944},
        {"name": "Toyota",
         "description": "Great cars. Japanese technology",
         "headquarters": "Toyota City, Japan",
         "website": "https://www.toyota-global.com",
         "country_of_origin": "Japan",
         "established_year": 1937},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(
                name=data['name'],
                description=data['description'],
                headquarters=data['headquarters'],
                website=data['website'],
                country_of_origin=data['country_of_origin'],
                established_year=data['established_year']
            )
        )

    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
        {"name": "Pathfinder",
         "type": "SUV",
         "year": 2023,
         "car_make": car_make_instances[0],
         "color": "Red",
         "price": 35000.00,
         "horsepower": 284,
         "fuel_type": "Gasoline",
         "transmission": "Automatic"},
        {"name": "Qashqai",
         "type": "SUV",
         "year": 2023,
         "car_make": car_make_instances[0],
         "color": "Blue",
         "price": 25000.00,
         "horsepower": 141,
         "fuel_type": "Gasoline",
         "transmission": "Automatic"},
        {"name": "XTRAIL",
         "type": "SUV",
         "year": 2023,
         "car_make": car_make_instances[0],
         "color": "Black",
         "price": 30000.00,
         "horsepower": 169,
         "fuel_type": "Gasoline",
         "transmission": "Automatic"},
        {"name": "A-Class",
         "type": "SUV",
         "year": 2023,
         "car_make": car_make_instances[1],
         "color": "White",
         "price": 40000.00,
         "horsepower": 188,
         "fuel_type": "Gasoline",
         "transmission": "Automatic"},
        {"name": "C-Class",
         "type": "SUV",
         "year": 2023,
         "car_make": car_make_instances[1],
         "color": "Silver",
         "price": 45000.00,
         "horsepower": 255,
         "fuel_type": "Gasoline",
         "transmission": "Automatic"},
        {"name": "E-Class",
         "type": "SUV",
         "year": 2023,
         "car_make": car_make_instances[1],
         "color": "Black",
         "price": 50000.00,
         "horsepower": 302,
         "fuel_type": "Gasoline",
         "transmission": "Automatic"},
        {"name": "Q5",
         "type": "SUV",
         "year": 2023,
         "car_make": car_make_instances[2],
         "color": "Blue",
         "price": 43000.00,
         "horsepower": 261,
         "fuel_type": "Gasoline",
         "transmission": "Automatic"},
        {"name": "Q7",
         "type": "SUV",
         "year": 2023,
         "car_make": car_make_instances[2],
         "color": "White",
         "price": 55000.00,
         "horsepower": 335,
         "fuel_type": "Gasoline",
         "transmission": "Automatic"},
        {"name": "Sportage",
         "type": "SUV",
         "year": 2023,
         "car_make": car_make_instances[3],
         "color": "Red",
         "price": 27000.00,
         "horsepower": 181,
         "fuel_type": "Gasoline",
         "transmission": "Automatic"},
        {"name": "Sorento",
         "type": "SUV",
         "year": 2023,
         "car_make": car_make_instances[3],
         "color": "Black",
         "price": 32000.00,
         "horsepower": 191,
         "fuel_type": "Gasoline",
         "transmission": "Automatic"},
        {"name": "Camry",
         "type": "Sedan",
         "year": 2023,
         "car_make": car_make_instances[4],
         "color": "Silver",
         "price": 25000.00,
         "horsepower": 203,
         "fuel_type": "Gasoline",
         "transmission": "Automatic"},
        {"name": "Corolla",
         "type": "Sedan",
         "year": 2023,
         "car_make": car_make_instances[4],
         "color": "Blue",
         "price": 20000.00,
         "horsepower": 169,
         "fuel_type": "Gasoline",
         "transmission": "Automatic"},
    ]

    for model in car_model_data:
        CarModel.objects.create(
            name=model['name'],
            type=model['type'],
            year=model['year'],
            car_make=model['car_make'],
            color=model['color'],
            price=model['price'],
            horsepower=model['horsepower'],
            fuel_type=model['fuel_type'],
            transmission=model['transmission']
        )
