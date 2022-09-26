function decode() {
  let text = document.getElementById("decode").value;
  if (text.startsWith('kr_')) {
    text = text.slice(3)
  }
  fetch('http://192.168.10.243/decode/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      text: text
    })
  }).then(response => response.text())
    .then(data => {
      document.getElementById("decoded").innerText = data;
    }).catch(error => console.error(error));
}

function encode() {
  let text = document.getElementById("encode").value;
  fetch('http://192.168.10.243/encode/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      text: text
    })
  }).then(response => response.text())
    .then(data => {
      document.getElementById("encoded").innerText = data;
    }).catch(error => console.error(error));
}