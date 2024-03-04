let doctor_id = localStorage.getItem("doctor_id");

let updateProfileButton = async (e) => {
  e.preventDefault();
  if (inputValue("checkPassword") != inputValue("password")) {
    alert("Password incorrect!");
    return;
  }

  const requestBody = {
    id: doctor_id,
    username: inputValue("username"),
    email: inputValue("updateEmail"),
    phone: inputValue("updatePhone"),
    password: inputValue("password"),
    firstname: inputValue("updateFirstname"),
    lastname: inputValue("updateLastname"),
    address: inputValue("inputAddress")+"|"+inputValue("inputAddress2")+"|"+inputValue("inputCity")+"|"+inputValue("inputState")+"|"+inputValue("inputZip"),
    medical_license: inputValue("updateLicense"),
  };
  const response = await asyncWebRequest("/doctors", PUT, requestBody);
  if (response.status < 300) {
    alert("Success!");
    location.reload();
  }
};

let updatePasswordButton = async (e) => {
  e.preventDefault();
  if (inputValue("currentPassword") != inputValue("password")) {
    alert("Password incorrect!");
    return;
  }
  if (inputValue("updatePassword") != inputValue("confirmPassword")) {
    alert("Passwords do not match!");
    return;
  }

  const requestBody = {
    id: doctor_id,
    password: inputValue("updatePassword"),
  };
  const response = await asyncWebRequest("/doctors/password", PUT, requestBody);
  if (response.status < 300) {
    alert("Success!");
    location.reload();
  }
};

let deleteUserButton = async (e) => {
  e.preventDefault();
  const confirmation = confirm("Are you sure you want to delete this user?");
  if (confirmation) {
    const requestBody = {
      id: doctor_id,
    };
    const response = await asyncWebRequest("/doctors", DELETE, requestBody);
    if (response.status < 300) {
      alert("Success!");
      localStorage.removeItem("doctor_id");
      location.href = "index.html";
    } else {
      alert(response.error);
    }
  }
};

window.addEventListener("load", async (e) => {
  $$("#updateProfileButton").addEventListener("click", updateProfileButton);
  $$("#updatePasswordButton").addEventListener("click", updatePasswordButton);
  $$("#deleteUserButton").addEventListener("click", deleteUserButton);

  const doctor = await asyncWebRequest("/doctors", GET, {
    id: doctor_id,
  });
  $$("#username").value = doctor.username;
  $$("#password").value = doctor.password;

  $$("#updateEmail").value = doctor.email;
  $$("#updatePhone").value = doctor.phone;
  $$("#updateFirstname").value = doctor.firstname;
  $$("#updateLastname").value = doctor.lastname;

  const addr = doctor.address.split("|")
  $$("#inputAddress").value = addr[0]
  $$("#inputAddress2").value = addr[1]
  $$("#inputCity").value = addr[2]
  $$("#inputState").value = addr[3]
  $$("#inputZip").value = addr[4]

  $$("#updateLicense").value = doctor.medical_license;
});
