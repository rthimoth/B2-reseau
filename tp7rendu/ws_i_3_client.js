const WebSocket = require('ws');
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const socket = new WebSocket('ws://127.0.0.1:8888');

socket.on('open', () => {
    rl.question('Entrez votre pseudo: ', (pseudo) => {
        socket.send(`Hello|${pseudo}`);
        rl.prompt();

        rl.on('line', (line) => {
            socket.send(line);
            rl.prompt();
        });
    });
});

socket.on('message', (data) => {
    console.log(`Reçu: ${data}`);
});

socket.on('close', () => {
    console.log("Le serveur s'est déconnecté.");
    process.exit(0);
});
