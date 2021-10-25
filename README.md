# PartidaAntolatzekoMaila
Elo rating system for the Club de Pelote Basque de Paris. Mostly in French, for local use.

## Méthode, équations
Lors d'une rencontre, le PAM moyen de chaque équipe est pris en compte pour calculer leurs probabilités de victoire. La différence entre le résultat final (victoire notée 1 ou défaite notée 0), multipliée par un facteur d'échelle `k`, est ensuite utilisée pour mettre à jour les PAMs de tous les joueurs. Le facteur d'échelle utilisé est actuellement calculé comme suit, avec un poids des parties par défaut à 1, modifiable pour les tournois spéciaux.

```
k = 30 * poids_partie
```

## Classement des joueurs
Un classement des joueurs au 25 Octobre 2021 est disponible ci-dessous. Attention, ce système de classement ne devient fiable qu'après un nombre important de parties jouées pour chaque joueur.

|   Classement | Joueur                   | Série   |   PAM |
|-------------:|:-------------------------|:--------|------:|
|            1 | Côme Saint-Pierre        | 1A      |  1536 |
|            2 | Thibault Martre          | 1A      |  1467 |
|            3 | Hugues Saint-Pierre      | 1A      |  1446 |
|            4 | Nicolas Ossard           | 1A      |  1421 |
|            5 | Ramire Nunez             | 1A      |  1415 |
|            6 | Rayann Sachs             | 1A      |  1409 |
|            7 | Georges Bachette-Peyrade | 1A      |  1406 |
|            8 | Olivier Waltener         | 1A      |  1379 |
|            9 | Charles Bachette-Peyrade | 1A      |  1379 |
|           10 | Julien Jimenez           | 1A      |  1366 |
|           11 | Peio Mendiarat           | 1A      |  1364 |
|           12 | Evhan Dijoux             | 1A      |  1357 |
|           13 | Jean-Luc Sallaberry      | 1A      |  1354 |
|           14 | Michel Lesueur           | 1B      |  1322 |
|           15 | Antoine Penin            | 1A      |  1296 |
|           16 | Charles Coustille        | 1A      |  1248 |
|           17 | Sébastien Picabea        | 1B      |  1247 |
|           18 | Loïc Harang              | 1B      |  1246 |
|           19 | Clément Bonnichon        | 1B      |  1245 |
|           20 | Thibaud Babled           | 1B      |  1206 |
|           21 | Baptiste Lagaillardie    | 1B      |  1204 |
|           22 | Thibault Leguillon       | 1B      |  1200 |
|           23 | Mathieu Leizagoyen       | 1B      |  1198 |
|           24 | Emmanuel Poidevin        | 1B      |  1193 |
|           25 | Alexandre Egurreguy      | 1B      |  1185 |
|           26 | Alexandre de la Raitrie  | 1B      |  1177 |
|           27 | Mathieu Olhagaray        | 1B      |  1175 |
|           28 | Arthur Capelier-Mourguy  | 1B      |  1171 |
|           29 | Victor Lassalle          | 1B      |  1168 |
|           30 | Pierre Meglin            | 1B      |  1158 |
|           31 | Olivier de Bernardi      | 2A      |  1101 |
|           32 | Éric Edwards             | 2A      |  1079 |
|           33 | Jean-Dominique Daragnes  | 2A      |  1066 |
|           34 | Vincent Pasquesoone      | 1B      |  1058 |
|           35 | Lawrence Robert          | 2A      |  1053 |
|           36 | Guillaume de Lamaze      | 2A      |  1041 |
|           37 | Quentin Dionnot          | 2A      |  1015 |
|           38 | Cyril Houplain           | 2A      |  1005 |
|           39 | Stéphane Vidaillet       | 2A      |  1004 |
|           40 | Alex Duthil              | 2A      |  1002 |
|           41 | Dimitri Girardetti       | 2A      |   995 |
|           42 | Igor de Maack            | 2A      |   987 |
|           43 | Pierre Privat            | 2A      |   984 |
|           44 | Hugo Houplain            | 2A      |   973 |
|           45 | Bertrand Lebel           | 2A      |   962 |
|           46 | Éric Dupuy               | 2A      |   962 |
|           47 | Laurent Fiat             | 2A      |   954 |
|           48 | Axel Bonneville          | 2A      |   914 |
|           49 | Baptiste Guyot           | 2B      |   910 |
|           50 | Haroun Sachs             | 2A      |   888 |
|           51 | Aloïs de Bouville        | 2B      |   870 |
|           52 | Peio Lagrolet            | 2B      |   864 |
|           53 | Pierre Chamberon         | 2B      |   849 |
|           54 | Christophe Jaulerry      | 2B      |   840 |
|           55 | Jacques Guerin           | 2B      |   832 |
|           56 | Jean-Marc Lanusse        | 2B      |   825 |
|           57 | Caroline Leclercq        | 2B      |   814 |
|           58 | Hugues Dupuy             | 2B      |   814 |
|           59 | Arthur Schwarzbard       | 2B      |   805 |
|           60 | Olivier Matteoli         | 2B      |   802 |
|           61 | Adrien Chamberon         | 2B      |   801 |
|           62 | Guillaume Benoit         | 2B      |   791 |
|           63 | Nicolas Robuchon         | 2B      |   788 |
|           64 | Pierre-Henri Lajouane    | 2B      |   774 |
|           65 | Stéphane Soulier         | 2B      |   769 |
|           66 | Jean-Philippe Louis      | 2B      |   763 |
|           67 | Florent Bartoli          | 2B      |   727 |
|           68 | Louis Babin              | 2B      |   714 |
