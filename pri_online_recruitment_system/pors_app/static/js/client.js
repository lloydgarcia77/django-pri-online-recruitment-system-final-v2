$(document).ready(function (e) {


    var ShowCreateRequestsForm = function (e) {
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
    var SaveSaveRequestsForm = function (e) {
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
                    $("#modal-form").modal('hide'); 
                    location.reload();
                } else {
                    $("#modal-form .modal-content").html(data.html_form);

                }
            }
        });

        return false;
    }
    $(".show-client-create-requests").on('click', ShowCreateRequestsForm);
    $("#modal-form").on('submit', '.client-create-requests', SaveSaveRequestsForm);

    $("#dataTable").on("click", ".show-client-edit-requests", ShowCreateRequestsForm);
    $("#modal-form").on('submit', '.client-edit-requests', SaveSaveRequestsForm);

    
    $("#dataTable").on("click", ".show-client-delete-requests", ShowCreateRequestsForm);
    $("#modal-form").on('submit', '.client-delete-requests', SaveSaveRequestsForm);

    $("#client-table-hired").on("click", ".fire-applicant", ShowCreateRequestsForm);
    $("#modal-form").on('submit', '.fire-hired-applicant', SaveSaveRequestsForm);


    $('#dataTable').DataTable();
    $('#client-table-hired').DataTable();


});