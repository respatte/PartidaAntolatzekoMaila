# PartidaAntolatzekoMaila
Elo rating system for the Club de Pelote Basque de Paris. Mostly in French, for local use.

## Méthode, équations
Lors d'une rencontre, le PAM moyen de chaque équipe est pris en compte pour calculer leurs probabilités de victoire. La différence entre le résultat final (victoire notée 1 ou défaite notée 0), multipliée par un facteur d'échelle `k`, est ensuite utilisée pour mettre à jour les PAMs de tous les joueurs. Le facteur d'échelle utilisé est actuellement calculé comme suit, avec un poids des parties par défaut à 1, modifiable pour les tournois spéciaux.

```
k = 30 * poids_partie
```

## Classement des joueurs
Un classement des joueurs au 28 Octobre 2021 est disponible ci-dessous. Attention, ce système de classement ne devient fiable qu'après un nombre important de parties jouées pour chaque joueur.

|   Classement | Joueur                   | Série   |   PAM |
|-------------:|:-------------------------|:--------|------:|
|            1 | Côme Saint-Pierre        | 1A      |  1526 |
|            2 | Thibault Martre          | 1A      |  1499 |
|            3 | Hugues Saint-Pierre      | 1A      |  1440 |
|            4 | Georges Bachette-Peyrade | 1A      |  1440 |
|            5 | Nicolas Ossard           | 1A      |  1429 |
|            6 | Rayann Sachs             | 1A      |  1419 |
|            7 | Ramire Nunez             | 1A      |  1396 |
|            8 | Charles Bachette-Peyrade | 1A      |  1369 |
|            9 | Julien Jimenez           | 1A      |  1366 |
|           10 | Peio Mendiarat           | 1A      |  1364 |
|           11 | Olivier Waltener         | 1A      |  1342 |
|           12 | Michel Lesueur           | 1B      |  1332 |
|           13 | Evhan Dijoux             | 1A      |  1332 |
|           14 | Jean-Luc Sallaberry      | 1A      |  1325 |
|           15 | Antoine Penin            | 1A      |  1296 |
|           16 | Charles Coustille        | 1A      |  1256 |
|           17 | Sébastien Picabea        | 1B      |  1247 |
|           18 | Loïc Harang              | 1B      |  1230 |
|           19 | Alexandre Egurreguy      | 1B      |  1222 |
|           20 | Thibaud Babled           | 1B      |  1210 |
|           21 | Thibault Leguillon       | 1B      |  1206 |
|           22 | Alexandre de la Raitrie  | 1B      |  1206 |
|           23 | Baptiste Lagaillardie    | 1B      |  1204 |
|           24 | Mathieu Leizagoyen       | 1B      |  1198 |
|           25 | Mathieu Olhagaray        | 1B      |  1198 |
|           26 | Emmanuel Poidevin        | 1B      |  1193 |
|           27 | Clément Bonnichon        | 1B      |  1191 |
|           28 | Pierre Meglin            | 1B      |  1157 |
|           29 | Arthur Capelier-Mourguy  | 1B      |  1155 |
|           30 | Olivier de Bernardi      | 2A      |  1131 |
|           31 | Victor Lassalle          | 1B      |  1126 |
|           32 | Éric Edwards             | 2A      |  1090 |
|           33 | Jean-Dominique Daragnes  | 2A      |  1066 |
|           34 | Vincent Pasquesoone      | 1B      |  1064 |
|           35 | Stéphane Vidaillet       | 2A      |  1055 |
|           36 | Lawrence Robert          | 2A      |  1053 |
|           37 | Guillaume de Lamaze      | 2A      |  1041 |
|           38 | Quentin Dionnot          | 2A      |  1012 |
|           39 | Cyril Houplain           | 2A      |  1005 |
|           40 | Alex Duthil              | 2A      |  1002 |
|           41 | Hugo Houplain            | 2A      |   988 |
|           42 | Pierre Privat            | 2A      |   984 |
|           43 | Igor de Maack            | 2A      |   976 |
|           44 | Bertrand Lebel           | 2A      |   962 |
|           45 | Éric Dupuy               | 2A      |   962 |
|           46 | Laurent Fiat             | 2A      |   954 |
|           47 | Dimitri Girardetti       | 2A      |   945 |
|           48 | Axel Bonneville          | 2A      |   914 |
|           49 | Baptiste Guyot           | 2B      |   910 |
|           50 | Haroun Sachs             | 2A      |   897 |
|           51 | Aloïs de Bouville        | 2B      |   870 |
|           52 | Peio Lagrolet            | 2B      |   870 |
|           53 | Pierre Chamberon         | 2B      |   867 |
|           54 | Christophe Jaulerry      | 2B      |   844 |
|           55 | Jacques Guerin           | 2B      |   840 |
|           56 | Jean-Marc Lanusse        | 2B      |   834 |
|           57 | Caroline Leclercq        | 2B      |   814 |
|           58 | Hugues Dupuy             | 2B      |   814 |
|           59 | Arthur Schwarzbard       | 2B      |   805 |
|           60 | Olivier Matteoli         | 2B      |   802 |
|           61 | Guillaume Benoit         | 2B      |   791 |
|           62 | Nicolas Robuchon         | 2B      |   788 |
|           63 | Adrien Chamberon         | 2B      |   786 |
|           64 | Stéphane Soulier         | 2B      |   769 |
|           65 | Pierre-Henri Lajouane    | 2B      |   760 |
|           66 | Jean-Philippe Louis      | 2B      |   760 |
|           67 | Florent Bartoli          | 2B      |   727 |
|           68 | Louis Babin              | 2B      |   705 |
