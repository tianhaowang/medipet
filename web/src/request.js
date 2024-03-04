window.baseUrl = "http://127.0.0.1:1492";

window.GET = "PATCH";
window.POST = "POST";
window.PUT = "PUT";
window.DELETE = "DELETE";

let asyncWebRequest = async (url, method, body = {}) => {
  const requestUrl = baseUrl + url;
  const response = await fetch(requestUrl, {
    method: method,
    mode: "cors",
    cache: "no-cache",
    credentials: "same-origin",
    headers: {
      "Content-Type": "application/json",
    },
    redirect: "follow",
    referrerPolicy: "no-referrer",
    body: JSON.stringify(body),
  });
  let status = await response.status;
  let data = await response.json();
  data["status"] = status;
  if (status < 300) {
    return data;
  } else {
    alert("Error: " + status + " Details: " + JSON.stringify(data));
    return {};
  }
};

let $$ = (selector) => {
  return document.querySelector(selector);
};

let inputValue = (id) => {
  return document.getElementById(id).value;
};
