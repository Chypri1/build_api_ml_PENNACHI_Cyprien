# Vers du DevOps (Code Engineering)

**Attention : ces TD font office de contrôle continu pour le module MLOps. Une note individuelle sera attribuée.**

## Partie I : 

### Contexte Général

Les deux séances de TD seront consacrées au déploiement (ingénierie logicielle). L'objectif est d'aborder des notions essentielles à travers un projet pratique. Ces notions seront intégrées dans l'ordre suivant :

1. Gérer la communication entre des microservices (API) avec Docker Compose, via des Domain Unix Sockets.
2. Ajouter une base de données dans l'écosystème.
3. Introduire les GitHub Actions (.github/workflows/ci_cd.yml).
4. **L'utilisation de Nginx est-elle nécessaire ?**
    - L'utilisation de nginx est utile dans une utilisation locale, cela permet de redirigé les ports vers des vrais noms de services. 
    Cela permet de donner une adresse pour plusieurs instance du même service derrière.
    Dans le cas d'une utilisation cloud, cela permet de redistribuer la charge des requêtes sur plusieurs instances du même composant. 
    Cela permet aussi de gérer les différents certitifats, et bloquer des adresses IP si besoin.
5. **Migrer de Docker Compose vers Kubernetes (Minikube) ?**
    - Dans notre contexte local, l'utilisation de docker compose a du sens pour pouvoir tester toute la chaine. Les github actions font une partie du travail pour le déploiement. 
    Dans le cas d'une utilisation cloud, le déploiement est plus simple avec kubernetes. La combinaison de docker compose en local et de kubernetes pour une solution cloud est utile et utilisée.
    
### Lien vers la base commune

Une base commune vous a été fournie sous le lien suivant : [https://github.com/AghilasSini/build_api_ml.git](https://github.com/AghilasSini/build_api_ml.git). Vous devrez décider si vous souhaitez intégrer ou non les éléments mentionnés dans la liste ci-dessus. Chaque choix devra être justifié.

---

## Instructions Générales : 

Une base commune vous a été fournie. À vous de décider si vous souhaitez intégrer ou non les éléments évoqués dans la liste ci-dessus. Chaque choix devra être justifié.

---

## Partie II – Un portail web adapté 

Il s'agit de concevoir une solution prenant en compte les éléments mentionnés ci-dessus et répondant au cahier des charges illustré par la figure ci-dessous (analogie avec Umtice).

![Projet](./un_portail_pour_les_gouverner_tous.png)
---

## Partie III – Un portail web pour tous les gouvernés (conception et architecture de système pour du ML)

Il s'agit de concevoir une plateforme d'annotation automatique de données brutes. Cette plateforme devra héberger des outils de traitement automatique des langues.

---

