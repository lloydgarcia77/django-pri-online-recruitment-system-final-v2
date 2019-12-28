from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import PRIUserInfo, PRIUserPermission, PRIClientsInfo, PRIRequestInfo, PRIJobVacancyInfo, PRIJobVacancyJobQualificationsInfo, PRIJobVacancyJobResponsibilitiesInfo, ExaminationInfo, QuestionInfo, ChoicesInfo, PRIApplicantProfileInfo, PRIApplicantSibilingsInfo, PRIApplicantEmploymentHistoryInfo, PRIApplicantEducationalAttainmentInfo, PRIApplicantTrainingsInfo, PRIApplicantCharacterReferencesInfo, PRIApplicantJobRequestInfo, PRIApplicantJobHiredInfo, PRIApplicantTest3EssayInfo, PRIApplicantTestSSCTInfo, PRIApplicantTest3SCTInfo, PRIApplicantExamScoreT1PEInfo, PRIApplicantExamScoreT2SEInfo, PRIApplicantExamScoreT3EInfo, PRIApplicantExamScoreT3PTSCTInfo, PRIApplicantExamScoreT4ARInfo, PRIApplicantExamScoreCCAInfo, PRIApplicantExamScoreARPInfo, PRIApplicantExamScoreSCCTInfo, PRIApplicantTestCCATInfo, PRIApplicantTestARPInfo
# Register your models here.


admin.site.site_header = "PRI Super Administrator"
admin.site.index_title = "PRI Super Administrator Page"
admin.site.site_title = "Administrator Panel"


class PRIUserAdmin(ImportExportModelAdmin):
    list_display = ('id', 'user', 'first_name', 'middle_name', 'last_name', 'age', 'gender',
                    'contact', 'address', 'position', 'department', 'image', 'level', 'date_added')
    list_editable = ('first_name', 'middle_name', 'last_name', 'age', 'gender',
                     'contact', 'address', 'position', 'department', 'image', 'level')
    list_per_page = 10
    search_fields = ('first_name', 'middle_name', 'last_name', 'age', 'gender',
                     'contact', 'address', 'position', 'department', 'level', 'date_added')
    list_filter = ('first_name', 'middle_name', 'last_name',
                   'gender', 'position', 'department', 'level')


admin.site.register(PRIUserInfo, PRIUserAdmin)


class PRIUserPermissionAdmin(ImportExportModelAdmin):
    list_display = ('id', 'pri_user',  
                    'pri_can_view_clients_page',
                    'pri_can_add_clients',
                    'pri_can_hired_clients',
                    'pri_can_edit_clients',
                    'pri_can_delete_clients', 
                    'pri_can_view_request_page',
                    'pri_can_add_request',
                    'pri_can_create_job_request',
                    'pri_can_view_request',
                    'pri_can_edit_request',
                    'pri_can_delete_request', 
                    'pri_can_view_job_vacancy_page',
                    'pri_can_view_job_vacancy_applicants',
                    'pri_can_edit_job_vacancy',
                    'pri_can_delete_job_vacancy', 
                    'pri_can_view_applicants_page',
                    'pri_can_delete_applicants', )
    list_editable = (
                    'pri_can_view_clients_page',
                    'pri_can_add_clients',
                    'pri_can_hired_clients',
                    'pri_can_edit_clients',
                    'pri_can_delete_clients', 
                    'pri_can_view_request_page',
                    'pri_can_add_request',
                    'pri_can_create_job_request',
                    'pri_can_view_request',
                    'pri_can_edit_request',
                    'pri_can_delete_request', 
                    'pri_can_view_job_vacancy_page',
                    'pri_can_view_job_vacancy_applicants',
                    'pri_can_edit_job_vacancy',
                    'pri_can_delete_job_vacancy', 
                    'pri_can_view_applicants_page',
                    'pri_can_delete_applicants', )
    list_per_page = 10


admin.site.register(PRIUserPermission, PRIUserPermissionAdmin)


class PRIClientAdmin(ImportExportModelAdmin):
    list_display = ('id', 'client_user', 'client_company_name', 'client_company_logo',
                    'client_location', 'contact_person', 'contact_mobile_no')
    list_editable = ('client_company_name', 'client_company_logo',
                     'client_location', 'contact_person', 'contact_mobile_no')
    list_per_page = 10
    search_fields = ('client_company_name', 'client_location',
                     'contact_person', 'contact_mobile_no')
    list_filter = ('client_location', 'contact_person', 'contact_mobile_no')


admin.site.register(PRIClientsInfo, PRIClientAdmin)


class PRIRequestAdmin(ImportExportModelAdmin):
    list_display = ('id', 'requested_client', 'status',
                    'content', 'data_requested', 'seen_by_admin')
    list_editable = ('status', 'content', 'seen_by_admin')
    list_per_page = 10
    search_fields = ('status', 'content', )
    list_filter = ('status', 'content', )


admin.site.register(PRIRequestInfo, PRIRequestAdmin)


class PRIJobVacancyAdmin(ImportExportModelAdmin):
    list_display = ('id', 'secure_id', 'client_request', 'job_title', 'job_category', 'job_specialization',
                    'job_minimum_experience', 'job_salary', 'job_deadline', 'job_company_overview', 'job_description')
    list_editable = ('job_title', 'job_category', 'job_specialization', 'job_minimum_experience',
                     'job_salary', 'job_deadline', 'job_company_overview', 'job_description')
    list_per_page = 10
    search_fields = ('job_title', 'job_category', 'job_specialization', 'job_minimum_experience',
                     'job_salary', 'job_deadline', 'job_company_overview', 'job_description', )
    list_filter = ('job_title', 'job_category', 'job_specialization',
                   'job_minimum_experience', 'job_salary', )


admin.site.register(PRIJobVacancyInfo, PRIJobVacancyAdmin)


class PRIJobVacancyJobQualificationsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'job_vacancy_jq', 'job_qualifications', )
    list_editable = ('job_qualifications', )
    list_per_page = 10
    search_fields = ('job_qualifications', )
    list_filter = ('job_qualifications', )


admin.site.register(PRIJobVacancyJobQualificationsInfo,
                    PRIJobVacancyJobQualificationsAdmin)


class PRIJobVacancyJobResponsibilitiesAdmin(ImportExportModelAdmin):
    list_display = ('id', 'job_vacancy_jr', 'job_responsibilities',)
    list_editable = ('job_responsibilities', )
    list_per_page = 10
    search_fields = ('job_responsibilities', )
    list_filter = ('job_responsibilities', )


admin.site.register(PRIJobVacancyJobResponsibilitiesInfo,
                    PRIJobVacancyJobResponsibilitiesAdmin)


class ExaminationAdmin(ImportExportModelAdmin):
    list_display = ('id', 'exam_type',)
    list_editable = ('exam_type',)
    list_per_page = 10
    search_fields = ('exam_type',)
    # list_filter = ()


admin.site.register(ExaminationInfo, ExaminationAdmin)


class QuestionAdmin(ImportExportModelAdmin):
    list_display = ('id', 'examination', 'question')
    list_editable = ('question', )
    list_per_page = 10
    search_fields = ('question', )
    list_filter = ()


admin.site.register(QuestionInfo, QuestionAdmin)


class ChoicesAdmin(ImportExportModelAdmin):
    list_display = ('id', 'question', 'choice')
    list_editable = ('choice', )
    list_per_page = 10
    search_fields = ('choice',)
    list_filter = ()


admin.site.register(ChoicesInfo, ChoicesAdmin)

# For applicant admin


class PRIApplicantProfileAdmin(ImportExportModelAdmin):
    list_display = ('id', 'secure_key_id', 'user',
                    'image',
                    'cv',
                    'date_filled',
                    'position_desired',
                    'company_assigned',
                    'erp_question',
                    'fname',
                    'mname',
                    'lname',
                    'mobile_no',
                    'telephone_no',
                    'gender',
                    'contact_person',
                    'relationship',
                    'contact_person_mobile_no',
                    'bldg_name_0',
                    'brgy_sub_0',
                    'dis_mun_0',
                    'cit_pro_0',
                    'bldg_name_1',
                    'brgy_sub_1',
                    'dis_mun_1',
                    'cit_pro_1',
                    'civil_status',
                    'weight',
                    'height',
                    'shirt_size',
                    'shoe_size',
                    'waistline',
                    'length_of_pants',
                    'sss',
                    'ctc',
                    'philhealth',
                    'tin',
                    'pagibig',
                    'spouse_full_name',
                    'spouse_contact_number',
                    'father_full_name',
                    'father_occupation',
                    'father_home_address',
                    'mother_full_name',
                    'mother_occupation',
                    'mother_home_address',
                    'question1',
                    'question2',
                    'question3',
                    'question4',
                    'slug',
                    )
    list_editable = (
        'image',
        'cv',
        'position_desired',
        'company_assigned',
        'erp_question',
        'fname',
        'mname',
        'lname',
        'mobile_no',
        'telephone_no',
        'gender',
        'contact_person',
        'relationship',
        'contact_person_mobile_no',
        'bldg_name_0',
        'brgy_sub_0',
        'dis_mun_0',
        'cit_pro_0',
        'bldg_name_1',
        'brgy_sub_1',
        'dis_mun_1',
        'cit_pro_1',
        'civil_status',
        'weight',
        'height',
        'shirt_size',
        'shoe_size',
        'waistline',
        'length_of_pants',
        'sss',
        'ctc',
        'philhealth',
        'tin',
        'pagibig',
        'spouse_full_name',
        'spouse_contact_number',
        'father_full_name',
        'father_occupation',
        'father_home_address',
        'mother_full_name',
        'mother_occupation',
        'mother_home_address',
        'question1',
        'question2',
        'question3',
        'question4',
    )
    list_per_page = 10
    search_fields = (
        'position_desired',
        'company_assigned',
        'fname',
        'mname',
        'lname',
        'bldg_name_0',
        'brgy_sub_0',
        'dis_mun_0',
        'cit_pro_0',
        'bldg_name_1',
        'brgy_sub_1',
        'dis_mun_1',
        'cit_pro_1',
        'civil_status',
    )
    list_filter = (
        'position_desired',
        'company_assigned',
        'civil_status',
    )


admin.site.register(PRIApplicantProfileInfo, PRIApplicantProfileAdmin)


class PRIApplicantSibilingsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'applicant_siblings', 'name', 'age', 'occ',)
    list_editable = ('name', 'age', 'occ',)
    list_per_page = 10
    search_fields = ('name', 'occ', )
    list_filter = ('occ', )


admin.site.register(PRIApplicantSibilingsInfo, PRIApplicantSibilingsAdmin)


class PRIApplicantEmploymentHistoryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'applicant_employment_history', 'date_from', 'date_to',
                    'company', 'position', 'reason_for_leaving', 'basic_salary_pay')
    list_editable = ('date_from', 'date_to', 'company',
                     'position', 'reason_for_leaving', 'basic_salary_pay')
    list_per_page = 10
    search_fields = ('company', 'position',
                     'reason_for_leaving', 'basic_salary_pay')
    list_filter = ('company', 'position', )


admin.site.register(PRIApplicantEmploymentHistoryInfo,
                    PRIApplicantEmploymentHistoryAdmin)


class PRIApplicantEducationalAttainmentAdmin(ImportExportModelAdmin):
    list_display = ('id', 'applicant_educational_attainment',
                    'college',
                    'college_course',
                    'college_address',
                    'csya_from',
                    'csya_to',
                    'vocational',
                    'vocational_course',
                    'vocational_address',
                    'vsya_from',
                    'vsya_to',
                    'highschool',
                    'highschool_address',
                    'hsya_from',
                    'hsya_to',
                    'elementary',
                    'elementary_address',
                    'esya_from',
                    'esya_to',
                    'special_skills',
                    'language_speak',
                    )
    list_editable = ('college',
                     'college_course',
                     'college_address',
                     'csya_from',
                     'csya_to',
                     'vocational',
                     'vocational_course',
                     'vocational_address',
                     'vsya_from',
                     'vsya_to',
                     'highschool',
                     'highschool_address',
                     'hsya_from',
                     'hsya_to',
                     'elementary',
                     'elementary_address',
                     'esya_from',
                     'esya_to',
                     'special_skills',
                     'language_speak',
                     )
    list_per_page = 10
    search_fields = ('college',
                     'college_course',
                     'college_address',
                     'vocational',
                     'vocational_course',
                     'vocational_address',
                     'highschool',
                     'highschool_address',
                     'elementary',
                     'elementary_address',
                     'special_skills',
                     'language_speak',)
    list_filter = ('college',
                   'college_course',
                   'vocational',
                   'vocational_course',
                   'highschool',
                   'elementary',
                   'special_skills',
                   'language_speak', )


admin.site.register(PRIApplicantEducationalAttainmentInfo,
                    PRIApplicantEducationalAttainmentAdmin)


class PRIApplicantTrainingsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'applicant_trainings', 'title', 'date_attended')
    list_editable = ('title', 'date_attended', )
    list_per_page = 10
    search_fields = ('title', 'date_attended', )
    list_filter = ('title', )


admin.site.register(PRIApplicantTrainingsInfo, PRIApplicantTrainingsAdmin)


class PRIApplicantCharacterReferencesAdmin(ImportExportModelAdmin):
    list_display = ('id', 'applicant_character_references',
                    'full_name', 'occupation', 'contact_no')
    list_editable = ('full_name', 'occupation', 'contact_no', )
    list_per_page = 10
    search_fields = ('full_name', 'occupation', 'contact_no')
    list_filter = ('full_name', 'occupation', )


admin.site.register(PRIApplicantCharacterReferencesInfo,
                    PRIApplicantCharacterReferencesAdmin)


class PRIApplicantJobRequestAdmin(ImportExportModelAdmin):
    list_display = ('id', 'job_vacancy_applied',
                    'applying_applicant', 'take_exam', 'date_applied', 'interview_date')
    list_editable = ( 'take_exam', 'interview_date')
    list_per_page = 10
    search_fields = ('id', 'job_vacancy_applied',
                     'applying_applicant', 'date_applied')
    list_filter = ('job_vacancy_applied', 'date_applied')


admin.site.register(PRIApplicantJobRequestInfo, PRIApplicantJobRequestAdmin)


class PRIApplicantJobHiredAdmin(ImportExportModelAdmin):
    list_display = ('id', 'applicant_id','company_name', 'hired_applicant', 'status','date_hired')
    list_editable = ('applicant_id','status',)
    list_per_page = 10
    search_fields = ('id', 'applicant_id','company_name', 'hired_applicant', 'status','date_hired')
    list_filter = ('company_name', 'status','date_hired')


admin.site.register(PRIApplicantJobHiredInfo, PRIApplicantJobHiredAdmin)


class PRIApplicantTest3EssayAdmin(ImportExportModelAdmin):
    list_display = ('id', 'applicant_exam', 'job_request_exam',
                    'question1', 'question2', 'question3')
    list_editable = ('question1', 'question2', 'question3')
    list_per_page = 10
    search_fields = ('id',  'question1', 'question2', 'question3')
    list_filter = ('applicant_exam', 'job_request_exam')


admin.site.register(PRIApplicantTest3EssayInfo, PRIApplicantTest3EssayAdmin)


class PRIApplicantTest3SCTAdmin(ImportExportModelAdmin):
    list_display = ('id', 'applicant_exam_sct', 'job_request_exam_sct', 'question1',
                    'question2',
                    'question3',
                    'question4',
                    'question5',
                    'question6',
                    'question7',
                    'question8',
                    'question9',
                    'question10',
                    'question11',
                    'question12',
                    'question13',
                    'question14',
                    'question15',)
    list_editable = ('question1',
                     'question2',
                     'question3',
                     'question4',
                     'question5',
                     'question6',
                     'question7',
                     'question8',
                     'question9',
                     'question10',
                     'question11',
                     'question12',
                     'question13',
                     'question14',
                     'question15',)
    list_per_page = 10
    search_fields = ('id', 'applicant_exam_sct', 'job_request_exam_sct', 'question1',
                     'question2',
                     'question3',
                     'question4',
                     'question5',
                     'question6',
                     'question7',
                     'question8',
                     'question9',
                     'question10',
                     'question11',
                     'question12',
                     'question13',
                     'question14',
                     'question15',)
    list_filter = ('applicant_exam_sct', 'job_request_exam_sct',)


admin.site.register(PRIApplicantTest3SCTInfo, PRIApplicantTest3SCTAdmin)


class PRIApplicantTestSSCTAdmin(ImportExportModelAdmin):
    list_display = ('id', 'applicant_exam_ssct', 'job_request_exam_ssct',
                    'question1',
                    'question2',
                    'question3',
                    'question4',
                    'question5',
                    'question6',
                    'question7',
                    'question8',
                    'question9',
                    'question10',
                    'question11',
                    'question12',
                    'question13',
                    'question14',
                    'question15',
                    'question16',
                    'question17',
                    'question18',
                    'question19',
                    'question20',
                    'question21',
                    'question22',
                    'question23',
                    'question24',
                    'question25',
                    'question26',
                    'question27',
                    'question28',
                    'question29',
                    'question30',
                    'question31',
                    'question32',
                    'question33',
                    'question34',
                    'question35',
                    'question36',
                    'question37',
                    'question38',
                    'question39',
                    'question40',
                    'question41',
                    'question42',
                    'question43',
                    'question44',
                    'question45',
                    'question46',
                    'question47',
                    'question48',
                    'question49',
                    'question50',
                    'question51',
                    'question52',
                    'question53',
                    'question54',
                    'question55',
                    'question56',
                    'question57',
                    'question58',
                    'question59',
                    'question60',)
    list_editable = (
        'question1',
        'question2',
        'question3',
        'question4',
        'question5',
        'question6',
        'question7',
        'question8',
        'question9',
        'question10',
        'question11',
        'question12',
        'question13',
        'question14',
        'question15',
        'question16',
        'question17',
        'question18',
        'question19',
        'question20',
        'question21',
        'question22',
        'question23',
        'question24',
        'question25',
        'question26',
        'question27',
        'question28',
        'question29',
        'question30',
        'question31',
        'question32',
        'question33',
        'question34',
        'question35',
        'question36',
        'question37',
        'question38',
        'question39',
        'question40',
        'question41',
        'question42',
        'question43',
        'question44',
        'question45',
        'question46',
        'question47',
        'question48',
        'question49',
        'question50',
        'question51',
        'question52',
        'question53',
        'question54',
        'question55',
        'question56',
        'question57',
        'question58',
        'question59',
        'question60',
    )
    list_per_page = 10
    search_fields = ('id',
                     'question1',
                     'question2',
                     'question3',
                     'question4',
                     'question5',
                     'question6',
                     'question7',
                     'question8',
                     'question9',
                     'question10',
                     'question11',
                     'question12',
                     'question13',
                     'question14',
                     'question15',
                     'question16',
                     'question17',
                     'question18',
                     'question19',
                     'question20',
                     'question21',
                     'question22',
                     'question23',
                     'question24',
                     'question25',
                     'question26',
                     'question27',
                     'question28',
                     'question29',
                     'question30',
                     'question31',
                     'question32',
                     'question33',
                     'question34',
                     'question35',
                     'question36',
                     'question37',
                     'question38',
                     'question39',
                     'question40',
                     'question41',
                     'question42',
                     'question43',
                     'question44',
                     'question45',
                     'question46',
                     'question47',
                     'question48',
                     'question49',
                     'question50',
                     'question51',
                     'question52',
                     'question53',
                     'question54',
                     'question55',
                     'question56',
                     'question57',
                     'question58',
                     'question59',
                     'question60',
                     )
    list_filter = ('applicant_exam_ssct', 'job_request_exam_ssct')


admin.site.register(PRIApplicantTestSSCTInfo, PRIApplicantTestSSCTAdmin)


class PRIApplicantTestCCATAdmin(ImportExportModelAdmin):
    list_display = ('id', 'applicant_exam_ccat', 'job_request_exam_ccat',
                    'question1',
                    'question2',
                    'question3',
                    'question4',
                    'question5',
                    'question6',
                    'question7',
                    'question8',
                    'question9',
                    'question10',
                    'question11',
                    'question12',
                    'question13',
                    'question14',
                    'question15',
                    'question16',
                    'question17',
                    'question18',
                    'question19',
                    'question20',
                    'question21',
                    'question22',
                    'question23',
                    'question24',
                    'question25',
                    'question26',
                    'question27',
                    'question28',
                    'question29',
                    'question30',
                    'question31',
                    'question32',
                    'question33',
                    'question34',
                    'question35',
                    'question36',
                    'question37',
                    'question38',
                    'question39',
                    'question40',
                    'question41',
                    'question42',
                    'question43',
                    'question44',
                    'question45',
                    'question46',
                    'question47',
                    'question48',
                    'question49',
                    'question50',
                    'question51',
                    'question52',
                    'question53',
                    'question54',
                    'question55',
                    'question56',
                    'question57',
                    'question58',
                    'question59',
                    'question60',)
    list_editable = (
        'question1',
        'question2',
        'question3',
        'question4',
        'question5',
        'question6',
        'question7',
        'question8',
        'question9',
        'question10',
        'question11',
        'question12',
        'question13',
        'question14',
        'question15',
        'question16',
        'question17',
        'question18',
        'question19',
        'question20',
        'question21',
        'question22',
        'question23',
        'question24',
        'question25',
        'question26',
        'question27',
        'question28',
        'question29',
        'question30',
        'question31',
        'question32',
        'question33',
        'question34',
        'question35',
        'question36',
        'question37',
        'question38',
        'question39',
        'question40',
        'question41',
        'question42',
        'question43',
        'question44',
        'question45',
        'question46',
        'question47',
        'question48',
        'question49',
        'question50',
        'question51',
        'question52',
        'question53',
        'question54',
        'question55',
        'question56',
        'question57',
        'question58',
        'question59',
        'question60',
    )
    list_per_page = 10
    search_fields = ('id',
                     'question1',
                     'question2',
                     'question3',
                     'question4',
                     'question5',
                     'question6',
                     'question7',
                     'question8',
                     'question9',
                     'question10',
                     'question11',
                     'question12',
                     'question13',
                     'question14',
                     'question15',
                     'question16',
                     'question17',
                     'question18',
                     'question19',
                     'question20',
                     'question21',
                     'question22',
                     'question23',
                     'question24',
                     'question25',
                     'question26',
                     'question27',
                     'question28',
                     'question29',
                     'question30',
                     'question31',
                     'question32',
                     'question33',
                     'question34',
                     'question35',
                     'question36',
                     'question37',
                     'question38',
                     'question39',
                     'question40',
                     'question41',
                     'question42',
                     'question43',
                     'question44',
                     'question45',
                     'question46',
                     'question47',
                     'question48',
                     'question49',
                     'question50',
                     'question51',
                     'question52',
                     'question53',
                     'question54',
                     'question55',
                     'question56',
                     'question57',
                     'question58',
                     'question59',
                     'question60',
                     )
    list_filter = ('applicant_exam_ccat', 'job_request_exam_ccat')


admin.site.register(PRIApplicantTestCCATInfo, PRIApplicantTestCCATAdmin)


class PRIApplicantTestARPAdmin(ImportExportModelAdmin):
    list_display = ('id', 'applicant_exam_arp', 'job_request_exam_arp',
                    'question1',
                    'question2',
                    'question3',
                    'question4',
                    'question5',
                    'question6',
                    'question7',
                    'question8',
                    'question9',
                    'question10',
                    'question11',
                    'question12',
                    'question13',
                    'question14',
                    'question15',
                    'question16',
                    'question17',
                    'question18',
                    'question19',
                    'question20',
                    'question21',
                    'question22',
                    'question23',
                    'question24',
                    'question25',
                    'question26',
                    'question27',
                    'question28',
                    'question29',
                    'question30',
                    'question31',
                    'question32',
                    'question33',
                    'question34',
                    'question35',
                    'question36',
                    'question37',
                    'question38',
                    'question39',
                    'question40',
                    'question41',
                    'question42',
                    'question43',
                    'question44',
                    'question45',
                    'question46',
                    'question47',
                    'question48',
                    'question49',
                    'question50',
                    'question51',
                    'question52',
                    'question53',
                    'question54',
                    'question55',
                    'question56',
                    'question57',
                    'question58',
                    'question59',
                    'question60',
                    'question61',
                    'question62',
                    'question63',
                    'question64',
                    'question65',
                    )

    list_editable = (
        'question1',
        'question2',
        'question3',
        'question4',
        'question5',
        'question6',
        'question7',
        'question8',
        'question9',
        'question10',
        'question11',
        'question12',
        'question13',
        'question14',
        'question15',
        'question16',
        'question17',
        'question18',
        'question19',
        'question20',
        'question21',
        'question22',
        'question23',
        'question24',
        'question25',
        'question26',
        'question27',
        'question28',
        'question29',
        'question30',
        'question31',
        'question32',
        'question33',
        'question34',
        'question35',
        'question36',
        'question37',
        'question38',
        'question39',
        'question40',
        'question41',
        'question42',
        'question43',
        'question44',
        'question45',
        'question46',
        'question47',
        'question48',
        'question49',
        'question50',
        'question51',
        'question52',
        'question53',
        'question54',
        'question55',
        'question56',
        'question57',
        'question58',
        'question59',
        'question60',
        'question61',
        'question62',
        'question63',
        'question64',
        'question65',
    )
    list_per_page = 10
    search_fields = ('id',
                     'question1',
                     'question2',
                     'question3',
                     'question4',
                     'question5',
                     'question6',
                     'question7',
                     'question8',
                     'question9',
                     'question10',
                     'question11',
                     'question12',
                     'question13',
                     'question14',
                     'question15',
                     'question16',
                     'question17',
                     'question18',
                     'question19',
                     'question20',
                     'question21',
                     'question22',
                     'question23',
                     'question24',
                     'question25',
                     'question26',
                     'question27',
                     'question28',
                     'question29',
                     'question30',
                     'question31',
                     'question32',
                     'question33',
                     'question34',
                     'question35',
                     'question36',
                     'question37',
                     'question38',
                     'question39',
                     'question40',
                     'question41',
                     'question42',
                     'question43',
                     'question44',
                     'question45',
                     'question46',
                     'question47',
                     'question48',
                     'question49',
                     'question50',
                     'question51',
                     'question52',
                     'question53',
                     'question54',
                     'question55',
                     'question56',
                     'question57',
                     'question58',
                     'question59',
                     'question60',
                     'question61',
                     'question62',
                     'question63',
                     'question64',
                     'question65',
                     )
    list_filter = ('applicant_exam_arp', 'job_request_exam_arp')


admin.site.register(PRIApplicantTestARPInfo, PRIApplicantTestARPAdmin)


# Scores

class PRIApplicantExamScoreT1PEAdmin(ImportExportModelAdmin):
    list_display = ('id', 'applicant_exam_score_t1pe', 'job_request_exam_score_t1pe', 'score_t1pe',
                    'over_t1pe', 'status_t1pe', 'ratings_t1pe', 'allow_retake_t1pe', 'date_taken_t1pe')
    list_editable = ('score_t1pe', 'over_t1pe', 'status_t1pe',
                     'ratings_t1pe', 'allow_retake_t1pe')
    list_per_page = 10
    search_fields = ('id', 'applicant_exam_score_t1pe', 'job_request_exam_score_t1pe', 'score_t1pe',
                     'over_t1pe', 'status_t1pe', 'ratings_t1pe', 'allow_retake_t1pe', 'date_taken_t1pe')
    list_filter = ('applicant_exam_score_t1pe',
                   'job_request_exam_score_t1pe', 'date_taken_t1pe')


admin.site.register(PRIApplicantExamScoreT1PEInfo,
                    PRIApplicantExamScoreT1PEAdmin)


class PRIApplicantExamScoreT2SEAdmin(ImportExportModelAdmin):
    list_display = ('id', 'applicant_exam_score_t2se', 'job_request_exam_score_t2se', 'score_t2se',
                    'over_t2se', 'status_t2se', 'ratings_t2se', 'allow_retake_t2se', 'date_taken_t2se')
    list_editable = ('score_t2se', 'over_t2se', 'status_t2se',
                     'ratings_t2se', 'allow_retake_t2se')
    list_per_page = 10
    search_fields = ('id', 'applicant_exam_score_t2se', 'job_request_exam_score_t2se', 'score_t2se',
                     'over_t2se', 'status_t2se', 'ratings_t2se', 'allow_retake_t2se', 'date_taken_t2se')
    list_filter = ('applicant_exam_score_t2se',
                   'job_request_exam_score_t2se', 'date_taken_t2se')


admin.site.register(PRIApplicantExamScoreT2SEInfo,
                    PRIApplicantExamScoreT2SEAdmin)


class PRIApplicantExamScoreT3EAdmin(ImportExportModelAdmin):
    list_display = ('id', 'applicant_exam_score_t3e', 'job_request_exam_score_t3e', 'score_t3e',
                    'over_t3e', 'status_t3e', 'ratings_t3e', 'allow_retake_t3e', 'date_taken_t3e')
    list_editable = ('score_t3e', 'over_t3e', 'status_t3e',
                     'ratings_t3e', 'allow_retake_t3e')
    list_per_page = 10
    search_fields = ('id', 'applicant_exam_score_t3e', 'job_request_exam_score_t3e', 'score_t3e',
                     'over_t3e', 'status_t3e', 'ratings_t3e', 'allow_retake_t3e', 'date_taken_t3e')
    list_filter = ('applicant_exam_score_t3e',
                   'job_request_exam_score_t3e', 'date_taken_t3e')


admin.site.register(PRIApplicantExamScoreT3EInfo,
                    PRIApplicantExamScoreT3EAdmin)


class PRIApplicantExamScoreT3PTSCTAdmin(ImportExportModelAdmin):
    list_display = ('id', 'applicant_exam_score_t3ptsct', 'job_request_exam_score_t3ptsct', 'score_t3ptsct',
                    'over_t3ptsct', 'status_t3ptsct', 'ratings_t3ptsct', 'allow_retake_t3ptsct', 'date_taken_t3ptsct')
    list_editable = ('score_t3ptsct', 'over_t3ptsct',
                     'status_t3ptsct', 'ratings_t3ptsct', 'allow_retake_t3ptsct')
    list_per_page = 10
    search_fields = ('id', 'applicant_exam_score_t3ptsct', 'job_request_exam_score_t3ptsct', 'score_t3ptsct',
                     'over_t3ptsct', 'status_t3ptsct', 'ratings_t3ptsct', 'allow_retake_t3ptsct', 'date_taken_t3ptsct')
    list_filter = ('applicant_exam_score_t3ptsct',
                   'job_request_exam_score_t3ptsct', 'date_taken_t3ptsct')


admin.site.register(PRIApplicantExamScoreT3PTSCTInfo,
                    PRIApplicantExamScoreT3PTSCTAdmin)


class PRIApplicantExamScoreT4ARAdmin(ImportExportModelAdmin):
    list_display = ('id', 'applicant_exam_score_t4ar', 'job_request_exam_score_t4ar', 'score_t4ar',
                    'over_t4ar', 'status_t4ar', 'ratings_t4ar', 'allow_retake_t4ar', 'date_taken_t4ar')
    list_editable = ('score_t4ar', 'over_t4ar', 'status_t4ar',
                     'ratings_t4ar', 'allow_retake_t4ar')
    list_per_page = 10
    search_fields = ('id', 'applicant_exam_score_t4ar', 'job_request_exam_score_t4ar', 'score_t4ar',
                     'over_t4ar', 'status_t4ar', 'ratings_t4ar', 'allow_retake_t4ar', 'date_taken_t4ar')
    list_filter = ('applicant_exam_score_t4ar',
                   'job_request_exam_score_t4ar', 'date_taken_t4ar')


admin.site.register(PRIApplicantExamScoreT4ARInfo,
                    PRIApplicantExamScoreT4ARAdmin)


class PRIApplicantExamScoreCCAAdmin(ImportExportModelAdmin):
    list_display = ('id', 'applicant_exam_score_cca', 'job_request_exam_score_cca', 'score_cca',
                    'over_cca', 'status_cca', 'ratings_cca', 'allow_retake_cca', 'date_taken_cca')
    list_editable = ('score_cca', 'over_cca', 'status_cca',
                     'ratings_cca', 'allow_retake_cca')
    list_per_page = 10
    search_fields = ('id', 'applicant_exam_score_cca', 'job_request_exam_score_cca', 'score_cca',
                     'over_cca', 'status_cca', 'ratings_cca', 'allow_retake_cca', 'date_taken_cca')
    list_filter = ('applicant_exam_score_cca',
                   'job_request_exam_score_cca', 'date_taken_cca')


admin.site.register(PRIApplicantExamScoreCCAInfo,
                    PRIApplicantExamScoreCCAAdmin)


class PRIApplicantExamScoreARPAdmin(ImportExportModelAdmin):
    list_display = ('id', 'applicant_exam_score_arp', 'job_request_exam_score_arp', 'score_arp',
                    'over_arp', 'status_arp', 'ratings_arp', 'allow_retake_arp', 'date_taken_arp')
    list_editable = ('score_arp', 'over_arp', 'status_arp',
                     'ratings_arp', 'allow_retake_arp')
    list_per_page = 10
    search_fields = ('id', 'applicant_exam_score_arp', 'job_request_exam_score_arp', 'score_arp',
                     'over_arp', 'status_arp', 'ratings_arp', 'allow_retake_arp', 'date_taken_arp')
    list_filter = ('applicant_exam_score_arp',
                   'job_request_exam_score_arp', 'date_taken_arp')


admin.site.register(PRIApplicantExamScoreARPInfo,
                    PRIApplicantExamScoreARPAdmin)


class PRIApplicantExamScoreSCCTAdmin(ImportExportModelAdmin):
    list_display = ('id', 'applicant_exam_score_scct', 'job_request_exam_score_scct', 'score_scct',
                    'over_scct', 'status_scct', 'ratings_scct', 'allow_retake_scct', 'date_taken_scct')
    list_editable = ('score_scct', 'over_scct', 'status_scct',
                     'ratings_scct', 'allow_retake_scct')
    list_per_page = 10
    search_fields = ('id', 'applicant_exam_score_scct', 'job_request_exam_score_scct', 'score_scct',
                     'over_scct', 'status_scct', 'ratings_scct', 'allow_retake_scct', 'date_taken_scct')
    list_filter = ('applicant_exam_score_scct',
                   'job_request_exam_score_scct', 'date_taken_scct')


admin.site.register(PRIApplicantExamScoreSCCTInfo,
                    PRIApplicantExamScoreSCCTAdmin)
