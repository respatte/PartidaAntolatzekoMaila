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
Un classement des joueurs avec les dernières informations entrées et synchronisées est disponible ci-dessous :

|   Classement | Joueur                   | Série   |   PAM |
|-------------:|:-------------------------|:--------|------:|
|            1 | Nicolas Ossard           | 1A      |  1420 |
|            2 | Hugues Saint-Pierre      | 1A      |  1412 |
|            3 | Peio Mendiarat           | 1A      |  1409 |
|            4 | Evhan Dijoux             | 1A      |  1402 |
|            5 | Thibault Martre          | 1A      |  1402 |
|            6 | Charles Bachette-Peyrade | 1A      |  1400 |
|            7 | Ramire Nunez             | 1A      |  1400 |
|            8 | Côme Saint-Pierre        | 1A      |  1387 |
|            9 | Jean-Luc Sallaberry      | 1A      |  1385 |
|           10 | Georges Bachette-Peyrade | 1A      |  1385 |
|           11 | Charles Coustille        | 1B      |  1234 |
|           12 | Arthur Capelier-Mourguy  | 1B      |  1200 |
|           13 | Vincent Pasquesoone      | 1B      |  1200 |
|           14 | Mathieu Olhagaray        | 1B      |  1200 |
|           15 | Mathieu Leizagoyen       | 1B      |  1200 |
|           16 | Loïc Harang              | 1B      |  1200 |
|           17 | Alexandre de la Raitrie  | 1B      |  1200 |
|           18 | Sébastien Picabea        | 1B      |  1200 |
|           19 | Thomas Damitio           | 1B      |  1200 |
|           20 | Baptiste Lagaillardie    | 1B      |  1200 |
|           21 | Thibaud Babled           | 1B      |  1190 |
|           22 | Olivier Waltener         | 1B      |  1187 |
|           23 | Michel Lesueur           | 1B      |  1181 |
|           24 | Pierre Privat            | 2A      |  1000 |
|           25 | Guillaume de Lamaze      | 2A      |  1000 |
|           26 | Peio Arcangues           | 2A      |  1000 |
|           27 | Victor Lassalle          | 2A      |  1000 |
|           28 | Emmanuel Poidevin        | 2A      |  1000 |
|           29 | Clément Bonnichon        | 2A      |  1000 |
|           30 | Pierre Meglin            | 2A      |  1000 |
|           31 | Olivier de Bernardi      | 2A      |  1000 |
|           32 | Bertrand Lebel           | 2A      |  1000 |
|           33 | Lawrence Robert          | 2A      |  1000 |
|           34 | Haroun Sachs             | 2A      |  1000 |
|           35 | Dimitri Girardetti       | 2B      |   700 |
|           36 | Andde                    | 2B      |   700 |
|           37 | Alois de Bouville        | 2B      |   700 |
|           38 | Adrien Chamberon         | 2B      |   700 |
|           39 | Jean-Dominique Daragnes  | 2B      |   700 |
|           40 | Olivier Matteoli         | 2B      |   700 |
|           41 | Laurent Fiat             | 2B      |   700 |
|           42 | Axel Bonneville          | 2B      |   700 |
|           43 | Jean-Philippe Louis      | 2B      |   700 |
|           44 | Stéphane Vidaillet       | 2B      |   700 |
|           45 | Florent Bartoli          | 2B      |   700 |
|           46 | Igor de Maack            | 2B      |   700 |

