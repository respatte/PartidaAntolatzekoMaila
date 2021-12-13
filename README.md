# PartidaAntolatzekoMaila
Elo rating system for the Club de Pelote Basque de Paris. Mostly in French, for local use.

## Méthode, équations
Vous pouvez retrouver un article détaillé expliquant le fonctionnement du PAM sur le [site web du club](https://www.trinquetdelacavalerie.fr/post/comment-marche-le-classement-des-joueurs). Pour faire simple, lors d'une rencontre, le PAM moyen de chaque équipe est pris en compte pour calculer leurs probabilités de victoire. La différence entre le résultat final (victoire notée 1 ou défaite notée 0), multipliée par un facteur d'échelle `k`, est ensuite utilisée pour mettre à jour les PAMs de tous les joueurs. Le facteur d'échelle utilisé est actuellement calculé comme suit, avec un poids des parties par défaut à 1, modifiable pour les tournois spéciaux.

```
k = 30 * poids_partie
```

## Classement des joueurs
Un classement des joueurs au 3 Décembre 2021 est disponible ci-dessous. Attention, ce système de classement ne devient fiable qu'après un nombre important de parties jouées pour chaque joueur.

|   Classement | Joueur                   | Série   |   PAM |   Parties jouées |
|-------------:|:-------------------------|:--------|------:|-----------------:|
|            1 | Côme Saint-Pierre        | 1A      |  1563 |               42 |
|            2 | Thibault Martre          | 1A      |  1508 |               42 |
|            3 | Nicolas Ossard           | 1A      |  1474 |               16 |
|            4 | Hugues Saint-Pierre      | 1A      |  1444 |               29 |
|            5 | Rayann Sachs             | 1A      |  1419 |               10 |
|            6 | Olivier Waltener         | 1A      |  1402 |               49 |
|            7 | Ramire Nunez             | 1A      |  1386 |               28 |
|            8 | Peio Mendiarat           | 1A      |  1385 |               21 |
|            9 | Georges Bachette-Peyrade | 1A      |  1383 |               21 |
|           10 | Michel Lesueur           | 1B      |  1364 |               54 |
|           11 | Evhan Dijoux             | 1A      |  1347 |               43 |
|           12 | Charles Bachette-Peyrade | 1A      |  1346 |               15 |
|           13 | Julien Jimenez           | 1A      |  1329 |               26 |
|           14 | Jean-Luc Sallaberry      | 1A      |  1312 |               41 |
|           15 | Charles Coustille        | 1A      |  1276 |               28 |
|           16 | Antoine Penin            | 1A      |  1255 |               21 |
|           17 | Mathieu Leizagoyen       | 1B      |  1254 |               22 |
|           18 | Thibaud Babled           | 1B      |  1234 |               40 |
|           19 | Alexandre de la Raitrie  | 1B      |  1230 |               20 |
|           20 | Mathieu Olhagaray        | 1B      |  1229 |                8 |
|           21 | Sébastien Picabea        | 1B      |  1228 |               33 |
|           22 | Thibault Leguillon       | 1B      |  1223 |               17 |
|           23 | Alexandre Egurreguy      | 1B      |  1222 |                9 |
|           24 | Emmanuel Poidevin        | 1B      |  1205 |               15 |
|           25 | Baptiste Lagaillardie    | 1B      |  1187 |               29 |
|           26 | Loïc Harang              | 1B      |  1149 |               12 |
|           27 | Guillaume de Lamaze      | 2A      |  1148 |               28 |
|           28 | Victor Lassalle          | 1B      |  1144 |               50 |
|           29 | Clément Bonnichon        | 1B      |  1132 |               48 |
|           30 | Pierre Meglin            | 1B      |  1119 |               18 |
|           31 | Éric Edwards             | 2A      |  1090 |               12 |
|           32 | Arthur Capelier-Mourguy  | 1B      |  1084 |               65 |
|           33 | Olivier de Bernardi      | 2A      |  1080 |               93 |
|           34 | Vincent Pasquesoone      | 1B      |  1078 |               27 |
|           35 | Lawrence Robert          | 2A      |  1062 |               16 |
|           36 | Peio Lagrolet            | 2B      |  1032 |               21 |
|           37 | Quentin Dionnot          | 2A      |  1006 |               21 |
|           38 | Cyril Houplain           | 2A      |  1005 |                5 |
|           39 | Hugo Houplain            | 2A      |  1003 |               12 |
|           40 | Alex Duthil              | 2A      |  1002 |                5 |
|           41 | Pierre Privat            | 2A      |   984 |               11 |
|           42 | Stéphane Vidaillet       | 2A      |   979 |               47 |
|           43 | Igor de Maack            | 2A      |   976 |               16 |
|           44 | Jean-Dominique Daragnes  | 2A      |   974 |               16 |
|           45 | Dimitri Girardetti       | 2A      |   958 |               22 |
|           46 | Bertrand Lebel           | 2A      |   942 |               21 |
|           47 | Axel Bonneville          | 2A      |   914 |               15 |
|           48 | Laurent Fiat             | 2A      |   913 |               17 |
|           49 | Christophe Jaulerry      | 2B      |   904 |               24 |
|           50 | Pierre Chamberon         | 2B      |   899 |               10 |
|           51 | Aloïs de Bouville        | 2B      |   875 |               51 |
|           52 | Éric Dupuy               | 2A      |   872 |               44 |
|           53 | Haroun Sachs             | 2A      |   867 |               31 |
|           54 | Jean-Marc Lanusse        | 2B      |   861 |               15 |
|           55 | Baptiste Guyot           | 2B      |   852 |               22 |
|           56 | Adrien Chamberon         | 2B      |   848 |               21 |
|           57 | Iñaki Darthayette        | 2B      |   846 |               15 |
|           58 | Guillaume Barnetche      | 2B      |   842 |                2 |
|           59 | Jacques Guerin           | 2B      |   840 |                8 |
|           60 | Gabriel Marot            | 2B      |   832 |               37 |
|           61 | Caroline Leclercq        | 2B      |   824 |                4 |
|           62 | Olivier Matteoli         | 2B      |   817 |                9 |
|           63 | Hugues Dupuy             | 2B      |   814 |                1 |
|           64 | Guillaume Benoit         | 2B      |   791 |                4 |
|           65 | Nicolas Robuchon         | 2B      |   780 |                9 |
|           66 | Pierre-Henri Lajouane    | 2B      |   778 |               14 |
|           67 | Arthur Schwarzbard       | 2B      |   772 |                9 |
|           68 | Stéphane Soulier         | 2B      |   751 |               19 |
|           69 | Florent Bartoli          | 2B      |   734 |               20 |
|           70 | Jean-Philippe Louis      | 2B      |   720 |               15 |
|           71 | Louis Babin              | 2B      |   706 |               41 |
