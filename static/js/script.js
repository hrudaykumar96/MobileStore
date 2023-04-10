function validate() {
    var uname = document.getElementById("form1Example1");
    var password = document.getElementById("form1Example2");
    var status = false;
    if (uname.value.trim() == "") {
        uname.style.border = "solid 3px red";
        document.getElementById("u_display").innerHTML = "Email ID cannot be blank"
        status = false;
    }
    else {
        uname.style.border = "solid 3px green";
        document.getElementById("u_display").innerHTML = "";
        status = true;

    }
    if (password.value.length < 6) {
        password.style.border = "solid 3px red"
        document.getElementById("p_display").innerHTML = "Password must be at least 6 char long"
        status = false;
    }
    else {
        password.style.border = "solid 3px green";
        document.getElementById("p_display").innerHTML = "";

    }
    return status;
}



function signup() {
    var f_name = document.getElementById("form3Example1");
    var l_name = document.getElementById("form3Example2");
    var email = document.getElementById("form3Example3");
    var pass = document.getElementById("form3Example4");
    var status = false;

    if (f_name.value.trim() == "") {
        f_name.style.border = "solid 3px red";
        document.getElementById("f_display").innerHTML = "Please Enter First Name";
        status = false;
    }
    else {
        f_name.style.border = "solid 3px green";
        document.getElementById("f_display").innerHTML = "";
        status = true;
    }
    if (l_name.value.trim() == "") {
        l_name.style.border = "solid 3px red";
        document.getElementById("l_display").innerHTML = "Please Enter Last Name";
        status = false;
    }
    else {
        l_name.style.border = "solid 3px green";
        document.getElementById("l_display").innerHTML = "";
        status = true;
    }
    if (email.value.trim() == "") {
        email.style.border = "solid 3px red";
        document.getElementById("e_display").innerHTML = "Please Enter Valid Email Id";
        status = false;
    }
    else {
        email.style.border = "solid 3px green";
        document.getElementById("e_display").innerHTML = "";
        status = true;
    }
    if (pass.value.length < 6) {
        pass.style.border = "solid 3px red";
        document.getElementById("pass_display").innerHTML = "Password must be at least 6 char long";
        status = false;
    }
    else {
        pass.style.border = "solid 3px green";
        document.getElementById("pass_display").innerHTML = "";
        status = true;
    }
    return status;
}

function change_password() {
    var new_password = document.getElementById("npass");
    var confirm_password = document.getElementById("cpass");
    var email = document.getElementById("email");
    var status = false;
    if (email.value.trim() == "") {
        email.style.border = "solid 3px red";
        document.getElementById("email_display").innerHTML = "Email ID cannot be blank"
        status = false;
    }
    else {
        email.style.border = "solid 3px green";
        document.getElementById("email_display").innerHTML = "";
        status = true;

    }
    if (new_password.value.length < 6) {
        new_password.style.border = "solid 3px red"
        document.getElementById("new_display").innerHTML = "Password must be at least 6 char long"
        status = false;
    }
    else {
        new_password.style.border = "solid 3px green";
        document.getElementById("new_display").innerHTML = "";
        status = true;
    }
    if (confirm_password.value.trim() != new_password.value.trim()) {
        confirm_password.style.border = "solid 3px red"
        document.getElementById("con_display").innerHTML = "New Password does not match with confirm password"
        status = false;
    }
    else {
        confirm_password.style.border = "solid 3px green";
        document.getElementById("con_display").innerHTML = "";
        status = true;
    }
    return status;
}