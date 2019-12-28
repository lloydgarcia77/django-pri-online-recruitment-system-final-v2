$(document).ready(function(){

    // Do not use arrow function in js when definin object
    const ShowJobRequestForm = function(e){ 
        e.preventDefault();
        let button = $(this); 
        $.ajax({
            url: button.attr("data-url"),
            type: 'GET',
            dataType: 'json',
            beforeSend: () => {
                $("#modal-form").modal("show");
            },
            success: (data) => { 
                $("#modal-form .modal-content").html(data.html_form);
            }
        });

    }

    const SendJobRequestForm = function(e){
        e.preventDefault();
        let form = $(this);

        $.ajax({
            url: form.attr("data-url"),
            data: form.serialize(),
            cache: false,
            type: form.attr("method"),
            dataType: 'json',
            success: (data) => {
                if(data.form_is_valid){
                    $("#modal-form").modal("hide"); 
                    location.reload(true);
                }else{
                    $("#modal-form .modal-content").html(data.html_form);
                }
            }
        });

        return false;
    }
    
 
    $(".show-apply-form").on("click", ShowJobRequestForm);
    $("#modal-form").on("submit", ".applicant-job-request-form", SendJobRequestForm);

    // Show applicant job request status

    const ShowJobRequestStatus = function(e){ 
        e.preventDefault();
        let button = $(this); 
        $.ajax({
            url: button.attr("data-url"),
            type: 'GET',
            dataType: 'json',
            beforeSend: () => {
                $("#modal-form-large").modal("show");
            },
            success: (data) => { 
                $("#modal-form-large .modal-content").html(data.html_form);
            }
        });

        return false;
    }

    $("#menu-show-job-request-status").click(ShowJobRequestStatus);
    $("#menu-show-job-hired-status").click(ShowJobRequestStatus);


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
    
    $("#modal-form-large").on("click", "#btnCancelRequests",function(e){  
        // The find() method returns descendant elements of the selected element.
        // A descendant is a child, grandchild, great-grandchild, and so on.
        /*
        $('#save').click(function () {
            $('#mytable').find('input[type="checkbox"]:checked').each(function () {
            //this is the current checkbox
            });
        });
         */

        const urlAttr = $(this).attr("data-url");

        let list = [];
        $("#modal-form-large #tblGrid").find('input[type="checkbox"]:checked').each(function(){
            list.push($(this).val());         
        }); 

        let data = {
            'ids': list,
        }

        data = JSON.stringify(data);

        $.ajax({
            headers: { "X-CSRFToken": getCookie("csrftoken") },
            type: 'POST',
            url: urlAttr,
            data: data,
            dataType: 'json',
            success: (data) =>{
                if(data.valid){
                    $("#modal-form").modal("hide"); 
                    location.reload(true);
                }
            }
        });

        console.log(data);
        
   
    });
    $("#modal-form-large").on('click', '#tblGrid .mycheckbox', function(){
        if($("#modal-form-large #tblGrid").find('input[type="checkbox"]:checked').length > 0){
            $("#modal-form-large #btnCancelRequests").prop("disabled", false);
        }else{
            $("#modal-form-large #btnCancelRequests").prop("disabled", true);
        }
    });
    // $("#modal-form-large").on('click', '#tblGrid .mycheckbox', function(){
    //     if($(this).prop("checked") == true){
    //         $("#modal-form-large #btnCancelRequests").prop("disabled", false);
    //     }else{
    //         $("#modal-form-large #btnCancelRequests").prop("disabled", true);
    //     }
    // });
    

});