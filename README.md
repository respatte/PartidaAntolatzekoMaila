# PartidaAntolatzekoMaila
Elo rating system for the Club de Pelote Basque de Paris. Mostly in French, for local use.

## Méthode, équations
Lors d'une rencontre, le PAM moyen de chaque équipe est pris en compte pour calculer leurs probabilités de victoire. La différence entre le résultat final (victoire notée 1 ou défaite notée 0), multipliée par un facteur d'échelle `k`, est ensuite utilisée pour mettre à jour les PAMs de tous les joueurs. Le facteur d'échelle utilisé est actuellement calculé comme suit, avec un poids des parties par défaut à 1, modifiable pour les tournois spéciaux.

```
k = 30 * poids_partie
```

## Classement des joueurs
Un classement des joueurs au 1er Octobre 2021 est disponible ci-dessous. Attention, ce système de classement ne devient fiable qu'après un nombre important de parties jouées pour chaque joueur.

|   Classement | Joueur                   | Série   |   PAM |
|-------------:|:-------------------------|:--------|------:|
|            1 | Côme Saint-Pierre        | 1A      |  1504 |
|            2 | Nicolas Ossard           | 1A      |  1438 |
|            3 | Thibault Martre          | 1A      |  1419 |
|            4 | Ramire Nunez             | 1A      |  1400 |
|            5 | Peio Mendiarat           | 1A      |  1387 |
|            6 | Julien Jimenez           | 1A      |  1386 |
|            7 | Hugues Saint-Pierre      | 1A      |  1385 |
|            8 | Charles Bachette-Peyrade | 1A      |  1372 |
|            9 | Georges Bachette-Peyrade | 1A      |  1337 |
|           10 | Evhan Dijoux             | 1A      |  1331 |
|           11 | Jean-Luc Sallaberry      | 1A      |  1320 |
|           12 | Michel Lesueur           | 1B      |  1285 |
|           13 | Olivier Waltener         | 1B      |  1274 |
|           14 | Charles Coustille        | 1B      |  1261 |
|           15 | Sébastien Picabea        | 1B      |  1232 |
|           16 | Loïc Harang              | 1B      |  1208 |
|           17 | Thibaud Babled           | 1B      |  1205 |
|           18 | Mathieu Olhagaray        | 1B      |  1200 |
|           19 | Mathieu Leizagoyen       | 1B      |  1187 |
|           20 | Thibault Leguillon       | 1B      |  1181 |
|           21 | Arthur Capelier-Mourguy  | 1B      |  1160 |
|           22 | Alexandre de la Raitrie  | 1B      |  1150 |
|           23 | Baptiste Lagaillardie    | 1B      |  1140 |
|           24 | Clément Bonnichon        | 2A      |  1106 |
|           25 | Vincent Pasquesoone      | 1B      |  1103 |
|           26 | Victor Lassalle          | 2A      |  1011 |
|           27 | Éric Edwards             | 2A      |  1011 |
|           28 | Pierre Meglin            | 2A      |  1011 |
|           29 | Guillaume de Lamaze      | 2A      |  1009 |
|           30 | Emmanuel Poidevin        | 2A      |  1003 |
|           31 | Bertrand Lebel           | 2A      |  1001 |
|           32 | Pierre Privat            | 2A      |  1000 |
|           33 | Alex Duthil              | 2A      |   994 |
|           34 | Cyril Houplain           | 2A      |   992 |
|           35 | Lawrence Robert          | 2A      |   978 |
|           36 | Olivier de Bernardi      | 2A      |   949 |
|           37 | Haroun Sachs             | 2A      |   921 |
|           38 | Jean-Dominique Daragnes  | 2B      |   872 |
|           39 | Alois de Bouville        | 2B      |   848 |
|           40 | Igor de Maack            | 2B      |   845 |
|           41 | Baptiste Guyot           | 2B      |   842 |
|           42 | Dimitri Girardetti       | 2B      |   833 |
|           43 | Caroline Leclercq        | 2B      |   822 |
|           44 | Quentin Dionnot          | 2B      |   820 |
|           45 | Arthur Schwarz           | 2B      |   819 |
|           46 | Axel Bonneville          | 2B      |   815 |
|           47 | Stéphane Vidaillet       | 2B      |   814 |
|           48 | Jacques Guerin           | 2B      |   804 |
|           49 | Éric Dupuy               | 2B      |   797 |
|           50 | Louis Babin              | 2B      |   792 |
|           51 | Olivier Matteoli         | 2B      |   791 |
|           52 | Pierre-Henri Lajouane    | 2B      |   784 |
|           53 | Nicolas Robuchon         | 2B      |   784 |
|           54 | Adrien Chamberon         | 2B      |   776 |
|           55 | Stéphane Soulier         | 2B      |   776 |
|           56 | Guillaume Benoit         | 2B      |   771 |
|           57 | Jean-Philippe Louis      | 2B      |   755 |
|           58 | Laurent Fiat             | 2B      |   747 |
|           59 | Florent Bartoli          | 2B      |   744 |
