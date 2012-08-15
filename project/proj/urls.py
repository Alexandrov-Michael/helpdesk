from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


from proj import settings
from ques import views
from company import views as vc
from profiles import views as vp
from wiki import views as vw

urlpatterns = patterns('',

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^admin_tools/', include('admin_tools.urls')),

    url(r'^tinymce/', include('tinymce.urls')),


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
    url(r'^add_companyadmins_for_user/(?P<pk>\d+)/$', vp.AddCompanyAdminsForUserView.as_view(), name='add_copmanyadmins_for_user'),
    url(r'^companyadmins_for_user/(?P<pk>\d+)/$', vp.CompanyAdminsForUserListView.as_view(), name='companyadmins_for_user'),
    url(r'^companyadmins_for_company/(?P<pk>\d+)/$', vp.CompanyAdminsForCompanyListView.as_view(), name='companyadmins_for_company'),
    url(r'^add_companyadmins_for_company/(?P<pk>\d+)/$', vp.AddCompanyAdminsForCompanyView.as_view(), name='add_companyadmins_for_company'),
    url(r'^chnage_user_to_for_ques/(?P<pk>\d+)/$',    views.ChangeUserToForQuestionView.as_view(), name='change_user_to_for_ques'),
    url(r'^departament_list/$',         vc.DepartamentsListView.as_view(), name='dep_list'),
    url(r'^edit_dep/(?P<pk>\d+)/$',     vc.EditDepartamentView.as_view(), name='edit_dep'),


    #### WIKI ####
    url(r'^wiki/$',                     vw.IndexWikiView.as_view(), name='wiki'),
    url(r'^add_page_wiki/$',            vw.AddArticleView.as_view(), name='add_page_wiki'),
    url(r'^read_page_wiki/(?P<pk>\d+)/$', vw.ReadArcticleView.as_view(), name='read_page_wiki'),
    url(r'^edit_page_wiki/(?P<pk>\d+)/$', vw.EditArticleView.as_view(), name='edit_page_wiki'),


    #### End WIKI ####


    #tehnikal
    url( r'^accounts/login/$',  'django.contrib.auth.views.login', { "template_name": "mylogin.html" } ),
    url( r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url': '/accounts/login/'} ),


    #ajax views
    url(r'^ajax/get_pc_from/$',                                     vc.GetPcFrom.as_view()),
    url(r'^ajax/get_ques/(?P<pk>\d+)/$',                            views.GetQuestionForChat.as_view()),
    url(r'^ajax/get_but/(?P<pk>\d+)/$',                             views.GetButtonForChat.as_view()),
    url(r'^ajax/get_chat_mess/(?P<pk>\d+)/$',                       views.GetChatMessages.as_view()),
    url(r'^ajax/get_index_ques/$',                                  views.QuestionList.as_view()),
    url(r'^ajax/get_company_for_pc_list/$',                         vc.GetCompanyForPcList.as_view(), name='ajax_GetCompanyForPcList'),
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
    url(r'^ajax/get_profile_src_img/(?P<pk>\d+)/$',                 vp.GetProfileImgView.as_view()),
    url(r'^ajax/get_company_for_add_dep/$',                         vc.GetCompanyForAddDepartametView.as_view()),
    url(r'^ajax/get_dep_list_for_dep_list/(?P<pk>\d+)/$',           vc.GetDepartamentsForDeplistView.as_view()),
    url(r'^ajax/get_dep_list_for_add_pc/(?P<pk>\d+)/$',             vc.GetDepartamentsForAddPCView.as_view()),
    url(r'^ajax/get_posts_for_add_ques/(?P<pk>\d+)/$',              vc.GetPostsForQuestionAddView.as_view()),
    url(r'^ajax/get_user_from_for_ques/(?P<pk>\d+)/$',              vc.GetPcFromForAddQues.as_view(), name='ajax_GetPcFromForAddQues'),


    #ajax type: POST
    url(r'^change_status/(?P<pk>\d+)/$', views.QuesChangeStatus.as_view()),



)


if not settings.HOSTER:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),


        #tests
        url('^test/$', vc.test.as_view(), name='test'),
    )