
var currentTab = 0;  // Current tab is set to be the first tab (0)
showTab(currentTab);

function showTab(n){
    // This function will display the specified tab of the form...
    //The getElementsByClassName() method returns a collection of all elements in the document with the specified class name, as a NodeList object.
    //The NodeList object represents a collection of nodes. The nodes can be accessed by index numbers. The index starts at 0.
    var x = document.getElementsByClassName("tab");

    x[n].style.display = "block";
      //... and fix the Previous/Next buttons:

     if (n == 0){
        document.getElementById("prevBtn").style.display = "none";
     } else {
        document.getElementById("prevBtn").style.display = "inline";
     }

     var lastPage = x.length;

     if (n == (lastPage - 1)){
        document.getElementById("nextBtn").innerHTML = "Submit";
     }else{
        document.getElementById("nextBtn").innerHTML = "Next";
     }
      //... and run a function that will display the correct step indicator:
      fixStepIndicator(n);
}

function fixStepIndicator(n){
    // This function removes the "active" class of all steps...
    var i, x = document.getElementsByClassName("step");

    for(i = 0; i < x.length; i++){
        x[i].className = x[i].className.replace(" active", "");
    }
    //... and adds the "active" class on the current step:
    x[n].className += " active";
}

function validateForm(){
    // This function deals with validation of the form fields
    var x, y, i, valid = true;
    x = document.getElementsByClassName("tab");
    y = x[currentTab].getElementsByTagName("input");
    // A loop that checks every input field in the current tab:

    for (i = 0; i < y.length; i++){
        // If a field is empty...
        if(y[i].value == "" && !(y[i].getAttribute('id') == "id_suffix")){
            // add an "invalid" class to the field:
            y[i].className += " invalid";

            // and set the current valid status to false
            valid = false;
        }else{
            y[i].style.backgroundColor = "#E8F0FE";
        }
    }
    // If the valid status is true, mark the step as finished and valid:
    if (valid){
        document.getElementsByClassName("step")[currentTab].className += " finish";
        document.getElementById("regForm-message-box").style.display = "none";
    }else{
        document.getElementById("regForm-message-box").style.display = "block";
        document.getElementById("regForm-message-box").innerHTML = "Please complete the form before proceeding to the next form!";
    }
    return valid;// return the valid status
}

function nextPrev(n){
    //This function will figure out which tab to display
    var x = document.getElementsByClassName("tab");

    //Exit the function if any field in the current tab is invalid
    if(n == 1 && !validateForm()){
        return false;
    }
    // Hide the current tab:
    x[currentTab].style.display = "none";
    // Increase or decrease the current tab by 1:
    currentTab = currentTab + n;
    // if you have reached the end of the form...
    var lastPage = x.length;
    if(currentTab >= lastPage){
        // ... the form gets submitted:
        document.getElementById("regForm").submit();
        return false;
    }
    // Otherwise, display the correct tab:
    showTab(currentTab);
}
$(document).ready(function() {
//$( document ).ready()
//A page can't be manipulated safely until the document is "ready." jQuery detects this state of readiness for you. Code included inside $( document ).ready() will only run once the page Document Object Model (DOM) is ready for JavaScript code to execute. Code included inside $( window ).on( "load", function() { ... }) will run once the entire page (images or iframes), not just the DOM, is ready.
//https://learn.jquery.com/using-jquery-core/document-ready/


$("#dob").datepicker({
   uiLibrary: 'bootstrap4',
   format: 'mmm dd yyyy'
});

});

