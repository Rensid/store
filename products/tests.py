from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from users.models import User
from products.models import Product


class IndexViewTestCase(TestCase):

    def test_view(self):
        path = reverse('index')  # '127.0.0.1:8000
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store')
        self.assertTemplateUsed(response, 'products/index.html')


class ProductsListViewTestCase(TestCase):

    fixtures = ['categories.json', 'goods.json']

    def test_list(self):
        path = reverse('products:index')
        response = self.client.get(path)

        products = Product.objects.all()
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Каталог')
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertEqual(list(response.context_data['object_list']), list(products[:3]))

    def test_list_with_category(self):
        path = reverse('products:category', args=[3])
        response = self.client.get(path)
        products = Product.objects.filter(category=3)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Каталог')
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertEqual(list(response.context_data['object_list']), list(products[:3]))
