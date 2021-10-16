# PartidaAntolatzekoMaila
Elo rating system for the Club de Pelote Basque de Paris. Mostly in French, for local use.

## Méthode, équations
Lors d'une rencontre, le PAM moyen de chaque équipe est pris en compte pour calculer leurs probabilités de victoire. La différence entre le résultat final (victoire notée 1 ou défaite notée 0), multipliée par un facteur d'échelle `k`, est ensuite utilisée pour mettre à jour les PAMs de tous les joueurs. Le facteur d'échelle utilisé est actuellement calculé comme suit, avec un poids des parties par défaut à 1, modifiable pour les tournois spéciaux.

```
k = 30 * poids_partie
```

## Classement des joueurs
Un classement des joueurs au 15 Octobre 2021 est disponible ci-dessous. Attention, ce système de classement ne devient fiable qu'après un nombre important de parties jouées pour chaque joueur.

|   Classement | Joueur                   | Série   |   PAM |
|-------------:|:-------------------------|:--------|------:|
|            1 | Côme Saint-Pierre        | 1A      |  1531 |
|            2 | Thibault Martre          | 1A      |  1433 |
|            3 | Nicolas Ossard           | 1A      |  1425 |
|            4 | Hugues Saint-Pierre      | 1A      |  1414 |
|            5 | Rayann Sachs             | 1A      |  1409 |
|            6 | Peio Mendiarat           | 1A      |  1390 |
|            7 | Ramire Nunez             | 1A      |  1382 |
|            8 | Julien Jimenez           | 1A      |  1376 |
|            9 | Charles Bachette-Peyrade | 1A      |  1372 |
|           10 | Evhan Dijoux             | 1A      |  1358 |
|           11 | Georges Bachette-Peyrade | 1A      |  1332 |
|           12 | Jean-Luc Sallaberry      | 1A      |  1331 |
|           13 | Antoine Penin            | 1A      |  1313 |
|           14 | Olivier Waltener         | 1B      |  1296 |
|           15 | Michel Lesueur           | 1B      |  1274 |
|           16 | Loïc Harang              | 1B      |  1234 |
|           17 | Charles Coustille        | 1B      |  1201 |
|           18 | Mathieu Olhagaray        | 1B      |  1200 |
|           19 | Sébastien Picabea        | 1B      |  1199 |
|           20 | Thibaud Babled           | 1B      |  1196 |
|           21 | Thibault Leguillon       | 1B      |  1186 |
|           22 | Mathieu Leizagoyen       | 1B      |  1172 |
|           23 | Alexandre de la Raitrie  | 1B      |  1150 |
|           24 | Clément Bonnichon        | 2A      |  1138 |
|           25 | Baptiste Lagaillardie    | 1B      |  1125 |
|           26 | Arthur Capelier-Mourguy  | 1B      |  1095 |
|           27 | Vincent Pasquesoone      | 1B      |  1075 |
|           28 | Éric Edwards             | 2A      |  1070 |
|           29 | Lawrence Robert          | 2A      |  1046 |
|           30 | Emmanuel Poidevin        | 2A      |  1014 |
|           31 | Pierre Privat            | 2A      |  1000 |
|           32 | Alex Duthil              | 2A      |   994 |
|           33 | Pierre Meglin            | 2A      |   993 |
|           34 | Guillaume de Lamaze      | 2A      |   993 |
|           35 | Cyril Houplain           | 2A      |   992 |
|           36 | Bertrand Lebel           | 2A      |   990 |
|           37 | Olivier de Bernardi      | 2A      |   986 |
|           38 | Victor Lassalle          | 2A      |   974 |
|           39 | Hugo Houplain            | 2A      |   969 |
|           40 | Jean-Dominique Daragnes  | 2B      |   938 |
|           41 | Stéphane Vidaillet       | 2B      |   896 |
|           42 | Baptiste Guyot           | 2B      |   877 |
|           43 | Haroun Sachs             | 2A      |   868 |
|           44 | Quentin Dionnot          | 2B      |   861 |
|           45 | Dimitri Girardetti       | 2B      |   853 |
|           46 | Igor de Maack            | 2B      |   841 |
|           47 | Christophe Jaulerry      | 2B      |   837 |
|           48 | Éric Dupuy               | 2B      |   828 |
|           49 | Jean-Marc Lanusse        | 2B      |   824 |
|           50 | Caroline Leclercq        | 2B      |   822 |
|           51 | Arthur Schwarzbard       | 2B      |   819 |
|           52 | Hugues Dupuy             | 2B      |   813 |
|           53 | Jacques Guerin           | 2B      |   804 |
|           54 | Axel Bonneville          | 2B      |   797 |
|           55 | Pierre-Henri Lajouane    | 2B      |   792 |
|           56 | Olivier Matteoli         | 2B      |   791 |
|           57 | Nicolas Robuchon         | 2B      |   784 |
|           58 | Stéphane Soulier         | 2B      |   781 |
|           59 | Laurent Fiat             | 2B      |   775 |
|           60 | Guillaume Benoit         | 2B      |   771 |
|           61 | Adrien Chamberon         | 2B      |   766 |
|           62 | Louis Babin              | 2B      |   749 |
|           63 | Aloïs de Bouville        | 2B      |   742 |
|           64 | Jean-Philippe Louis      | 2B      |   738 |
|           65 | Florent Bartoli          | 2B      |   728 |
