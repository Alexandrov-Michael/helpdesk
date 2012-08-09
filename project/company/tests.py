# -*- coding:utf-8 -*-


from django.test import TestCase
from company.models import PcOptions



class SimpleTest(TestCase):
    """
    Тест представлений
    """
    fixtures = ['fixture1.json']

    def test_PcDetail(self):
        """
        проверка представления по деталицаии ПК
        """
        c = self.client

        login_success = c.login(username='admin', password='123')
        self.assertTrue(login_success)
        response = c.get('/pc_detail/1/')
        self.assertEqual(response.status_code, 200)
        resp = c.get('/pc_detail/99999999999/')
        self.assertEqual(resp.status_code, 404)
        c.logout()

        login_success = c.login(username='ferromet', password='user12345')
        self.assertTrue(login_success)
        response = c.get('/pc_detail/1/')
        self.assertEqual(response.status_code, 404)
        c.logout()


    def test_AddPcOption(self):
        """
        AddPcOption
        """
        c = self.client
        login_success = c.login(username='admin', password='123')
        self.assertTrue(login_success)
        resp = c.get('/add_opt/1/')
        self.assertEqual(resp.status_code, 200)

        resp1 = c.get('/add_opt/99999999999/')
        self.assertEqual(resp1.status_code, 404)

        option = PcOptions.objects.get(pk=1)
        resp2 = c.post('/add_opt/1/', {'option': option, 'body': 'test'})
        self.assertEqual(resp2.status_code, 200)


    def test_GetCompanyForAddDepartametView(self):
        """
        GetCompanyForAddDepartametView
        """
        c = self.client
        login_success = c.login(username='admin', password='123')
        self.assertTrue(login_success)
        resp = c.get('/ajax/get_company_for_add_dep/')
        self.assertEqual(resp.status_code, 200)
        c.logout()

        login_success = c.login(username='ferromet', password='user12345')
        self.assertTrue(login_success)
        response = c.get('/ajax/get_company_for_add_dep/')
        self.assertEqual(response.status_code, 404)
        c.logout()
        ### response mimetype = json проверить





