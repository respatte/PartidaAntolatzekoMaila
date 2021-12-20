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
|            1 | Côme Saint-Pierre        | 1A      |  1576 |               43 |
|            2 | Thibault Martre          | 1A      |  1498 |               44 |
|            3 | Nicolas Ossard           | 1A      |  1480 |               19 |
|            4 | Georges Bachette-Peyrade | 1A      |  1429 |               24 |
|            5 | Rayann Sachs             | 1A      |  1428 |               11 |
|            6 | Hugues Saint-Pierre      | 1A      |  1426 |               30 |
|            7 | Olivier Waltener         | 1A      |  1395 |               55 |
|            8 | Peio Mendiarat           | 1A      |  1385 |               21 |
|            9 | Ramire Nunez             | 1A      |  1375 |               33 |
|           10 | Evhan Dijoux             | 1A      |  1330 |               48 |
|           11 | Julien Jimenez           | 1A      |  1329 |               26 |
|           12 | Charles Bachette-Peyrade | 1A      |  1321 |               19 |
|           13 | Jean-Luc Sallaberry      | 1A      |  1316 |               44 |
|           14 | Michel Lesueur           | 1B      |  1288 |               63 |
|           15 | Charles Coustille        | 1A      |  1272 |               30 |
|           16 | Mathieu Leizagoyen       | 1B      |  1270 |               23 |
|           17 | Alexandre de la Raitrie  | 1B      |  1256 |               22 |
|           18 | Thibaud Babled           | 1B      |  1250 |               44 |
|           19 | Alexandre Egurreguy      | 1B      |  1234 |               10 |
|           20 | Antoine Penin            | 1A      |  1231 |               26 |
|           21 | Mathieu Olhagaray        | 1B      |  1229 |                8 |
|           22 | Sébastien Picabea        | 1B      |  1228 |               33 |
|           23 | Emmanuel Poidevin        | 1B      |  1210 |               16 |
|           24 | Thibault Leguillon       | 1B      |  1209 |               18 |
|           25 | Baptiste Lagaillardie    | 1B      |  1201 |               30 |
|           26 | Guillaume de Lamaze      | 2A      |  1164 |               29 |
|           27 | Victor Lassalle          | 1B      |  1159 |               53 |
|           28 | Pierre Meglin            | 1B      |  1153 |               21 |
|           29 | Loïc Harang              | 1B      |  1149 |               12 |
|           30 | Éric Edwards             | 2A      |  1090 |               12 |
|           31 | Arthur Capelier-Mourguy  | 1B      |  1086 |               68 |
|           32 | Clément Bonnichon        | 1B      |  1081 |               54 |
|           33 | Vincent Pasquesoone      | 1B      |  1078 |               27 |
|           34 | Olivier de Bernardi      | 2A      |  1076 |              103 |
|           35 | Lawrence Robert          | 2A      |  1062 |               16 |
|           36 | Peio Lagrolet            | 2B      |  1032 |               21 |
|           37 | Quentin Dionnot          | 2A      |  1006 |               21 |
|           38 | Cyril Houplain           | 2A      |  1005 |                5 |
|           39 | Hugo Houplain            | 2A      |  1003 |               12 |
|           40 | Alex Duthil              | 2A      |  1002 |                5 |
|           41 | Bertrand Lebel           | 2A      |   993 |               25 |
|           42 | Pierre Privat            | 2A      |   984 |               11 |
|           43 | Stéphane Vidaillet       | 2A      |   979 |               47 |
|           44 | Igor de Maack            | 2A      |   976 |               16 |
|           45 | Jean-Dominique Daragnes  | 2A      |   974 |               16 |
|           46 | Dimitri Girardetti       | 2A      |   958 |               22 |
|           47 | Axel Bonneville          | 2A      |   914 |               15 |
|           48 | Laurent Fiat             | 2A      |   913 |               17 |
|           49 | Pierre Chamberon         | 2B      |   899 |               10 |
|           50 | Iñaki Darthayette        | 2B      |   878 |               18 |
|           51 | Éric Dupuy               | 2A      |   872 |               44 |
|           52 | Christophe Jaulerry      | 2B      |   869 |               33 |
|           53 | Aloïs de Bouville        | 2B      |   865 |               57 |
|           54 | Jean-Marc Lanusse        | 2B      |   861 |               15 |
|           55 | Adrien Chamberon         | 2B      |   846 |               26 |
|           56 | Guillaume Barnetche      | 2B      |   842 |                2 |
|           57 | Jacques Guerin           | 2B      |   840 |                8 |
|           58 | Caroline Leclercq        | 2B      |   824 |                4 |
|           59 | Haroun Sachs             | 2A      |   821 |               34 |
|           60 | Gabriel Marot            | 2B      |   820 |               42 |
|           61 | Olivier Matteoli         | 2B      |   817 |                9 |
|           62 | Hugues Dupuy             | 2B      |   814 |                1 |
|           63 | Baptiste Guyot           | 2B      |   812 |               25 |
|           64 | Guillaume Benoit         | 2B      |   791 |                4 |
|           65 | Louis Babin              | 2B      |   781 |               46 |
|           66 | Nicolas Robuchon         | 2B      |   780 |                9 |
|           67 | Pierre-Henri Lajouane    | 2B      |   778 |               14 |
|           68 | Arthur Schwarzbard       | 2B      |   772 |                9 |
|           69 | Stéphane Soulier         | 2B      |   751 |               19 |
|           70 | Florent Bartoli          | 2B      |   734 |               20 |
|           71 | Jean-Philippe Louis      | 2B      |   720 |               15 |
