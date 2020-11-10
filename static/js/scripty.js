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

    $(document).on("submit", '#login-form', function(e) {
    e.preventDefault();
    var form = $(this).serialize();
    console.log("Variable form: ", form);
        $.ajax({
            url: "/check-login",
            type: "POST",
            data: form,
            success: function(response) {
                if (response == "error") {
                    alert("Could not login");
                } else {
                    console.log("Logged in as: ", response);
                }
        }
        });
    });
});
