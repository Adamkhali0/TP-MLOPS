# MLOps Monitoring

Prérequis:
- Installer docker
- Python
- Un IDE: Pycharm ou Vscode

Pour créer une image docker de l'application api titanic, dans un terminal, se placer dans le dossier du projet

```
docker build -t titanic_api . 
```

Pour démarrer l'application dans un conteneur docker:

```
docker run -p 5000:5000 -it titanic_api
```

En mode dev, le plus simple c'est de démarrer l'application via vscode ou pycharm, cela nous permet de debugger plus facilement si besoin.

Pour démarrer le tendem prometheus/grafana:

```
docker compose up -d
```

Tout est configuré pour fonctionner avec l'application démarrée en mode dev, c'est à dire démrée avec Pycharm ou vscode.
