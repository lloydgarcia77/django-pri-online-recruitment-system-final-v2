from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import os
from multiselectfield import MultiSelectField
from django.utils.text import slugify

# Create your models here.

def file_validator(value):

    file_size = value.size
    valid_file_extension = ['.jpg', '.png', '.jpeg', '.pdf', '.doc', '.docx']

    file_extension = os.path.splitext(value.name)[1]

    print("File Name: ", value.name)
    print("File Extension: ", file_extension)

    file_size_kb = file_size * 0.001
    file_size_mb = file_size_kb * 0.0001

    print("File Size: ", file_size, " Bytes")
    print("File Size: ", file_size_kb, " KB")
    print("File Size: ", file_size_mb, " MB")

    if not file_extension in valid_file_extension:
        print("Invalid file! Valid files only: ('.jpg', '.png', '.jpeg', 'pdf', 'doc', 'docx')")
        raise ValidationError("Invalid file! Valid files only: ('.jpg', '.png', '.jpeg', 'pdf', 'doc', 'docx')")

    else:
        if file_size_mb > 5: # 5MB
            print("File too large! The maximum file size can be upload is 5 MB")
            raise ValidationError("The maximum file size can be upload is 5 MB")
        else:
            print('FILE is VALID')
            return value

class PRIUserInfo(models.Model):

    GENDER_LIST = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    USER_LEVELS = (
        ('Administrator', 'Administrator'),
        ('Sub Admin', 'Sub Admin'),
        ('Employee', 'Employee'),
        ('Client', 'Client'),
        # ('Applicant', 'Applicant'),
    )


    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_fk')

    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=50, choices=GENDER_LIST, default=GENDER_LIST[0])
    contact = models.CharField(max_length=12, unique=True)
    #dob = models.DateField(verbose_name="Date of Birth")
    address = models.CharField(max_length=250)
    position = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True, validators=[file_validator])
    level = models.CharField(max_length=50, choices=USER_LEVELS, default=USER_LEVELS[0])
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.last_name + " " + self.first_name + " " + self.middle_name)


# to be check
class PRIUserPermission(models.Model):
    # Clients
    pri_user = models.OneToOneField(PRIUserInfo, on_delete=models.CASCADE, related_name='policy_user_fk')
    pri_can_view_clients_page = models.BooleanField(default=False, verbose_name="Can View Clients Page")
    pri_can_add_clients = models.BooleanField(default=False, verbose_name="Can Add Clients")
    pri_can_hired_clients = models.BooleanField(default=False, verbose_name="Can Hired Clients")
    pri_can_edit_clients = models.BooleanField(default=False, verbose_name="Can Edit Clients")
    pri_can_delete_clients = models.BooleanField(default=False, verbose_name="Can Delete Clients")
    # Request
    pri_can_view_request_page = models.BooleanField(default=False, verbose_name="Can View Requests Page")
    pri_can_add_request = models.BooleanField(default=False, verbose_name="Can Add Requests")
    pri_can_create_job_request = models.BooleanField(default=False, verbose_name="Can Create Job Requests")
    pri_can_view_request = models.BooleanField(default=False, verbose_name="Can View Requests")
    pri_can_edit_request = models.BooleanField(default=False, verbose_name="Can Edit Requests")
    pri_can_delete_request = models.BooleanField(default=False, verbose_name="Can Delete Requests")
    # Job Vacancy
    pri_can_view_job_vacancy_page = models.BooleanField(default=False, verbose_name="Can View Job Vacancy Page")  
    pri_can_view_job_vacancy_applicants = models.BooleanField(default=False, verbose_name="Can View Job Vacancy Applicants")
    pri_can_edit_job_vacancy = models.BooleanField(default=False, verbose_name="Can Edit Job Vacancy")
    pri_can_delete_job_vacancy = models.BooleanField(default=False, verbose_name="Can Delete Job Vacancy")
    # Applicants
    pri_can_view_applicants_page = models.BooleanField(default=False, verbose_name="Can View Applicants Page")  
    pri_can_delete_applicants = models.BooleanField(default=False, verbose_name="Can Delete Applicants")


    date_modified = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.pri_user)

class PRIClientsInfo(models.Model):

    client_user = models.OneToOneField(PRIUserInfo, on_delete=models.CASCADE, related_name='client_user_fk')
    client_company_name = models.CharField(max_length=50, null=True)
    client_company_logo = models.ImageField(upload_to='images/', blank=True, null=True, validators=[file_validator])
    client_location = models.CharField(max_length=250)
    contact_person = models.CharField(max_length=80)
    contact_mobile_no = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return str(self.client_company_name)

class PRIRequestInfo(models.Model):

    STATUS_LIST = (
        ('Started', 'Started'),
        ('On Going', 'On Going'),
        ('Completed', 'Completed'),
        ('Deadline', 'Deadline'),
        ('Failed', 'Failed'),
    )

    requested_client = models.ForeignKey(PRIClientsInfo, on_delete=models.CASCADE, related_name='requested_client_fk')
    status = models.CharField(max_length=50, choices=STATUS_LIST, default=STATUS_LIST[0])
    content = models.TextField()
    data_requested = models.DateField(auto_now_add=True)
    seen_by_admin = models.BooleanField(default=False)

    def __str__(self):
        return str(self.requested_client)


class PRIJobVacancyInfo(models.Model):
    CATEGORY_LIST = (
        ('Janitor', 'Janitor'),
        ('Others', 'Others'),
    )
    
    secure_id = models.CharField(max_length=255,unique=True, blank=True)
    client_request = models.OneToOneField(PRIRequestInfo, on_delete=models.CASCADE, related_name='job_vacancy_client_request_fk')
    job_title = models.CharField(max_length=150)
    job_category = models.CharField(max_length=10, choices=CATEGORY_LIST, default=CATEGORY_LIST[0])
    job_specialization = models.CharField(max_length=50)
    job_minimum_experience = models.CharField(max_length=15)
    job_salary = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    job_deadline = models.DateField()
    job_company_overview = models.TextField(blank=True)
    job_description = models.TextField(blank=True)

    def __str__(self):
        return str(self.job_title)

    # job logo from parent
    # job location from parent
    # job request client from parent
    # job company from parent

class PRIJobVacancyJobQualificationsInfo(models.Model):

    job_vacancy_jq = models.ForeignKey(PRIJobVacancyInfo, on_delete=models.CASCADE, related_name='job_vacancy_jq_fk')
    job_qualifications = models.CharField(max_length=250, null=True)

    def __str__(self):
        return str(self.job_qualifications)

class PRIJobVacancyJobResponsibilitiesInfo(models.Model):

    job_vacancy_jr = models.ForeignKey(PRIJobVacancyInfo, on_delete=models.CASCADE, related_name='job_vacancy_jr_fk')
    job_responsibilities = models.CharField(max_length=250, null=True)

    def __str__(self):
        return str(self.job_responsibilities)


class PRIApplicantProfileInfo(models.Model):

    ERP_QUESTION_LIST = (
        ('Referral', 'Referral'),
        ('Online Job Portal', 'Online Job Portal'),
        ('Leaflets', 'Leaflets'),
        ('Walk-in', 'Walk-in'),
        ('Job fair', 'Job fair'),
    )

    GENDER_LIST = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    CIVIL_STATUS_LIST = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
        ('Separated', 'Separated'),
    )
 
    secure_key_id = models.CharField(max_length=255, unique=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='applicant_user_fk')
    image = models.ImageField(upload_to='images/', blank=True, verbose_name="Picture/Image")
    cv = models.FileField(upload_to='documents/%Y/%m/%d', blank=True, validators=[file_validator], verbose_name="Resume/Curriculum Vitae (Optional):",null=True)
    date_filled = models.DateField(auto_now_add=True)
    #for checking
    position_desired = models.CharField(max_length=100, blank=True)
    company_assigned = models.CharField(max_length=100, blank=True) 

    erp_question = MultiSelectField(choices=ERP_QUESTION_LIST, verbose_name="How did you found out about thid job?", blank=True)
    fname = models.CharField(max_length=100, verbose_name="First Name")
    mname = models.CharField(max_length=100, verbose_name="Middle Name")
    lname = models.CharField(max_length=100, verbose_name="Last Name")
    mobile_no = models.CharField(max_length=12, null=True, blank=True)
    telephone_no = models.CharField(max_length=12, null=True,  blank=True)
    # mobile_no = models.CharField(max_length=12, unique=True, blank=True)
    # telephone_no = models.CharField(max_length=12, unique=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_LIST, default=GENDER_LIST[0])
    
    #Person to notify
    contact_person = models.CharField(max_length=100, verbose_name="Contact Person Name", null=True, blank=True)
    relationship = models.CharField(max_length=100, null=True, blank=True)
    contact_person_mobile_no = models.CharField(max_length=100, unique=True, null=True, blank=True)

    #present address
    bldg_name_0 = models.CharField(max_length=250, verbose_name="Bldg Name.", blank=True)
    brgy_sub_0 = models.CharField(max_length=250, verbose_name="Brgy Sub.", blank=True)
    dis_mun_0 = models.CharField(max_length=250, verbose_name="District/Municipality.", blank=True)
    cit_pro_0 = models.CharField(max_length=250, verbose_name="City/Province", blank=True)

    #permanent address
    bldg_name_1 = models.CharField(max_length=250, verbose_name="Bldg Name.", blank=True)
    brgy_sub_1 = models.CharField(max_length=250, verbose_name="Brgy Sub.", blank=True)
    dis_mun_1 = models.CharField(max_length=250, verbose_name="District/Municipality.", blank=True)
    cit_pro_1 = models.CharField(max_length=250, verbose_name="City/Province", blank=True)

    civil_status = models.CharField(max_length=100, choices=CIVIL_STATUS_LIST, default=CIVIL_STATUS_LIST[0])

    weight = models.DecimalField(default=0, max_digits=5, decimal_places=2, verbose_name="Weight (Lbs)", blank=True)
    height = models.DecimalField(default=0, max_digits=5, decimal_places=2, verbose_name="Height (Inch)", blank=True)
    shirt_size = models.DecimalField(default=0, max_digits=5, decimal_places=2, blank=True)
    shoe_size = models.DecimalField(default=0, max_digits=5, decimal_places=2, blank=True)
    waistline = models.DecimalField(default=0, max_digits=5, decimal_places=2, blank=True)
    length_of_pants = models.DecimalField(default=0, max_digits=5, decimal_places=2, blank=True)

    sss = models.CharField(max_length=10, unique=True, blank=True, null=True)
    ctc = models.CharField(max_length=8, unique=True, blank=True, null=True)
    philhealth = models.CharField(max_length=12, unique=True, blank=True, null=True)
    tin = models.CharField(max_length=9, unique=True, blank=True, null=True)
    pagibig = models.CharField(max_length=12, unique=True, blank=True, null=True)

    #if married, fill this up
    spouse_full_name = models.CharField(max_length=100, verbose_name="Spouse full name", blank=True, null=True)
    spouse_contact_number = models.CharField(max_length=12, verbose_name="Contact #", blank=True, null=True)

    father_full_name = models.CharField(max_length=100, blank=True)
    father_occupation = models.CharField(max_length=100, blank=True)
    father_home_address = models.CharField(max_length=100, blank=True)

    mother_full_name = models.CharField(max_length=100, blank=True)
    mother_occupation = models.CharField(max_length=100, blank=True)
    mother_home_address = models.CharField(max_length=100, blank=True)

    #Survey Question
    question1 = models.CharField(max_length=200, blank=True, verbose_name="Do you have a relative by any degree by consangunity or affinty working with poerlane or any of its client? (If yes state the name of your relative , position/company name.)")
    question2 = models.CharField(max_length=200, blank=True, verbose_name="Have you been confined in a medical facility due to illness, dreaded/contagious disease, or minor/major surgery? (If yes, what disease/illness when & name of the medical facility)")
    question3 = models.CharField(max_length=200, blank=True, verbose_name="Have you ever been changed or sentenced by any court of law of any crime? (If Yes, please give details.)")
    question4 = models.CharField(max_length=200, blank=True, verbose_name="Have you in the past applied at powerlane or any of its client & was not hired nor employed? (If yes when and state the reason.)")

    slug = models.SlugField(unique=True, allow_unicode=True, default="none")

    def __str__(self):
        return str(self.lname + ", " + self.fname + " " + self.lname)

    def save(self, *args, **kwargs):
        name = str(self.lname + self.fname + self.mname)
        self.slug = slugify(name)
        return super(PRIApplicantProfileInfo, self).save(*args, **kwargs)


    

class PRIApplicantSibilingsInfo(models.Model):
    applicant_siblings = models.ForeignKey(PRIApplicantProfileInfo, on_delete=models.CASCADE, related_name='siblings_applicant_fk', blank=True)
    name = models.CharField(max_length=50, blank=True)
    age = models.PositiveIntegerField()
    occ = models.CharField(max_length=50, verbose_name="Occupation/Company", blank=True)

    def __str__(self):
        return str(self.name)
 

class PRIApplicantEmploymentHistoryInfo(models.Model):
    applicant_employment_history = models.ForeignKey(PRIApplicantProfileInfo, on_delete=models.CASCADE, related_name='employment_applicant_fk', blank=True)
    date_from = models.DateField(blank=True)
    date_to = models.DateField(blank=True)
    company = models.CharField(max_length=150, verbose_name="Employer/Company Name", blank=True)
    position = models.CharField(max_length=100, blank=True)
    reason_for_leaving = models.CharField(max_length=250, blank=True)
    basic_salary_pay = models.DecimalField(default=0, max_digits=12, decimal_places=2, blank=True)

    def __str__(self):
        return str(self.applicant_employment_history)


class PRIApplicantEducationalAttainmentInfo(models.Model):
    applicant_educational_attainment = models.ForeignKey(PRIApplicantProfileInfo, on_delete=models.CASCADE, related_name='educational_applicant_fk')
    college = models.CharField(max_length=200, verbose_name="Name of School", blank=True, default="")
    college_course = models.CharField(max_length=51, blank=True, default="")
    college_address = models.CharField(max_length=200, blank=True, default="")
    csya_from = models.DateField(verbose_name="From", blank=True, null=True)
    csya_to = models.DateField(verbose_name="To", blank=True, null=True)
   
    vocational = models.CharField(max_length=200, verbose_name="Name of School", blank=True, default="")
    vocational_course = models.CharField(max_length=50, blank=True, default="")
    vocational_address = models.CharField(max_length=200, blank=True, default="")
    vsya_from = models.DateField(verbose_name="From", blank=True, null=True)
    vsya_to = models.DateField(verbose_name="To", blank=True, null=True)
   
    highschool = models.CharField(max_length=15, blank=True, default="")
    highschool_address = models.CharField(max_length=200,  blank=True, default="")
    hsya_from = models.DateField(verbose_name="From", blank=True, null=True)
    hsya_to = models.DateField(verbose_name="To", blank=True, null=True)
   
    elementary = models.CharField(max_length=150, blank=True, default="")
    elementary_address = models.CharField(max_length=250, blank=True, default="")
    esya_from = models.DateField(verbose_name="From", blank=True, null=True)
    esya_to = models.DateField(verbose_name="To", blank=True, null=True)

    special_skills = models.CharField(max_length=150, blank=True, default="")
    language_speak = models.CharField(max_length=100, blank=True, default="")


    def __str__(self):
        return str(self.applicant_educational_attainment)


class PRIApplicantTrainingsInfo(models.Model):
    applicant_trainings = models.ForeignKey(PRIApplicantProfileInfo, on_delete=models.CASCADE, related_name='tranings_applicant_fk', blank=True)
    title = models.CharField(max_length=100, verbose_name='Title of traning', blank=True)
    date_attended = models.DateField(blank=True)

    def __str__(self):
        return str(self.title)

class PRIApplicantCharacterReferencesInfo(models.Model):
 
    applicant_character_references = models.ForeignKey(PRIApplicantProfileInfo, on_delete=models.CASCADE, related_name='character_references_applicant_fk', blank=True)
    full_name = models.CharField(max_length=150, blank=True)
    occupation = models.CharField(max_length=150, blank=True)
    contact_no = models.CharField(max_length=12, unique=True, blank=True, null=True)

    def __str__(self):
        return str(self.full_name)


# Applicant status

class PRIApplicantJobRequestInfo(models.Model):
    job_vacancy_applied = models.ForeignKey(PRIJobVacancyInfo, on_delete=models.CASCADE, related_name='job_vacancy_applied_fk')
    applying_applicant = models.ForeignKey(PRIApplicantProfileInfo, on_delete=models.CASCADE, related_name='applying_applicant_fk')        
    date_applied = models.DateField(auto_now_add=True)
    take_exam = models.BooleanField(default=False)
    interview_date = models.DateTimeField(null=True, blank=True,)

    def __str__(self):
        return str(self.job_vacancy_applied)


class PRIApplicantJobHiredInfo(models.Model):
    HIRED_STATUS = (
        ("Available", "Available"),
        ("Terminated","Terminated"),
        ("6 Months Contract","6 Months Contract"),
    )
    company_name = models.ForeignKey(PRIClientsInfo, on_delete=models.CASCADE, related_name='company_name_fk')
    hired_applicant = models.ForeignKey(PRIApplicantProfileInfo, on_delete=models.CASCADE, related_name='hired_applicant_fk')
    applicant_id = models.CharField(max_length=101, blank=True)
    date_hired = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=HIRED_STATUS, default='Available')

    def __str__(self):
        return str(self.hired_applicant)


class PRIApplicantTest3EssayInfo(models.Model):
    applicant_exam = models.ForeignKey(PRIApplicantProfileInfo, on_delete=models.CASCADE, related_name='applicant_exam_fk')
    job_request_exam = models.ForeignKey(PRIApplicantJobRequestInfo, on_delete=models.CASCADE, related_name='job_request_exam_fk')
    question1 = models.CharField(max_length = 250, verbose_name="What can you say about yourself?")
    question2 = models.CharField(max_length = 250, verbose_name="Why do you need a job?")
    question3 = models.CharField(max_length = 250, verbose_name="What are the values/traits do you need to succeed in life?")
    def __str__(self):
        return str(self.job_request_exam)

class PRIApplicantTest3SCTInfo(models.Model):
    applicant_exam_sct = models.ForeignKey(PRIApplicantProfileInfo, on_delete=models.CASCADE, related_name='applicant_exam_sct_fk')
    job_request_exam_sct = models.ForeignKey(PRIApplicantJobRequestInfo, on_delete=models.CASCADE, related_name='job_request_exam_sct_fk')
    # Sentence completion test

    question1 = models.CharField(max_length = 250, verbose_name="I like my mother but ")
    question2 = models.CharField(max_length = 250, verbose_name="I wish my father ")
    question3 = models.CharField(max_length = 250, verbose_name="Compared with most families, mine is ")
    question4 = models.CharField(max_length = 250, verbose_name="If I had a sexual relationship")
    question5 = models.CharField(max_length = 250, verbose_name="I don’t like people who")
    question6 = models.CharField(max_length = 250, verbose_name="If people work for me")
    question7 = models.CharField(max_length = 250, verbose_name="When I see the boss coming")
    question8 = models.CharField(max_length = 250, verbose_name="My fears sometimes force me to")
    question9 = models.CharField(max_length = 250, verbose_name="My greatest mistake was")
    question10 = models.CharField(max_length = 250, verbose_name="Someday")
    question11 = models.CharField(max_length = 250, verbose_name="I could be perfeclty happy if")
    question12 = models.CharField(max_length = 250, verbose_name="In school, my teacher was ")
    question13 = models.CharField(max_length = 250, verbose_name="I work best when")
    question14 = models.CharField(max_length = 250, verbose_name="I believe that I have the ability to")
    question15 = models.CharField(max_length = 250, verbose_name="My feeling about married life")

    def __str__(self):
        return str(self.job_request_exam_sct)
    
class PRIApplicantTestSSCTInfo(models.Model):
    applicant_exam_ssct = models.ForeignKey(PRIApplicantProfileInfo, on_delete=models.CASCADE, related_name='applicant_exam_ssct_fk')
    job_request_exam_ssct = models.ForeignKey(PRIApplicantJobRequestInfo, on_delete=models.CASCADE, related_name='job_request_exam_ssct_fk')
    question1 = models.CharField(max_length = 250, verbose_name="I feel that my father seldom (Pakiramdam ko ang aking ama ay bihirang)")
    question2 = models.CharField(max_length = 250, verbose_name="When the odds are against me (Kapag ang lahat ay laban sa akin)")
    question3 = models.CharField(max_length = 250, verbose_name="I always wanted to (Matagal ko ng gustong)")
    question4 = models.CharField(max_length = 250, verbose_name="If I were in charge (Kung ako ay namamahala)")
    question5 = models.CharField(max_length = 250, verbose_name="To me the future looks (Para sa akin ang kinabukasan ay)")
    question6 = models.CharField(max_length = 250, verbose_name="The persons over me (Ang mga taong nakakataas sa akin)")
    question7 = models.CharField(max_length = 250, verbose_name="I am silly but I am afraid of (Alam kong kakatwa subalit ako'y takot)")
    question8 = models.CharField(max_length = 250, verbose_name="I feel that a real firend (Sa aking palagay ang tunay na kaibigan)")
    question9 = models.CharField(max_length = 250, verbose_name="When I was a child (Noong ako'y bata pa)")
    question10 = models.CharField(max_length = 250, verbose_name="My idea of a perfect woman/man (Para sa akin ang isang katangi-tanging babae/lalaki)")
    question11 = models.CharField(max_length = 250, verbose_name="When I see a man and woman together (Kapag nakakakita ako ng isang babae at lalaking magkasama)")
    question12 = models.CharField(max_length = 250, verbose_name="Compared with most families, mine (Kung ihahambing sa maraming mag-anak, ang sa akin)")
    question13 = models.CharField(max_length = 250, verbose_name="At work, I get aling best with (Sa gawain, nakakasundo kong mabuti)")
    question14 = models.CharField(max_length = 250, verbose_name="My mother (Ang aking ina)")
    question15 = models.CharField(max_length = 250, verbose_name="I would do anything to forget the time (Gagawin ko ang lahat upang makalimutan ang sandaling)")
    question16 = models.CharField(max_length = 250, verbose_name="If my father would only (Kung ang ama kong lamang)")
    question17 = models.CharField(max_length = 250, verbose_name="I believe that I have the ability (Ako ay naniniwalang ako ay may kakayahang)")
    question18 = models.CharField(max_length = 250, verbose_name="I could be perfectly happy if  (Ako ay magiging higit na maligaya kung)")
    question19 = models.CharField(max_length = 250, verbose_name="If people work for me (Kung maglilingkod ang mga tao sa akin)")
    question20 = models.CharField(max_length = 250, verbose_name="I look forward to (Inaasahan kong)")
    question21 = models.CharField(max_length = 250, verbose_name="In school, my teachers (Sa paaralan, ang aking mga guro)")
    question22 = models.CharField(max_length = 250, verbose_name="Most of my friends don’t know that I am afraid of (Karamihan sa aking mga kaibigan ay hindi nakakaalam na ako’y takot sa)")
    question23 = models.CharField(max_length = 250, verbose_name="I don’t like people who (Hindi ko gusto ang mga taong)")
    question24 = models.CharField(max_length = 250, verbose_name="Before, I (Noon, ako)")
    question25 = models.CharField(max_length = 250, verbose_name="I think most girls (Sa aking palagay karamihan sa mga kababaihan ay)")
    question26 = models.CharField(max_length = 250, verbose_name="My feeling about married life (Ang aking pakiramdam sa buhay mag-asawa ay)")
    question27 = models.CharField(max_length = 250, verbose_name="My family treat me (Ang aking kaanak ay itunuturing ako tulad ng)")
    question28 = models.CharField(max_length = 250, verbose_name="Those I work with are (Ang mga kasama ko sa gawain ay)")
    question29 = models.CharField(max_length = 250, verbose_name="My mother and I (Ang aking ina at ako)")
    question30 = models.CharField(max_length = 250, verbose_name="My greatest mistake was (Ang aking pinakamalaking kamalian ay)")
    question31 = models.CharField(max_length = 250, verbose_name="I wish that my father (Sana ang aking ama)")
    question32 = models.CharField(max_length = 250, verbose_name="My greatest weakness (Ang pinakamalaking kahinaan ko)")
    question33 = models.CharField(max_length = 250, verbose_name="My secret ambition in life (Ang lihim kong mithiin sa buhay)")
    question34 = models.CharField(max_length = 250, verbose_name="The people who work for me (Ang mga taong naglilingkod sa akin)")
    question35 = models.CharField(max_length = 250, verbose_name="Someday, I (Balang araw ako)")
    question36 = models.CharField(max_length = 250, verbose_name="When I see my boss coming (Kapag nakikita kong dumarating ang aking pinuno)")
    question37 = models.CharField(max_length = 250, verbose_name="I wish I could lose fear of (Sana mawala sa akin ang takot sa)")
    question38 = models.CharField(max_length = 250, verbose_name="The people I like best (Ang mga taong gusting gusto ko)")
    question39 = models.CharField(max_length = 250, verbose_name="If I were young again (Kung ako’y maging bata muli)")
    question40 = models.CharField(max_length = 250, verbose_name="I believe most women/men (Ako’y naniniwala na karamihan sa mga babae at lalaki)")
    question41 = models.CharField(max_length = 250, verbose_name="If I have a sex relation (Kung ako’y makakaron ng karanasang sekswal)")
    question42 = models.CharField(max_length = 250, verbose_name="Most families I know (Halos lahat ng mag-anak na kilala ko)")
    question43 = models.CharField(max_length = 250, verbose_name="I like working with (Naiibigan kong magtrabaho)")
    question44 = models.CharField(max_length = 250, verbose_name="I think most mothers (Sa aking palagay, karamihan sa mga ina)")
    question45 = models.CharField(max_length = 250, verbose_name="When I was younger, I felt guilty (Noong kabataan ko, ako’y inuusig ng aking budhi tungkol)")
    question46 = models.CharField(max_length = 250, verbose_name="I feel that my father is (Nadarama kong ang aking ama ay)")
    question47 = models.CharField(max_length = 250, verbose_name="When luck turn against me (Kapag ang kapalaran ay hindi naayon sa akin)")
    question48 = models.CharField(max_length = 250, verbose_name="In giving orders to others, I (Sa pagbibigay-utos sa iba)")
    question49 = models.CharField(max_length = 250, verbose_name="What I want most out of life (Ang aking pinkamimithi sa buhay)")
    question50 = models.CharField(max_length = 250, verbose_name="When I am older (Kapag ako’y tumanda)")
    question51 = models.CharField(max_length = 250, verbose_name="People whom I consider my superiors (Ang mga taong itinuturing kong nakatataas sa akin)")
    question52 = models.CharField(max_length = 250, verbose_name="My fears sometimes force me (kung minsan ang aking pangamba ay pumipilit sa akin)")
    question53 = models.CharField(max_length = 250, verbose_name="When I am not around, my friend (kapag wala ako sa paligid, ang mga kaibigan ko ay)")
    question54 = models.CharField(max_length = 250, verbose_name="My most vivid childhood memory (Ang tandang tanda kong karanasan noong kabataan ko)")
    question55 = models.CharField(max_length = 250, verbose_name="What I like least about women (Ang pinakagusto ko sa mga kababaihan)")
    question56 = models.CharField(max_length = 250, verbose_name="My sex life (Ang aking buhay sekswal)")
    question57 = models.CharField(max_length = 250, verbose_name="When I was a child, my family (Noong ako’y bata pa, ang aking pamilya)")
    question58 = models.CharField(max_length = 250, verbose_name="People who work with me usually (Ang aking kasamahan sa paggawa ay kadalasang)")
    question59 = models.CharField(max_length = 250, verbose_name="I like my mother but (Gusto ko ang aking ina subalit)")
    question60 = models.CharField(max_length = 250, verbose_name="The worst thing I ever did (Ang pinakamaling bagay na aking nagawa)")

    def __str__(self):
        return str(self.job_request_exam_ssct)

CHOICE_LIST = (
    ('Strongly Agree', 'Strongly Agree'),
    ('Agree', 'Agree'),
    ('Neutral', 'Neutral'),
    ('Disagree', 'Disagree'),
    ('Strongly Disagree', 'Strongly Disagree'),
)

class PRIApplicantTestCCATInfo(models.Model):
    applicant_exam_ccat = models.ForeignKey(PRIApplicantProfileInfo, on_delete=models.CASCADE, related_name='applicant_exam_ccat_fk')
    job_request_exam_ccat = models.ForeignKey(PRIApplicantJobRequestInfo, on_delete=models.CASCADE, related_name='job_request_exam_ccat_fk')
    question1 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="My coworkers would describe me as outgoing.")
    question2 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="In my day-to-day working situations, I tend to be more courteous than most people.")
    question3 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="I don't believe that one ever has to compremise.")
    question4 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Change in organizations is usually for the better.")
    question5 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Enjoy spending time with others more than I enjoy spending time alone.")
    question6 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Due to my ability to focus on my work at times I can be perceived as being cold or distant.")
    question7 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="One of my strengths is my ability to adopt to change.")
    question8 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="One of the best parts of going to work is interacting with other people.")
    question9 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="I enjoy working with people more than I enjoy working with things.")
    question10 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Change usually leads to positive outcomes.")
    question11 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Success is more matter of luck than hard work.")
    question12 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Like most people, I sometimes worry that I will not be able accomplish whatever is set before me.")
    question13 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="I am guilty of trying to be too controlling at time.")
    question14 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="When ir comes to work, I am pretty easy going.")
    question15 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Most people have little control over their career achievements.")
    question16 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="When it comes to doing something for the first time. I let others try it first before I take the initial risk.")
    question17 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="There are usually limits as to how far one can go.")
    question18 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="My coworkers would descrbe me as being more assertive than most.")
    question19 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="The opportunities that come with leading the way outweigh the risk one has to take in the process.")
    question20 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="'Bouncing back' from defeat is easier said than done.")
    question21 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Employees should not expect all employees to be hard-working and dependable.")
    question22 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="My coworkers would describe me as steady rather impulsive.")
    question23 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="When I am working on a project and I am confronted with an obstacle, I find that it is more effiecient to work around it rather than deal with it.")
    question24 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Some problems just can't be solved.")
    question25 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="When attending meetings or other work-related functions I tend to arrive early more than arrive right on time.")
    question26 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="People have less control over their lives than they think.")
    question27 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Being reliable is more important than being impulsive.")
    question28 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="More often than not, cautious people lose out in the long run.")
    question29 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Given today's Business environment as it used to be in order to stay employee.")
    question30 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Disorganizations does not bother me.")
    question31 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Co-workers should be treated as if they were one's customers.")
    question32 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Working cooperatively with others is easier said than done.")
    question33 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="I tend to resist change because, from myeperince, it is rarely for the better.")
    question34 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Spending time alone tends to bore me.")
    question35 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="I am more understanding than I am demanding.")
    question36 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Sometimes I can be selfish and think only of myself.")
    question37 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="I would describe myself as queit and reserved.")
    question38 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="I often create more work for myself by helping people out.")
    question39 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Adapting to change is easier said than done.")
    question40 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Employees who are resistant to learning new job functions, as requested by their supervisor, should be terminated.")
    question41 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Something positive usually comes out of a negative situation.")
    question42 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="I try not be too optimastic to avoid being disappointed if things don't work out.")
    question43 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Being critisized for poor performance only makes do better.")
    question44 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="When in a group meeting, I ussually like to sit back and listen rather than control the conversation.")
    question45 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="I am motivated more by people around me than by my own internal drive.")
    question46 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="My coworkers would describe me as a dominant person.")
    question47 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Sometimes being too persistent is not worth the effort because one may upset others along the way.")
    question48 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="I have a strong need to achieve.")
    question49 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="I tend to take control of mostconversations in which I am involved.")
    question50 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="In today's rapidly changing work wnvironment, setting career goals is often a waste of time.")
    question51 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Sometimes the risk of taking full responsibility for something is not worth the consequence of failure.")
    question52 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Employees who are predictable are boring.")
    question53 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="If I complete 8 out of 10 projects on schedule. I feel I have been successful.")
    question54 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Most organizations today do not care about the well-being of their employees.")
    question55 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="When I complete a project, I feel a greate sense of satisfaction and accomplishment.")
    question56 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Control is something we all have a little of.")
    question57 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="If a project is behind schedule, I try not to worry about it. Things like this usually get resolved on their own.")
    question58 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Employees absences put added pressure on the employer's coworkers.")
    question59 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="All people should be expected to reach realistic goals.")
    question60 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Sometimes, doing whatever it takes to get the job done is not worth the effort because one may annoy some people along the way.")

    def __str__(self):
        return str(self.job_request_exam_ccat)

class PRIApplicantTestARPInfo(models.Model):
    applicant_exam_arp = models.ForeignKey(PRIApplicantProfileInfo, on_delete=models.CASCADE, related_name='applicant_exam_arp_fk')
    job_request_exam_arp = models.ForeignKey(PRIApplicantJobRequestInfo, on_delete=models.CASCADE, related_name='job_request_exam_arp_fk')
    question1 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="There have been a few intances when I have questioned my own abilities.")
    question2 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="It is sometimes hard for me to continue my work if I am not motivated.")
    question3 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="If an employee is seen taking something that does not belong to him her, sometimes, it is best to keep quiet and not get involved.")
    question4 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="In general, I believe that the only way to get ahead is to play fair.")
    question5 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="It is understandable why people who work with money are more tempted to steal than those who don't work money.")
    question6 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Telling the complete truth is always the best way to handle any situation.")
    question7 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Today's working environment causes people to do things they noemally would not do.")
    question8 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Employee who are cought stealing from their employer should be terminated immediately rather than given a second chance.")
    question9 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="If a company finds out that is best employee lied about his/her credentials on the job application, the company should terminate the employee immidiately.")
    question10 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Most employers make too much out of illegal druf use in the workplace.")
    question11 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Sometimes the increase in work productivity that is observed is some people who use illegal drugs justifies their illegal drug us on the job.")
    question12 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Strict enforcement of drug testing policies will make for a safer workplace.")
    question13 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Illegal drug users are all more prone to engage in other unproductive behaviors on the job.")
    question14 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Being under the influence of illegal drugs at work is not as dangerous as everyone thinks.")
    question15 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="As long as employees continue to perform in safe and effective manner at work, whether or not they are under the influence of illegal drugs not be an issue.")
    question16 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="It is dificault for employees to perform in a satisfactory manner if they are under the influence of illegal drugs.")
    question17 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="In order to succeed in today's world, one has to break the rules a bit.")
    question18 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="If employees would have fewer policies and procedures, there would negative employee conduct.")
    question19 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="If a majority of employees disagree with their manager's policies they have the right to change them a little, as no one  gets hurt.")
    question20 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Most people have been fired from at least one previous job.")
    question21 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Rules were made to be questioned.")
    question22 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Employees who always do what they are told usually do so out of fear of being terminated.")
    question23 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="It takes great effort at times to stay within the rules.")
    question24 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Companies' policies tend to be too strict.To be productive, employees should not be as restricted as they usually are.")
    question25 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Most people truly care about others.")
    question26 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="In today's working environment it easy to feel good about the work that one does.")
    question27 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="The thought of hunting someone is a natural feeling.")
    question28 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="There is nothing wrong with behaving violently at work if one is being taken advantage of or being treated unfairly.")
    question29 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="It is natural to get involved in a pysical fight once in a while.")
    question30 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Most employers care about the welfare of their employees.")
    question31 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Some of my friends would consider me to have a short temper.")
    question32 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="I have never told a lie to void negative consequences.")
    question33 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="I sometimes disagree with the opinion of my manager.")
    question34 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="I sometimes get upset when things do not go my way")
    question35 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Being completely truthful about everything who potentially steal from them are wasting their time and money.")
    question36 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Compananies that try to screen out employees who could potentially steal from them are wasting their time and money.")
    question37 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Most employees feel that their employer treat them fairly.")
    question38 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Not telling the truth is sometimes a better way to avoid a conflict.")
    question39 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="When it is advantageous to lie, most people will.")
    question40 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="People's behaviors are usually guidedby the thought, 'What is in it for me?'")
    question41 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Most supervisors tend to believe what their employees have to say.")
    question42 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Much of the stealing that goes on in companies stems from the inequites that employees eperience.")
    question43 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Using illegal drugs at work every so often is not as serious a problem as using them on regular basis.")
    question44 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Even if nobody is getting hurt, the use of illegal drugs in the workplace should be looked at as a serious problem.")
    question45 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Working under the influence of illegal drugs is extreme dangerous and should never be attempted.")
    question46 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Illegal drug use at work  usually results in expensive consequences for the employer.")
    question47 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Managers and supervisors need to be more strict in enforcing illegal drug use policies.")
    question48 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Employers who use illegal drugs at work can usually function effectively.")
    question49 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Formal,illegal drug-use policies in the workplace are important for mainteaining a safe, drug free working environment.")
    question50 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Illegal drug-use work always leads to an unsafe working environment.")
    question51 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="While it is important to stick to company policies, bending the rules now and then is OK.")
    question52 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="People who bend the rules should be left alone as long as their job performance is satisfactory.")
    question53 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Sometimes irt is not worth taking the time to understand all of the company's rules.")
    question54 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="People who are always testing their supervisors are annoying.")
    question55 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Few employees do exactly as their supervisors ask them to do.")
    question56 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Co-workers will tend to go behind another's back if something good will come out of it.")
    question57 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="It is almost impossible to keep employees happy all of the time.")
    question58 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="There are no legitimate reasons for ever hitting anyone.")
    question59 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="No matter how unfairly one is treated, one should never resort to physical harm.")
    question60 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Sexual harrasment is a form of hostle behavior.")
    question61 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="There are times when get the urge to strike someone.")
    question62 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="If I am provoked enough, I may hit another person.")
    question63 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="There have been times when I have been oushed so far tha I have had to strike the person(s).")
    question64 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="Fighters back is always the best way to handle a potentially violent situation.")
    question65 = models.CharField(max_length = 250, choices=CHOICE_LIST, default=CHOICE_LIST[0], verbose_name="I tend to get into arguments when others disaper with me.")
    
    def __str__(self):
        return str(self.job_request_exam_arp)

# Exam Scores

STATUS_LIST = (
    ('Passed','Passed'),
    ('Failed','Failed'),
    ('On progress','On progress'),
)

RATINGS_LIST = (
    ('Outstanding','Outstanding'),
    ('Average','Average'),
    ('Below Average','Below Average'),
    ('Poor','Poor'),
    ('On progress','On progress'),
)

class PRIApplicantExamScoreT1PEInfo(models.Model):
    applicant_exam_score_t1pe = models.ForeignKey(PRIApplicantProfileInfo, on_delete=models.CASCADE, related_name='applicant_exam_score_t1pe_fk')
    job_request_exam_score_t1pe = models.ForeignKey(PRIApplicantJobRequestInfo, on_delete=models.CASCADE, related_name='job_request_exam_score_t1pe_fk')
    score_t1pe = models.PositiveIntegerField()
    over_t1pe = models.PositiveIntegerField()
    status_t1pe = models.CharField(max_length=50, choices=STATUS_LIST) 
    ratings_t1pe = models.CharField(max_length=50, choices=RATINGS_LIST)
    allow_retake_t1pe = models.BooleanField(default=True)
    date_taken_t1pe = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.job_request_exam_score_t1pe)

class PRIApplicantExamScoreT2SEInfo(models.Model):
    applicant_exam_score_t2se = models.ForeignKey(PRIApplicantProfileInfo, on_delete=models.CASCADE, related_name='applicant_exam_score_t2se_fk')
    job_request_exam_score_t2se = models.ForeignKey(PRIApplicantJobRequestInfo, on_delete=models.CASCADE, related_name='job_request_exam_score_t2se_fk')
    score_t2se = models.PositiveIntegerField()
    over_t2se = models.PositiveIntegerField()
    status_t2se = models.CharField(max_length=50, choices=STATUS_LIST) 
    ratings_t2se = models.CharField(max_length=50, choices=RATINGS_LIST)
    allow_retake_t2se = models.BooleanField(default=True)
    date_taken_t2se = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.job_request_exam_score_t2se)

class PRIApplicantExamScoreT3EInfo(models.Model):
    applicant_exam_score_t3e = models.ForeignKey(PRIApplicantProfileInfo, on_delete=models.CASCADE, related_name='applicant_exam_score_t3e_fk')
    job_request_exam_score_t3e = models.ForeignKey(PRIApplicantJobRequestInfo, on_delete=models.CASCADE, related_name='job_request_exam_score_t3e_fk')
    score_t3e = models.PositiveIntegerField()
    over_t3e = models.PositiveIntegerField()
    status_t3e = models.CharField(max_length=50, choices=STATUS_LIST) 
    ratings_t3e = models.CharField(max_length=50, choices=RATINGS_LIST)
    allow_retake_t3e = models.BooleanField(default=True)
    date_taken_t3e = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.job_request_exam_score_t3e)
    
class PRIApplicantExamScoreT3PTSCTInfo(models.Model):
    applicant_exam_score_t3ptsct = models.ForeignKey(PRIApplicantProfileInfo, on_delete=models.CASCADE, related_name='applicant_exam_score_t3ptsct_fk')
    job_request_exam_score_t3ptsct = models.ForeignKey(PRIApplicantJobRequestInfo, on_delete=models.CASCADE, related_name='job_request_exam_score_t3ptsct_fk')
    score_t3ptsct = models.PositiveIntegerField()
    over_t3ptsct = models.PositiveIntegerField()
    status_t3ptsct = models.CharField(max_length=50, choices=STATUS_LIST) 
    ratings_t3ptsct = models.CharField(max_length=50, choices=RATINGS_LIST)
    allow_retake_t3ptsct = models.BooleanField(default=True)
    date_taken_t3ptsct = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.job_request_exam_score_t3ptsct)

class PRIApplicantExamScoreT4ARInfo(models.Model):
    applicant_exam_score_t4ar = models.ForeignKey(PRIApplicantProfileInfo, on_delete=models.CASCADE, related_name='applicant_exam_score_t4ar_fk')
    job_request_exam_score_t4ar = models.ForeignKey(PRIApplicantJobRequestInfo, on_delete=models.CASCADE, related_name='job_request_exam_score_t4ar_fk')
    score_t4ar = models.PositiveIntegerField()
    over_t4ar = models.PositiveIntegerField()
    status_t4ar = models.CharField(max_length=50, choices=STATUS_LIST) 
    ratings_t4ar = models.CharField(max_length=50, choices=RATINGS_LIST)
    allow_retake_t4ar = models.BooleanField(default=True)
    date_taken_t4ar = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.job_request_exam_score_t4ar)

class PRIApplicantExamScoreCCAInfo(models.Model):
    applicant_exam_score_cca = models.ForeignKey(PRIApplicantProfileInfo, on_delete=models.CASCADE, related_name='applicant_exam_score_cca_fk')
    job_request_exam_score_cca = models.ForeignKey(PRIApplicantJobRequestInfo, on_delete=models.CASCADE, related_name='job_request_exam_score_cca_fk')
    score_cca = models.PositiveIntegerField()
    over_cca = models.PositiveIntegerField()
    status_cca = models.CharField(max_length=50, choices=STATUS_LIST) 
    ratings_cca = models.CharField(max_length=50, choices=RATINGS_LIST)
    allow_retake_cca = models.BooleanField(default=True)
    date_taken_cca = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.job_request_exam_score_cca)

class PRIApplicantExamScoreARPInfo(models.Model):
    applicant_exam_score_arp = models.ForeignKey(PRIApplicantProfileInfo, on_delete=models.CASCADE, related_name='applicant_exam_score_arp_fk')
    job_request_exam_score_arp = models.ForeignKey(PRIApplicantJobRequestInfo, on_delete=models.CASCADE, related_name='job_request_exam_score_arp_fk')
    score_arp = models.PositiveIntegerField()
    over_arp = models.PositiveIntegerField()
    status_arp = models.CharField(max_length=50, choices=STATUS_LIST) 
    ratings_arp = models.CharField(max_length=50, choices=RATINGS_LIST)
    allow_retake_arp = models.BooleanField(default=True)
    date_taken_arp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.job_request_exam_score_arp)
        
class PRIApplicantExamScoreSCCTInfo(models.Model):
    applicant_exam_score_scct = models.ForeignKey(PRIApplicantProfileInfo, on_delete=models.CASCADE, related_name='applicant_exam_score_scct_fk')
    job_request_exam_score_scct = models.ForeignKey(PRIApplicantJobRequestInfo, on_delete=models.CASCADE, related_name='job_request_exam_score_scct_fk')
    score_scct = models.PositiveIntegerField()
    over_scct = models.PositiveIntegerField()
    status_scct = models.CharField(max_length=50, choices=STATUS_LIST) 
    ratings_scct = models.CharField(max_length=50, choices=RATINGS_LIST)
    allow_retake_scct = models.BooleanField(default=True)
    date_taken_scct = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.job_request_exam_score_scct)
"""
------------------------
******Examinations******
------------------------
"""

"""
------------------------
******Scores******
------------------------
"""

"""
category: others/janitor


job description
job qualifications
job responsibilities
company overview

deadline

min exp
salary




------------------ to be inherit
company
logo
location
------------------
search category:
job title
location
spcialization
min salary php
"""

"""
---
---PERSONAL PROFILE----
---
image~
attachment of cv~
date field ~
position desired~
company assigned~
 
how did you know us? (Referral, Online Job Portal, Leaflets, Walk-in, Job fair)~
first name~
middle name~
last name~
contact no (mobile)~
contact no (tel)~
present address - bldg name, brgy sub, district municipality, city/province
permannet address - bldg name, brgy sub, district municipality, city/province
gender ~
civil status (single, married, divorced, widowed, separated)
weight (lbs)
height (inch)
shirt size
shoe size
waistline
lenght of pants

SSS (10digits)
CTC (8digits)
philhealth(12digits)
TIN(1st 9digits)
Pagi-ibig(12digits)

if married spose name
spouse contact #
children name/age

father's name
father occupation
father home address

mother's name
mother occupation
mother home address

siblings - 1-10
name
age
occupation/company


---
---EMPLOYMENT HISTORY----5 only
---
from
to
employer/company name
position
reason for leaving
basic salary rate

---
---EDUCATIONAL ATTAINMENT----
---
name of school/ college/ university
address
school years attended (from-to)
college
course
-collage address
vacational
course
-vacational address

highschool
highschool address

elementary
elem address
special skills
language speak

---
---Traning, Seminars & Workshop----
---

name or title of the training/sem/workshop
dates attended

---
---Character references---- 3 max
---

complete name,
occupation/company
contact no


Do you have a relative by any degree by consangunity or affinty working with poerlane or any of its client?
IF yes state the name of your relative , position/company name.

Have you been confined in a medical facility due to illness, dreaded/contagious disease, or minor/major surgery?
if yes, what disease/illness when & name of the medical facility

Have you ever been changed or sentenced by any court of law of any crime?
if Yes, please give details.

Have you in the past applied at powerlane or any of its client & was not hired nor employed?
if yes when and state the reason.


"""

#For testing
#score tracking
#progress tracking
#pts for each question
#dynamin questions and choices
#clock
#editable
#randomize
#choices if multiple choice, single choice, essay, image
class ExaminationInfo(models.Model):
    exam_type = models.CharField(max_length=50)

    def __str__(self):
        return self.exam_type

class QuestionInfo(models.Model):

    examination = models.ForeignKey(ExaminationInfo, on_delete=models.CASCADE, related_name='exam_question_fk')
    question = models.CharField(max_length=100)

    def __str__(self):
        return self.question

class ChoicesInfo(models.Model):

    question = models.ForeignKey(QuestionInfo, on_delete=models.CASCADE, related_name='question_choices_fk')
    choice = models.CharField(max_length=250)

    def __str__(self):
        return self.choice
