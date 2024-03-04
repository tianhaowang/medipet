let initCalendar = (element, events) => {
  var calendar = new FullCalendar.Calendar(element, {
    initialView: "dayGridMonth",
    initialDate: "2024-02-07",
    headerToolbar: {
      left: "prev,next today",
      center: "title",
      right: "dayGridMonth,timeGridWeek,timeGridDay",
    },
    events: events,
    eventDidMount: function(info) {
      if (info.event.textColor) {
        info.el.style.color = info.event.textColor;
      }
    }
  });

  calendar.render();
};
