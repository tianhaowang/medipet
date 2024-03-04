const getMedicines = async () => {
  let medicines = await asyncWebRequest("/medicines/all", GET, {});
  $$("#medicines-table-body").innerHTML = "";
  medicines.forEach(async (med) => {
    $$("#medicines-table-body").innerHTML +=
      `
      <tr>
          <th scope="row">` +
      med.medicine_id +
      `</th>
        <td>` +
      med.name +
      `</td>
        <td style="max-width: 400px;
        text-overflow: ellipsis;
        white-space: nowrap;
        overflow: hidden;">` +
      med.description +
      `</td>
        <td>
      <img style="max-height: 2em; margin: -10px; padding-left: 10px;" 
        src="` + med.image + `"/>
        </td>
        <td>
          <button style="margin: -10px; padding: 5px; font-size: 0.8em;" 
            type="button" 
            class="btn btn-secondary" onclick="editMedicine('` + med.medicine_id + `')">Edit</button>
        </td>
      </tr>
      `;
  });
};

const saveMedicine = async (id, dialog) => {
  let req = await asyncWebRequest("/medicines", PUT, {
    id: id,
    name: $$("#dialog #med-name").value,
    description: $$("#dialog #med-desc").value
  });
  getMedicines();
  dialog.dialog( "close" );
}

const deleteMedicine = async (id, dialog) => {
  let req = await asyncWebRequest("/medicines", DELETE, {
    id: id
  });
  getMedicines();
  dialog.dialog( "close" );
}

const editMedicine = async (id) => {
  const medicine = await asyncWebRequest("/medicines", GET, {
    id: id,
  });
  $$("#dialog #med-name").value = medicine.name
  $$("#dialog #med-desc").value = medicine.description
  $( "#dialog" ).dialog({
    resizable: true,
    height: "auto",
    width: 400,
    modal: true,
    buttons: {
      "Save": function() {
        saveMedicine(id, $(this))
      },
      "Delete": function() {
        deleteMedicine(id, $(this))
      },
      Cancel: function() {
        $( this ).dialog( "close" );
      }
    }
  });
}

const addMedicine = async () => {
  if ($$("#new-medicine #name").value == "" || $$("#new-medicine #description").value == "") {
    alert("Cannot submit empty form!")
    return;
  }
  let formData = new FormData();
  formData.append('file', $$("#new-medicine #file").files[0]); 
  formData.append('name', $$("#new-medicine #name").value); 
  formData.append('description', $$("#new-medicine #description").value);
  $$("form#new-medicine").reset();

  const requestUrl = baseUrl + "/medicines_with_image";
  const response = await fetch(requestUrl, {
    method: "POST",
    mode: "cors",
    cache: "no-cache",
    credentials: "same-origin",
    headers: { },
    redirect: "follow",
    referrerPolicy: "no-referrer",
    body: formData,
  });
  getMedicines();
  let status = await response.status;
  let data = await response.json();
  data["status"] = status;
  if (status < 300) {
    alert("Entry added!");
  } else {
    alert("Error: " + status + " Details: " + JSON.stringify(data));
  }
}

window.addEventListener("load", async (e) => {
  getMedicines();
});
