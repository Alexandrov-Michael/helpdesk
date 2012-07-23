# -*- coding:utf-8 -*-
__author__ = 'michael'
from company.models import Company, CompanyPC, Posts, CompanyAdmins, PcOptions, PcOptionsList, Departments
from profiles.models import Profile
from django.contrib.auth.models import User, Group
from proj import settings
from random import randrange

def run():

    mypass = u'user12345'

    admin = User.objects.get(pk=1)
    admin_profile = Profile(user=admin, is_report=True, telefon = '+1222333')
    admin_profile.save()


    alexandrov = User(username = u'alexandrov', first_name = u'Михаил', last_name = u'Александров' )
    alexandrov.set_password(mypass)
    alexandrov.email = 'al@ferromet.ru'
    alexandrov.save()

    alexandrov_profile = Profile(user=alexandrov, is_report = True, is_company=False, telefon='+7-911-234-44-55')
    alexandrov_profile.save()


    ivanov = User(username = u'ivanov', first_name = u'Сергей', last_name = u'Иванов' )
    ivanov.set_password(mypass)
    ivanov.save()


    ivanov_profile = Profile(user=ivanov, is_company=False, telefon ='+7-921-355-34-34')
    ivanov_profile.save()

    petrov = User(username = u'petrov', first_name = u'Павел', last_name = u'Петров' )
    petrov.set_password(mypass)
    petrov.save()

    petrov_profile = Profile(user=petrov, is_company=False, telefon= '+7-904-122-12-12')
    petrov_profile.save()


    maslov = User(username= 'maslov', first_name = u'Алексей', last_name = u'Маслов')
    maslov.set_password('megapass123')
    maslov.save()

    maslov_profile = Profile(user=maslov, is_company=False, telefon='+7-812-211-44-44')
    maslov_profile.save()







    usersList = [ alexandrov, ivanov, petrov, maslov]

    ferromet = User(username = u'ferromet', first_name = u'ООО ФЕРРОМЕТ')
    ferromet.set_password(mypass)
    ferromet.save()

    intersteel = User(username = u'intersteel', first_name = u'ООО ИНТЕРСТАЛЬ' )
    intersteel.set_password(mypass)
    intersteel.save()

    rbk = User(username = u'rbk', first_name = u'ООО РБК' )
    rbk.set_password(mypass)
    rbk.save()

    sevsap = User(username = u'sevzap', first_name = u'ООО СЕВЗАП')
    sevsap.set_password(mypass)
    sevsap.save()

    test = User(username='test', first_name = u'ООО Приборы')
    test.set_password('test12345')
    test.save()

    Profile(user=ferromet).save()
    Profile(user=intersteel).save()
    Profile(user=rbk).save()
    Profile(user=sevsap).save()
    Profile(user=test).save()



    companyUserList = [ferromet, intersteel, rbk, sevsap, test]


    com_ferromet = Company( com_user = ferromet)
    com_ferromet.save()

    com_interseel = Company( com_user = intersteel)
    com_interseel.save()

    com_rbk = Company( com_user = rbk)
    com_rbk.save()

    com_sevsap = Company( com_user = sevsap)
    com_sevsap.save()

    com_test = Company(com_user = test)
    com_test.save()


    main_dep = Departments(name = u'Основной')
    main_dep.save()
    buh_dep = Departments(name = u'Бухгалтерия')
    buh_dep.save()
    dir_dep = Departments(name = u'Директорат')
    dir_dep.save()
    fin_dep = Departments(name = u'Финансисты')
    fin_dep.save()


    dep_list = [
        main_dep,
        buh_dep,
        dir_dep,
        fin_dep,
    ]

    companyList = [
        com_ferromet,
        com_interseel,
        com_rbk,
        com_sevsap,
        com_test
    ]


    alfavitList = ['a', 'b', 'z', 'r', 'e', 'y', 't', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'j', 'o', 'p', 'm']



    kurator = Posts(name=u'Куратор', decription=u'По главным вопросам')
    kurator.save()

    gelezo = Posts(name=u'Железо', decription=u'По вопросам железа')
    gelezo.save()

    admin1c = Posts(name=u'1с', decription=u'По вопросам 1c')
    admin1c.save()

    access = Posts(name=u'Аксес', decription=u'По вопросам Access')
    access.save()



    postsList = [kurator, gelezo, admin1c, access]

    for i in range(0,20):
        CompanyAdmins(username=usersList[randrange(0, len(usersList))], company=companyList[randrange(0,len(companyList))], post=postsList[randrange(0, len(postsList))]).save()

    CompanyAdmins(username=alexandrov, company = com_ferromet, post = kurator).save()


    proccesor   = PcOptions(name = u'Процессор')
    proccesor.save()
    video       = PcOptions(name = u'Видеокарта')
    video.save()
    hard        = PcOptions(name = u'Жесткий диск')
    hard.save()





    host_names_list = ['server', 'buh', 'manager', 'mail', 'secretary']


    for i in range(0, 30):
        com = randrange(0, len(companyList))
        CompanyPC(
            company = companyList[com],
            pc_nameId = i,
            pc_name = u'%s %s' % (companyList[com], host_names_list[randrange(0, len(host_names_list))]),
            departament = dep_list[randrange(0, len(dep_list))],
        ).save()




    option_list = PcOptions.objects.all()
    pc_list = CompanyPC.objects.all()

    for one_pc in pc_list:
        for one_option in option_list:
            PcOptionsList(pc = one_pc, option=one_option, body=alfavitList[randrange(0, len(alfavitList))]).save()