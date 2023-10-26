TP1 : Maîtrise réseau du poste
Pour ce TP, on va utiliser uniquement votre poste (pas de VM, rien, quedal, quetchi).
Le but du TP : se remettre dans le bain tranquillement en manipulant pas mal de concepts qu'on a vu l'an dernier.
C'est un premier TP chill, qui vous(ré)apprend à maîtriser votre poste en ce qui concerne le réseau. Faites le seul ou avec votre mate préféré bien sûr, mais jouez le jeu, faites vos propres recherches.
La "difficulté" va crescendo au fil du TP, mais la solution tombe très vite avec une ptite recherche Google si vos connaissances de l'an dernier deviennent floues.

TP1 : Maîtrise réseau du poste
I. Basics
II. Go further
III. Le requin


I. Basics

Tout est à faire en ligne de commande, sauf si précision contraire.

☀️ Carte réseau WiFi
Déterminer...

l'adresse MAC de votre carte WiFi 

```
ipconfig /all  4C-03-4F-E7-6A-FD
```

l'adresse IP de votre carte WiFi

``` 
ipconfig /all 10.33.76.204
```

le masque de sous-réseau du réseau LAN auquel vous êtes connectés en WiFi
en notation CIDR, par exemple /16

```
/20
```

ET en notation décimale, par exemple 255.255.0.0

```
255.255.240.0
```






☀️ Déso pas déso
Pas besoin d'un terminal là, juste une feuille, ou votre tête, ou un tool qui calcule tout hihi. Déterminer...

l'adresse de réseau du LAN auquel vous êtes connectés en WiFi

```
https://www.site24x7.com/fr/tools/ipv4-sous-reseau-calculatrice.html Je pense qu'il est super 4096
```

l'adresse de broadcast
le nombre d'adresses IP disponibles dans ce réseau

```
 ipconfig 10.33.79.255
 ```

☀️ Hostname

déterminer le hostname de votre PC

```
hostname Timo
```

☀️ Passerelle du réseau
Déterminer...

l'adresse IP de la passerelle du réseau

```
ipconfig /all 
10.33.79.254
```

l'adresse MAC de la passerelle du réseau

```
ipconfig /all 
4C-03-4F-E7-6A-FD
```

☀️ Serveur DHCP et DNS
Déterminer...

l'adresse IP du serveur DHCP qui vous a filé une IP

``` 
ipconfig /all 
10.33.79.254
```

l'adresse IP du serveur DNS que vous utilisez quand vous allez sur internet

```
ipconfig /all 
serveurs DNS 8.8.8.8 8.8.4.4
```

☀️ Table de routage
Déterminer...

dans votre table de routage, laquelle est la route par défaut

```
 netstat -r 

  0.0.0.0          0.0.0.0     10.33.79.254     10.33.76.204     30

```




II. Go further

Toujours tout en ligne de commande.


☀️ Hosts ?

faites en sorte que pour votre PC, le nom b2.hello.vous corresponde à l'IP 1.1.1.1



prouvez avec un ping b2.hello.vous que ça ping bien 1.1.1.1



Vous pouvez éditer en GUI, et juste me montrer le contenu du fichier depuis le terminal pour le compte-rendu.


☀️ Go mater une vidéo youtube et déterminer, pendant qu'elle tourne...

l'adresse IP du serveur auquel vous êtes connectés pour regarder la vidéo
le port du serveur auquel vous êtes connectés
le port que votre PC a ouvert en local pour se connecter au port du serveur distant

``` 
netstat -n TCP    
10.33.76.204:52893     162.159.133.234:443    TIME_WAIT 
```

☀️ Requêtes DNS
Déterminer...

à quelle adresse IP correspond le nom de domaine www.ynov.com

```
 PS C:\Users\Timot> nslookup www.ynov.com
Serveur :   dns.google
Address:  8.8.8.8

Réponse ne faisant pas autorité :
Nom :    www.ynov.com
Addresses:  2606:4700:20::681a:be9
          2606:4700:20::681a:ae9
          2606:4700:20::ac43:4ae2
          104.26.10.233
          172.67.74.226
          104.26.11.233

```


Ca s'appelle faire un "lookup DNS".


à quel nom de domaine correspond l'IP 174.43.238.89

```
PS C:\Users\Timot> nslookup 174.43.238.89
Serveur :   dns.google
Address:  8.8.8.8

Nom :    89.sub-174-43-238.myvzw.com
Address:  174.43.238.89
```

Ca s'appelle faire un "reverse lookup DNS".


☀️ Hop hop hop
Déterminer...

par combien de machines vos paquets passent quand vous essayez de joindre www.ynov.com

```
PS C:\Users\Timot> tracert www.ynov.com

Détermination de l’itinéraire vers www.ynov.com [104.26.10.233]
avec un maximum de 30 sauts :

  1     1 ms     1 ms     1 ms  192.168.1.1
  2     8 ms     8 ms     8 ms  1.51.147.77.rev.sfr.net [77.147.51.1]
  3     7 ms     7 ms     7 ms  149.235.64.86.rev.sfr.net [86.64.235.149]
  4     8 ms     7 ms     7 ms  129.237.64.86.rev.sfr.net [86.64.237.129]
  5    12 ms    11 ms    10 ms  149.98.0.109.rev.sfr.net [109.0.98.149]
  6     9 ms     8 ms     7 ms  6.179.96.84.rev.sfr.net [84.96.179.6]
  7     9 ms     9 ms     9 ms  10.179.96.84.rev.sfr.net [84.96.179.10]
  8    16 ms    15 ms    16 ms  12.148.6.194.rev.sfr.net [194.6.148.12]
  9    15 ms    15 ms    15 ms  12.148.6.194.rev.sfr.net [194.6.148.12]
 10    16 ms    18 ms    16 ms  141.101.67.48
 11    17 ms    20 ms    20 ms  172.71.128.4
 12    16 ms    16 ms    16 ms  104.26.10.233
```


☀️ IP publique
Déterminer...

l'adresse IP publique de la passerelle du réseau (le routeur d'YNOV donc si vous êtes dans les locaux d'YNOV quand vous faites le TP)

```
PS C:\Users\Timot> nslookup myip.opendns.com resolver1.opendns.com
Serveur :   dns.opendns.com
Address:  208.67.222.222

Réponse ne faisant pas autorité :
Nom :    myip.opendns.com
Address:  77.147.51.5
```


☀️ Scan réseau
Déterminer...

combien il y a de machines dans le LAN auquel vous êtes connectés


Allez-y mollo, on va vite flood le réseau sinon. :)

```
Itinéraire déterminé.
PS C:\Users\Timot> arp -a

Interface : 192.168.1.39 --- 0xc
  Adresse Internet      Adresse physique      Type
  192.168.1.1           44-ce-7d-f3-ae-b0     dynamique
  192.168.1.255         ff-ff-ff-ff-ff-ff     statique
  224.0.0.22            01-00-5e-00-00-16     statique
  224.0.0.251           01-00-5e-00-00-fb     statique
  224.0.0.252           01-00-5e-00-00-fc     statique
  239.255.255.250       01-00-5e-7f-ff-fa     statique
  255.255.255.255       ff-ff-ff-ff-ff-ff     statique

Interface : 192.168.56.1 --- 0x12
  Adresse Internet      Adresse physique      Type
  192.168.56.255        ff-ff-ff-ff-ff-ff     statique
  224.0.0.22            01-00-5e-00-00-16     statique
  224.0.0.251           01-00-5e-00-00-fb     statique
  224.0.0.252           01-00-5e-00-00-fc     statique
  239.255.255.250       01-00-5e-7f-ff-fa     statique
```


III. Le requin
Faites chauffer Wireshark. Pour chaque point, je veux que vous me livrez une capture Wireshark, format .pcap donc.
Faites clean 🧹, vous êtes des grands now :

livrez moi des captures réseau avec uniquement ce que je demande et pas 40000 autres paquets autour

vous pouvez sélectionner seulement certains paquets quand vous enregistrez la capture dans Wireshark


stockez les fichiers .pcap dans le dépôt git et côté rendu Markdown, vous me faites un lien vers le fichier, c'est cette syntaxe :


[Lien vers capture ARP](./captures/arp.pcap)



☀️ Capture ARP


📁 fichier arp.pcap

capturez un échange ARP entre votre PC et la passerelle du réseau


Si vous utilisez un filtre Wireshark pour mieux voir ce trafic, précisez-le moi dans le compte-rendu.


[lien vers capture ARP](./testarp.pcap)
```
filtre wireshark utilisé 'arp'

```

☀️ Capture DNS


📁 fichier dns.pcap

capturez une requête DNS vers le domaine de votre choix et la réponse
vous effectuerez la requête DNS en ligne de commande


Si vous utilisez un filtre Wireshark pour mieux voir ce trafic, précisez-le moi dans le compte-rendu.


[lien vers capture DNS](./dns3.pcap)
```
filtre utilisé dans wireshark 'dns'
```

☀️ Capture TCP


📁 fichier tcp.pcap

effectuez une connexion qui sollicite le protocole TCP
je veux voir dans la capture :

un 3-way handshake
un peu de trafic
la fin de la connexion TCP


[lien vers capture TCP](./tcpparfait.pcapng)
```
filtre utilisé 'tcp'
```


Si vous utilisez un filtre Wireshark pour mieux voir ce trafic, précisez-le moi dans le compte-rendu.




Je sais que je vous l'ai déjà servi l'an dernier lui, mais j'aime trop ce meme hihi 🐈