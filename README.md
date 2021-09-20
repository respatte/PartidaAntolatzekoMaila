# PartidaAntolatzekoMaila
Elo rating system for the Club de Pelote Basque de Paris. Mostly in French, for local use.

## Méthode, équations
Lors d'une rencontre, le PAM moyen de chaque équipe est pris en compte pour calculer leurs probabilités de victoire. La différence entre le résultat final (victoire notée 1 ou défaite notée 0), multipliée par un facteur d'échelle `k`, est ensuite utilisée pour mettre à jour les PAMs de tous les joueurs. Le facteur d'échelle utilisé est actuellement calculé comme suit, avec un poids des parties par défaut à 1, modifiable pour les tournois spéciaux.

```
k = 30 * poids_partie
```

## Classement des joueurs
Un classement des joueurs avec les dernières informations entrées et synchronisées est disponible ci-dessous :

|   Classement | Joueur                   | Série   |   PAM |
|-------------:|:-------------------------|:--------|------:|
|            1 | Hugues Saint-Pierre      | 1A      |  1419 |
|            2 | Nicolas Ossard           | 1A      |  1414 |
|            3 | Peio Mendiarat           | 1A      |  1407 |
|            4 | Ramire Nunez             | 1A      |  1400 |
|            5 | Charles Bachette-Peyrade | 1A      |  1392 |
|            6 | Thibault Martre          | 1A      |  1386 |
|            7 | Georges Bachette-Peyrade | 1A      |  1383 |
|            8 | Côme Saint-Pierre        | 1A      |  1382 |
|            9 | Evhan Dijoux             | 1A      |  1378 |
|           10 | Jean-Luc Sallaberry      | 1A      |  1362 |
|           11 | Julien Jimenez           | 1A      |  1356 |
|           12 | Olivier Waltener         | 1B      |  1253 |
|           13 | Charles Coustille        | 1B      |  1239 |
|           14 | Thibaud Babled           | 1B      |  1234 |
|           15 | Michel Lesueur           | 1B      |  1218 |
|           16 | Sébastien Picabea        | 1B      |  1207 |
|           17 | Mathieu Olhagaray        | 1B      |  1200 |
|           18 | Baptiste Lagaillardie    | 1B      |  1200 |
|           19 | Loïc Harang              | 1B      |  1200 |
|           20 | Vincent Pasquesoone      | 1B      |  1197 |
|           21 | Mathieu Leizagoyen       | 1B      |  1191 |
|           22 | Alexandre de la Raitrie  | 1B      |  1178 |
|           23 | Arthur Capelier-Mourguy  | 1B      |  1167 |
|           24 | Clément Bonnichon        | 2A      |  1022 |
|           25 | Victor Lassalle          | 2A      |  1018 |
|           26 | Éric Edwards             | 2A      |  1011 |
|           27 | Emmanuel Poidevin        | 2A      |  1009 |
|           28 | Bertrand Lebel           | 2A      |  1000 |
|           29 | Pierre Meglin            | 2A      |  1000 |
|           30 | Pierre Privat            | 2A      |  1000 |
|           31 | Guillaume de Lamaze      | 2A      |  1000 |
|           32 | Alex Duthil              | 2A      |   994 |
|           33 | Cyril Houplain           | 2A      |   992 |
|           34 | Olivier de Bernardi      | 2A      |   987 |
|           35 | Lawrence Robert          | 2A      |   978 |
|           36 | Haroun Sachs             | 2A      |   956 |
|           37 | Dimitri Girardetti       | 2B      |   850 |
|           38 | Stéphane Vidaillet       | 2B      |   841 |
|           39 | Alois de Bouville        | 2B      |   826 |
|           40 | Caroline Leclercq        | 2B      |   822 |
|           41 | Quentin Dionnot          | 2B      |   820 |
|           42 | Louis de Lignac          | 2B      |   806 |
|           43 | Jacques Guerin           | 2B      |   804 |
|           44 | Jean-Dominique Daragnes  | 2B      |   800 |
|           45 | Olivier Matteoli         | 2B      |   797 |
|           46 | Jean-Philippe Louis      | 2B      |   792 |
|           47 | Axel Bonneville          | 2B      |   790 |
|           48 | Éric Dupuy               | 2B      |   787 |
|           49 | Igor de Maack            | 2B      |   786 |
|           50 | Laurent Fiat             | 2B      |   783 |
|           51 | Adrien Chamberon         | 2B      |   777 |
|           52 | Florent Bartoli          | 2B      |   777 |
|           53 | Stéphane Soulier         | 2B      |   776 |
|           54 | Guillaume Benoit         | 2B      |   771 |
