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
|            1 | Hugues Saint-Pierre      | 1A      |  1438 |
|            2 | Nicolas Ossard           | 1A      |  1431 |
|            3 | Peio Mendiarat           | 1A      |  1420 |
|            4 | Côme Saint-Pierre        | 1A      |  1413 |
|            5 | Ramire Nunez             | 1A      |  1400 |
|            6 | Thibault Martre          | 1A      |  1389 |
|            7 | Georges Bachette-Peyrade | 1A      |  1388 |
|            8 | Charles Bachette-Peyrade | 1A      |  1372 |
|            9 | Evhan Dijoux             | 1A      |  1357 |
|           10 | Julien Jimenez           | 1A      |  1356 |
|           11 | Jean-Luc Sallaberry      | 1A      |  1350 |
|           12 | Olivier Waltener         | 1B      |  1246 |
|           13 | Michel Lesueur           | 1B      |  1245 |
|           14 | Sébastien Picabea        | 1B      |  1235 |
|           15 | Thibaud Babled           | 1B      |  1228 |
|           16 | Charles Coustille        | 1B      |  1224 |
|           17 | Loïc Harang              | 1B      |  1200 |
|           18 | Mathieu Olhagaray        | 1B      |  1200 |
|           19 | Baptiste Lagaillardie    | 1B      |  1197 |
|           20 | Mathieu Leizagoyen       | 1B      |  1191 |
|           21 | Thibault Leguillon       | 1B      |  1189 |
|           22 | Alexandre de la Raitrie  | 1B      |  1175 |
|           23 | Vincent Pasquesoone      | 1B      |  1170 |
|           24 | Arthur Capelier-Mourguy  | 1B      |  1167 |
|           25 | Clément Bonnichon        | 2A      |  1053 |
|           26 | Pierre Meglin            | 2A      |  1027 |
|           27 | Éric Edwards             | 2A      |  1011 |
|           28 | Pierre Privat            | 2A      |  1000 |
|           29 | Bertrand Lebel           | 2A      |  1000 |
|           30 | Emmanuel Poidevin        | 2A      |   998 |
|           31 | Alex Duthil              | 2A      |   994 |
|           32 | Cyril Houplain           | 2A      |   992 |
|           33 | Victor Lassalle          | 2A      |   992 |
|           34 | Olivier de Bernardi      | 2A      |   989 |
|           35 | Guillaume de Lamaze      | 2A      |   984 |
|           36 | Lawrence Robert          | 2A      |   978 |
|           37 | Haroun Sachs             | 2A      |   946 |
|           38 | Dimitri Girardetti       | 2B      |   850 |
|           39 | Stéphane Vidaillet       | 2B      |   841 |
|           40 | Alois de Bouville        | 2B      |   826 |
|           41 | Caroline Leclercq        | 2B      |   822 |
|           42 | Quentin Dionnot          | 2B      |   820 |
|           43 | Louis de Lignac          | 2B      |   806 |
|           44 | Jacques Guerin           | 2B      |   804 |
|           45 | Jean-Dominique Daragnes  | 2B      |   800 |
|           46 | Olivier Matteoli         | 2B      |   797 |
|           47 | Jean-Philippe Louis      | 2B      |   792 |
|           48 | Axel Bonneville          | 2B      |   790 |
|           49 | Éric Dupuy               | 2B      |   787 |
|           50 | Igor de Maack            | 2B      |   786 |
|           51 | Laurent Fiat             | 2B      |   783 |
|           52 | Adrien Chamberon         | 2B      |   777 |
|           53 | Florent Bartoli          | 2B      |   777 |
|           54 | Stéphane Soulier         | 2B      |   776 |
|           55 | Guillaume Benoit         | 2B      |   771 |
