from django.test import TestCase
from .models import Student
from .forms import StudentForm
from django.urls import reverse
from django.test import Client
import datetime
client = Client()

class Student_TestCase(TestCase):
	def setUp(self):
		self.student = Student(
			first_name="Lucie", 
			last_name="Kamuyu", 
			date_of_birth=datetime.date(2000,10,31), 
			registration_number="12345", 
			gmail="muringolucie@gmail.com", 
			phone_number="0712345678", 
			place_of_residence="Ruai", 
			guardian_name="0712345678", 
			id_name="098765", 
			date_joined=datetime.date.today(),
			)

	def test_full_name_contains_first_name(self):
		self.assertIn(self.student.first_name, self.student.full_name())


	def test_full_name_contains_last_name(self):
		self.assertIn(self.student.last_name, self.student.full_name())

		def test_age_is_always_above_18(self):
			self.assertFalse(self.student.clean() <18)

			def test_age_is_always_below_30(self):
				self.assertFalse(self.student.clean() >30)




class CreateStudentTestCase(TestCase):
	def setUp(self):
		self.data = {"first_name" : "Lucie", 
			         "last_name" : "Kamuyu", 
			         "date_of_birth" : datetime.date(2000,10,31),
			         "registration_number" : "12345",
			         "gmail" : "muringolucie@gmail.com",
			         "phone_number" : "0712345678",
			         "place_of_residence" : "Ruai",
			         "guardian_name" : "0712345678",
			         "id_name" : "098765",
			         "date_joined" : datetime.date.today()
			}

		self.bad_data = {"first_name" : "Mary", 
			             "last_name" : "", 
			             "date_of_birth" : datetime.date(1990,10,21),
			             "registration_number" : "",
			             "gmail" : "",
			             "phone_number" : "0798765432",
			             "place_of_residence" : "",
			             "guardian_name" : "",
			             "id_name" : "",
			             "date_joined" : datetime.date.today()
			}


	def test_student_form_accepts_valid_data(self):
		form = StudentForm(self.data)
		self.assertTrue(form.is_valid())


	def test_student_form_rejects_invalid_data(self):
		form = StudentForm(self.data)
		self.assertTrue(form.is_valid())


	def test_add_student_view(self):
		url=reverse("add_student")
		request=client.post(url,self.data)
		self.assertEqual(request.status_code, 200)

	def test_add_student_view_bad_data(self):
		url=reverse("add_student")
		request=client.post(url,self.bad_data)
		self.assertEqual(request.status_code, 400)


	
		

			

