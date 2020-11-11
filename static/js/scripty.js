// Wait until the page has fully loaded before applying the script
$(document).ready(function(e) {
    console.log("loaded");

    $("#register-form").submit(function(e) {
    e.preventDefault(); // avoid to execute the actual submit of the form.
    var form = $(this).serialize();
    console.log("Variable form: ", form);
        $.ajax({
            url: "/postregistration",
            type: "POST",
            data: form,
            success: function(response) {
                console.log(response) // show response from the php script.
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
                if (response == "error") {
                    alert("Could not login.")
                } else {
                    console.log("Logged in successfully", response);
                    // window.location.href = '/'
                }
        }
        });
    });
});
