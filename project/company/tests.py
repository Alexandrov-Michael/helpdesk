# -*- coding:utf-8 -*-


from django.test import TestCase
from company.models import PcOptions
from django.contrib.auth.models import User
from company.models import CompanyPC, Company, Departments, PcOptions
from profiles.models import Profile
from django.core.urlresolvers import reverse
import views



class SimpleTest(TestCase):
    """
    Тест представлений
    """
    def setUp(self):
        ### USERS ###
        self.password = '123'

        ferromet = User()
        ferromet.username = 'ferromet'
        ferromet.first_name = 'FERROMET'
        ferromet.set_password(self.password)
        ferromet.save()

        admin = User()
        admin.username = 'admin'
        admin.first_name = 'Главный куратор'
        admin.set_password(self.password)
        admin.save()

        ### PROFILES ###

        profile1 = Profile()
        profile1.user = admin
        profile1.is_company = False
        profile1.is_report = True
        profile1.is_super_user = True
        profile1.telefon = '+7 921 622 22 50'
        profile1.save()

        profile2 = Profile()
        profile2.user = ferromet
        profile2.save()

        ### COMPANYS ###


        fer_com = Company()
        fer_com.com_user = ferromet
        fer_com.save()


        ### DEPS ###

        dep1 = Departments()
        dep1.pk = 1
        dep1.company = fer_com
        dep1.name = u'Основной'
        dep1.save()

        ### PC ###

        pc1 = CompanyPC()
        pc1.id = 1
        pc1.company = fer_com
        pc1.departament = dep1
        pc1.pc_nameId = '1'
        pc1.pc_name = 'buh'
        pc1.save()

        ### PC_OPTIONS ###

        option1 = PcOptions()
        option1.id = 1
        option1.name = u'Процессор'
        option1.save()


        ### Departments ###




    def test_PcDetail(self):
        """
        проверка представления по деталицаии ПК
        """
        c = self.client

        login_success = c.login(username='admin', password=self.password)
        self.assertTrue(login_success)
        response = c.get('/pc_detail/1/')
        self.assertEqual(response.status_code, 200)
        resp = c.get('/pc_detail/99999999999/')
        self.assertEqual(resp.status_code, 404)
        c.logout()

        login_success = c.login(username='ferromet', password=self.password)
        self.assertTrue(login_success)
        response = c.get('/pc_detail/1/')
        self.assertEqual(response.status_code, 404)
        c.logout()


    def test_AddPcOption(self):
        """
        AddPcOption
        """
        c = self.client
        login_success = c.login(username='admin', password=self.password)
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
        login_success = c.login(username='admin', password=self.password)
        self.assertTrue(login_success)
        resp = c.get('/ajax/get_company_for_add_dep/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp['Content-Type'], 'application/json')
        c.logout()

        login_success = c.login(username='ferromet', password=self.password)
        self.assertTrue(login_success)
        response = c.get('/ajax/get_company_for_add_dep/')
        self.assertEqual(response.status_code, 404)
        c.logout()

    def test_GetDepartamentsForAddPCView(self):
        """
        GetDepartamentsForAddPCView
        """
        c = self.client
        login_success = c.login(username='admin', password=self.password)
        self.assertTrue(login_success)

        ferromet = Company.objects.get(com_user__username = 'ferromet')
        resp = c.get('/ajax/get_dep_list_for_add_pc/%s/' % (ferromet.id))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp['Content-Type'], 'application/json')

        resp = c.get('/ajax/get_dep_list_for_add_pc/999999/')
        self.assertEqual(resp.status_code, 404)
        c.logout()

        login_success = c.login(username='ferromet', password=self.password)
        self.assertTrue(login_success)
        response = c.get('/ajax/get_dep_list_for_add_pc/%s/' % (ferromet.id))
        self.assertEqual(response.status_code, 404)
        c.logout()

    def test_GetDepartamentsForDeplistView(self):
        """
        GetDepartamentsForDeplistView
        """
        c = self.client

        # тестируем на удачный логин
        login_success = c.login(username='admin', password=self.password)
        self.assertTrue(login_success)

        ferromet = Company.objects.get(com_user__username = 'ferromet')
        resp = c.get('/ajax/get_dep_list_for_dep_list/%s/' % (ferromet.id))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp['Content-Type'], 'application/json')

        resp = c.get('/ajax/get_dep_list_for_dep_list/999999/')
        self.assertEqual(resp.status_code, 404)
        c.logout()

        # тестируем на запрет для компаний
        login_success = c.login(username='ferromet', password=self.password)
        self.assertTrue(login_success)
        response = c.get('/ajax/get_dep_list_for_dep_list/%s/' % (ferromet.id))
        self.assertEqual(response.status_code, 404)
        c.logout()

    def test_AddDepartamentView(self):
        """
        AddDepartamentView
        """
        c = self.client

        # тестируем на удачный логин
        login_success = c.login(username='admin', password=self.password)
        self.assertTrue(login_success)

        # разрешение на вход
        resp2 = c.get('/add_dep/')
        self.assertEqual(resp2.status_code, 200)

        # отправка post запроса
        ferromet = Company.objects.get(com_user__username = 'ferromet')
        resp1 = c.post('/add_dep/', { 'company': ferromet , 'name': 'Отдел 1'})
        self.assertEqual(resp1.status_code, 200)
        c.logout()

        # тестируем на запрет для компаний
        login_success = c.login(username='ferromet', password=self.password)
        self.assertTrue(login_success)
        response = c.get('/ajax/get_dep_list_for_dep_list/%s/' % (ferromet.id))
        self.assertEqual(response.status_code, 404)
        c.logout()


    def test_GetPostsForQuestionAddView(self):
        """
        GetPostsForQuestionAddView
        """
        c = self.client

        # тестируем на удачный логин
        login_success = c.login(username='admin', password=self.password)
        self.assertTrue(login_success)

        # разрешение на вход
        ferromet = Company.objects.get(com_user__username = 'ferromet')
        resp2 = c.get('/ajax/get_posts_for_add_ques/%s/' % (ferromet.com_user.id))
        self.assertEqual(resp2.status_code, 200)
        self.assertEqual(resp2['Content-Type'], 'application/json')

        #если не находит такого юзера
        resp3 = c.get('/ajax/get_posts_for_add_ques/99999999/')
        self.assertEqual(resp3.status_code, 404)
        c.logout()

        login_success = c.login(username='ferromet', password=self.password)
        self.assertTrue(login_success)

        admin = User.objects.get(username = 'admin')
        resp4 = c.get('/ajax/get_posts_for_add_ques/%s/' % (admin.id))
        self.assertEqual(resp4.status_code, 200)
        self.assertEqual(resp4['Content-Type'], 'application/json')
        c.logout()


    def test_EditDepartamentView(self):
        """
        EditDepartamentView
        """
        c = self.client

        # тестируем на удачный логин
        login_success = c.login(username='admin', password=self.password)
        self.assertTrue(login_success)

        # разрешение на вход
        dep1 = Departments.objects.get(pk=1)
        url = reverse('edit_dep', args=[dep1.id])
        resp1 = c.get(url)
        self.assertEqual(resp1.status_code, 200)


        #если не находит такой компании
        url = reverse('edit_dep', args=[999999])
        resp2 = c.get(url)
        self.assertEqual(resp2.status_code, 404)
        c.logout()


        #заходим под пользователем компании
        login_success = c.login(username='ferromet', password=self.password)
        self.assertTrue(login_success)

        ferromet = Company.objects.get(com_user__username = 'ferromet')
        url = reverse('edit_dep', args=[ferromet.com_user.id])
        self.checkUrlToStatusGET(c, url, 404)
        c.logout()



    def checkUrlToStatusGET(self, client, url, status):
        """
        проверка урла запросом гет
        """
        response = client.get(url)
        self.assertEqual(response.status_code, status)

    def test_GetPcFromForAddQues(self):
        """
        GetPcFromForAddQues
        """
        c = self.client

        # тестируем на удачный логин
        login_success = c.login(username='admin', password=self.password)
        self.assertTrue(login_success)


        # разрешение на вход
        dep1 = Departments.objects.get(pk=1)
        url = reverse('ajax_GetPcFromForAddQues', args=[dep1.id])
        resp1 = c.get(url)
        self.checkUrlToStatusGET(c, url, 200)
        self.assertEqual(resp1['Content-Type'], 'application/json')


        #если не находит такой
        url = reverse('ajax_GetPcFromForAddQues', args=[999999])
        resp2 = c.get(url)
        self.checkUrlToStatusGET(c, url, 404)
        c.logout()

        #заходим под пользователем компании
        login_success = c.login(username='ferromet', password=self.password)
        self.assertTrue(login_success)

        dep1 = Departments.objects.get(pk=1)
        url = reverse('ajax_GetPcFromForAddQues', args=[dep1.id])
        self.checkUrlToStatusGET(c, url, 200)
        c.logout()


