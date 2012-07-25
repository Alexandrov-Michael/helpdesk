from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


from proj import settings
from ques import views
from company import views as vc
from profiles import views as vp

urlpatterns = patterns('',

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^admin_tools/', include('admin_tools.urls')),


    #working
    url(r'^$',                          views.IndexView.as_view()),
    url(r'^add_q/$',                    views.QuesAdd.as_view(), name=u'add_q'),
    url(r'^chat/(?P<pk>\d+)/$',         views.QuesChatForm.as_view(), name = u'chat'),
    url(r'^pc_list/$',                  vc.PcList.as_view(), name = 'pc_list'),
    url(r'^pc_detail/(?P<pk>\d+)/$',    vc.PcDetail.as_view(), name='pc_detail'),
    url(r'^pc_history/(?P<pk>\d+)/$',   vc.PcOptionHistoryView.as_view()),
    url(r'^change_opt/(?P<pk>\d+)/$',   vc.ChangePcOption.as_view(), name='option_change'),
    url(r'^add_opt/(?P<pk>\d+)/$',      vc.AddPcOption.as_view(), name='add_option' ),
    url(r'^add_pc/$',                   vc.AddCompanyPcView.as_view(), name='add_pc'),
    url(r'^add_pc_option_for_all/(?P<pk>\d+)/$',    vc.AddPcOptionForAllView.as_view(), name='add_pc_option_for_all'),
    url(r'^report_ques/$',              views.MainReportForQuestionsView.as_view(), name='report_ques'),
    url(r'^report_pc_history/$',        views.MainReportForPcHistoryView.as_view(), name='report_pc_history'),
    url(r'^short_company_name/$',       vc.ShortCompanyNameListView.as_view(), name='short_company_name'),
    url(r'^add_dep/$',                  vc.AddDepartamentView.as_view(), name='add_dep'),
    url(r'^add_file_for_pc/(?P<pk>\d+)/$', vc.AddFileForPcView.as_view(), name='file_for_pc'),
    url(r'^add_user/$',                 vp.CreateUserView.as_view(), name='add_user'),
    url(r'^user_list/$',                vp.UserListView.as_view(), name='user_list'),
    url(r'^company_list/$',             vp.CompanyListView.as_view(), name='company_list'),
    url(r'^add_company/$',              vp.CreateCompanyView.as_view(), name='add_company'),


    #tehnikal
    url( r'^accounts/login/$',  'django.contrib.auth.views.login', { "template_name": "mylogin.html" } ),
    url( r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url': '/accounts/login/'} ),


    #ajax views
    url(r'^ajax/get_pc_from/$',                                     vc.GetPcFrom.as_view()),
    url(r'^ajax/get_user_to/$',                                     vc.GetUserTo.as_view()),
    url(r'^ajax/get_company_to/$',                                  vc.GetCompanyTo.as_view()),
    url(r'^ajax/get_ques/(?P<pk>\d+)/$',                            views.GetQuestionForChat.as_view()),
    url(r'^ajax/get_but/(?P<pk>\d+)/$',                             views.GetButtonForChat.as_view()),
    url(r'^ajax/get_chat_mess/(?P<pk>\d+)/$',                       views.GetChatMessages.as_view()),
    url(r'^ajax/get_index_ques/$',                                  views.QuestionList.as_view()),
    url(r'^ajax/get_company_for_pc_list/$',                         vc.GetCompanyForPcList.as_view()),
    url(r'^ajax/get_pc_for_list/(?P<company>\d+)/(?P<dep>\d+)/$',   vc.GetPcForPcList.as_view()),
    url(r'^ajax/get_options_for_add/(?P<pk>\d+)/$',                 vc.GetOptionsForAdd.as_view()),
    url(r'^ajax/get_company_for_pc_add/$',                          vc.GetCompanyForPcAddView.as_view()),
    url(r'^ajax/get_company_for_report_ques/$',                     views.GetCompanyListForReportForQuesView.as_view()),
    url(r'^ajax/get_users_for_report_ques/$',                       views.GetUserListForReportForQuesView.as_view()),
    url(r'^ajax/get_report_for_report_ques/(?P<company>\d+)/(?P<user>\d+)/$', views.GetReportListForReportForQuesView.as_view()),
    url(r'^ajax/get_pc_for_report_pc_history/(?P<company>\d+)/$',   views.GetPcListForReportPcHistoryView.as_view()),
    url(r'^ajax/get_company_for_report_pc_history/$',               views.GetCompanyListForReportForPcHistoryView.as_view()),
    url(r'^ajax/get_report_pc_history/(?P<pc>\d+)/(?P<user>\d+)/(?P<company>\d+)/$', views.GetReportForPcHistoryView.as_view()),
    url(r'^ajax/get_departament_for_pc_list/(?P<pk>\d+)/$',         vc.GetDepartamentForPcListView.as_view()),



    #ajax type: POST
    url(r'^change_status/(?P<pk>\d+)/$', views.QuesChangeStatus.as_view()),



    #tests
    url('^test/$', vc.test),
)


if not settings.HOSTER:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
    )