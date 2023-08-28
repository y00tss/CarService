from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from client.models import Tasks, Userguides, UserguidesImages
from django.urls import reverse
from django.contrib.auth.models import User
from client.models import Userguides, UserguidesImages, Tasks
from authorisation.models import CustomUserUser

User = get_user_model()


# -------------------------------------------------------Models------------------------------------------------------
class TasksModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpassword')

        Tasks.objects.create(
            username=cls.user,
            task_name='Oil Change',
            task_description='Change the oil',
            task_price_job=50,
            task_price_equipment=20,
            task_status=False,
            task_progress=False
        )

    def test_task_str_representation(self):
        task = Tasks.objects.get(id=1)
        self.assertEqual(str(task), 'Oil Change')

    def test_task_total_price(self):
        task = Tasks.objects.get(id=1)
        self.assertEqual(task.total_price(), 70)

    def test_start_task_method(self):
        task = Tasks.objects.get(id=1)
        task.start_task()
        self.assertTrue(task.task_progress)

    def test_finish_task_method(self):
        task = Tasks.objects.get(id=1)
        task.finish_task()
        self.assertTrue(task.task_status)


class UserguidesModelTest(TestCase):
    def test_userguides_str_representation(self):
        guide = Userguides.objects.create(guide_name='Guide Name', guide_description='Guide Description')
        self.assertEqual(str(guide), 'Guide Name')


class UserguidesImagesModelTest(TestCase):
    def test_userguides_images_relation(self):
        guide = Userguides.objects.create(guide_name='Guide Name', guide_description='Guide Description')
        image = UserguidesImages.objects.create(guide=guide, image='path/to/image.jpg')
        self.assertEqual(image.guide, guide)


# --------------------------------------------------------Views--------------------------------------------------------

class ClientViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.mechanic = CustomUserUser.objects.create(user=self.user, is_mechanic=True)
        self.guide = Userguides.objects.create(title='Test Guide', content='Guide content')
        self.image = UserguidesImages.objects.create(guide=self.guide, image='test_image.jpg')
        self.task = Tasks.objects.create(title='Test Task', description='Task description', username=self.user)

    def test_home_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'client/index.html')

    def test_manuals_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('manuals'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'client/manuals.html')

    def test_create_task_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('create_task'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'client/order.html')

        form_data = {'title': 'New Test Task', 'description': 'New Task description'}
        response = self.client.post(reverse('create_task'), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Tasks.objects.count(), 2)

    # Add more tests as needed
