let doctor_id = localStorage.getItem("doctor_id");

const toggleClasses = () => {
  $$("#my-patients").classList.toggle("hidden");
  $$("#edit-patient").classList.toggle("hidden");
};

const editUser = async (user_id, reload = false) => {
  let user = await asyncWebRequest("/users", GET, { id: user_id });
  $$("#edit-patient-id").innerHTML = user.user_id;
  $$("#edit-patient-firstname").innerHTML = user.firstname;
  $$("#edit-patient-lastname").innerHTML = user.lastname;
  $$("#edit-patient-address").innerHTML = user.address.replaceAll("|", ", ");
  $$("#edit-patient-email").innerHTML = user.email;
  $$("#edit-patient-phone").innerHTML = user.phone;
  if (!reload) {
    toggleClasses();
  }
  getSchedule(user_id)
};

const getSchedule = async (user_id) => {
  let sched = await asyncWebRequest("/schedule", GET, { user_id: user_id });
  $$("#schedule-table-body").innerHTML = ""
  sched.forEach(async (item) => {
    const medicine = await asyncWebRequest("/medicines", GET, {
      id: item.medicine_id,
    });
    $$("#schedule-table-body").innerHTML +=
      `
    <tr>
        <td scope="row">` +
      item.id +
      `</td>
      <td>` +
      item.time +
      `</td>
        <td>` +
      medicine.name +
      `</td>
      <td>` +
      (item.taken ? `<i class="fa fa-check" aria-hidden="true" style="color: green;"></i>` : `<i class="fa fa-times" aria-hidden="true" style="color: red;"></i>`) +
      `</td>
    </tr>
    `;
  });
};

let discharge = async () => {
  const response = await asyncWebRequest("/doctor_id_user_id", DELETE, {
    doctor_id: doctor_id,
    user_id: $$("#edit-patient-id").innerHTML
  });
  if (response.status < 300) {
    alert("Success!");
  } else {
    alert(response.error);
  }
  location.reload();
}

let addPatientButton = async (e) => {
  e.preventDefault();
  const requestBody = {
    doctor_id: doctor_id,
    user_id: inputValue("select-patient").split(" - ")[0],
  };
  const response = await asyncWebRequest("/doctor_user", POST, requestBody);
  location.reload();
};

let addScheduleButton = async (e) => {
  e.preventDefault();
  let user_id = $$("#edit-patient-id").innerHTML;
  const requestBody = {
    user_id: user_id,
    medicine_id: inputValue("select-medicine").split(" - ")[0],
    time: inputValue("select-date-input"),
    dosage: inputValue("dosage"),
    taken: false,
  };
  const response = await asyncWebRequest("/schedule", POST, requestBody);
  if (response.status <= 300) {
    editUser(user_id, true);
  }
};

window.addEventListener("load", async (e) => {
  $$("#add-patient-form").addEventListener("submit", addPatientButton);
  $$("#add-schedule-form").addEventListener("submit", addScheduleButton);
  $("#select-date").datetimepicker();

  // Get My Patients
  const patients = await asyncWebRequest("/doctor_user/user", GET, {
    doctor_id: doctor_id,
  });
  patients.users.forEach(async (user_id) => {
    const patient = await asyncWebRequest("/users", GET, {
      id: user_id,
    });
    $$("#patient-table-body").innerHTML +=
      `
    <tr>
        <td scope="row">` +
      patient.user_id +
      `</td>
        <td>` +
      patient.firstname +
      `</td>
        <td>` +
      patient.lastname +
      `</td>
        <td onclick="editUser(` +
      patient.user_id +
      `);" class="patient-edit-button">➔</td>
    </tr>
    `;
    sortTable($$('#patients-table'), 0, force=true);
  });

  // Create Dropdown
  const users = await asyncWebRequest("/users/all", GET, {});
  let patientOptions = `
  <select
    class="form-control selectpicker"
    id="select-patient"
    data-live-search="true"
  >`;
  users.forEach((user) => {
    patientOptions +=
      `<option data-tokens="` +
      user.user_id +
      `">` +
      user.user_id +
      ` - ` +
      user.firstname +
      ` ` +
      user.lastname +
      `</option>`;
  });
  patientOptions += "</select>";
  $$("#select-patient-options").innerHTML = patientOptions;
  $("#select-patient").selectpicker();

  // Edit Users
  const medicines = await asyncWebRequest("/medicines/all", GET);
  let medicineOptions = `
  <select
    class="form-control selectpicker"
    id="select-medicine"
    data-live-search="true"
  >`;
  medicines.forEach((medicine) => {
    medicineOptions +=
      `<option data-tokens="` +
      medicine.medicine_id +
      `">` +
      medicine.medicine_id +
      ` - ` +
      medicine.name +
      `</option>`;
  });
  medicineOptions += "</select>";
  $$("#select-medicine-options").innerHTML = medicineOptions;
  $("#select-medicine").selectpicker();
});
