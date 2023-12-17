
# MLOps

The project was made by : KHALI Mohammed Adam ,LAABYDY Mohamed :)

![225813708-98b745f2-7d22-48cf-9150-083f1b00d6c9](https://github.com/Adamkhali0/TP-TDLOG/assets/118823327/2b4d03ca-0eb6-4e42-8f5b-d188fa1f5bdd)
# TWITTER STOCK MARKET ![241765460-cc4fe88c-7f7a-41d8-b449-34b7a178c1c6](https://github.com/Adamkhali0/TP-TDLOG/assets/118823327/422c48e3-cc6c-4229-a29f-5ccdcfcbb916)

Twitter a été fondé en 2006 et a été coté en bourse en 2013. Depuis la fondation de Twitter, l'année 2022 a été un événement mémorable pour Twitter. Lorsque Elon Musk a pris le contrôle de Twitter, il a été retiré de la Bourse de New York. Comme 2022 a été si mouvementée pour Twitter, analysons la chronologie complète de Twitter sur le marché boursier de 2013 à 2022.

Twitter est l'une des applications de médias sociaux populaires où les gens partagent ce qu'ils ressentent en un nombre limité de mots. Twitter est populaire, mais pas en bourse.

La data contient :

  Date

  The opening Price of the day

  The highest price of the day

  The lowest price of the day

  The closing price of the day

  The adjusted closing price of the day

  The total number of shares traded in the day (volume)
  
L'objectif de ce projet est d'analyser la performance de Twitter sur le marché boursier au cours de la période de 2013 à 2022, et predire en mettant en évidence les événements clés de cette période.
)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Création de l'Image Docker pour l'API de Prédiction de Crise Cardiaque

1. Ouvrez un terminal et naviguez jusqu'au dossier de votre projet.
2. Exécutez la commande suivante pour construire l'image Docker :
    ```bash
    docker build -t api_TSM.py .
    ```

## Démarrage de l'Application en Mode Développement

- Pour un débogage facile, il est recommandé de démarrer l'application via votre IDE (PyCharm ou VSCode).

## Démarrage de Prometheus et Grafana

1. Exécutez la commande suivante pour démarrer Prometheus et Grafana :
    ```bash
    docker compose up -d
    ```

2. Cette configuration est prête à fonctionner avec l'application lancée en mode développement.

## Accès à Prometheus et Grafana

- Ouvrez un navigateur et accédez à Prometheus sur le port 9090.
- Pour Grafana, accédez au port 3000. Utilisez "admin" comme nom d'utilisateur et "grafana" comme mot de passe.

## Surveillance des Métriques

- Une fois dans Grafana, vous pouvez choisir les métriques à suivre, comme `not_survived_total` et `survived_total`.

En suivant ces étapes, vous serez en mesure de configurer et de surveiller efficacement votre application de prédiction de crises cardiaques, en utilisant Docker pour la gestion des conteneurs, Prometheus pour la surveillance des métriques, et Grafana pour la visualisation des données.

