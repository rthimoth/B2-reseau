const WebSocket = require('ws');
const redis = require('redis');

// Créez un serveur WebSocket
const wss = new WebSocket.Server({host: '10.1.2.12', port: 8888 });

// Ensemble pour garder une trace des clients connectés
const connectedClients = new Set();

// Connexion au serveur Redis
const redisClient = redis.createClient({ host: '10.1.2.12', port: 6379 });

// Fonction pour diffuser des messages à tous les clients connectés
function broadcastMessage(message, exclude) {
    for (const client of connectedClients) {
        if (client !== exclude && client.readyState === WebSocket.OPEN) {
            client.send(message);
        }
    }
}

wss.on('connection', (ws) => {
    connectedClients.add(ws);

    ws.on('message', async (message) => {
        console.log(`Message reçu : ${message}`);

        if (message.startsWith('Hello|')) {
            const pseudo = message.split('|')[1];
            await redisClient.setAsync(ws._socket.remoteAddress, pseudo);
            broadcastMessage(`Annonce : ${pseudo} a rejoint la chatroom`, ws);
        } else {
            broadcastMessage(message, ws);
        }
    });

    ws.on('close', () => {
        connectedClients.delete(ws);
        console.log('Client déconnecté');
        // Envoyer un message de déconnexion aux autres clients
        broadcastMessage('Un client s\'est déconnecté', ws);
    });
});

console.log('Serveur WebSocket en écoute sur le port 8888');
