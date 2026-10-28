from django.test import TestCase
from .models import Service, Car, Coordinate, ContactForm, CarForm, Review
from django.utils.text import slugify

class ServiceModelTest(TestCase):
    def setUp(self):
        self.service = Service.objects.create(name="Test Service", description="Test description")

    def test_service_creation(self):
        self.assertEqual(self.service.name, "Test Service")
        self.assertEqual(self.service.description, "Test description")

    def test_service_str(self):
        self.assertEqual(str(self.service), "Test Service")


class CarModelTest(TestCase):
    def setUp(self):
        self.car = Car.objects.create(
            name="Test Car",
            slug=slugify("Test Car"),
            price=25000.00,
            speed=200.50,
            essence="Diesel",
            year=2022,
            description="Test description"
        )

    def test_car_creation(self):
        self.assertEqual(self.car.name, "Test Car")
        self.assertEqual(self.car.slug, "test-car")
        self.assertEqual(self.car.price, 25000.00)
        self.assertEqual(self.car.speed, 200.50)
        self.assertEqual(self.car.essence, "Diesel")
        self.assertEqual(self.car.year, 2022)
        self.assertEqual(self.car.description, "Test description")

    def test_car_str(self):
        self.assertEqual(str(self.car), "Test Car")


class CoordinateModelTest(TestCase):
    def setUp(self):
        self.coordinate = Coordinate.objects.create(
            adress="123 Test Street",
            email="test@example.com",
            phone="1234567890",
            schedules="9am - 5pm",
            status="Open"
        )

    def test_coordinate_creation(self):
        self.assertEqual(self.coordinate.adress, "123 Test Street")
        self.assertEqual(self.coordinate.email, "test@example.com")
        self.assertEqual(self.coordinate.phone, "1234567890")
        self.assertEqual(self.coordinate.schedules, "9am - 5pm")
        self.assertEqual(self.coordinate.status, "Open")


class ContactFormModelTest(TestCase):
    def setUp(self):
        self.contact = ContactForm.objects.create(
            name="John",
            lastname="Doe",
            email="john@example.com",
            phone="1234567890",
            message="Test message"
        )

    def test_contact_form_creation(self):
        self.assertEqual(self.contact.name, "John")
        self.assertEqual(self.contact.lastname, "Doe")
        self.assertEqual(self.contact.email, "john@example.com")
        self.assertEqual(self.contact.phone, "1234567890")
        self.assertEqual(self.contact.message, "Test message")

    def test_contact_form_str(self):
        self.assertEqual(str(self.contact), "John")


class CarFormModelTest(TestCase):
    def setUp(self):
        self.car_form = CarForm.objects.create(
            name="Jane",
            lastname="Doe",
            title="Car Inquiry",
            email="jane@example.com",
            phone="0987654321",
            message="Interested in the car"
        )

    def test_car_form_creation(self):
        self.assertEqual(self.car_form.name, "Jane")
        self.assertEqual(self.car_form.lastname, "Doe")
        self.assertEqual(self.car_form.title, "Car Inquiry")
        self.assertEqual(self.car_form.email, "jane@example.com")
        self.assertEqual(self.car_form.phone, "0987654321")
        self.assertEqual(self.car_form.message, "Interested in the car")

    def test_car_form_str(self):
        self.assertEqual(str(self.car_form), "Car Inquiry")


class ReviewModelTest(TestCase):
    def setUp(self):
        self.review = Review.objects.create(
            author="Alice",
            rating=5,
            content="Great car!",
            active=True
        )

    def test_review_creation(self):
        self.assertEqual(self.review.author, "Alice")
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.content, "Great car!")
        self.assertEqual(self.review.active, True)

    def test_review_str(self):
        self.assertEqual(str(self.review), "Review Great car! by Alice")

    def test_get_stars(self):
        self.assertEqual(list(self.review.get_stars()), [1, 2, 3, 4, 5])
