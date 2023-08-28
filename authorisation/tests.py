from django.test import TestCase
from authorisation.models import CustomUserUser
from django.urls import reverse
from django.contrib.auth import get_user_model
from authorisation.forms import SignUpForm, ProfileEditForm

# -------------------------------------------------------Models------------------------------------------------------
class CustomUserUserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CustomUserUser.objects.create(username='testuser', email='test@example.com')

    def test_is_mechanic_default_value(self):
        user = CustomUserUser.objects.get(id=1)
        self.assertEqual(user.is_mechanic, False)

    def test_description_field(self):
        user = CustomUserUser.objects.get(id=1)
        field = user._meta.get_field('description')
        self.assertEqual(field.max_length, 500)
        self.assertTrue(field.blank)

    def test_telegram_username_field(self):
        user = CustomUserUser.objects.get(id=1)
        field = user._meta.get_field('telegram_username')
        self.assertEqual(field.max_length, 20)
        self.assertTrue(field.blank)

    def test_usertg_id_field(self):
        user = CustomUserUser.objects.get(id=1)
        field = user._meta.get_field('usertg_id')
        self.assertTrue(field.blank)
        self.assertIsNone(field.default)
        self.assertIsNone(field.null)

    def test_avatar_upload_to(self):
        user = CustomUserUser.objects.get(id=1)
        field = user._meta.get_field('avatar')
        self.assertEqual(field.upload_to, 'authorisation/images/profile_avatar')



User = get_user_model()


class AuthorisationViewTest(TestCase):
    def test_authorisation_view(self):
        response = self.client.get(reverse('authorisation'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authorisation/authorisation.html')


class SignUpViewTest(TestCase):
    def test_signup_view(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/registration.html')

    def test_signup_form_valid(self):
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'telegram_username': 'testuser_telegram'
        }
        response = self.client.post(reverse('signup'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 1)


class EditProfileViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_edit_profile_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('edit_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/edit_profile.html')

    def test_edit_profile_form_valid(self):
        self.client.login(username='testuser', password='testpassword')
        data = {
            'telegram_username': 'new_telegram_username'
        }
        response = self.client.post(reverse('edit_profile'), data)
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        self.assertEqual(self.user.telegram_username, 'new_telegram_username')


class ProfileViewTest(TestCase):
    def test_profile_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/profile.html')


class ClosedAccessViewTest(TestCase):
    def test_closed_access_view(self):
        response = self.client.get(reverse('closed_access'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/closed_access.html')
