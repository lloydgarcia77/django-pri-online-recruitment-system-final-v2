$(document).ready(function () {

    $("#id_employment_applicant_fk-0-date_from").datepicker({
        uiLibrary: 'bootstrap4',
        iconsLibrary: 'fontawesome',
        format: 'mmm dd yyyy',
    });

    $("#id_employment_applicant_fk-0-date_to").datepicker({
        uiLibrary: 'bootstrap4',
        iconsLibrary: 'fontawesome',
        format: 'mmm dd yyyy',
    });

    $("#c_date_from").datepicker({
        uiLibrary: 'bootstrap4',
        iconsLibrary: 'fontawesome',
        format: 'mmm dd yyyy',
    });

    $("#c_date_to").datepicker({
        uiLibrary: 'bootstrap4',
        iconsLibrary: 'fontawesome',
        format: 'mmm dd yyyy',
    });

    $("#v_date_from").datepicker({
        uiLibrary: 'bootstrap4',
        iconsLibrary: 'fontawesome',
        format: 'mmm dd yyyy',
    });

    $("#v_date_to").datepicker({
        uiLibrary: 'bootstrap4',
        iconsLibrary: 'fontawesome',
        format: 'mmm dd yyyy',
    });

    $("#h_date_from").datepicker({
        uiLibrary: 'bootstrap4',
        iconsLibrary: 'fontawesome',
        format: 'mmm dd yyyy',
    });

    $("#h_date_to").datepicker({
        uiLibrary: 'bootstrap4',
        iconsLibrary: 'fontawesome',
        format: 'mmm dd yyyy',
    });

    $("#e_date_from").datepicker({
        uiLibrary: 'bootstrap4',
        iconsLibrary: 'fontawesome',
        format: 'mmm dd yyyy',
    });

    $("#e_date_to").datepicker({
        uiLibrary: 'bootstrap4',
        iconsLibrary: 'fontawesome',
        format: 'mmm dd yyyy',
    });

    
    $("#id_tranings_applicant_fk-0-date_attended").datepicker({
        uiLibrary: 'bootstrap4',
        iconsLibrary: 'fontawesome',
        format: 'mmm dd yyyy',
    });

    // Spouse if married
    $("#id_civil_status").change(() => {
        const item = $("#id_civil_status").find(":selected").text();
        if(item === "Married"){
            $("#id_spouse_full_name").attr("readonly", false);
            $("#id_spouse_contact_number").attr("readonly", false); 
        }else{
            
            $("#id_spouse_full_name").attr("readonly", true);            
            $("#id_spouse_full_name").val("");
            $("#id_spouse_contact_number").attr("readonly", true); 
            $("#id_spouse_contact_number").val("0");
        }
    });

    // Siblings add remove
    
    $("#add-field-form-applicant-siblings").click(function(e){
        e.preventDefault();
        let  form_idx = $("#form-applicant-siblings #id_siblings_applicant_fk-TOTAL_FORMS").val();
        let divs = $("#empty-form-applicant-siblings-set div");
        const list_divs = [...divs];   

        let row = '<div class="form-row">' + 
                    '<div class="form-group col-md-4 mb-0"> '+
                        list_divs[0].outerHTML+
                    '</div>' +
                    '<div class="form-group col-md-4 mb-0"> '+
                        list_divs[2].outerHTML+
                    '</div>' +
                    '<div class="form-group col-md-4 mb-0"> '+
                        list_divs[4].outerHTML+
                    '</div>' +
                '</div>';           

        $("#form-applicant-siblings-set #form-applicant-siblings").append(row.replace(/__prefix__/g, form_idx));   

        $("#form-applicant-siblings #id_siblings_applicant_fk-TOTAL_FORMS").val(parseInt(form_idx)+1);
    
        let  form_idx_after = $("#form-applicant-siblings #id_siblings_applicant_fk-TOTAL_FORMS").val();
        if(form_idx_after > 1){
            $("#del-field-form-applicant-siblings").show();
        }else{
            $("#del-field-form-applicant-siblings").hide();
        }
        return false;
        
    });

    $("#del-field-form-applicant-siblings").click((e) => {
        e.preventDefault();
        
        let  form_idx = $("#form-applicant-siblings #id_siblings_applicant_fk-TOTAL_FORMS").val();
        // remove the copied from empty fields
        $('#form-applicant-siblings-set #form-applicant-siblings div.form-row').last().remove();      
        $("#form-applicant-siblings #id_siblings_applicant_fk-TOTAL_FORMS").val(parseInt(form_idx)-1);

        let  form_idx_after = $("#form-applicant-siblings #id_siblings_applicant_fk-TOTAL_FORMS").val();
        if(form_idx_after > 1){
            $("#del-field-form-applicant-siblings").show();
        }else{
            $("#del-field-form-applicant-siblings").hide();
        }

        return false;
    });

    // Employment History

    $("#add-field-form-applicant-employment-history").click((e) => {
        e.preventDefault();
        let  form_idx = $("#form-applicant-employement-history-set #id_employment_applicant_fk-TOTAL_FORMS").val();

        let divs = $("#empty-form-applicant-employement-history-set div");
        let list_divs = [...divs];

        let row = '<div class="form-row">' +  
                    '<div class="form-group col-md-4 mb-0"> '+
                        list_divs[4].outerHTML+
                    '</div>' +
                    '<div class="form-group col-md-4 mb-0"> '+
                        list_divs[0].outerHTML+
                    '</div>' +
                    '<div class="form-group col-md-4 mb-0"> '+
                        list_divs[2].outerHTML+
                    '</div>' +
                '</div>' +
                '<div class="form-row">' + 
                    '<div class="form-group col-md-4 mb-0"> '+
                        list_divs[6].outerHTML+
                    '</div>' +
                    '<div class="form-group col-md-4 mb-0"> '+
                        list_divs[8].outerHTML+
                    '</div>' +
                    '<div class="form-group col-md-4 mb-0"> '+
                        list_divs[10].outerHTML+
                    '</div>' +
                '</div>';   
    
        $("#form-applicant-employement-history-set #form-applicant-employement-history").append(row.replace(/__prefix__/g, form_idx));   

        $(`#id_employment_applicant_fk-${form_idx}-date_from`).datepicker({
            uiLibrary: 'bootstrap4',
            iconsLibrary: 'fontawesome',
            format: 'mmm dd yyyy',
        });

        $(`#id_employment_applicant_fk-${form_idx}-date_to`).datepicker({
            uiLibrary: 'bootstrap4',
            iconsLibrary: 'fontawesome',
            format: 'mmm dd yyyy',
        });
        $("#form-applicant-employement-history-set #id_employment_applicant_fk-TOTAL_FORMS").val(parseInt(form_idx)+1);

        let  form_idx_after = $("#form-applicant-employement-history-set #id_employment_applicant_fk-TOTAL_FORMS").val();

        if(form_idx_after > 1){
            $("#del-field-form-applicant-employment-history").show();
        }else{
            $("#del-field-form-applicant-employment-history").hide();
        }      
        
        return false;
    });

    $("#del-field-form-applicant-employment-history").click((e) => {
        e.preventDefault();
        let  form_idx = $("#form-applicant-employement-history-set #id_employment_applicant_fk-TOTAL_FORMS").val();

        $("#form-applicant-employement-history-set #form-applicant-employement-history div.form-row").slice(-2).remove();
        $("#form-applicant-employement-history-set #id_employment_applicant_fk-TOTAL_FORMS").val(parseInt(form_idx)-1);

        let  form_idx_after = $("#form-applicant-employement-history-set #id_employment_applicant_fk-TOTAL_FORMS").val();

        if(form_idx_after > 1){
            $("#del-field-form-applicant-employment-history").show();
        }else{
            $("#del-field-form-applicant-employment-history").hide();
        }

        return false;
    });

    // Applicant tranings

    $("#add-field-form-applicant-trainings").click((e) => {
        e.preventDefault();
        let form_idx = $("#form-applicant-trainings-set #form-applicant-trainings #id_tranings_applicant_fk-TOTAL_FORMS").val();
        let divs = $("#empty-form-applicant-trainings-set div");
        const list_divs = [...divs];

        let row = '<div class="form-row">' + 
                    '<div class="form-group col-md-8 mb-0"> '+
                        list_divs[0].outerHTML+
                    '</div>' +
                    '<div class="form-group col-md-4 mb-0"> '+
                        list_divs[2].outerHTML+
                    '</div>' + 
                '</div>';  


        $("#form-applicant-trainings-set #form-applicant-trainings").append(row.replace(/__prefix__/g, form_idx));

        $("#form-applicant-trainings-set #form-applicant-trainings #id_tranings_applicant_fk-TOTAL_FORMS").val(parseInt(form_idx)+1);

        $(`#id_tranings_applicant_fk-${form_idx}-date_attended`).datepicker({
            uiLibrary: 'bootstrap4',
            iconsLibrary: 'fontawesome',
            format: 'mmm dd yyyy',
        });
        let  form_idx_after = $("#form-applicant-trainings-set #form-applicant-trainings #id_tranings_applicant_fk-TOTAL_FORMS").val();

        if(form_idx_after > 1){
            $("#del-field-form-applicant-trainings").show(); 
        }else{
            $("#del-field-form-applicant-trainings").hide();
        }

        return false;
    });

    $("#del-field-form-applicant-trainings").click((e) => {
        e.preventDefault();
        
        let form_idx = $("#form-applicant-trainings-set #form-applicant-trainings #id_tranings_applicant_fk-TOTAL_FORMS").val();
        $("#form-applicant-trainings-set #form-applicant-trainings div.form-row").last().remove();
        $("#form-applicant-trainings-set #form-applicant-trainings #id_tranings_applicant_fk-TOTAL_FORMS").val(parseInt(form_idx)-1);

        let form_idx_after = $("#form-applicant-trainings-set #form-applicant-trainings #id_tranings_applicant_fk-TOTAL_FORMS").val();

        if(form_idx_after > 1){
            $("#del-field-form-applicant-trainings").show(); 
        }else{
            $("#del-field-form-applicant-trainings").hide();
        }
        return false;
    });
    // Applicant Character Reference
    $("#add-field-form-applicant-character-reference").click((e) => {
        e.preventDefault();
        let form_idx = $("#form-applicant-character-reference-set #form-applicant-character-reference #id_character_references_applicant_fk-TOTAL_FORMS").val();
        let divs = $("#empty-form-applicant-character-reference-set div");
        const list_divs =[...divs];

        let row = '<div class="form-row">' + 
                    '<div class="form-group col-md-4 mb-0"> '+
                        list_divs[0].outerHTML+
                    '</div>' +
                    '<div class="form-group col-md-4 mb-0"> '+
                        list_divs[2].outerHTML+
                    '</div>' +
                    '<div class="form-group col-md-4 mb-0"> '+
                        list_divs[4].outerHTML+
                    '</div>' +
                '</div>';      
        
        $("#form-applicant-character-reference-set #form-applicant-character-reference").append(row.replace(/__prefix__/g, form_idx));
        $("#form-applicant-character-reference-set #form-applicant-character-reference #id_character_references_applicant_fk-TOTAL_FORMS").val(parseInt(form_idx)+1);
        let form_idx_after = $("#form-applicant-character-reference-set #form-applicant-character-reference #id_character_references_applicant_fk-TOTAL_FORMS").val();

        if(form_idx_after > 1){
            $("#del-field-form-applicant-character-reference").show();
        }else{
            $("#del-field-form-applicant-character-reference").hide();
        }

        return false;
    });

    $("#del-field-form-applicant-character-reference").click((e) => {
        e.preventDefault();
        let form_idx = $("#form-applicant-character-reference-set #form-applicant-character-reference #id_character_references_applicant_fk-TOTAL_FORMS").val();
        $("#form-applicant-character-reference-set #form-applicant-character-reference div.form-row").last().remove();
        $("#form-applicant-character-reference-set #form-applicant-character-reference #id_character_references_applicant_fk-TOTAL_FORMS").val(parseInt(form_idx)-1);
        let form_idx_after = $("#form-applicant-character-reference-set #form-applicant-character-reference #id_character_references_applicant_fk-TOTAL_FORMS").val();
        if(form_idx_after > 1){
            $("#del-field-form-applicant-character-reference").show();
        }else{
            $("#del-field-form-applicant-character-reference").hide();
        }
        return false;
    });
}); 