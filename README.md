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
|           12 | Mathieu Leizagoyen       | 1B      |  1209 |
|           13 | Sébastien Picabea        | 1B      |  1205 |
|           14 | Arthur Capelier-Mourguy  | 1B      |  1203 |
|           15 | Baptiste Lagaillardie    | 1B      |  1200 |
|           16 | Alexandre de la Raitrie  | 1B      |  1200 |
|           17 | Mathieu Olhagaray        | 1B      |  1200 |
|           18 | Loïc Harang              | 1B      |  1200 |
|           19 | Vincent Pasquesoone      | 1B      |  1192 |
|           20 | Thibaud Babled           | 1B      |  1190 |
|           21 | Olivier Waltener         | 1B      |  1187 |
|           22 | Michel Lesueur           | 1B      |  1181 |
|           23 | Olivier de Bernardi      | 2A      |  1016 |
|           24 | Emmanuel Poidevin        | 2A      |  1012 |
|           25 | Pierre Meglin            | 2A      |  1000 |
|           26 | Bertrand Lebel           | 2A      |  1000 |
|           27 | Guillaume de Lamaze      | 2A      |  1000 |
|           28 | Pierre Privat            | 2A      |  1000 |
|           29 | Haroun Sachs             | 2A      |  1000 |
|           30 | Lawrence Robert          | 2A      |  1000 |
|           31 | Clément Bonnichon        | 2A      |  1000 |
|           32 | Victor Lassalle          | 2A      |   997 |
|           33 | Alois de Bouville        | 2B      |   824 |
|           34 | Quentin Dionnot          | 2B      |   818 |
|           35 | Dimitri Girardetti       | 2B      |   814 |
|           36 | Igor de Maack            | 2B      |   800 |
|           37 | Adrien Chamberon         | 2B      |   800 |
|           38 | Jean-Dominique Daragnes  | 2B      |   800 |
|           39 | Stéphane Vidaillet       | 2B      |   800 |
|           40 | Olivier Matteoli         | 2B      |   800 |
|           41 | Louis de Lignac          | 2B      |   795 |
|           42 | Éric Dupuy               | 2B      |   793 |
|           43 | Axel Bonneville          | 2B      |   792 |
|           44 | Jean-Philippe Louis      | 2B      |   789 |
|           45 | Stéphane Soulier         | 2B      |   778 |
|           46 | Guillaume Benoit         | 2B      |   775 |
|           47 | Florent Bartoli          | 2B      |   775 |
|           48 | Laurent Fiat             | 2B      |   772 |
