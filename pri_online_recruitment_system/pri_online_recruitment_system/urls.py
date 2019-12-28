"""pri_online_recruitment_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from pors_app import views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('pri_administrator/login/', views.pri_user_login, name="user_login"),
    path('pri_administrator/logout/', auth_views.LogoutView.as_view(), name="logout"),

    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


    #FOR APPLICANT SIDE
    path('pri/applicant_side/account/registration', views.pri_applicant_account_registration_page, name='applicant_side_account_registration'),
    path('pri/applicant_side/registration/<str:slug>/', views.pri_applicant_registration_page, name='applicant_side_registration'),
    path('pri/applicant_side/update/profile/<str:slug>/', views.pri_applicant_edit_profile_page, name='applicant_side_update_profile'),
    
    path('pri/applicant_side/job/posts/all/', views.PRIApplicantSideJobPostPageAll.as_view(), name='applicant_side_job_posts_all'),
    path('pri/applicant_side/job/posts/recommended/', views.PRIApplicantSideJobPostPageRecommended.as_view(), name='applicant_side_job_posts_recommended'),
    path('pri/applicant_side/job/posts/search/results/', views.PRIApplicantSideJobPostSearchPage, name='applicant_side_job_posts_search'),
    path('pri/applicant_side/job/posts/category/filter/results/', views.PRIApplicantSideFilterCategoryPage, name='applicant_side_job_category_filter'),

    path('pri/applicant_side/job/posts/request/<int:jv_id>/<int:a_id>/', views.pri_applicant_job_request, name='applicant_side_job_request'),
    path('pri/applicant_side/job/applicant/request/status/ongoing/<int:id>/', views.pri_applicant_job_request_ongoing_status, name='applicant_side_job_request_ongoing_status'),
    path('pri/applicant_side/job/applicant/request/cancel/', views.pri_applicant_job_request_cancel, name='applicant_side_job_request_cancel'),
    path('pri/applicant_side/job/applicant/hired/<int:id>/', views.pri_applicant_job_hired, name='applicant_side_job_hired'),

    #Client Side
    path('pri/client_side/home/', views.PRIClientHomePage.as_view(), name='client_side_home_page'),
    path('pri/client_side/create/request/', views.pri_client_side_create_requests, name='client_side_create_request'),
    path('pri/client_side/edit/request/<int:id>/', views.pri_client_side_edit_requests, name='client_side_edit_request'),
    path('pri/client_side/delete/request/<int:id>/', views.pri_client_side_delete_requests, name='client_side_delete_request'),
    path('pri/client_side/hired/applicants/', views.PRIClientHiredApplicantPage.as_view(), name='client_side_hired_applicants_page'),
    path('pri/client_side/fire/hired/applicants/<int:id>/', views.pri_client_delete_applicants, name='client_side_fire_hired_applicants'),

    
    path('export/csv/', views.export_users_csv, name="export_users_csv"),
    path('export/xls/', views.export_users_xls, name="export_users_xls"),
    path('export/xlsx/', views.export_users_xlsx, name="export_users_xlsx"),

    # Reports
    path('export/report/xlsx/applicants/', views.export_report_xlsx_applicants, name="export_report_xlsx_applicants"),
    path('export/report/xlsx/applying/applicants/', views.export_report_xlsx_applying_applicants, name="export_report_xlsx_applying_applicants"),
    path('export/report/xlsx/job/vacancy/', views.export_report_xlsx_job_vacants, name="export_report_xlsx_job_vacancy"),
    path('export/report/xlsx/client/requests/', views.export_report_xlsx_client_requests, name="export_report_xlsx_client_requests"),
    path('export/report/xlsx/hired/applicants/', views.export_report_xlsx_hired_applicants, name="export_report_xlsx_hired_applicants"),
    path('export/report/xlsx/clients/', views.export_report_xlsx_clients, name="export_report_xlsx_clients"),
    path('export/report/xlsx/users/', views.export_report_xlsx_current_users, name="export_report_xlsx_users"),

    path('', include('pors_app.urls')),
    path('admin/', admin.site.urls),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#use to access files and images in static
