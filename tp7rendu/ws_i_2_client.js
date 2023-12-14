// ws_client.js
var socket = new WebSocket('ws://localhost:8765');

socket.onopen = function(event) {
    console.log('Connexion établie');
};

socket.onmessage = function(event) {
    console.log('Message reçu: ' + event.data);
    var div = document.createElement('div');
    div.textContent = 'Réponse du serveur: ' + event.data;
    document.body.appendChild(div);
};

function sendMessage(message) {
    socket.send(message);
    console.log('Message envoyé: ' + message);
}

window.sendMessage = sendMessage;