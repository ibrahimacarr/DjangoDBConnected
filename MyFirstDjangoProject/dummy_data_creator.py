import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyFirstDjangoProject.settings')
import django
django.setup()


## Dummy Data Creator
import random
from my_first_app.models import User, Car
from faker import Faker

fakegen = Faker()

def populate(N=5):

    models = ['Opel', 'Audi', 'BMW' 'FIAT', 'Mercedes']

    for entry in range(N):
        fake_name = fakegen.name()
        fake_date = fakegen.date()
        fake_last_name = fakegen.last_name()
        fake_plate = fakegen.license_plate()
        fake_model = random.choice(models)

        # Create User
        user = User.objects.get_or_create(Name=fake_name, Surname=fake_last_name, BirthDate=fake_date, Plate=fake_plate)[0]

        # Create Fake car
        car = Car.objects.get_or_create(Plate=user, Model=fake_model)[0]


if __name__ == '__main__':
    print("Populating fake data..")
    populate(20)
    print("Populating complete")
