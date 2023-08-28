from django.test import TestCase, Client
from service.models import ShopSupply
from django.urls import reverse
from django.contrib.auth.models import User
from client.models import Tasks


# ----------------------------------------------------SHOP----------------------------------------------------
class ShopSupplyModelTestCase(TestCase):
    def setUp(self):
        self.supply = ShopSupply.objects.create(
            el_name='Test Item',
            company_name='Test Manufacturer',
            type_el='Test Category',
            quantity=10,
            price=100,
            availability=True
        )

    def test_shop_supply_creation(self):
        self.assertTrue(isinstance(self.supply, ShopSupply))
        self.assertEqual(str(self.supply), 'Test Item')

    def test_fields(self):
        self.assertEqual(self.supply.el_name, 'Test Item')
        self.assertEqual(self.supply.company_name, 'Test Manufacturer')
        self.assertEqual(self.supply.type_el, 'Test Category')
        self.assertEqual(self.supply.quantity, 10)
        self.assertEqual(self.supply.price, 100)
        self.assertTrue(self.supply.availability)

    def test_image_field_upload(self):
        self.assertEqual(self.supply.image_item.path.split('/')[-1], 'test_image.jpg')
        self.assertEqual(self.supply.image_item.url, '/media/service/images/shop/test_image.jpg')

    def test_verbose_names(self):
        self.assertEqual(self.supply._meta.verbose_name, 'Spare part')
        self.assertEqual(self.supply._meta.verbose_name_plural, 'Spare parts')


# ---------------------------------------------------TASKS---------------------------------------------------


class ServiceViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.supply = ShopSupply.objects.create(el_name='Test Item', company_name='Test Manufacturer',
                                                type_el='Test Category', quantity=10, price=100, availability=True)
        self.task = Tasks.objects.create(title='Test Task', description='Task description', username=self.user)

    def test_shop_catalog_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('shop_catalog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'service/shop.html')

    def test_order_item_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('order_item', args=[self.supply.pk]))
        self.assertEqual(response.status_code, 302)

        post_data = {'task_id': self.task.pk}
        response = self.client.post(reverse('order_item', args=[self.supply.pk]), data=post_data)
        self.assertEqual(response.status_code, 302)

    def test_home_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'service/index.html')


