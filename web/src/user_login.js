let loginButton = async (e) => {
    e.preventDefault();
    const requestBody = {
      username: inputValue("loginUsername"),
      password: inputValue("loginPassword"),
    };
    const response = await asyncWebRequest("/users/login", POST, requestBody);
    if (response.status < 300) {
      localStorage.setItem("user_id", response.user_id);
      location.href = "schedule.html";
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
    };
    const response = await asyncWebRequest("/users", POST, requestBody);
    if (response.status < 300) {
      localStorage.setItem("user_id", response.user_id);
      location.href = "schedule.html";
    }
  };
  
  window.addEventListener("load", (e) => {
    $$("#login-form").addEventListener("submit", loginButton);
    $$("#register-form").addEventListener("submit", registerButton);
  
    if (localStorage.getItem("user_id")) {
      location.href = "schedule.html";
    }
  });
  