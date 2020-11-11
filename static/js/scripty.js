// Wait until the page has fully loaded before applying the script
$(document).ready(function(e) {
    console.log("loaded");

    // Bind a function to the submit form
    $(document).on("submit", '#register-form', function(e) {
        // Prevent the default form post behavior to prevent the page from reloading
        e.preventDefault();
        console.log("form submitted")

        // Get the form data
        var form = $('#register-form').serialize();
        console.log("Variable form: ", form);
        // Send an ajax request over to the route /postregisteration
        $.ajax({
            url: "/postregistration",
            type: "POST",
            data: form,
            success: function(response) {
                console.log(response);
        }
        });
    });

    $("#login-form").submit(function(e) {
    e.preventDefault(); // avoid to execute the actual submit of the form.
    var form = $(this).serialize();
    console.log("Variable form: ", form);
        $.ajax({
            url: "/check-login",
            type: "POST",
            data: form,
            success: function(response) {
                console.log(response) // show response from the php script.
        }
        });
    });
});
