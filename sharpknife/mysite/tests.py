# -*- coding: utf-8 -*-
from django.test import TestCase

from .models import AppleAccountModel

# Create your tests here.

class AppleAccountModelTest(TestCase):
    def test_get_account_set(self):
        query_set = AppleAccountModel.objects.filter(used=True)
        for item in query_set:
            print(item.game_name)