# HAI716I - Projet 2 : THOMAS Lucas

## Lancement

```bash
python3 main.py True 0 0 123456
```

Les arguments sont, dans l’ordre:
1) "True" pour afficher les logs, "False" pour afficher seulement le classement
2) la matrice : "0" pour Axelrod, "1" pour la chasse au cerf
3) le pourcentage de bruit
4) la seed, si vide elle sera randomisée

## Tournoi de base

Dans "main.py", utiliser les cinq stratégies du cours:

```python
joueurs = [p1, p2, p3, p4, p5]
```

Puis lancer:

```bash
python3 main.py True 0 0 123456
```

## Tournoi avec les nouvelles stratégies

Dans "main.py", decommenter les huit stratégies:

```python
joueurs = [p1, p2, p3, p4, p5, p6, p7, p8]
```

Puis lancer:

```bash
python3 main.py True 0 0 123456
```

## Modifications du tournoi

Avec les huit stratégies:

### Chasse au cerf

```bash
python3 main.py True 1 0 123456
```

### Avec bruit de 5 %

```bash
python3 main.py True 0 5 123456
```