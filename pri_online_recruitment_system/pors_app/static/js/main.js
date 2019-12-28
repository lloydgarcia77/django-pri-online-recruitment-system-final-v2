$(document).ready(function () {

    //FOR PRI ADMIN PROFILE UPDATE 

    var ShowPRIAdminProfileUpdateForm = function (e) {
        e.preventDefault();


        var button = $(this);
        $.ajax({
            url: button.attr("data-url"),
            type: 'GET',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-form").modal("show");
            },
            success: function (data) {
                $("#modal-form .modal-content").html(data.html_form);
            }
        });

    }

    var SavePRIAdminProfileUpdateForm = function (e) {
        e.preventDefault();

        var form = $(this);
        var formData = false;

        if (window.FormData) {
            formData = new FormData(form[0]);
        }

        $.ajax({
            url: form.attr("data-url"),
            data: formData ? formData : form.serialize(),
            cache: false,
            contentType: false,
            processData: false,
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#modal-form").modal("hide");
                    $("#table_admin tbody").html(data.table_records_admin);
                    $("#pagination_admin").html(data.pagination_admin);
                } else {
                    $("#modal-form .modal-content").html(data.html_form);
                }
            }
        });

        return false;
    }


    $(".show-form-create-admin").on("click", ShowPRIAdminProfileUpdateForm);
    $("#modal-form").on("submit", ".pri-admin-users-create-form", SavePRIAdminProfileUpdateForm);

    $("#table_admin").on('click', '.show-form-edit-admin', ShowPRIAdminProfileUpdateForm);
    $("#modal-form").on("submit", ".update-profile-form", SavePRIAdminProfileUpdateForm);

    $("#table_admin").on('click', '.show-form-delete-admin', ShowPRIAdminProfileUpdateForm);
    $("#modal-form").on("submit", ".delete-profile-form", SavePRIAdminProfileUpdateForm);


    var ImgSrc;

    function readImageURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $("#imgProfile").attr('src', e.target.result);
            };
            reader.readAsDataURL(input.files[0]);
        }
    }

    $("#modal-form").on("click", "#btnChangePicture", function () {
        //Triggers the click function of hidden input file field

        if (!$("#btnChangePicture").hasClass("changing")) {// flag
            //default image
            ImgSrc = $("#imgProfile").attr('src');
            $("#profilePicture").click();
        } else {

        }

    });

    $("#modal-form").on('change', '#profilePicture', function () {
        readImageURL(this);
        $("#btnChangePicture").addClass('changing');
        $("#btnChangePicture").attr("value", "Confirm");
        $("#btnDiscard").removeClass('d-none');
    });


    $("#modal-form").on('click', "#btnDiscard", function () {
        $("#btnChangePicture").removeClass('changing');
        $("#btnChangePicture").attr('value', 'Change');
        $("#btnDiscard").addClass('d-none');
        $("#imgProfile").attr('src', ImgSrc);
        $("#profilePicture").val('');
    });

    // Applying policy

    const ShowUserPolicyForm = function (e){
        e.preventDefault(); 

        let button = $(this).attr("data-url");
        $.ajax({
            url: button,
            type: 'GET',
            dataType: 'json',
            beforeSend: () => {
                $("#modal-form-normal").modal("show");
            },
            success: (data) => {
                $("#modal-form-normal .modal-content").html(data.html_form);
            }

        });
        

        return false;
    }

    const ShowApplyUserPolicyForm = function(e){
        e.preventDefault();
        
        let form = $(this);

        $.ajax({
            url:  form.attr("data-url"),
            data: form.serialize(),
            cache: false,
            type: form.attr("method"),
            dataType: 'json',
            success: (data) => {
                if(data.form_is_valid){
                    $("#modal-form-normal").modal('hide');
                }else{
                    $("#modal-form-normal .modal-content").html(data.html_form);
                }

            }
        });
        return false;
    }

    $("#table_admin").on("click", ".show-user-policy",ShowUserPolicyForm);
    $("#modal-form-normal").on("submit", ".apply-user-policy", ShowApplyUserPolicyForm);

    /*
    --------------------------------------------------------
    *****************PRI ADMIN FUNCTIONS********************
    --------------------------------------------------------
    */
    /*
    --------------------------------------------------------
    ********************FOR SORTING*************************
    --------------------------------------------------------
    */
    $("#button-sort-admin").click(function (e) {
        e.preventDefault();
        var column = $("#column-admin").val() == null ? 'Id' : $("#column-admin").val();
        var sort_order = $("#sort-order-admin").val();
        var data = {
            'sortBy': sort_order,
            'column': column,
        }

        $.ajax({
            type: 'GET',
            url: '/admin/user/sort_admin/',
            data: data,
            dataType: 'json',
            success: function (data) {
                $("#table_admin tbody").html(data.table_records_admin);
                $("#pagination_admin").html(data.pagination_admin);
            },
            error: function (data) {
                console.log(data);
            }
        });

    });


    /*
    --------------------------------------------------------
    ********************FOR LIMIT**************************
    --------------------------------------------------------
    */

    $("#record-limit-admin").change(function (e) {
        var limit = $(this).val();
        var data = { 'limit': limit };

        $.ajax({
            type: 'GET',
            url: '/admin/user/record_limit_admin/',
            data: data,
            dataType: 'json',
            success: function (data) {
                $("#table_admin tbody").html(data.table_records_admin);
                $("#pagination_admin").html(data.pagination_admin);
            },
            error: function (data) {
                console.log(data);
            }

        });
    });

    /*
    --------------------------------------------------------
    ********************FOR SEARCH**************************
    --------------------------------------------------------
    */

    function searchResultsAdmin() {
        var searchVal = $("#search-admin").val();

        var data = {
            'search_text': searchVal
        };

        $.ajax({
            type: 'GET',
            url: '/admin/user/search_admin/',
            data: data,
            dataType: 'json',
            success: function (data) {
                $("#table_admin tbody").html(data.table_records_admin);
                $("#pagination_admin").html(data.pagination_admin);
            },
            error: function (data) {
                console.log(data);
            }
        });
    }

    $(".btn-search-admin").click(function (e) {
        e.preventDefault();
        //check if input box is empty or spaces only .trim()
        var val = $("#search-admin").val();
        if (val.trim() === "") {

        } else {
            searchResultsAdmin();
        }

    });

    $("#form-search-admin").submit(function (e) {
        e.preventDefault();

        var val = $("#search-admin").val();
        if (val.trim() === "") {

        } else {
            searchResultsAdmin();
        }
    });

    $("#search-admin").keyup(function (e) {
        if (e.which == '13') {
            return false;
            e.preventDefault();
        }
        if ($("#search-admin").val().length <= 0) {
            searchResultsAdmin();
        }
    });

    /*
    --------------------------------------------------------
    ********************FOR PAGINATION**********************
    --------------------------------------------------------
    */

    $("#pagination_admin").on('click', '.page-link', function (e) {
        var currentPage = $(this).text();
        var href = $(this).attr('href');

        $.ajax({
            type: 'GET',
            url: '/admin/user/paging_admin/',
            dataType: 'json',
            success: function (data) {
                $("#table_admin tbody").html(data.table_records_admin);
                $("#pagination_admin").html(data.pagination_admin);
            },
            error: function (data) {
                console.log(data);
            }
        });

        return false;

    });

    /*
    /*
    ========================================================
    ********************END PRI User************************
    ========================================================
    */

    /*
    ========================================================
    **********************PRI Client************************
    ========================================================
    */


    var ShowPRIClientsForm = function (e) {
        e.preventDefault();


        var button = $(this);
        $.ajax({
            url: button.attr("data-url"),
            type: 'GET',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-form-normal").modal("show");
            },
            success: function (data) {
                $("#modal-form-normal .modal-content").html(data.html_form);
            }
        });
    }

    var SavePRIClientsForm = function (e) {

        e.preventDefault();

        var form = $(this);
        var formData = false;

        if (window.FormData) {
            formData = new FormData(form[0]);
        }

        $.ajax({
            url: form.attr("data-url"),
            data: formData ? formData : form.serialize(),
            cache: false,
            contentType: false,
            processData: false,
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#modal-form-normal").modal('hide');
                    $("#table-client tbody").html(data.table_records_client);
                    $("#pagination-client").html(data.pagination_client);
                } else {
                    $("#modal-form-normal .modal-content").html(data.html_form);

                }
            }
        });

        return false;
    }

    $(".show-form-create-client").on('click', ShowPRIClientsForm);
    $("#modal-form-normal").on("submit", ".pri-admin-create-clients", SavePRIClientsForm);

    $("#table-client").on("click", ".show-form-edit-client", ShowPRIClientsForm);
    $("#modal-form-normal").on("submit", ".pri-admin-edit-clients", SavePRIClientsForm);

    $("#table-client").on("click", ".show-form-delete-client", ShowPRIClientsForm);
    $("#modal-form-normal").on("submit", ".delete-client-form", SavePRIClientsForm);

    // Show clients applicants

    var ShowDeleteClientApplicant = function (e) {
        e.preventDefault();

        var button = $(this);
        $.ajax({
            url: button.attr("data-url"),
            type: 'GET',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-form-normal").modal("show");
            },
            success: function (data) {
                $("#modal-form-normal .modal-content").html(data.html_form);
            }
        });
    }

    const SaveDeleteClientApplicant = function (e) {
        e.preventDefault();

        let form = $(this);

        $.ajax({
            url: form.attr("data-url"),
            data: form.serialize(),
            cache: false,
            type: form.attr("method"),
            dataType: 'json',
            success: (data) => {
                if (data.form_is_valid) {
                    $("#modal-form-normal").modal('hide');
                    // $("#clientApplicantDataTable tbody").html(data.table_records); 
                    location.reload();
                } else {
                    $("#modal-form-normal .modal-content").html(data.html_form);
                }
            }
        });

        return false;
    }

    $("#clientApplicantDataTable").on("click", ".show-fire-client-applicant", ShowDeleteClientApplicant);
    $("#modal-form-normal").on("submit", ".delete-client-applicant-form", SaveDeleteClientApplicant);



    /*
    --------------------------------------------------------
    *****************PRI CLIENT FUNCTIONS********************
    --------------------------------------------------------
    */
    /*
    --------------------------------------------------------
    ********************FOR SORTING*************************
    --------------------------------------------------------
    */
    $("#button-sort-client").click(function (e) {
        e.preventDefault();
        var column = $("#column-client").val() == null ? 'Id' : $("#column-client").val();
        var sort_order = $("#sort-order-client").val();
        var data = {
            'sortBy': sort_order,
            'column': column,
        }

        $.ajax({
            type: 'GET',
            url: '/admin/clients/sort_clients/',
            data: data,
            dataType: 'json',
            success: function (data) {
                $("#table-client tbody").html(data.table_records_client);
                $("#pagination-client").html(data.pagination_client);
            },
            error: function (data) {
                console.log(data);
            }
        });

    });


    /*
    --------------------------------------------------------
    ********************FOR LIMIT**************************
    --------------------------------------------------------
    */

    $("#record-limit-client").change(function (e) {
        var limit = $(this).val();
        var data = { 'limit': limit };

        $.ajax({
            type: 'GET',
            url: '/admin/clients/record_limit_clients/',
            data: data,
            dataType: 'json',
            success: function (data) {
                $("#table-client tbody").html(data.table_records_client);
                $("#pagination-client").html(data.pagination_client);
            },
            error: function (data) {
                console.log(data);
            }

        });
    });

    /*
    --------------------------------------------------------
    ********************FOR SEARCH**************************
    --------------------------------------------------------
    */

    function searchResultsClient() {
        var searchVal = $("#search-client").val();

        var data = {
            'search_text': searchVal
        };

        $.ajax({
            type: 'GET',
            url: '/admin/clients/search_clients/',
            data: data,
            dataType: 'json',
            success: function (data) {
                $("#table-client tbody").html(data.table_records_client);
                $("#pagination-client").html(data.pagination_client);
            },
            error: function (data) {
                console.log(data);
            }
        });
    }

    $(".btn-search-client").click(function (e) {
        e.preventDefault();
        //check if input box is empty or spaces only .trim()
        var val = $("#search-client").val();
        if (val.trim() === "") {

        } else {
            searchResultsClient();
        }

    });

    $("#form-search-client").submit(function (e) {
        e.preventDefault();

        var val = $("#search-client").val();
        if (val.trim() === "") {

        } else {
            searchResultsClient();
        }
    });

    $("#search-client").keyup(function (e) {
        if (e.which == '13') {
            return false;
            e.preventDefault();
        }
        if ($("#search-client").val().length <= 0) {
            searchResultsClient();
        }
    });

    /*
    --------------------------------------------------------
    ********************FOR PAGINATION**********************
    --------------------------------------------------------
    */

    $("#pagination-client").on('click', '.page-link', function (e) {
        var currentPage = $(this).text();
        var href = $(this).attr('href');

        $.ajax({
            type: 'GET',
            url: '/admin/clients/paging_clients/',
            dataType: 'json',
            success: function (data) {
                $("#table-client tbody").html(data.table_records_client);
                $("#pagination-client").html(data.pagination_client);
            },
            error: function (data) {
                console.log(data);
            }
        });

        return false;

    });


    ////Replace the first lowercase t we find with X
    //'This is sparta!'.replace(/t/,'X');
    ////result: 'This is sparXa!'
    //
    ////Replace the first letter t (upper or lower) with X
    //'This is sparta!'.replace(/t/i, 'X');
    ////result: 'Xhis is sparta!'
    //
    ////Replace all the Ts in the text (upper or lower) with X
    //'This is sparta!'.replace(/t/gi, 'X' );
    ////result: 'Xhis is sparXa!'
    //
    /*
    ========================================================
    ********************END PRI Client**********************
    ========================================================
    */


    /*
    ========================================================
    **********************PRI REQUEST***********************
    ========================================================
    */

    /*
    --------------------------------------------------------
    *****************PRI REQUEST FUNCTIONS******************
    --------------------------------------------------------
    */

    /*
    --------------------------------------------------------
    ********************FOR SORTING*************************
    --------------------------------------------------------
    */
    $("#button-sort-requests").click(function (e) {
        e.preventDefault();
        var column = $("#column-requests").val() == null ? 'Id' : $("#column-requests").val();
        var sort_order = $("#sort-order-requests").val();
        var data = {
            'sortBy': sort_order,
            'column': column,
        }

        $.ajax({
            type: 'GET',
            url: '/admin/requests/sort_requests/',
            data: data,
            dataType: 'json',
            success: function (data) {
                $("#table-requests tbody").html(data.table_records_requests);
                $("#pagination-requests").html(data.pagination_requests);
            },
            error: function (data) {
                console.log(data);
            }
        });

    });


    /*
    --------------------------------------------------------
    ********************FOR LIMIT**************************
    --------------------------------------------------------
    */

    $("#record-limit-requests").change(function (e) {
        var limit = $(this).val();
        var data = { 'limit': limit };

        $.ajax({
            type: 'GET',
            url: '/admin/requests/record_limit_requests/',
            data: data,
            dataType: 'json',
            success: function (data) {
                $("#table-requests tbody").html(data.table_records_requests);
                $("#pagination-requests").html(data.pagination_requests);
            },
            error: function (data) {
                console.log(data);
            }

        });
    });


    /*
    --------------------------------------------------------
    ********************FOR SEARCH**************************
    --------------------------------------------------------
    */

    function searchResultsRequests() {
        var searchVal = $("#search-requests").val();

        var data = {
            'search_text': searchVal
        };

        $.ajax({
            type: 'GET',
            url: '/admin/requests/search_requests/',
            data: data,
            dataType: 'json',
            success: function (data) {
                $("#table-requests tbody").html(data.table_records_requests);
                $("#pagination-requests").html(data.pagination_requests);
            },
            error: function (data) {
                console.log(data);
            }
        });
    }

    $(".btn-search-requests").click(function (e) {
        e.preventDefault();
        //check if input box is empty or spaces only .trim()
        var val = $("#search-requests").val();
        if (val.trim() === "") {

        } else {
            searchResultsRequests();
        }

    });

    $("#form-search-requests").submit(function (e) {
        e.preventDefault();

        var val = $("#search-requests").val();
        if (val.trim() === "") {

        } else {
            searchResultsRequests();
        }
    });

    $("#search-requests").keyup(function (e) {
        if (e.which == '13') {
            return false;
            e.preventDefault();
        }
        if ($("#search-requests").val().length <= 0) {
            searchResultsRequests();
        }
    });



    /*
    --------------------------------------------------------
    ********************FOR PAGINATION**********************
    --------------------------------------------------------
    */

    $("#pagination-requests").on('click', '.page-link', function (e) {
        var currentPage = $(this).text();
        var href = $(this).attr('href');

        $.ajax({
            type: 'GET',
            url: '/admin/requests/paging_requests/',
            dataType: 'json',
            success: function (data) {
                $("#table-requests tbody").html(data.table_records_requests);
                $("#pagination-requests").html(data.pagination_requests);
            },
            error: function (data) {
                console.log(data);
            }
        });

        return false;

    });



    var ShowPRIRequestsForm = function (e) {
        e.preventDefault();

        var button = $(this);
        $.ajax({
            url: button.attr("data-url"),
            type: 'GET',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-form-normal").modal("show");
            },
            success: function (data) {
                $("#modal-form-normal .modal-content").html(data.html_form);
            }
        });
    }
    var SavePRIRequestsForm = function (e) {
        e.preventDefault();
        var form = $(this);

        $.ajax({
            url: form.attr("data-url"),
            data: form.serialize(),
            cache: false,
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#modal-form-normal").modal('hide');
                    $("#table-requests tbody").html(data.table_records_requests);
                    $("#pagination-requests").html(data.pagination_requests);
                } else {
                    $("#modal-form-normal .modal-content").html(data.html_form);

                }
            }
        });

        return false;
    }


    $(".show-form-create-requests").on('click', ShowPRIRequestsForm);
    $("#modal-form-normal").on('submit', '.pri-admin-create-requests', SavePRIRequestsForm);

    $("#table-requests").on("click", ".show-form-edit-requests", ShowPRIRequestsForm);
    $("#modal-form-normal").on('submit', '.pri-admin-edit-requests', SavePRIRequestsForm);


    $("#table-requests").on("click", ".show-form-delete-requests", ShowPRIRequestsForm);
    $("#modal-form-normal").on('submit', '.pri-admin-delete-requests', SavePRIRequestsForm);


    var ShowPRIRequestsViewForm = function (e) {
        e.preventDefault();

        var button = $(this);
        $.ajax({
            url: button.attr("data-url"),
            type: 'GET',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-form-normal").modal("show");
            },
            success: function (data) {
                $("#table-requests tbody").html(data.table_records_requests);
                $("#pagination-requests").html(data.pagination_requests);
                $("#modal-form-normal .modal-content").html(data.html_form);
            }
        });
    }

    $("#table-requests").on("click", ".show-form-view-requests", ShowPRIRequestsViewForm);
    /*
    ========================================================
    ********************END PRI REQUEST**********************
    ========================================================
    */


    /*
    ========================================================
    **********************PRI JOBS***********************
    ========================================================
    */

    /*
    --------------------------------------------------------
    *****************PRI JOBS FUNCTIONS******************
    --------------------------------------------------------
    */


    var ShowPRIJobsForm = function (e) {
        e.preventDefault();

        var button = $(this);
        $.ajax({
            url: button.attr("data-url"),
            type: 'GET',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-form-normal").modal("show");
            },
            success: function (data) {
                $("#modal-form-normal .modal-content").html(data.html_form);
                $("#job_deadline").datepicker({
                    uiLibrary: 'bootstrap4',
                    iconsLibrary: 'fontawesome',
                    format: 'mmm dd yyyy'
                });

            }
        });
    }

    var SavePRIJobsForm = function (e) {
        e.preventDefault();
        var form = $(this);

        $.ajax({
            url: form.attr("data-url"),
            data: form.serialize(),
            cache: false,
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#modal-form-normal").modal('hide');
                    $("#table-jobs tbody").html(data.table_records_jobs);
                    $("#pagination-jobs").html(data.pagination_jobs);
                } else {
                    $("#modal-form-normal .modal-content").html(data.html_form);

                }
            }
        });

        return false;
    }

    $("#table-requests").on("click", ".show-form-create-job-vacancy-requests", ShowPRIJobsForm);
    $("#modal-form-normal").on("submit", ".pri-admin-create-jobs", SavePRIJobsForm);

    $("#table-jobs").on("click", ".show-form-edit-jobs", ShowPRIJobsForm);
    $("#modal-form-normal").on("submit", ".pri-admin-edit-jobs", SavePRIJobsForm);

    $("#table-jobs").on("click", ".show-form-delete-jobs", ShowPRIJobsForm);
    $("#modal-form-normal").on("submit", ".pri-admin-delete-jobs", SavePRIJobsForm);

    // for viewing applicant requests

    $("#table-jobs").on("click", ".show-applicant-requests", function (e) {
        e.preventDefault();

        const button = $(this);

        window.location.href = button.attr("data-url");


        return false;
    });

    /*
    --------------------------------------------------------
    ********************FOR SORTING*************************
    --------------------------------------------------------
    */

    $("#button-sort-jobs").click(function (e) {
        e.preventDefault();
        var column = $("#column-jobs").val() == null ? 'Id' : $("#column-jobs").val();
        var sort_order = $("#sort-order-jobs").val();
        var data = {
            'sortBy': sort_order,
            'column': column,
        }

        $.ajax({
            type: 'GET',
            url: '/admin/jobs/sort_jobs/',
            data: data,
            dataType: 'json',
            success: function (data) {
                $("#table-jobs tbody").html(data.table_records_jobs);
                $("#pagination-jobs").html(data.pagination_jobs);
            },
            error: function (data) {
                console.log(data);
            }
        });

    });
    /*
    --------------------------------------------------------
    ********************FOR LIMIT**************************
    --------------------------------------------------------
    */

    $("#record-limit-jobs").change(function (e) {
        var limit = $(this).val();
        var data = { 'limit': limit };

        $.ajax({
            type: 'GET',
            url: '/admin/jobs/record_limit_jobs/',
            data: data,
            dataType: 'json',
            success: function (data) {
                $("#table-jobs tbody").html(data.table_records_jobs);
                $("#pagination-jobs").html(data.pagination_jobs);
            },
            error: function (data) {
                console.log(data);
            }

        });
    });

    /*
    --------------------------------------------------------
    ********************FOR SEARCH**************************
    --------------------------------------------------------
    */

    function searchResultsJobs() {
        var searchVal = $("#search-jobs").val();

        var data = {
            'search_text': searchVal
        };

        $.ajax({
            type: 'GET',
            url: '/admin/jobs/search_jobs/',
            data: data,
            dataType: 'json',
            success: function (data) {
                $("#table-jobs tbody").html(data.table_records_jobs);
                $("#pagination-jobs").html(data.pagination_jobs);
            },
            error: function (data) {
                console.log(data);
            }
        });
    }

    $(".btn-search-jobs").click(function (e) {
        e.preventDefault();
        //check if input box is empty or spaces only .trim()
        var val = $("#search-jobs").val();
        if (val.trim() === "") {

        } else {
            searchResultsJobs();
        }

    });

    $("#form-search-jobs").submit(function (e) {
        e.preventDefault();

        var val = $("#search-jobs").val();
        if (val.trim() === "") {

        } else {
            searchResultsJobs();
        }

    });


    $("#search-jobs").keyup(function (e) {

        if (e.which == '13') {
            return false;
            e.preventDefault();
        }

        if ($("#search-jobs").val().length <= 0) {
            searchResultsJobs();
        }
    });



    /*
    --------------------------------------------------------
    ********************FOR PAGINATION**********************
    --------------------------------------------------------
    */

    $("#pagination-jobs").on('click', '.page-link', function (e) {
        var currentPage = $(this).text();
        var href = $(this).attr('href');

        $.ajax({
            type: 'GET',
            url: '/admin/jobs/paging_jobs/',
            dataType: 'json',
            success: function (data) {
                $("#table-jobs tbody").html(data.table_records_jobs);
                $("#pagination-jobs").html(data.pagination_jobs);
            },
            error: function (data) {
                console.log(data);
            }
        });

        return false;

    });
    /*
    --------------------------------------------------------
    ********************END OF FUNCTIONS********************
    --------------------------------------------------------
    */

    // PRI JOBS APPLICANT REQUEST

    function setInterviewDate(datePicker) {
        let urlAttr = $(datePicker).attr("data-url");

        // https://gijgo.com/datepicker/methods/value
        let date = {
            'date': $(datePicker).val(),
        }

        data = JSON.stringify(date);

        $.ajax({
            // https://docs.djangoproject.com/en/2.2/ref/csrf/
            headers: { "X-CSRFToken": getCookie("csrftoken") },
            type: 'POST',
            url: urlAttr,
            data: data,
            dataType: 'json',
            success: (data) => {

            }
        });
    }

    // $(".set-schedule-interview").each(function () {
    //     $(this).datetimepicker({
    //         uiLibrary: 'bootstrap4',
    //         iconsLibrary: 'fontawesome',
    //         // format: 'mmm dd yyyy',
    //         // https://gijgo.com/datepicker/events/change
    //         change: function (e) {
    //             setInterviewDate(this);
    //         },
    //     });
    // });
    $(".set-schedule-interview").each(function () {
        $(this).datetimepicker({
            uiLibrary: 'bootstrap4',
            iconsLibrary: 'fontawesome',
            format: 'mmm dd yyyy hh:mm TT',
            //format: 'yyyy-mm-dd HH:MM',
            datepicker: { showOtherMonths: true, calendarWeeks: true },
            // https://gijgo.com/datepicker/events/change
            change: function (e) {
                setInterviewDate(this);
            },
            modal: true,
            footer: true
        });
    });
    /*
     --------------------------------------------------------
     -------------------SEND JSON USING AJAX TO DJANGO-------
     --------------------------------------------------------
     */



    function getCookie(cname) {
        var name = cname + "=";
        var decodedCookie = decodeURIComponent(document.cookie);
        var ca = decodedCookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0) == ' ') {
                c = c.substring(1);
            }
            if (c.indexOf(name) == 0) {
                return c.substring(name.length, c.length);
            }
        }
        return "";
    }
    $("#jobRequestApplicantsDataTable").on("click", ".switch input[type=checkbox]", function () {
        const urlAttr = $(this).attr("data-url");

        let is_checked = $(this).prop("checked") == true ? false : true;

        // attach csrf token cookie
        // how to get cookies in javascript https://www.w3schools.com/js/js_cookies.asp
        // so that django will accept the post method with csrf token
        // $.ajaxSetup({
        //     headers: { "X-CSRFToken": getCookie("csrftoken") }
        // });

        // data in javascript object format
        let data = {
            'is_exam': is_checked,
        }
        // convert to json
        data = JSON.stringify(data);
        // create request to be sent to django backend

        $.ajax({
            // https://docs.djangoproject.com/en/2.2/ref/csrf/
            headers: { "X-CSRFToken": getCookie("csrftoken") },
            type: 'POST', // must be in POST
            url: urlAttr,
            data: data, // json object to be transfer
            dataType: 'json',
            success: (data) => {
                //   location.reload();
                $("#jobRequestApplicantsDataTable tbody").html(data.table_records_job_applicant_requests);
                $(".set-schedule-interview").each(function () {
                    $(this).datetimepicker({
                        uiLibrary: 'bootstrap4',
                        iconsLibrary: 'fontawesome',
                        format: 'mmm dd yyyy hh:mm TT',
                        datepicker: { showOtherMonths: true, calendarWeeks: true },
                        change: function (e) {
                            setInterviewDate(this);
                        },
                        modal: true,
                        footer: true
                    });
                });
            },
        });
        console.log(data);
    });

    // Schedule of interview

    $("#jobRequestApplicantsDataTable").on("change", ".set-schedule-interview", function (e) {
        // e.preventDefault();
        alert("Hellodas");
        // return false;
    });



    /*
    ========================================================
    ********************END PRI JOBS**********************
    ========================================================
    */

    /*
    =======================================================
    *************PRI ADMIN APPLICANT HANDLING***************
    =======================================================
     */

    // For datatable
    // https://datatables.net/examples/api/add_row.html
    $('#applicantDataTable').DataTable();
    $('#schedulesDataTable').DataTable();
    $('#jobRequestApplicantsDataTable').DataTable();
    $('#clientApplicantDataTable').DataTable();
    // $('#schedulesDataTable').DataTable().ajax.reload();
    $("#schedulesDataTable").on("click", ".toogle-applicant-exam", function (e) {
        e.preventDefault();

        let button = $(this);
        $.ajax({
            url: button.attr("data-url"),
            type: 'GET',
            cache: false,
            dataType: 'json',
            success: (data) => {
                $("#schedulesDataTable tbody").html(data.table_records_schedule);
                $('#applicantDataTable').DataTable().ajax.reload();
            }
        });

        return false;
    });

    const ShowDeleteApplicantForm = function (e) {
        e.preventDefault();

        let button = $(this).attr("data-url");

        $.ajax({
            url: button,
            type: 'GET',
            dataType: 'json',
            beforeSend: () => {
                $("#modal-form-normal").modal("show");
            },
            success: (data) => {
                $("#modal-form-normal .modal-content").html(data.html_form);
            }

        });

        return false;
    }

    const SaveDeleteApplicantForm = function (e) {
        e.preventDefault();

        let form = $(this);

        $.ajax({
            url: form.attr("data-url"),
            data: form.serialize(),
            cache: false,
            type: form.attr("method"),
            dataType: 'json',
            success: (data) => {
                if (data.form_is_valid) {
                    $("#modal-form-normal").modal('hide');
                    $("#applicantDataTable tbody").html(data.table_records_applicants);
                } else {
                    $("#modal-form-normal .modal-content").html(data.html_form);
                }
            }
        });

        return false;
    }

    $("#applicantDataTable").on("click", ".show-delete-applicant-data", ShowDeleteApplicantForm);
    $("#modal-form-normal").on('submit', '.delete-applicant-form', SaveDeleteApplicantForm);

    // for hired client
    $("#clientApplicantDataTable").on("change", ".hired-applicant-status", function () {
        const urlAttr = $(this).attr("data-url");
        let status = $(this).val();
        let data = {
            "status": status
        }
        data = JSON.stringify(data);

        $.ajax({
            // https://docs.djangoproject.com/en/2.2/ref/csrf/
            headers: { "X-CSRFToken": getCookie("csrftoken") },
            type: 'POST', // must be in POST
            url: urlAttr,
            data: data, // json object to be transfer
            dataType: 'json',
            success: (data) => {
                // console.log(data.confirmation);
            },

        });
    });



    //END of ready function
});