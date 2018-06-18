from django.test import TestCase
from django.urls import reverse
from django.conf import settings

from .factories import SiderealTargetFactory, NonSiderealTargetFactory


class TestTargetDetail(TestCase):
    def setUp(self):
        self.st = SiderealTargetFactory.create()
        self.nst = NonSiderealTargetFactory.create()

    def test_sidereal_target_detail(self):
        response = self.client.get(reverse('targets:detail', kwargs={'pk': self.st.id}))
        self.assertContains(response, self.st.id)

    def test_non_sidereal_target_detail(self):
        response = self.client.get(reverse('targets:detail', kwargs={'pk': self.nst.id}))
        self.assertContains(response, self.nst.id)

    def test_sidereal_target_create(self):
        response = self.client.get(reverse('targets:create'))
        self.assertContains(response, settings.SIDEREAL)

    def test_non_sidereal_target_create(self):
        response = self.client.get(reverse('targets:create'))
        self.assertContains(response, settings.NON_SIDEREAL)