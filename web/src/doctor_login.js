let loginButton = async (e) => {
  e.preventDefault();
  const requestBody = {
    username: inputValue("loginUsername"),
    password: inputValue("loginPassword"),
  };
  const response = await asyncWebRequest("/doctors/login", POST, requestBody);
  if (response.status < 300) {
    localStorage.setItem("doctor_id", response.doctor_id);
    location.href = "patients.html";
  }
};

let registerButton = async (e) => {
  e.preventDefault();
  if (inputValue("confirmPassword") != inputValue("registerPassword")) {
    alert("Passwords do not match!");
    return;
  }

  const requestBody = {
    username: inputValue("registerUsername"),
    email: inputValue("updateEmail"),
    phone: inputValue("updatePhone"),
    password: inputValue("registerPassword"),
    firstname: inputValue("updateFirstname"),
    lastname: inputValue("updateLastname"),
    address: inputValue("inputAddress")+"|"+inputValue("inputAddress2")+"|"+inputValue("inputCity")+"|"+inputValue("inputState")+"|"+inputValue("inputZip"),
    medical_license: inputValue("updateLicense"),
  };
  const response = await asyncWebRequest("/doctors", POST, requestBody);
  if (response.status < 300) {
    localStorage.setItem("doctor_id", response.doctor_id);
    location.href = "patients.html";
  }
};

window.addEventListener("load", (e) => {
  $$("#login-form").addEventListener("submit", loginButton);
  $$("#register-form").addEventListener("submit", registerButton);

  if (localStorage.getItem("doctor_id")) {
    location.href = "patients.html";
  }
});
