# PartidaAntolatzekoMaila
Elo rating system for the Club de Pelote Basque de Paris. Mostly in French, for local use.

## Méthode, équations
Lors d'une rencontre, le PAM moyen de chaque équipe est pris en compte pour calculer leurs probabilités de victoire. La différence entre le résultat final (victoire notée 1 ou défaite notée 0), multipliée par un facteur d'échelle `k`, est ensuite utilisée pour mettre à jour les PAMs de tous les joueurs. Le facteur d'échelle utilisé est actuellement calculé comme suit, avec un poids des parties par défaut à 1, modifiable pour les tournois spéciaux.

```
k = 30 * poids_partie
```

## Classement des joueurs
Un classement des joueurs au 15 Novembre 2021 est disponible ci-dessous. Attention, ce système de classement ne devient fiable qu'après un nombre important de parties jouées pour chaque joueur.

|   Classement | Joueur                   | Série   |   PAM |   Parties jouées |
|-------------:|:-------------------------|:--------|------:|-----------------:|
|            1 | Côme Saint-Pierre        | 1A      |  1546 |               40 |
|            2 | Thibault Martre          | 1A      |  1489 |               34 |
|            3 | Hugues Saint-Pierre      | 1A      |  1437 |               28 |
|            4 | Nicolas Ossard           | 1A      |  1429 |               10 |
|            5 | Georges Bachette-Peyrade | 1A      |  1419 |               18 |
|            6 | Rayann Sachs             | 1A      |  1419 |               10 |
|            7 | Ramire Nunez             | 1A      |  1396 |               20 |
|            8 | Julien Jimenez           | 1A      |  1376 |               18 |
|            9 | Peio Mendiarat           | 1A      |  1373 |               15 |
|           10 | Charles Bachette-Peyrade | 1A      |  1369 |                9 |
|           11 | Jean-Luc Sallaberry      | 1A      |  1353 |               33 |
|           12 | Olivier Waltener         | 1A      |  1333 |               40 |
|           13 | Evhan Dijoux             | 1A      |  1322 |               38 |
|           14 | Michel Lesueur           | 1B      |  1321 |               42 |
|           15 | Antoine Penin            | 1A      |  1270 |               19 |
|           16 | Charles Coustille        | 1A      |  1246 |               20 |
|           17 | Alexandre de la Raitrie  | 1B      |  1227 |               14 |
|           18 | Mathieu Leizagoyen       | 1B      |  1224 |               15 |
|           19 | Alexandre Egurreguy      | 1B      |  1222 |                9 |
|           20 | Baptiste Lagaillardie    | 1B      |  1220 |               25 |
|           21 | Mathieu Olhagaray        | 1B      |  1216 |                7 |
|           22 | Loïc Harang              | 1B      |  1213 |                8 |
|           23 | Thibault Leguillon       | 1B      |  1206 |               11 |
|           24 | Sébastien Picabea        | 1B      |  1203 |               25 |
|           25 | Emmanuel Poidevin        | 1B      |  1200 |               12 |
|           26 | Clément Bonnichon        | 1B      |  1195 |               37 |
|           27 | Olivier de Bernardi      | 2A      |  1162 |               74 |
|           28 | Thibaud Babled           | 1B      |  1159 |               36 |
|           29 | Arthur Capelier-Mourguy  | 1B      |  1155 |               54 |
|           30 | Pierre Meglin            | 1B      |  1138 |               12 |
|           31 | Vincent Pasquesoone      | 1B      |  1126 |               30 |
|           32 | Victor Lassalle          | 1B      |  1102 |               37 |
|           33 | Guillaume de Lamaze      | 2A      |  1095 |               17 |
|           34 | Éric Edwards             | 2A      |  1090 |               12 |
|           35 | Jean-Dominique Daragnes  | 2A      |  1066 |               11 |
|           36 | Lawrence Robert          | 2A      |  1041 |               11 |
|           37 | Hugo Houplain            | 2A      |  1019 |                9 |
|           38 | Quentin Dionnot          | 2A      |  1008 |               19 |
|           39 | Cyril Houplain           | 2A      |  1005 |                5 |
|           40 | Alex Duthil              | 2A      |  1002 |                5 |
|           41 | Stéphane Vidaillet       | 2A      |   989 |               40 |
|           42 | Igor de Maack            | 2A      |   976 |               16 |
|           43 | Pierre Privat            | 2A      |   971 |                6 |
|           44 | Bertrand Lebel           | 2A      |   967 |               18 |
|           45 | Laurent Fiat             | 2A      |   954 |               10 |
|           46 | Dimitri Girardetti       | 2A      |   945 |               20 |
|           47 | Éric Dupuy               | 2A      |   920 |               33 |
|           48 | Baptiste Guyot           | 2B      |   918 |               14 |
|           49 | Axel Bonneville          | 2A      |   914 |               15 |
|           50 | Christophe Jaulerry      | 2B      |   894 |               21 |
|           51 | Haroun Sachs             | 2A      |   892 |               27 |
|           52 | Aloïs de Bouville        | 2B      |   883 |               36 |
|           53 | Peio Lagrolet            | 2B      |   870 |                6 |
|           54 | Pierre Chamberon         | 2B      |   867 |                5 |
|           55 | Jean-Marc Lanusse        | 2B      |   847 |                9 |
|           56 | Guillaume Barnetche      | 2B      |   841 |                2 |
|           57 | Jacques Guerin           | 2B      |   840 |                8 |
|           58 | Hugues Dupuy             | 2B      |   814 |                1 |
|           59 | Olivier Matteoli         | 2B      |   802 |                7 |
|           60 | Caroline Leclercq        | 2B      |   800 |                2 |
|           61 | Guillaume Benoit         | 2B      |   791 |                4 |
|           62 | Nicolas Robuchon         | 2B      |   788 |                4 |
|           63 | Adrien Chamberon         | 2B      |   786 |               14 |
|           64 | Arthur Schwarzbard       | 2B      |   772 |                9 |
|           65 | Gabriel Marot            | 2B      |   769 |               28 |
|           66 | Stéphane Soulier         | 2B      |   765 |               16 |
|           67 | Pierre-Henri Lajouane    | 2B      |   760 |                7 |
|           68 | Jean-Philippe Louis      | 2B      |   760 |               11 |
|           69 | Florent Bartoli          | 2B      |   734 |               20 |
|           70 | Louis Babin              | 2B      |   713 |               30 |
