# PartidaAntolatzekoMaila
Elo rating system for the Club de Pelote Basque de Paris. Mostly in French, for local use.

## Méthode, équations
Vous pouvez retrouver un article détaillé expliquant le fonctionnement du PAM sur le [site web du club](https://www.trinquetdelacavalerie.fr/post/comment-marche-le-classement-des-joueurs). Pour faire simple, lors d'une rencontre, le PAM moyen de chaque équipe est pris en compte pour calculer leurs probabilités de victoire. La différence entre le résultat final (victoire notée 1 ou défaite notée 0), multipliée par un facteur d'échelle `k`, est ensuite utilisée pour mettre à jour les PAMs de tous les joueurs. Le facteur d'échelle utilisé est actuellement calculé comme suit, avec un poids des parties par défaut à 1, modifiable pour les tournois spéciaux.

```
k = 30 * poids_partie
```

De plus, tous les 3 mois, le PAM des joueurs est partiellement remis à niveau pour le recentré sur la série du joueur. Ceci permet entre autre de gérer les changements de série, et permet d'uniformiser le classement sur le long terme.

## Classement des joueurs
Un classement des joueurs au 9 Décembre 2022 est disponible ci-dessous. Attention, ce système de classement ne devient fiable qu'après un nombre important de parties jouées pour chaque joueur.

|   Classement | Joueur                   | Série   |   PAM |   Parties jouées |
|-------------:|:-------------------------|:--------|------:|-----------------:|
|            1 | Côme Saint-Pierre        | 1A      |  1471 |               44 |
|            2 | Thibault Martre          | 1A      |  1445 |               44 |
|            3 | Nicolas Ossard           | 1A      |  1444 |               19 |
|            4 | Olivier Waltener         | 1A      |  1434 |               59 |
|            5 | Georges Bachette-Peyrade | 1A      |  1432 |               27 |
|            6 | Hugues Saint-Pierre      | 1A      |  1413 |               30 |
|            7 | Ramire Nunez             | 1A      |  1410 |               34 |
|            8 | Rayann Sachs             | 1A      |  1405 |               13 |
|            9 | Evhan Dijoux             | 1A      |  1391 |               49 |
|           10 | Peio Mendiarat           | 1A      |  1387 |               21 |
|           11 | Julien Jimenez           | 1A      |  1370 |               31 |
|           12 | Charles Bachette-Peyrade | 1A      |  1360 |               19 |
|           13 | Charles Coustille        | 1A      |  1345 |               30 |
|           14 | Alexandre Egurreguy      | 1A      |  1317 |               10 |
|           15 | Jean-Luc Sallaberry      | 1A      |  1312 |               48 |
|           16 | Alexandre de la Raitrie  | 1B      |  1290 |               29 |
|           17 | Antoine Penin            | 1A      |  1287 |               28 |
|           18 | Thibaud Babled           | 1B      |  1257 |               52 |
|           19 | Mathieu Leizagoyen       | 1B      |  1230 |               25 |
|           20 | Mathieu Olhagaray        | 1B      |  1214 |                8 |
|           21 | Thibault Leguillon       | 1B      |  1204 |               18 |
|           22 | Loïc Harang              | 1B      |  1203 |               16 |
|           23 | Baptiste Lagaillardie    | 1B      |  1200 |               30 |
|           24 | Pierre Meglin            | 1B      |  1190 |               26 |
|           25 | Sébastien Picabea        | 1B      |  1186 |               35 |
|           26 | Michel Lesueur           | 1B      |  1179 |               70 |
|           27 | Emmanuel Poidevin        | 1B      |  1177 |               22 |
|           28 | Victor Lassalle          | 1B      |  1173 |               60 |
|           29 | Arthur Capelier-Mourguy  | 1B      |  1169 |               70 |
|           30 | Vincent Pasquesoone      | 1B      |  1139 |               27 |
|           31 | Lawrence Robert          | 1B      |  1131 |               16 |
|           32 | Clément Bonnichon        | 1B      |  1123 |               59 |
|           33 | Guillaume de Lamaze      | 1B      |  1121 |               36 |
|           34 | Olivier de Bernardi      | 2A      |  1069 |              117 |
|           35 | Éric Edwards             | 2A      |  1045 |               12 |
|           36 | Jean-Dominique Daragnes  | 2A      |  1026 |               16 |
|           37 | Dimitri Girardetti       | 2A      |  1019 |               31 |
|           38 | Pierre Privat            | 2A      |  1004 |               14 |
|           39 | Cyril Houplain           | 2A      |  1002 |                5 |
|           40 | Alex Duthil              | 2A      |  1001 |                5 |
|           41 | Quentin Dionnot          | 2A      |   996 |               24 |
|           42 | Peio Lagrolet            | 2A      |   995 |               21 |
|           43 | Igor de Maack            | 2A      |   988 |               16 |
|           44 | Bertrand Lebel           | 2A      |   982 |               25 |
|           45 | Hugo Houplain            | 2A      |   978 |               14 |
|           46 | Stéphane Vidaillet       | 2A      |   977 |               47 |
|           47 | Axel Bonneville          | 2A      |   957 |               15 |
|           48 | Laurent Fiat             | 2A      |   939 |               18 |
|           49 | Éric Dupuy               | 2A      |   936 |               44 |
|           50 | Gabriel Marot            | 2A      |   923 |               43 |
|           51 | Haroun Sachs             | 2A      |   908 |               36 |
|           52 | Aloïs de Bouville        | 2B      |   851 |               58 |
|           53 | Christophe Jaulerry      | 2B      |   847 |               33 |
|           54 | Baptiste Guyot           | 2B      |   841 |               26 |
|           55 | Iñaki Darthayette        | 2B      |   831 |               18 |
|           56 | Pierre Chamberon         | 2B      |   821 |               11 |
|           57 | Guillaume Barnetche      | 2B      |   821 |                2 |
|           58 | Jean-Marc Lanusse        | 2B      |   820 |               15 |
|           59 | Jacques Guerin           | 2B      |   820 |                8 |
|           60 | Adrien Chamberon         | 2B      |   819 |               27 |
|           61 | Caroline Leclercq        | 2B      |   816 |                6 |
|           62 | Olivier Matteoli         | 2B      |   813 |                9 |
|           63 | Hugues Dupuy             | 2B      |   807 |                1 |
|           64 | Pierre-Henri Lajouane    | 2B      |   798 |               14 |
|           65 | Guillaume Benoit         | 2B      |   795 |                4 |
|           66 | Guillaume Teboul         | 2B      |   795 |                1 |
|           67 | Louis Babin              | 2B      |   790 |               46 |
|           68 | Stéphane Soulier         | 2B      |   789 |               20 |
|           69 | Nicolas Robuchon         | 2B      |   787 |                9 |
|           70 | Arthur Schwarzbard       | 2B      |   786 |                9 |
|           71 | Florent Bartoli          | 2B      |   758 |               22 |
|           72 | Jean-Philippe Louis      | 2B      |   741 |               17 |
