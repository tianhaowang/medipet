let user_id = localStorage.getItem("user_id");

const getSchedule = async () => {
  let sched = await asyncWebRequest("/schedule", GET, { user_id: user_id });
  $$("#schedule-table-body").innerHTML = "";
  const events = []

  for (let i = 0; i < sched.length; i++) {
    const item = sched[i]
    const medicine = await asyncWebRequest("/medicines", GET, {
      id: item.medicine_id,
    });
    events.push({
      title: medicine.name,
      start: Date.parse(item.time),
      color: item.taken ? "green" : "red",
      textColor: item.taken ? "green" : "red",
      url: 'javascript:createPopup(' + item.id + ', "' + medicine.name + '", "' + medicine.image + '", "' + item.dosage + '", "' + medicine.description + '", ' + item.taken + ')',
    })
    $$("#schedule-table-body").innerHTML +=
      `
      <tr>
          <th scope="row">` +
      item.id +
      `</th>
        <td>` +
      item.time +
      `</td>
          <td>` +
      medicine.medicine_id +
      ` - ` +
      medicine.name +
      `</td>
        <td>` +
      item.taken +
      `</td>
      </tr>
      `;
  }

  let elem = $$("#calendar");
  initCalendar(elem, events)
};

let markTaken = async (id, dialog) => {
  let req = await asyncWebRequest("/schedule/"+id, PUT, { taken: true });
  getSchedule();
  dialog.dialog("close")
}

let createPopup = (id, name, image, dosage, desc, taken) => {
  $$("#dialog #title").innerHTML = name;
  if (taken) {
    $$("#dialog #dosage").innerHTML = "Already Taken!"
  } else {
    $$("#dialog #dosage").innerHTML = dosage
  }
  $$("#dialog #desc").innerHTML = desc
  $$("#dialog #img").setAttribute("src", image)

  if (!taken) {
    $( "#dialog" ).dialog({
      resizable: true,
      height: "auto",
      width: 400,
      modal: true,
      buttons: {
        "Mark as taken": function() {
          markTaken(id, $(this))
        },
        Cancel: function() {
          $( this ).dialog( "close" );
        }
      }
    });
  } else {
    $( "#dialog" ).dialog({
      resizable: true,
      height: "auto",
      width: 400,
      modal: true,
      buttons: {
        Done: function() {
          $( this ).dialog( "close" );
        }
      }
    });
  }
}

window.addEventListener("load", async (e) => {
  getSchedule();
});