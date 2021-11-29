# PartidaAntolatzekoMaila
Elo rating system for the Club de Pelote Basque de Paris. Mostly in French, for local use.

## Méthode, équations
Lors d'une rencontre, le PAM moyen de chaque équipe est pris en compte pour calculer leurs probabilités de victoire. La différence entre le résultat final (victoire notée 1 ou défaite notée 0), multipliée par un facteur d'échelle `k`, est ensuite utilisée pour mettre à jour les PAMs de tous les joueurs. Le facteur d'échelle utilisé est actuellement calculé comme suit, avec un poids des parties par défaut à 1, modifiable pour les tournois spéciaux.

```
k = 30 * poids_partie
```

## Classement des joueurs
Un classement des joueurs au 28 Novembre 2021 est disponible ci-dessous. Attention, ce système de classement ne devient fiable qu'après un nombre important de parties jouées pour chaque joueur.

|   Classement | Joueur                   | Série   |   PAM |   Parties jouées |
|-------------:|:-------------------------|:--------|------:|-----------------:|
|            1 | Côme Saint-Pierre        | 1A      |  1563 |               42 |
|            2 | Thibault Martre          | 1A      |  1498 |               38 |
|            3 | Hugues Saint-Pierre      | 1A      |  1444 |               29 |
|            4 | Nicolas Ossard           | 1A      |  1429 |               10 |
|            5 | Rayann Sachs             | 1A      |  1419 |               10 |
|            6 | Peio Mendiarat           | 1A      |  1395 |               18 |
|            7 | Olivier Waltener         | 1A      |  1394 |               44 |
|            8 | Georges Bachette-Peyrade | 1A      |  1389 |               20 |
|            9 | Ramire Nunez             | 1A      |  1386 |               28 |
|           10 | Michel Lesueur           | 1B      |  1370 |               46 |
|           11 | Julien Jimenez           | 1A      |  1348 |               22 |
|           12 | Evhan Dijoux             | 1A      |  1347 |               43 |
|           13 | Jean-Luc Sallaberry      | 1A      |  1335 |               38 |
|           14 | Charles Bachette-Peyrade | 1A      |  1331 |               13 |
|           15 | Antoine Penin            | 1A      |  1272 |               19 |
|           16 | Charles Coustille        | 1A      |  1247 |               26 |
|           17 | Thibaud Babled           | 1B      |  1233 |               36 |
|           18 | Mathieu Olhagaray        | 1B      |  1229 |                8 |
|           19 | Alexandre de la Raitrie  | 1B      |  1227 |               14 |
|           20 | Alexandre Egurreguy      | 1B      |  1222 |                9 |
|           21 | Sébastien Picabea        | 1B      |  1215 |               28 |
|           22 | Thibault Leguillon       | 1B      |  1214 |               13 |
|           23 | Clément Bonnichon        | 1B      |  1208 |               39 |
|           24 | Emmanuel Poidevin        | 1B      |  1205 |               14 |
|           25 | Baptiste Lagaillardie    | 1B      |  1204 |               26 |
|           26 | Mathieu Leizagoyen       | 1B      |  1194 |               17 |
|           27 | Loïc Harang              | 1B      |  1189 |               10 |
|           28 | Pierre Meglin            | 1B      |  1127 |               15 |
|           29 | Victor Lassalle          | 1B      |  1123 |               39 |
|           30 | Arthur Capelier-Mourguy  | 1B      |  1114 |               63 |
|           31 | Guillaume de Lamaze      | 2A      |  1103 |               19 |
|           32 | Éric Edwards             | 2A      |  1090 |               12 |
|           33 | Olivier de Bernardi      | 2A      |  1085 |               84 |
|           34 | Vincent Pasquesoone      | 1B      |  1078 |               27 |
|           35 | Jean-Dominique Daragnes  | 2A      |  1066 |               11 |
|           36 | Lawrence Robert          | 2A      |  1039 |               12 |
|           37 | Hugo Houplain            | 2A      |  1023 |                9 |
|           38 | Quentin Dionnot          | 2A      |  1006 |               21 |
|           39 | Cyril Houplain           | 2A      |  1005 |                5 |
|           40 | Alex Duthil              | 2A      |  1002 |                5 |
|           41 | Pierre Privat            | 2A      |   986 |                9 |
|           42 | Stéphane Vidaillet       | 2A      |   980 |               44 |
|           43 | Peio Lagrolet            | 2B      |   976 |               12 |
|           44 | Igor de Maack            | 2A      |   976 |               16 |
|           45 | Bertrand Lebel           | 2A      |   970 |               18 |
|           46 | Dimitri Girardetti       | 2A      |   945 |               20 |
|           47 | Laurent Fiat             | 2A      |   918 |               15 |
|           48 | Axel Bonneville          | 2A      |   914 |               15 |
|           49 | Aloïs de Bouville        | 2B      |   899 |               44 |
|           50 | Christophe Jaulerry      | 2B      |   894 |               21 |
|           51 | Haroun Sachs             | 2A      |   888 |               28 |
|           52 | Pierre Chamberon         | 2B      |   867 |                5 |
|           53 | Iñaki Darthayette        | 2B      |   857 |               14 |
|           54 | Baptiste Guyot           | 2B      |   852 |               22 |
|           55 | Jean-Marc Lanusse        | 2B      |   846 |               10 |
|           56 | Guillaume Barnetche      | 2B      |   842 |                2 |
|           57 | Jacques Guerin           | 2B      |   840 |                8 |
|           58 | Gabriel Marot            | 2B      |   839 |               34 |
|           59 | Éric Dupuy               | 2A      |   833 |               38 |
|           60 | Adrien Chamberon         | 2B      |   833 |               16 |
|           61 | Caroline Leclercq        | 2B      |   824 |                4 |
|           62 | Hugues Dupuy             | 2B      |   814 |                1 |
|           63 | Olivier Matteoli         | 2B      |   802 |                7 |
|           64 | Guillaume Benoit         | 2B      |   791 |                4 |
|           65 | Nicolas Robuchon         | 2B      |   788 |                4 |
|           66 | Arthur Schwarzbard       | 2B      |   772 |                9 |
|           67 | Stéphane Soulier         | 2B      |   765 |               16 |
|           68 | Pierre-Henri Lajouane    | 2B      |   760 |                7 |
|           69 | Florent Bartoli          | 2B      |   734 |               20 |
|           70 | Jean-Philippe Louis      | 2B      |   718 |               13 |
|           71 | Louis Babin              | 2B      |   713 |               37 |
