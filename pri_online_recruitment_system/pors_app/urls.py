from django.urls import path
from . import views

app_name = "pri"

urlpatterns = [
    path('', views.PriAdminDashboard.as_view(), name='dashboard'),
    path('administrator/', views.PriAdmin.as_view(), name='admin'),
    path('administrator/user/policy/<int:id>/', views.pri_admin_apply_policy, name='admin_user_apply_policy'),
    path('client/', views.PriClients.as_view(), name='client'),
    path('client/hired/', views.PriHired.as_view(), name='hired'),
    path('client/jobs/', views.PriJobs.as_view(), name='jobs'),
    path('client/schedules/', views.PriSchedules.as_view(), name='schedules'),
    path('client/requests/', views.PriRequest.as_view(), name='requests'),    
    path('applicants/', views.PriApplicants.as_view(), name='applicants'),
    path('applicants/application_form/', views.PriApplicationForm.as_view(), name='application_form'),
    path('applicants/examination/', views.PriExamninations.as_view(), name='examination'),

    #Pri Admin Users

    path('admin/user/sort_admin/', views.pri_admin_users_sort_records, name='sort_admin'),
    path('admin/user/record_limit_admin/', views.pri_admin_users_record_limiter, name="record_limit_admin"),
    path('admin/user/search_admin/', views.pri_admin_users_search_filter, name="search_admin"),
    path('admin/user/paging_admin/', views.pri_admin_users_paging, name="paging_admin"),

    path('admin/user/create/account/', views.pri_admin_users_create_account_form, name="create_account_admin"),
    path('admin/update/profile/<int:id>/', views.pri_admin_update_profile, name='admin_update_profile'),
    path('admin/delete/profile/<int:id>/', views.pri_admin_users_delete_form, name='delete_account_admin'),

    #PRI Admin Clients
    path('admin/clients/create/client/', views.pri_admin_create_clients, name="create_clients"),
    path('admin/clients/edit/client/<int:id>/', views.pri_admin_edit_clients, name="edit_clients"),
    path('admin/clients/delete/client/<int:id>/', views.pri_admin_delete_clients, name="delete_clients"),

    path('admin/clients/sort_clients/', views.pri_admin_client_sort_records, name='sort_clients'),
    path('admin/clients/record_limit_clients/', views.pri_admin_client_record_limiter, name="record_limit_clients"),
    path('admin/clients/search_clients/', views.pri_admin_client_search_filter, name="search_clients"),
    path('admin/clients/paging_clients/', views.pri_admin_client_paging, name="paging_clients"),

    path('client/applicants/<int:id>/', views.pri_admin_client_show_applicants, name='client_applicants'),
    path('client/applicants/delete/<int:id>/<int:aid>/', views.pri_admin_client_delete_applicants, name='delete_client_applicants'),
    # Client hired applicant set status
    path('client/applicants/set/status/<int:id>/', views.pri_admin_client_hired_applicant_set_status, name='client_hired_applicant_set_status'),

    #PRI Admin Request
    path('admin/requests/create/requests/', views.pri_admin_create_requests, name="create_requests"),
    path('admin/requests/edit/requests/<int:id>/', views.pri_admin_edit_requests, name="edit_requests"),
    path('admin/requests/delete/requests/<int:id>/', views.pri_admin_delete_requests, name="delete_requests"),
    path('admin/requests/view/requests/<int:id>/', views.pri_admin_view_requests, name="view_requests"),

    path('admin/requests/sort_requests/', views.pri_admin_requests_sort_records, name='sort_requests'),
    path('admin/requests/record_limit_requests/', views.pri_admin_requests_record_limiter, name="record_limit_requests"),
    path('admin/requests/search_requests/', views.pri_admin_requests_search_filter, name="search_requests"),
    path('admin/requests/paging_requests/', views.pri_admin_requests_paging, name="paging_requests"),

    #PRI Admin Jobs
    path('admin/jobs/create/jobs/<int:id>/', views.pri_admin_create_jobs, name="create_jobs"),
    path('admin/jobs/edit/jobs/<int:id>/', views.pri_admin_edit_jobs, name="edit_jobs"),
    path('admin/jobs/delete/jobs/<int:id>/', views.pri_admin_delete_jobs, name="delete_jobs"),
    # path('admin/jobs/delete/jobs/<int:id>/', views.pri_admin_delete_jobs, name="delete_jobs"),
    path('admin/jobs/show/details/<str:key>/', views.pri_admin_job_details, name="show_job_details"),


    path('admin/jobs/sort_jobs/', views.pri_admin_jobs_sort_records, name='sort_jobs'),
    path('admin/jobs/record_limit_jobs/', views.pri_admin_jobs_record_limiter, name="record_limit_jobs"),
    path('admin/jobs/search_jobs/', views.pri_admin_jobs_search_filter, name="search_jobs"),
    path('admin/jobs/paging_jobs/', views.pri_admin_jobs_paging, name="paging_jobs"),

    path('admin/jobs/applicant/<str:key>/', views.PriJobsApplicantsRequests.as_view(), name="applicant_request_jobs"),
    path('admin/jobs/applicant/profile/view/<int:id>/<str:akey>/', views.pri_applicant_profile_view, name="applicant_profile_viewer"),

    #toggle exam
    path('admin/jobs/applicant/exam/<str:key>/<int:id>/', views.pri_jobs_applicant_requests_toggle_exam, name="applicant_request_jobs_toggle_exams"),
    #schedules
    path('admin/jobs/applicant/interview/schedule/<str:key>/<int:id>/', views.pri_jobs_applicant_requests_set_interview_sched, name="applicant_request_jobs_set_interview_sched"),

    #PRI Schedules
    path('admin/schedules/job/request/applicant/toggleexam/<int:id>/', views.pri_schedules_toggle_exam, name="toggle_exams"),

    #PRI Applicants
    path('admin/applicants/registered/delete/<str:key>/', views.pri_admin_delete_applicants, name="applicant_delete_record"),

    path('admin/applicants/job/request/exam/list/<str:key>/<int:id>/', views.PRIApplicantExamListPage.as_view(), name="applicant_exam_list"),
    path('admin/applicants/job/request/exam/test1/pre_employment/<str:key>/<int:id>/', views.pri_applicant_test1_pre_employment, name="applicant_exam_test1"),
    path('admin/applicants/job/request/exam/test2/simple_english/<str:key>/<int:id>/', views.pri_applicant_test2_simple_english, name="applicant_exam_test2"),
    path('admin/applicants/job/request/exam/test3/essay/<str:key>/<int:id>/', views.pri_applicant_test3_essay, name="applicant_exam_test3"),
    path('admin/applicants/job/request/exam/test3/sct/<str:key>/<int:id>/', views.pri_applicant_test3_sct, name="applicant_exam_test3_sct"),
    path('admin/applicants/job/request/exam/test4/abstract_reasoning/<str:key>/<int:id>/', views.pri_applicant_test4_abstract_reasoning, name="applicant_exam_test4"),
    path('admin/applicants/job/request/exam/ssct/<str:key>/<int:id>/', views.pri_applicant_exam_ssct, name="applicant_exam_scct"),
    path('admin/applicants/job/request/exam/ccat/<str:key>/<int:id>/', views.pri_applicant_exam_ccat, name="applicant_exam_ccat"),
    path('admin/applicants/job/request/exam/arp/<str:key>/<int:id>/', views.pri_applicant_exam_arp, name="applicant_exam_arp"),
    #PRI Applicant Examination Review

    path('admin/applicants/job/request/exam/review/test3/essay/<str:key>/<int:id>/', views.pri_applicant_test3_essay_review, name="applicant_exam_test3_review"),
    path('admin/applicants/job/request/exam/review/test3/t3ptsct/<str:key>/<int:id>/', views.pri_applicant_test3_ptsct_review, name="applicant_exam_test3_t3ptsct_review"),
    path('admin/applicants/job/request/exam/review/ccat/<str:key>/<int:id>/', views.pri_applicant_test_ccat_review, name="applicant_exam_ccat_review"),
    path('admin/applicants/job/request/exam/review/arp/<str:key>/<int:id>/', views.pri_applicant_test_arp_review, name="applicant_exam_arp_review"),
    path('admin/applicants/job/request/exam/review/scct/<str:key>/<int:id>/', views.pri_applicant_test_scct_review, name="applicant_exam_scct_review"),

    path('admin/applicants/job/request/exam/review/test1/<str:key>/<int:id>/', views.pri_applicant_test1_review, name="applicant_exam_test1_review"),
    path('admin/applicants/job/request/exam/review/test2/<str:key>/<int:id>/', views.pri_applicant_test2_review, name="applicant_exam_test2_review"),
    path('admin/applicants/job/request/exam/review/test4/<str:key>/<int:id>/', views.pri_applicant_test4_review, name="applicant_exam_test4_review"),

    

]
