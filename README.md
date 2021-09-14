# PartidaAntolatzekoMaila
Elo rating system for the Club de Pelote Basque de Paris. Mostly in French, for local use.

## Méthode, équations
Lors d'une rencontre, le PAM moyen de chaque équipe est pris en compte pour calculer leurs probabilités de victoire. La différence entre le résultat final (victoire notée 1 ou défaite notée 0), multipliée par un facteur d'échelle `k`, est ensuite utilisée pour mettre à jour les PAMs de tous les joueurs. Le facteur d'échelle utilisé est actuellement calculé comme suit :

```
k = 20 * (3 - 2*min(score_gagnant, score_perdant)/score_gagnant)
# min() important dans le cas où l'équipe perdante marque plus de points au total
```

Ainsi, le changement de PAM pour une partie serrée à niveau équivalent est d'environ 10 points PAM, et peut aller jusqu'à 30 points pour une victoire écrasante à niveau équivalent. Dans le cas de la victoire d'une équipe donnée gagnante, le changement de PAM tend vers 0, alors que dans le cas extrême d'une victoire écrasante d'une équipe annoncée perdante le changement peut être de 60 points.

## Classement des joueurs
Un classement des joueurs avec les dernières informations entrées et synchronisées sera disponible ci-dessous.
