# PartidaAntolatzekoMaila
Elo rating system for the Club de Pelote Basque de Paris. Mostly in French, for local use.

## Méthode, équations
Lors d'une rencontre, le PAM moyen de chaque équipe est pris en compte pour calculer leurs probabilités de victoire. La différence entre le résultat final (victoire notée 1 ou défaite notée 0), multipliée par un facteur d'échelle `k`, est ensuite utilisée pour mettre à jour les PAMs de tous les joueurs. Le facteur d'échelle utilisé est actuellement calculé comme suit, avec un poids des parties par défaut à 1, modifiable pour les tournois spéciaux.

```
k = 30 * poids_partie
```

## Classement des joueurs
Un classement des joueurs au 3 Décembre 2021 est disponible ci-dessous. Attention, ce système de classement ne devient fiable qu'après un nombre important de parties jouées pour chaque joueur.

|   Classement | Joueur                   | Série   |   PAM |   Parties jouées |
|-------------:|:-------------------------|:--------|------:|-----------------:|
|            1 | Côme Saint-Pierre        | 1A      |  1563 |               42 |
|            2 | Thibault Martre          | 1A      |  1508 |               42 |
|            3 | Hugues Saint-Pierre      | 1A      |  1444 |               29 |
|            4 | Nicolas Ossard           | 1A      |  1429 |               10 |
|            5 | Rayann Sachs             | 1A      |  1419 |               10 |
|            6 | Olivier Waltener         | 1A      |  1397 |               46 |
|            7 | Ramire Nunez             | 1A      |  1386 |               28 |
|            8 | Peio Mendiarat           | 1A      |  1386 |               19 |
|            9 | Michel Lesueur           | 1B      |  1383 |               50 |
|           10 | Georges Bachette-Peyrade | 1A      |  1383 |               21 |
|           11 | Evhan Dijoux             | 1A      |  1347 |               43 |
|           12 | Charles Bachette-Peyrade | 1A      |  1346 |               15 |
|           13 | Julien Jimenez           | 1A      |  1335 |               23 |
|           14 | Jean-Luc Sallaberry      | 1A      |  1323 |               40 |
|           15 | Charles Coustille        | 1A      |  1276 |               28 |
|           16 | Antoine Penin            | 1A      |  1272 |               19 |
|           17 | Mathieu Leizagoyen       | 1B      |  1254 |               22 |
|           18 | Alexandre de la Raitrie  | 1B      |  1242 |               19 |
|           19 | Mathieu Olhagaray        | 1B      |  1229 |                8 |
|           20 | Thibault Leguillon       | 1B      |  1223 |               17 |
|           21 | Alexandre Egurreguy      | 1B      |  1222 |                9 |
|           22 | Thibaud Babled           | 1B      |  1214 |               37 |
|           23 | Emmanuel Poidevin        | 1B      |  1205 |               15 |
|           24 | Baptiste Lagaillardie    | 1B      |  1204 |               26 |
|           25 | Loïc Harang              | 1B      |  1189 |               10 |
|           26 | Sébastien Picabea        | 1B      |  1188 |               31 |
|           27 | Guillaume de Lamaze      | 2A      |  1164 |               25 |
|           28 | Clément Bonnichon        | 1B      |  1163 |               42 |
|           29 | Victor Lassalle          | 1B      |  1151 |               44 |
|           30 | Pierre Meglin            | 1B      |  1109 |               16 |
|           31 | Éric Edwards             | 2A      |  1090 |               12 |
|           32 | Arthur Capelier-Mourguy  | 1B      |  1084 |               65 |
|           33 | Vincent Pasquesoone      | 1B      |  1078 |               27 |
|           34 | Jean-Dominique Daragnes  | 2A      |  1066 |               11 |
|           35 | Lawrence Robert          | 2A      |  1062 |               16 |
|           36 | Olivier de Bernardi      | 2A      |  1044 |               87 |
|           37 | Quentin Dionnot          | 2A      |  1006 |               21 |
|           38 | Cyril Houplain           | 2A      |  1005 |                5 |
|           39 | Hugo Houplain            | 2A      |  1004 |               11 |
|           40 | Alex Duthil              | 2A      |  1002 |                5 |
|           41 | Pierre Privat            | 2A      |   986 |                9 |
|           42 | Peio Lagrolet            | 2B      |   976 |               14 |
|           43 | Igor de Maack            | 2A      |   976 |               16 |
|           44 | Dimitri Girardetti       | 2A      |   958 |               22 |
|           45 | Stéphane Vidaillet       | 2A      |   955 |               45 |
|           46 | Bertrand Lebel           | 2A      |   942 |               21 |
|           47 | Laurent Fiat             | 2A      |   917 |               16 |
|           48 | Axel Bonneville          | 2A      |   914 |               15 |
|           49 | Aloïs de Bouville        | 2B      |   893 |               45 |
|           50 | Éric Dupuy               | 2A      |   884 |               43 |
|           51 | Christophe Jaulerry      | 2B      |   883 |               22 |
|           52 | Haroun Sachs             | 2A      |   868 |               30 |
|           53 | Adrien Chamberon         | 2B      |   855 |               19 |
|           54 | Pierre Chamberon         | 2B      |   853 |                6 |
|           55 | Baptiste Guyot           | 2B      |   852 |               22 |
|           56 | Jean-Marc Lanusse        | 2B      |   848 |               12 |
|           57 | Iñaki Darthayette        | 2B      |   846 |               15 |
|           58 | Guillaume Barnetche      | 2B      |   842 |                2 |
|           59 | Jacques Guerin           | 2B      |   840 |                8 |
|           60 | Gabriel Marot            | 2B      |   827 |               36 |
|           61 | Caroline Leclercq        | 2B      |   824 |                4 |
|           62 | Olivier Matteoli         | 2B      |   817 |                9 |
|           63 | Hugues Dupuy             | 2B      |   814 |                1 |
|           64 | Guillaume Benoit         | 2B      |   791 |                4 |
|           65 | Nicolas Robuchon         | 2B      |   788 |                4 |
|           66 | Arthur Schwarzbard       | 2B      |   772 |                9 |
|           67 | Pierre-Henri Lajouane    | 2B      |   770 |               11 |
|           68 | Stéphane Soulier         | 2B      |   755 |               18 |
|           69 | Florent Bartoli          | 2B      |   734 |               20 |
|           70 | Jean-Philippe Louis      | 2B      |   718 |               13 |
|           71 | Louis Babin              | 2B      |   707 |               38 |
