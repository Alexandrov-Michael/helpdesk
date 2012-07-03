# -*- coding:utf-8 -*-
__author__ = 'michael'
from company.models import Company, CompanyPC, Posts, CompanyAdmins, PcOptions, PcOptionsList
from django.contrib.auth.models import User, Group
from proj import settings
from random import randrange

def run():

    group, created = Group.objects.get_or_create(name = settings.COMPANY_GROUP_NAME)
    mypass = u'123'

    reports_group, created = Group.objects.get_or_create(name = settings.GROUP_REPORT_ADMIN)

    alexandrov = User(username = u'alexandrov', first_name = u'Михаил', last_name = u'Александров' )
    alexandrov.set_password(mypass)
    alexandrov.save()
    alexandrov.groups.add(reports_group)

    ivanov = User(username = u'ivanov', first_name = u'Сергей', last_name = u'Иванов' )
    ivanov.set_password(mypass)
    ivanov.save()

    petrov = User(username = u'petrov', first_name = u'Павел', last_name = u'Петров' )
    petrov.set_password(mypass)
    petrov.save()

    sidorov = User(username = u'sidorov', first_name = u'Иван', last_name = u'Сидоров')
    sidorov.set_password(mypass)
    sidorov.save()

    panev = User(username = u'panev', first_name = u'Александр', last_name = u'Панев')
    panev.set_password(mypass)
    panev.save()

    maslov = User(username= 'maslov', first_name = u'Алексей', last_name = u'Маслов')
    maslov.set_password('megapass123')
    maslov.save()

    usersList = [ alexandrov, ivanov, petrov, sidorov, panev, maslov]

    ferromet = User(username = u'ferromet', first_name = u'ООО ФЕРРОМЕТ')
    ferromet.set_password(mypass)
    ferromet.save()
    ferromet.groups.add(group)

    intersteel = User(username = u'intersteel', first_name = u'ООО ИНТЕРСТАЛЬ' )
    intersteel.set_password(mypass)
    intersteel.save()
    intersteel.groups.add(group)

    rbk = User(username = u'rbk', first_name = u'ООО РБК' )
    rbk.set_password(mypass)
    rbk.save()
    rbk.groups.add(group)

    sevsap = User(username = u'sevzap', first_name = u'ООО СЕВЗАП')
    sevsap.set_password(mypass)
    sevsap.save()
    sevsap.groups.add(group)



    companyUserList = [ferromet, intersteel, rbk, sevsap,]


    com_ferromet = Company( com_user = ferromet)
    com_ferromet.save()

    com_interseel = Company( com_user = intersteel)
    com_interseel.save()

    com_rbk = Company(com_user = rbk)
    com_rbk.save()

    com_sevsap = Company( com_user = sevsap)
    com_sevsap.save()


    companyList = [
        com_ferromet,
        com_interseel,
        com_rbk,
        com_sevsap
    ]


    alfavitList = ['a', 'b', 'z', 'r', 'e', 'y', 't', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'j', 'o', 'p', 'm']



    kurator = Posts(name=u'Куратор')
    kurator.save()

    gelezo = Posts(name=u'Железо')
    gelezo.save()

    admin1c = Posts(name=u'1с')
    admin1c.save()

    access = Posts(name=u'Аксес')
    access.save()



    postsList = [kurator, gelezo, admin1c, access]

    for i in range(0,20):
            CompanyAdmins(username=usersList[randrange(0, len(usersList))], company=companyList[randrange(0,len(companyList))], post=postsList[randrange(0, len(postsList))]).save()


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
            pc_name = u'%s %s' % (companyList[com], host_names_list[randrange(0, len(host_names_list))] )
        ).save()




    option_list = PcOptions.objects.all()
    pc_list = CompanyPC.objects.all()

    for one_pc in pc_list:
        for one_option in option_list:
            PcOptionsList(pc = one_pc, option=one_option, body=alfavitList[randrange(0, len(alfavitList))]).save()