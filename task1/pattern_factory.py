from abc import ABC, abstractmethod
import logging
from colorlog import ColoredFormatter
from typing import Type

# Налаштування кольорового логування
formatter = ColoredFormatter(
    "%(log_color)s%(levelname)s: %(message)s",
    log_colors={
        "DEBUG": "white",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red",
    },
)

handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Абстрактний базовий клас для транспортних засобів
class Vehicle(ABC):
    def __init__(self, make: str, model: str, spec: str) -> None:
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self) -> None:
        pass

# Клас для автомобіля
class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.spec}): Двигун запущено")

# Клас для мотоцикла
class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.spec}): Мотор заведено")

# Абстрактна фабрика для створення транспортних засобів
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass

# Фабрика для США
class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "US Spec")

# Фабрика для Європи
class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "EU Spec")

# Використання фабрик
def create_vehicles(factory: Type[VehicleFactory]) -> None:
    # Створюємо автомобілі та мотоцикли
    vehicle1 = factory.create_car("Ford", "Peugeot")
    vehicle1.start_engine()

    vehicle2 = factory.create_motorcycle("Yamaha", "Honda")
    vehicle2.start_engine()

    vehicle3 = factory.create_car("Volkswagen", "Citroen")
    vehicle3.start_engine()

    vehicle4 = factory.create_motorcycle("BMW", "Ducati")
    vehicle4.start_engine()

# Створюємо транспортні засоби для США
us_factory = USVehicleFactory()
create_vehicles(us_factory)

# Створюємо транспортні засоби для Європи
eu_factory = EUVehicleFactory()
create_vehicles(eu_factory)
