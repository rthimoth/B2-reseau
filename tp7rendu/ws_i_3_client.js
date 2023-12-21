// const WebSocket = require('ws');
// const readline = require('readline');

// // Création d'une interface de lecture de ligne pour les entrées utilisateur
// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
// });

// // Connexion au serveur WebSocket
// const socket = new WebSocket('ws://127.0.0.1:8888');

// // Événement déclenché lors de l'ouverture de la connexion WebSocket
// socket.on('open', () => {
//     rl.question('Entrez votre pseudo: ', (pseudo) => {
//         socket.send(`Hello|${pseudo}`);
//         rl.prompt();

//         rl.on('line', (line) => {
//             socket.send(line);
//             rl.prompt();
//         });
//     });
// });

function toto() {
  return new Promise((resolve) => {
    console.log('toto')
  });
}
function yuyu() {
    return new Promise((resolve) => {
      console.log('tutu')
    });
  }


  async function asyncCall() {
    console.log('calling');
    const result = await toto();
    const resdddult = await yuyu    ();
    console.log(result);
    // Expected output: "resolved"
  }
  
// Gestionnaire pour les messages reçus du serveur
// socket.on('message', (data) => {
//     console.log("Événement message déclenché.");
//     console.log(`Reçu: ${data}`);
// });
socket.onmessage = (event) => {
    console.log(event.data);
  };

// Gestionnaire pour les erreurs WebSocket
socket.on('error', (error) => {
    console.error("Erreur WebSocket:", error);
});

// Gestionnaire pour la fermeture de la connexion WebSocket
socket.on('close', () => {
    console.log("Le serveur s'est déconnecté.");
    process.exit(0);
});
