from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from .models import Menu, Item, Ingredient

class MenuModelTests(TestCase):
    def test_Menu_creation(self):
        menu = Menu.objects.create(
            season = "test season",
        )
        now = timezone.now()
        self.assertEqual("test season", menu.season)
        self.assertLess(menu.created_date, now)


class MenuViewTest(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            id='1',
            username='123',
            email='123@email.com',
            password='123'
        )
        self.item = Item.objects.create(
            name = "test name",
            description = "test description",
            chef = self.test_user
        )
        self.menu = Menu.objects.create(
            season = "test season",

        )
        self.menu2 = Menu.objects.create(
            season = "test season 2",
        )

    def test_menu_list_view(self):
        resp = self.client.get(reverse('menu_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.menu, resp.context['menus'])
        self.assertIn(self.menu2, resp.context['menus'])
        self.assertTemplateUsed(resp, 'menu/list_all_current_menus.html')
        self.assertContains(resp, self.menu.season)

    def test_menu_detail_view(self):
        resp = self.client.get(reverse('menu_detail',
                                        kwargs={'pk':self.menu.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.menu, resp.context['menu'])
        resp2 = self.client.get(reverse('menu_detail',
                                        kwargs={'pk':self.menu2.pk}))
        self.assertEqual(self.menu2, resp2.context['menu'])
        self.assertTemplateUsed(resp, 'menu/menu_detail.html')
        self.assertContains(resp, self.menu.season)
        self.assertContains(resp2, self.menu2.season)

    def test_create_new_menu_view(self):
        resp = self.client.get(reverse('menu_new'))
        self.assertTemplateUsed(resp, 'menu/menu_edit.html')
    def test_edit_menu_view(self):
        resp = self.client.get(reverse('menu_edit',
                                        kwargs={'pk':self.menu.pk}))
        self.assertTemplateUsed(resp, 'menu/change_menu.html')


class ItemModelTests(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            id='1',
            username='123',
            email='123@email.com',
            password='123'
        )
    def test_Item_creation(self):
        item = Item.objects.create(
            name = "test name",
            description = "test description",
            chef = self.test_user
        )
        now = timezone.now()
        self.assertEqual("test name", item.name)
        self.assertLess(item.created_date, now)

class ItemViewTest(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            id='1',
            username='123',
            email='123@email.com',
            password='123'
        )
        self.item = Item.objects.create(
            name = "test name",
            description = "test description",
            chef = self.test_user
        )
    def test_item_detail_view(self):
        resp = self.client.get(reverse('item_detail',
                kwargs={'pk':self.item.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.item, resp.context['item'])
        self.assertTemplateUsed(resp, 'menu/detail_item.html')

class IngredientModelTests(TestCase):
    def test_ingredient_creation(self):
        ingredient = Ingredient.objects.create(
            name = "test name",
        )
        self.assertEqual("test name", ingredient.name)  
