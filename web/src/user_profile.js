let user_id = localStorage.getItem("user_id");

let updateProfileButton = async (e) => {
  e.preventDefault();
  if (inputValue("checkPassword") != inputValue("password")) {
    alert("Password incorrect!");
    return;
  }

  const requestBody = {
    id: user_id,
    username: inputValue("username"),
    email: inputValue("updateEmail"),
    phone: inputValue("updatePhone"),
    password: inputValue("password"),
    firstname: inputValue("updateFirstname"),
    lastname: inputValue("updateLastname"),
    address: inputValue("inputAddress")+"|"+inputValue("inputAddress2")+"|"+inputValue("inputCity")+"|"+inputValue("inputState")+"|"+inputValue("inputZip"),
  };
  const response = await asyncWebRequest("/users", PUT, requestBody);
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
    id: user_id,
    password: inputValue("updatePassword"),
  };
  const response = await asyncWebRequest("/users/password", PUT, requestBody);
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
      id: user_id,
    };
    const response = await asyncWebRequest("/users", DELETE, requestBody);
    if (response.status < 300) {
      alert("Success!");
      localStorage.removeItem("user_id");
      location.href = "index.html";
    } else {
      alert(response.error);
    }
  }
};

window.addEventListener("load", async (e) => {
  $$("#updateProfileButton").addEventListener("click", updateProfileButton);
  $$("#updatePasswordButton").addEventListener("click", updatePasswordButton);
  // $$("#deleteUserButton").addEventListener("click", deleteUserButton);

  const user = await asyncWebRequest("/users", GET, {
    id: user_id,
  });
  $$("#username").value = user.username;
  $$("#password").value = user.password;

  $$("#updateEmail").value = user.email;
  $$("#updatePhone").value = user.phone;
  $$("#updateFirstname").value = user.firstname;
  $$("#updateLastname").value = user.lastname;

  const addr = user.address.split("|")
  $$("#inputAddress").value = addr[0]
  $$("#inputAddress2").value = addr[1]
  $$("#inputCity").value = addr[2]
  $$("#inputState").value = addr[3]
  $$("#inputZip").value = addr[4]
});
