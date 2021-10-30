# PartidaAntolatzekoMaila
Elo rating system for the Club de Pelote Basque de Paris. Mostly in French, for local use.

## Méthode, équations
Lors d'une rencontre, le PAM moyen de chaque équipe est pris en compte pour calculer leurs probabilités de victoire. La différence entre le résultat final (victoire notée 1 ou défaite notée 0), multipliée par un facteur d'échelle `k`, est ensuite utilisée pour mettre à jour les PAMs de tous les joueurs. Le facteur d'échelle utilisé est actuellement calculé comme suit, avec un poids des parties par défaut à 1, modifiable pour les tournois spéciaux.

```
k = 30 * poids_partie
```

## Classement des joueurs
Un classement des joueurs au 28 Octobre 2021 est disponible ci-dessous. Attention, ce système de classement ne devient fiable qu'après un nombre important de parties jouées pour chaque joueur.

|   Classement | Joueur                   | Série   |   PAM |   Parties jouées |
|-------------:|:-------------------------|:--------|------:|-----------------:|
|            1 | Côme Saint-Pierre        | 1A      |  1526 |               38 |
|            2 | Thibault Martre          | 1A      |  1499 |               32 |
|            3 | Hugues Saint-Pierre      | 1A      |  1440 |               26 |
|            4 | Georges Bachette-Peyrade | 1A      |  1440 |               16 |
|            5 | Nicolas Ossard           | 1A      |  1429 |               10 |
|            6 | Rayann Sachs             | 1A      |  1419 |               10 |
|            7 | Ramire Nunez             | 1A      |  1396 |               20 |
|            8 | Charles Bachette-Peyrade | 1A      |  1369 |                9 |
|            9 | Julien Jimenez           | 1A      |  1366 |               17 |
|           10 | Peio Mendiarat           | 1A      |  1364 |               14 |
|           11 | Olivier Waltener         | 1A      |  1342 |               39 |
|           12 | Michel Lesueur           | 1B      |  1332 |               32 |
|           13 | Evhan Dijoux             | 1A      |  1332 |               36 |
|           14 | Jean-Luc Sallaberry      | 1A      |  1325 |               30 |
|           15 | Antoine Penin            | 1A      |  1296 |               17 |
|           16 | Charles Coustille        | 1A      |  1256 |               19 |
|           17 | Sébastien Picabea        | 1B      |  1247 |               23 |
|           18 | Loïc Harang              | 1B      |  1230 |                6 |
|           19 | Alexandre Egurreguy      | 1B      |  1222 |                9 |
|           20 | Thibaud Babled           | 1B      |  1210 |               26 |
|           21 | Thibault Leguillon       | 1B      |  1206 |               11 |
|           22 | Alexandre de la Raitrie  | 1B      |  1206 |               13 |
|           23 | Baptiste Lagaillardie    | 1B      |  1204 |               24 |
|           24 | Mathieu Leizagoyen       | 1B      |  1198 |               13 |
|           25 | Mathieu Olhagaray        | 1B      |  1198 |                4 |
|           26 | Emmanuel Poidevin        | 1B      |  1193 |               10 |
|           27 | Clément Bonnichon        | 1B      |  1191 |               34 |
|           28 | Pierre Meglin            | 1B      |  1157 |                9 |
|           29 | Arthur Capelier-Mourguy  | 1B      |  1155 |               43 |
|           30 | Olivier de Bernardi      | 2A      |  1131 |               57 |
|           31 | Victor Lassalle          | 1B      |  1126 |               32 |
|           32 | Éric Edwards             | 2A      |  1090 |               12 |
|           33 | Jean-Dominique Daragnes  | 2A      |  1066 |               11 |
|           34 | Vincent Pasquesoone      | 1B      |  1064 |               22 |
|           35 | Stéphane Vidaillet       | 2A      |  1055 |               25 |
|           36 | Lawrence Robert          | 2A      |  1053 |                9 |
|           37 | Guillaume de Lamaze      | 2A      |  1041 |               14 |
|           38 | Quentin Dionnot          | 2A      |  1012 |               16 |
|           39 | Cyril Houplain           | 2A      |  1005 |                5 |
|           40 | Alex Duthil              | 2A      |  1002 |                5 |
|           41 | Hugo Houplain            | 2A      |   988 |                6 |
|           42 | Pierre Privat            | 2A      |   984 |                4 |
|           43 | Igor de Maack            | 2A      |   976 |               16 |
|           44 | Bertrand Lebel           | 2A      |   962 |               12 |
|           45 | Éric Dupuy               | 2A      |   962 |               27 |
|           46 | Laurent Fiat             | 2A      |   954 |               10 |
|           47 | Dimitri Girardetti       | 2A      |   945 |               20 |
|           48 | Axel Bonneville          | 2A      |   914 |               15 |
|           49 | Baptiste Guyot           | 2B      |   910 |               12 |
|           50 | Haroun Sachs             | 2A      |   897 |               21 |
|           51 | Aloïs de Bouville        | 2B      |   870 |               34 |
|           52 | Peio Lagrolet            | 2B      |   870 |                6 |
|           53 | Pierre Chamberon         | 2B      |   867 |                5 |
|           54 | Christophe Jaulerry      | 2B      |   844 |               12 |
|           55 | Jacques Guerin           | 2B      |   840 |                8 |
|           56 | Jean-Marc Lanusse        | 2B      |   834 |                4 |
|           57 | Caroline Leclercq        | 2B      |   814 |                1 |
|           58 | Hugues Dupuy             | 2B      |   814 |                1 |
|           59 | Arthur Schwarzbard       | 2B      |   805 |                6 |
|           60 | Olivier Matteoli         | 2B      |   802 |                7 |
|           61 | Guillaume Benoit         | 2B      |   791 |                4 |
|           62 | Nicolas Robuchon         | 2B      |   788 |                4 |
|           63 | Gabriel Marot            | 2B      |   788 |               21 |
|           64 | Adrien Chamberon         | 2B      |   786 |               14 |
|           65 | Stéphane Soulier         | 2B      |   769 |               13 |
|           66 | Pierre-Henri Lajouane    | 2B      |   760 |                7 |
|           67 | Jean-Philippe Louis      | 2B      |   760 |               11 |
|           68 | Florent Bartoli          | 2B      |   727 |               17 |
|           69 | Louis Babin              | 2B      |   705 |               24 |
