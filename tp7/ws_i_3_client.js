const WebSocket = require('ws');
const readline = require('readline');

// Création d'une interface de lecture de ligne
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Fonction pour demander une entrée utilisateur de manière asynchrone
async function askQuestionAsync(question) {
  return new Promise((resolve, reject) => {
    rl.question(question, (input) => {
      resolve(input);
    });
  });
}

// Connexion au serveur WebSocket
const socket = new WebSocket('ws://127.0.0.1:8888');

// Gestionnaire pour l'ouverture du WebSocket
socket.on('open', async () => {
  const pseudo = await askQuestionAsync('Entrez votre pseudo: ');

  // Envoi du pseudo au serveur
  await socket.send(`Hello|${pseudo}`);

  // Boucle pour gérer les entrées utilisateur de manière asynchrone
  for await (const message of rl.on('line', (line) => line)) {
    socket.send(message);
  }
});

// Gestionnaires pour les messages, erreurs, et fermeture du WebSocket
socket.on('message', (data) => {
  console.log(`Message reçu d'un autre utilisateur: ${data}`);
});

socket.on('error', (error) => {
  console.error("Erreur WebSocket:", error);
});

socket.on('close', () => {
  console.log("Le serveur s'est déconnecté.");
  process.exit(0);
});
