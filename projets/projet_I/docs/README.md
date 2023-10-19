

# Setup 

## Installer PyEnv  & créer un environnement virtuel
- Guide dans le fichier `setup_env.html ``




## Exécuter le code 
```bash
# Activer l'environnement virtuel (linux)
source env/bin/activate 
python3 main.py
```

# Exercices 

## Exercice 1
- On ne récupère actuellement que la liste d'un équipage. Modifier le code pour que l'on récupère la liste de tous les pirates de la Nouvelle Vague : http://www.volonte-d.com/perso/pirates.php.


- Pour chaque personnage, rapatrier la liste des noms des techniques de combat. Créer le dictionnaire : 
    ```
    {personnage:["technique_1_nom", "technique_2_nom"...]}
    ```

- Créer une table `équipages` avec les colonnes suivantes : 
    - Id (entier positif unique par ligne)
    - Nom de l'équipage
    - Nombre de membres

- Créer une table `personnages` avec les colonnes suivantes : 
    - Id (entier positif unique par ligne)
    - Nom du personnage
    - Foreign Key sur l'équipage de la table `équipage` (donc l'id de l'équipage auquel appartient le personnage)

- Créer une table `techniques` avec les colonnes suivantes : 
    - Id (entier positif unique par ligne)
    - Nom de la technique
    - Foreign Key sur le personnage de la table `personnages` (donc l'id du personnage qui possède la technique)

- *Cette question est plus difficile et nécessite de faire des recherches.* Pour chaque technique de combat, récupérer la photo associée. Créer une nouvelle colonne dans la table technique, et stocker la photo (il faut trouver comment la stocker).



## Exercice 2
Avec le site de votre choix qui contient des données qui permettront de créer deux tables dont une table contient une Foreign Key pointant sur l'autre table, reproduire la démarche du projet_I.