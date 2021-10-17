# PartidaAntolatzekoMaila
Elo rating system for the Club de Pelote Basque de Paris. Mostly in French, for local use.

## Méthode, équations
Lors d'une rencontre, le PAM moyen de chaque équipe est pris en compte pour calculer leurs probabilités de victoire. La différence entre le résultat final (victoire notée 1 ou défaite notée 0), multipliée par un facteur d'échelle `k`, est ensuite utilisée pour mettre à jour les PAMs de tous les joueurs. Le facteur d'échelle utilisé est actuellement calculé comme suit, avec un poids des parties par défaut à 1, modifiable pour les tournois spéciaux.

```
k = 30 * poids_partie
```

## Classement des joueurs
Un classement des joueurs au 17 Octobre 2021 est disponible ci-dessous. Attention, ce système de classement ne devient fiable qu'après un nombre important de parties jouées pour chaque joueur.

|   Classement | Joueur                   | Série   |   PAM |
|-------------:|:-------------------------|:--------|------:|
|            1 | Côme Saint-Pierre        | 1A      |  1498 |
|            2 | Hugues Saint-Pierre      | 1A      |  1441 |
|            3 | Thibault Martre          | 1A      |  1433 |
|            4 | Nicolas Ossard           | 1A      |  1425 |
|            5 | Rayann Sachs             | 1A      |  1403 |
|            6 | Ramire Nunez             | 1A      |  1402 |
|            7 | Peio Mendiarat           | 1A      |  1390 |
|            8 | Georges Bachette-Peyrade | 1A      |  1384 |
|            9 | Charles Bachette-Peyrade | 1A      |  1372 |
|           10 | Evhan Dijoux             | 1A      |  1358 |
|           11 | Jean-Luc Sallaberry      | 1A      |  1343 |
|           12 | Julien Jimenez           | 1A      |  1337 |
|           13 | Michel Lesueur           | 1B      |  1291 |
|           14 | Olivier Waltener         | 1B      |  1290 |
|           15 | Antoine Penin            | 1A      |  1286 |
|           16 | Loïc Harang              | 1B      |  1234 |
|           17 | Charles Coustille        | 1B      |  1201 |
|           18 | Mathieu Olhagaray        | 1B      |  1200 |
|           19 | Sébastien Picabea        | 1B      |  1199 |
|           20 | Thibaud Babled           | 1B      |  1196 |
|           21 | Thibault Leguillon       | 1B      |  1186 |
|           22 | Alexandre Egurreguy      | 1B      |  1182 |
|           23 | Mathieu Leizagoyen       | 1B      |  1172 |
|           24 | Alexandre de la Raitrie  | 1B      |  1150 |
|           25 | Baptiste Lagaillardie    | 1B      |  1142 |
|           26 | Clément Bonnichon        | 2A      |  1138 |
|           27 | Arthur Capelier-Mourguy  | 1B      |  1095 |
|           28 | Vincent Pasquesoone      | 1B      |  1075 |
|           29 | Éric Edwards             | 2A      |  1070 |
|           30 | Lawrence Robert          | 2A      |  1046 |
|           31 | Emmanuel Poidevin        | 2A      |  1014 |
|           32 | Olivier de Bernardi      | 2A      |   997 |
|           33 | Alex Duthil              | 2A      |   994 |
|           34 | Pierre Meglin            | 2A      |   993 |
|           35 | Guillaume de Lamaze      | 2A      |   993 |
|           36 | Cyril Houplain           | 2A      |   992 |
|           37 | Bertrand Lebel           | 2A      |   990 |
|           38 | Victor Lassalle          | 2A      |   974 |
|           39 | Hugo Houplain            | 2A      |   969 |
|           40 | Pierre Privat            | 2A      |   959 |
|           41 | Jean-Dominique Daragnes  | 2B      |   938 |
|           42 | Stéphane Vidaillet       | 2B      |   896 |
|           43 | Haroun Sachs             | 2A      |   894 |
|           44 | Baptiste Guyot           | 2B      |   877 |
|           45 | Quentin Dionnot          | 2B      |   861 |
|           46 | Dimitri Girardetti       | 2B      |   853 |
|           47 | Igor de Maack            | 2B      |   841 |
|           48 | Éric Dupuy               | 2B      |   828 |
|           49 | Jean-Marc Lanusse        | 2B      |   824 |
|           50 | Arthur Schwarzbard       | 2B      |   822 |
|           51 | Caroline Leclercq        | 2B      |   822 |
|           52 | Christophe Jaulerry      | 2B      |   821 |
|           53 | Hugues Dupuy             | 2B      |   813 |
|           54 | Jacques Guerin           | 2B      |   804 |
|           55 | Axel Bonneville          | 2B      |   797 |
|           56 | Pierre-Henri Lajouane    | 2B      |   792 |
|           57 | Olivier Matteoli         | 2B      |   791 |
|           58 | Nicolas Robuchon         | 2B      |   784 |
|           59 | Stéphane Soulier         | 2B      |   781 |
|           60 | Laurent Fiat             | 2B      |   775 |
|           61 | Guillaume Benoit         | 2B      |   771 |
|           62 | Adrien Chamberon         | 2B      |   766 |
|           63 | Louis Babin              | 2B      |   749 |
|           64 | Aloïs de Bouville        | 2B      |   742 |
|           65 | Jean-Philippe Louis      | 2B      |   738 |
|           66 | Florent Bartoli          | 2B      |   728 |
