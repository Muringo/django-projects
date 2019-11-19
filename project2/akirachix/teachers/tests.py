from django.test import TestCase
from .models import Teachers
import datetime
from teachers.forms import TeacherForm
from django.test import Client
from django.urls import reverse
client=Client()
# Create your tests here.
class AddTeachersTestCase(TestCase):
   def setUp(self):
       self.data={"first_name":"Antony",
       "last_name":"Orenge",
       "teacher_hour":"datetime.date(2019,2,15)",
       "gender":"Male",
       "staff_number":"1234",
       "email":"antorenge@gmail.com",
       "contact":"+254743675424",
       "date_employed":"datetime.date.today()",
       }
       self.bad_data={"first_name":"Antony",
       "last_name":"",
       "teacher_hour":"datetime.date(2019,2,15)",
       "gender":"Male",
       "staff_number":"",
       "email":"",
       "contact":"",
       "date_employed":"datetime.date.today()",
       }
   def test_teacher_form_accepts_valid_data(self):
       form = TeacherForm(self.data)
       self.assertFalse(form.is_valid())

   def test_teacher_form_rejects_invalid_data(self):
       form = TeacherForm(self.bad_data)
       self.assertFalse(form.is_valid())

   def test_add_teacher_view(self):
       url=reverse("add_teacher")
       response=client.post(url,self.data)
       self.assertEqual(response.status_code,200)

   def test_add_teacher_view_bad_data(self):
       url = reverse("add_teacher")
       response=client.post(url,self.bad_data)
       self.assertEqual(response.status_code,400)

      




