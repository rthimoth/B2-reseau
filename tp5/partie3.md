```
[ranvin@Client ~]$ curl 127.0.0.1:13337
<h1>Hello, je suis un serveur HTTP</h1>
```

je n'ai pas essayer sur internet je suis sur une vm je prèfére trafiquer sur une vm
```
[ranvin@Client ~]$ python tp5_web_client_2.py
http://127.0.0.1:13337) : https://www.ynov.com/
Statut de la réponse : 200
Contenu de la réponse :
<!DOCTYPE html>
<html class="no-js"
      xml:lang="fr" lang="fr-FR"
      x-data="{ isMobileNavOpen: false }" x-on:keydown.escape="isMobileNavOpen = false"
      :class="{ 'nav-is-open': isMobileNavOpen }">
```


```
[ranvin@Client bs_client]$ cat bs_clients.log
2023-12-01 11:42:14,152:INFO:File served: www/index.html to ('127.0.0.1', 49828)
```