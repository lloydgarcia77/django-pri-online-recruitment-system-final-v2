from django import forms
from django.forms import formset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PRIUserInfo, PRIUserPermission, PRIClientsInfo, PRIRequestInfo, PRIJobVacancyInfo, PRIJobVacancyJobQualificationsInfo, PRIJobVacancyJobResponsibilitiesInfo, ExaminationInfo, QuestionInfo, ChoicesInfo, PRIApplicantProfileInfo, PRIApplicantSibilingsInfo, PRIApplicantEmploymentHistoryInfo, PRIApplicantEducationalAttainmentInfo, PRIApplicantTrainingsInfo, PRIApplicantCharacterReferencesInfo, PRIApplicantTest3EssayInfo, PRIApplicantTest3SCTInfo, PRIApplicantTestSSCTInfo, PRIApplicantTestCCATInfo, PRIApplicantTestARPInfo
from decimal import Decimal

class PRIUserAccountRegistrationForm(UserCreationForm):

    email = forms.EmailField(label='Email')

    class Meta():
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(PRIUserAccountRegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs = {
            'class': 'form-control form-control-danger',
            'placeholder': 'Username',
            'required': 'required',
            'autofocus': 'autofocus',
        }

        self.fields['email'].widget.attrs = {
            'type': 'email',
            'class': 'form-control',
            'placeholder': 'Email',
            'required': 'required',
            'autofocus': 'autofocus',
            'style': 'color: #000000',
        }

        self.fields['password1'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Password',
            'required': 'required',
            'autofocus': 'autofocus',
        }

        self.fields['password2'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Password',
            'required': 'required',
            'autofocus': 'autofocus',
        }

class PRIUserProfileRegistrationForm(forms.ModelForm):

    class Meta():
        model = PRIUserInfo
        exclude = ("user", "date_added")

    GENDER_LIST = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    # dob = forms.DateField(
    #     widget=forms.DateInput(
    #         format='%b %d %Y',
    #         attrs={
    #             'id': 'dob',
    #         }
    #     ),
    #     input_formats=('%b %d %Y', )
    # )

    image = forms.ImageField(widget=forms.FileInput, required=False)

    gender = forms.ChoiceField(choices=GENDER_LIST, widget=forms.RadioSelect, initial='Male', )

    def __init__(self, *args, **kwargs):
        super(PRIUserProfileRegistrationForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs = {
            'class': 'form-control form-control-danger',
            'placeholder': 'First name',
            'required': 'required',
            'autofocus': 'autofocus',
        }

        self.fields['middle_name'].widget.attrs = {
            'class': 'form-control form-control-danger',
            'placeholder': 'Middle name',
            'required': 'required',
            'autofocus': 'autofocus',
        }

        self.fields['last_name'].widget.attrs = {
            'class': 'form-control form-control-danger',
            'placeholder': 'Last name',
            'required': 'required',
            'autofocus': 'autofocus',
        }

        self.fields['age'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Age',
            'required': 'required',
            'autofocus': 'autofocus',
            'maxlength': '2',
        }


        self.fields['gender'].widget.attrs = {
            'class': 'form-control',
            'required': 'required',
        }

        self.fields['contact'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Contact',
            'required': 'required',
            'autofocus': 'autofocus',
            'maxlength': '12',
        }



        self.fields['address'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Address',
            'required': 'required',
            'autofocus': 'autofocus',
        }

        self.fields['position'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'position',
            'required': 'required',
            'autofocus': 'autofocus',
        }

        self.fields['department'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'department',
            'required': 'required',
            'autofocus': 'autofocus',
        }

        self.fields['level'].widget.attrs = {
            'class': 'form-control',
            'autofocus': 'autofocus',
        }

        self.fields['image'].widget.attrs = {
            'id': 'profilePicture',
            'type': 'file',
            'name': 'file',
            'style': 'display: none;',
        }

class PRIUserPermissionForm(forms.ModelForm):

    class Meta:
        model = PRIUserPermission
        exclude = ("pri_user", )

class PRIClientForm(forms.ModelForm):
    client_company_logo = forms.ImageField(widget=forms.FileInput, required=False)
    class Meta:
        model = PRIClientsInfo
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(PRIClientForm, self).__init__(*args, **kwargs)

        self.fields['client_company_logo'].widget.attrs = {
            'class': 'form-control',
            'type': 'file',
            'name': 'file',
        }

class PRIRequestForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'width': "100%", 'cols': "20", 'rows': "10", }))

    class Meta:
        model = PRIRequestInfo
        #fields = '__all__'
        exclude = ('seen_by_admin', )

class PRIClientRequestForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'width': "100%", 'cols': "20", 'rows': "10", }))

    class Meta:
        model = PRIRequestInfo
        #fields = '__all__'
        exclude = ('seen_by_admin', 'requested_client', 'status',)

class PRIJobVacancyForm(forms.ModelForm):
    job_company_overview = forms.CharField(widget=forms.Textarea(attrs={'width': "100%", 'cols': "20", 'rows': "5", }))
    job_description = forms.CharField(widget=forms.Textarea(attrs={'width': "100%", 'cols': "20", 'rows': "5", }))
    job_salary = forms.DecimalField(max_digits=12, decimal_places=2, initial=Decimal("0.00"), required=True)

    job_deadline = forms.DateField(
        widget=forms.DateInput(
            format='%b %d %Y',
            attrs={
                'id': 'job_deadline',
            }
        ), input_formats=('%b %d %Y', )
    )

    class Meta:
        model = PRIJobVacancyInfo
        #fields = '__all__'
        exclude = ('client_request', 'secure_id', )

    def __init__(self, *args, **kwargs):
        super(PRIJobVacancyForm, self).__init__(*args, **kwargs)

        self.fields['job_deadline'].widget.attrs = {
            'id': 'job_deadline',
            'class': 'form-control',
            'placeholder': 'Deadline',
            'required': 'required',
            'autofocus': 'autofocus',
        }

class PRIJobVacancyJobQualificationsForm(forms.ModelForm):

    class Meta:
        model = PRIJobVacancyJobQualificationsInfo
        #fields = '__all__'
        exclude = ('job_vacancy_jq',)

    def __init__(self, *args, **kwargs):
        super(PRIJobVacancyJobQualificationsForm, self).__init__(*args, **kwargs)

        self.fields['job_qualifications'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Enter Job Qualifications',
        }

#JobVacancyJobQualificationsFormset = formset_factory(PRIJobVacancyJobQualificationsForm, extra=1, can_delete=True)

class PRIJobVacancyJobResponsibilitiesForm(forms.ModelForm):

    class Meta:
        model = PRIJobVacancyJobResponsibilitiesInfo
        #fields = '__all__'
        exclude = ('job_vacancy_jr',)

    def __init__(self, *args, **kwargs):
        super(PRIJobVacancyJobResponsibilitiesForm, self).__init__(*args, **kwargs)

        self.fields['job_responsibilities'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Enter Job Responsibilities',
        }
#JobVacancyJobResponsibilitiesFormset = formset_factory(PRIJobVacancyJobResponsibilitiesForm, extra=1, can_delete=True)

#For applicant side

class PRIApplicantProfileForm(forms.ModelForm):

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

    # gender = forms.ChoiceField(choices=GENDER_LIST, widget=forms.RadioSelect, initial='Single')
    mobile_no = forms.IntegerField(required=False)
    telephone_no = forms.IntegerField(required=False)
    spouse_contact_number = forms.IntegerField(initial=0)
    image = forms.ImageField(widget=forms.FileInput, required=False)
    cv = forms.FileField(widget=forms.FileInput, required=False, label="Resume/Curriculum Vitae (Optional):") 
    class Meta:
        model = PRIApplicantProfileInfo
        exclude = ("user", "date_filled", "slug", "position_desired", "company_assigned", "secure_key_id")

    def __init__(self, *args, **kwargs):
        super(PRIApplicantProfileForm, self).__init__(*args, **kwargs)

        # self.fields['position_desired'].widget.attrs = {
        #     'class': 'form-control',
        #     'placeholder': 'Position Desired',
        #     'required': 'required',
        #     'autofocus': 'autofocus',
        #     'maxlength' : '200',
        # }

        # self.fields['company_assigned'].widget.attrs = {
        #     'class': 'form-control',
        #     'placeholder': 'Company Assigned',
        #     'required': 'required',
        #     'autofocus': 'autofocus',
        #     'maxlength' : '200',
        # }

        self.fields['fname'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'First Name',
            'required': 'required',
            'autofocus': 'autofocus',
            'maxlength' : '200',
        } 

        self.fields['mname'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Middle Name',
            'required': 'required',
            'autofocus': 'autofocus',
            'maxlength' : '200',
        }

        self.fields['lname'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Last Name',
            'required': 'required',
            'autofocus': 'autofocus',
            'maxlength' : '200',
        }

        self.fields['mobile_no'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Mobile No',
            # 'required': 'required',
            'autofocus': 'autofocus',
            'onKeyPress' : 'if(this.value.length==12) return false;',       
            'onkeydown': 'javascript: return event.keyCode == 69 ? false : true',
        }
        
        self.fields['telephone_no'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Telephone No',
            # 'required': 'required',
            'autofocus': 'autofocus',
            'onKeyPress' : 'if(this.value.length==12) return false;', 
            'onkeydown': 'javascript: return event.keyCode == 69 ? false : true',
        }
        # Contact person

        self.fields['contact_person'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Contact Person',
            'autofocus': 'autofocus',
            'maxlength' : '200',
        }

        self.fields['relationship'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Relationship',
            'autofocus': 'autofocus',
            'maxlength' : '200',
        }

        self.fields['contact_person_mobile_no'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Contact Person Mobile No',
            'autofocus': 'autofocus',
            'onKeyPress' : 'if(this.value.length==12) return false;', 
            'onkeydown': 'javascript: return event.keyCode == 69 ? false : true',
        }

        #Present Address

        self.fields['bldg_name_0'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Building Name',
            # 'required': 'required',
            'autofocus': 'autofocus',
            'maxlength' : '150',
        }

        self.fields['brgy_sub_0'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Barangay/Subdivision',
            # 'required': 'required',
            'autofocus': 'autofocus',
            'maxlength' : '150',
        }

        self.fields['dis_mun_0'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'District/Municipality',
            # 'required': 'required',
            'autofocus': 'autofocus',
            'maxlength' : '150',
        }

        self.fields['cit_pro_0'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'City/Province',
            # 'required': 'required',
            'autofocus': 'autofocus',
            'maxlength' : '150',
        }

        #Permanent Address
        self.fields['bldg_name_1'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Building Name',
            # 'required': 'required',
            'autofocus': 'autofocus',
            'maxlength' : '150',
        }

        self.fields['brgy_sub_1'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Barangay/Subdivision',
            # 'required': 'required',
            'autofocus': 'autofocus',
            'maxlength' : '150',
        }

        self.fields['dis_mun_1'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'District/Municipality',
            # 'required': 'required',
            'autofocus': 'autofocus',
            'maxlength' : '150',
        }

        self.fields['cit_pro_1'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'City/Province',
            # 'required': 'required',
            'autofocus': 'autofocus',
            'maxlength' : '150',
        }
        
        #Body measurement

        self.fields['weight'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Weight',
            'autofocus': 'autofocus',
            'onKeyPress' : 'if(this.value.length==3) return false;', 
            'onkeydown': 'javascript: return event.keyCode == 69 ? false : true',
        }

        self.fields['height'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Height',
            'autofocus': 'autofocus',
            'onKeyPress' : 'if(this.value.length==3) return false;', 
            'onkeydown': 'javascript: return event.keyCode == 69 ? false : true',
        }

        self.fields['shirt_size'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Shirt Size',
            'autofocus': 'autofocus',
            'onKeyPress' : 'if(this.value.length==3) return false;', 
            'onkeydown': 'javascript: return event.keyCode == 69 ? false : true',
        }

        self.fields['shoe_size'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Shoe Size',
            'autofocus': 'autofocus',
            'onKeyPress' : 'if(this.value.length==3) return false;', 
            'onkeydown': 'javascript: return event.keyCode == 69 ? false : true',
        }

        self.fields['waistline'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Waistline',
            'autofocus': 'autofocus',
            'onKeyPress' : 'if(this.value.length==3) return false;', 
            'onkeydown': 'javascript: return event.keyCode == 69 ? false : true',
        }

        self.fields['length_of_pants'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Length of pants',
            'autofocus': 'autofocus',
            'onKeyPress' : 'if(this.value.length==3) return false;', 
            'onkeydown': 'javascript: return event.keyCode == 69 ? false : true',
        }

        #Government

        self.fields['sss'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'SSS',
            'autofocus': 'autofocus',
            'onKeyPress' : 'if(this.value.length==10) return false;', 
            'onkeydown': 'javascript: return event.keyCode == 69 ? false : true',
        }
        self.fields['ctc'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'CTC',
            'autofocus': 'autofocus',
            'onKeyPress' : 'if(this.value.length==8) return false;', 
            'onkeydown': 'javascript: return event.keyCode == 69 ? false : true',
        }
        self.fields['philhealth'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Philhealth',
            'autofocus': 'autofocus',
            'onKeyPress' : 'if(this.value.length==12) return false;', 
            'onkeydown': 'javascript: return event.keyCode == 69 ? false : true',
        }
        self.fields['tin'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'TIN',
            'autofocus': 'autofocus',
            'onKeyPress' : 'if(this.value.length==9) return false;', 
            'onkeydown': 'javascript: return event.keyCode == 69 ? false : true',
        }
        self.fields['pagibig'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Pagibig',
            'autofocus': 'autofocus',
            'onKeyPress' : 'if(this.value.length==12) return false;', 
            'onkeydown': 'javascript: return event.keyCode == 69 ? false : true',
        }

        #Spouse
        self.fields['spouse_full_name'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Spouse full name',
            'autofocus': 'autofocus',
            'maxlength' : '50',
            'readonly': 'readonly',
        }

        self.fields['spouse_contact_number'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Spouse Contact Number',
            'autofocus': 'autofocus',
            'onKeyPress' : 'if(this.value.length==12) return false;', 
            'onkeydown': 'javascript: return event.keyCode == 69 ? false : true',
            'readonly': 'readonly',
        }

        self.fields['father_full_name'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Father full name',
            'autofocus': 'autofocus',
            'maxlength' : '50',
        }

        self.fields['father_occupation'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Father Occupation',
            'autofocus': 'autofocus',
            'maxlength' : '50',
        }

        self.fields['father_home_address'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Father Home Address',
            'autofocus': 'autofocus',
            'maxlength' : '50',
        }
        
        self.fields['mother_full_name'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Mother full name',
            'autofocus': 'autofocus',
            'maxlength' : '50',
        }

        self.fields['mother_occupation'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Mother Occupation',
            'autofocus': 'autofocus',
            'maxlength' : '50',
        }

        self.fields['mother_home_address'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Mother Home Address',
            'autofocus': 'autofocus',
            'maxlength' : '50',
        }

        
        

class PRIApplicantSibilingsForm(forms.ModelForm):
    class Meta:
        model = PRIApplicantSibilingsInfo
        exclude = ("applicant_siblings",)

    def __init__(self, *args, **kwargs):
        super(PRIApplicantSibilingsForm, self).__init__(*args, **kwargs)        

        
        self.fields['name'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Name of Siblings', 
            'autofocus': 'autofocus',
            'maxlength' : '50',
        }

         
        self.fields['occ'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Occupation/Company', 
            'autofocus': 'autofocus',
            'maxlength' : '50',
        }

        self.fields['age'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Age', 
            'autofocus': 'autofocus',
            'onKeyPress' : 'if(this.value.length==2) return false;', 
            'onkeydown': 'javascript: return event.keyCode == 69 ? false : true',
        }


class PRIApplicantEmploymentHistoryForm(forms.ModelForm):
    date_from = forms.DateField(
        widget=forms.DateInput(
            format='%b %d %Y',  
        ),
        input_formats=('%b %d %Y', )
    )

    date_to = forms.DateField(
        widget=forms.DateInput(
            format='%b %d %Y', 
        ),
        input_formats=('%b %d %Y', )
    )
    class Meta:
        model = PRIApplicantEmploymentHistoryInfo
        exclude = ("applicant_employment_history", )

    def __init__(self, *args, **kwargs):
        super(PRIApplicantEmploymentHistoryForm, self).__init__(*args, **kwargs)        

        self.fields['company'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Company', 
            'autofocus': 'autofocus',
            'maxlength' : '50',
        }

        self.fields['position'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Position', 
            'autofocus': 'autofocus',
            'maxlength' : '50',
        }

        self.fields['reason_for_leaving'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Reason for leaving', 
            'autofocus': 'autofocus',
            'maxlength' : '50',
        }

        self.fields['date_from'].widget.attrs = {
            'class': 'form-control mydatepicker',
            'placeholder': 'Date from', 
            'autofocus': 'autofocus',
            'readonly': 'readonly',
        }

        self.fields['date_to'].widget.attrs = {
            'class': 'form-control mydatepicker',
            'placeholder': 'Date To', 
            'autofocus': 'autofocus',
            'readonly': 'readonly',
        }

        self.fields['basic_salary_pay'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Basic Salary Payment', 
            'autofocus': 'autofocus',
            'onKeyPress' : 'if(this.value.length==7) return false;', 
            'onkeydown': 'javascript: return event.keyCode == 69 ? false : true',
        }

class PRIApplicantEducationalAttainmentForm(forms.ModelForm):
    #college
    csya_from = forms.DateField(
        widget=forms.DateInput(
            format='%b %d %Y',  
        ),
        input_formats=('%b %d %Y', ), label="From",
        required=False,
    )

    csya_to = forms.DateField(
        widget=forms.DateInput(
            format='%b %d %Y', 
        ),
        input_formats=('%b %d %Y', )
        , label="To",
        required=False,
    )
    #vocational
    vsya_from = forms.DateField(
        widget=forms.DateInput(
            format='%b %d %Y',  
        ),
        input_formats=('%b %d %Y', ), label="From",
        required=False,
    )

    vsya_to = forms.DateField(
        widget=forms.DateInput(
            format='%b %d %Y', 
        ),
        input_formats=('%b %d %Y', ), label="To",
        required=False,
    )
    #highschool

    hsya_from = forms.DateField(
        widget=forms.DateInput(
            format='%b %d %Y',  
        ),
        input_formats=('%b %d %Y', ), label="From",
        required=False,
    )

    hsya_to = forms.DateField(
        widget=forms.DateInput(
            format='%b %d %Y', 
        ),
        input_formats=('%b %d %Y', ), label="To",
        required=False,
    )
    #elementary

    esya_from = forms.DateField(
        widget=forms.DateInput(
            format='%b %d %Y',  
        ),
        input_formats=('%b %d %Y', ), label="From",
        required=False,
    )

    esya_to = forms.DateField(
        widget=forms.DateInput(
            format='%b %d %Y', 
        ),
        input_formats=('%b %d %Y', ), label="To",
        required=False,
    )


    class Meta:
        model = PRIApplicantEducationalAttainmentInfo
        exclude = ("applicant_educational_attainment", )

    def __init__(self, *args, **kwargs):
        super(PRIApplicantEducationalAttainmentForm, self).__init__(*args, **kwargs)   

        self.fields['college'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Name of school',
            'autofocus': 'autofocus',
            'maxlength' : '50',
        }

        self.fields['college_course'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'College Course',
            'autofocus': 'autofocus',
            'maxlength' : '50',
        }

        self.fields['college_address'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'College Address',
            'autofocus': 'autofocus',
            'maxlength': '250',
        }

        self.fields['csya_from'].widget.attrs = {
            'id': 'c_date_from',
            'class': 'form-control',
            'placeholder': 'Date from',
            'autofocus': 'autofocus',
            'readonly': 'readonly',
        }

        
        self.fields['csya_to'].widget.attrs = {
            'id': 'c_date_to',
            'class': 'form-control',
            'placeholder': 'Date to',
            'autofocus': 'autofocus',
            'readonly': 'readonly',
        }
            
        self.fields['vocational'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Name of school',
            'autofocus': 'autofocus',
            'maxlength' : '50',
        }

        self.fields['vocational_course'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Vocational Course',
            'autofocus': 'autofocus',
            'maxlength' : '50',
        }

        self.fields['vocational_address'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Vocational Address',
            'autofocus': 'autofocus',
            'maxlength': '250',
        }

        self.fields['vsya_from'].widget.attrs = {
            'id': 'v_date_from',
            'class': 'form-control',
            'placeholder': 'Date from',
            'autofocus': 'autofocus',
            'readonly': 'readonly',
        }

        
        self.fields['vsya_to'].widget.attrs = {
            'id': 'v_date_to',
            'class': 'form-control',
            'placeholder': 'Date to',
            'autofocus': 'autofocus',
            'readonly': 'readonly',
        }

        self.fields['highschool'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Highschool',
            'autofocus': 'autofocus',
            'maxlength' : '50',
        }

        self.fields['highschool_address'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Highschool Address',
            'autofocus': 'autofocus',
            'maxlength': '250',
        }

        
        self.fields['hsya_from'].widget.attrs = {
            'id': 'h_date_from',
            'class': 'form-control',
            'placeholder': 'Date from',
            'autofocus': 'autofocus',
            'readonly': 'readonly',
        }

        
        self.fields['hsya_to'].widget.attrs = {
            'id': 'h_date_to',
            'class': 'form-control',
            'placeholder': 'Date to',
            'autofocus': 'autofocus',
            'readonly': 'readonly',
        }

        self.fields['elementary'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Elementary',
            'autofocus': 'autofocus',
            'maxlength' : '50',
        }

        self.fields['elementary_address'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Elementary Address',
            'autofocus': 'autofocus',
            'maxlength': '250',
        }

        self.fields['esya_from'].widget.attrs = {
            'id': 'e_date_from',
            'class': 'form-control',
            'placeholder': 'Date from',
            'autofocus': 'autofocus',
            'readonly': 'readonly',
        }

        
        self.fields['esya_to'].widget.attrs = {
            'id': 'e_date_to',
            'class': 'form-control',
            'placeholder': 'Date to',
            'autofocus': 'autofocus',
            'readonly': 'readonly',
        }

        self.fields['special_skills'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Special Skills',
            'autofocus': 'autofocus',
            'maxlength': '250',
        }

        self.fields['language_speak'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Language Speak',
            'autofocus': 'autofocus',
            'maxlength': '250',
        }

class PRIApplicantTrainingsForm(forms.ModelForm):

    date_attended = forms.DateField(
        widget=forms.DateInput(
            format='%b %d %Y',  
        ),
        input_formats=('%b %d %Y', )
    )
 
    class Meta:
        model = PRIApplicantTrainingsInfo
        exclude = ("applicant_trainings", )

    def __init__(self, *args, **kwargs):
        super(PRIApplicantTrainingsForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs = {
            'class': 'form-control ',
            'placeholder': 'Title',
            'autofocus': 'autofocus',
            'maxlength': '50',
        }

        self.fields['date_attended'].widget.attrs = { 
            'class': 'form-control mydatepicker',
            'placeholder': 'Date Attended',
            'autofocus': 'autofocus',
            'readonly': 'readonly',
        }
 

class PRIApplicantCharacterReferencesForm(forms.ModelForm):
    class Meta:
        model = PRIApplicantCharacterReferencesInfo
        exclude = ("applicant_character_references", )
    
    contact_no = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super(PRIApplicantCharacterReferencesForm, self).__init__(*args, **kwargs)

        self.fields['full_name'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Full Name', 
            'autofocus': 'autofocus',
            'maxlength': '50',
        }

        self.fields['occupation'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Occupation', 
            'autofocus': 'autofocus',
            'maxlength': '50',
        }

        self.fields['contact_no'].widget.attrs = {
            'class': 'form-control',
            'placeholder': 'Contact No', 
            'autofocus': 'autofocus',
            'onKeyPress' : 'if(this.value.length==12) return false;', 
            'onkeydown': 'javascript: return event.keyCode == 69 ? false : true',
        }

class PRIApplicantTest3EssayForm(forms.ModelForm):
    class Meta:
        model = PRIApplicantTest3EssayInfo
        exclude = ("applicant_exam", "job_request_exam", )

class PRIApplicantTest3SCTForm(forms.ModelForm):
    class Meta:
        model = PRIApplicantTest3SCTInfo
        exclude = ("applicant_exam_sct", "job_request_exam_sct", )
        
class PRIApplicantTestSSCTForm(forms.ModelForm):
    class Meta:
        model = PRIApplicantTestSSCTInfo
        exclude = ("applicant_exam_ssct", "job_request_exam_ssct", )

CHOICE_LIST = (
    ('Strongly Agree', 'Strongly Agree'),
    ('Agree', 'Agree'),
    ('Neutral', 'Neutral'),
    ('Disagree', 'Disagree'),
    ('Strongly Disagree', 'Strongly Disagree'),
)

class PRIApplicantTestCCATForm(forms.ModelForm):    
    class Meta:
        model = PRIApplicantTestCCATInfo
        exclude = ("applicant_exam_ccat", "job_request_exam_ccat", )

class PRIApplicantTestARPForm(forms.ModelForm):
    class Meta:
        model = PRIApplicantTestARPInfo
        exclude = ("applicant_exam_arp", "job_request_exam_arp", )



#For testing

class ExaminationForm(forms.ModelForm):
    class Meta:
        model = ExaminationInfo
        fields = '__all__'

class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionInfo
        fields = '__all__'

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = ChoicesInfo
        fields = '__all__'



