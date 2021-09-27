# PartidaAntolatzekoMaila
Elo rating system for the Club de Pelote Basque de Paris. Mostly in French, for local use.

## Méthode, équations
Lors d'une rencontre, le PAM moyen de chaque équipe est pris en compte pour calculer leurs probabilités de victoire. La différence entre le résultat final (victoire notée 1 ou défaite notée 0), multipliée par un facteur d'échelle `k`, est ensuite utilisée pour mettre à jour les PAMs de tous les joueurs. Le facteur d'échelle utilisé est actuellement calculé comme suit, avec un poids des parties par défaut à 1, modifiable pour les tournois spéciaux.

```
k = 30 * poids_partie
```

## Classement des joueurs
Un classement des joueurs avec les dernières informations entrées et synchronisées est disponible ci-dessous. Attention, ce système de classement ne devient fiable qu'après un nombre important de parties jouées pour chaque joueur.

|   Classement | Joueur                   | Série   |   PAM |
|-------------:|:-------------------------|:--------|------:|
|            1 | Hugues Saint-Pierre      | 1A      |  1446 |
|            2 | Nicolas Ossard           | 1A      |  1438 |
|            3 | Côme Saint-Pierre        | 1A      |  1421 |
|            4 | Peio Mendiarat           | 1A      |  1420 |
|            5 | Thibault Martre          | 1A      |  1404 |
|            6 | Ramire Nunez             | 1A      |  1400 |
|            7 | Georges Bachette-Peyrade | 1A      |  1391 |
|            8 | Charles Bachette-Peyrade | 1A      |  1372 |
|            9 | Julien Jimenez           | 1A      |  1356 |
|           10 | Jean-Luc Sallaberry      | 1A      |  1344 |
|           11 | Evhan Dijoux             | 1A      |  1342 |
|           12 | Olivier Waltener         | 1B      |  1274 |
|           13 | Michel Lesueur           | 1B      |  1245 |
|           14 | Sébastien Picabea        | 1B      |  1235 |
|           15 | Thibaud Babled           | 1B      |  1228 |
|           16 | Charles Coustille        | 1B      |  1216 |
|           17 | Mathieu Olhagaray        | 1B      |  1200 |
|           18 | Loïc Harang              | 1B      |  1200 |
|           19 | Baptiste Lagaillardie    | 1B      |  1193 |
|           20 | Thibault Leguillon       | 1B      |  1189 |
|           21 | Mathieu Leizagoyen       | 1B      |  1186 |
|           22 | Alexandre de la Raitrie  | 1B      |  1172 |
|           23 | Arthur Capelier-Mourguy  | 1B      |  1167 |
|           24 | Vincent Pasquesoone      | 1B      |  1120 |
|           25 | Clément Bonnichon        | 2A      |  1080 |
|           26 | Pierre Meglin            | 2A      |  1027 |
|           27 | Éric Edwards             | 2A      |  1011 |
|           28 | Bertrand Lebel           | 2A      |  1001 |
|           29 | Pierre Privat            | 2A      |  1000 |
|           30 | Emmanuel Poidevin        | 2A      |   998 |
|           31 | Alex Duthil              | 2A      |   994 |
|           32 | Cyril Houplain           | 2A      |   992 |
|           33 | Victor Lassalle          | 2A      |   992 |
|           34 | Olivier de Bernardi      | 2A      |   989 |
|           35 | Guillaume de Lamaze      | 2A      |   984 |
|           36 | Lawrence Robert          | 2A      |   978 |
|           37 | Haroun Sachs             | 2A      |   916 |
|           38 | Dimitri Girardetti       | 2B      |   863 |
|           39 | Caroline Leclercq        | 2B      |   822 |
|           40 | Quentin Dionnot          | 2B      |   820 |
|           41 | Baptiste Guyot           | 2B      |   819 |
|           42 | Arthur Schwarz           | 2B      |   819 |
|           43 | Alois de Bouville        | 2B      |   818 |
|           44 | Igor de Maack            | 2B      |   817 |
|           45 | Stéphane Vidaillet       | 2B      |   814 |
|           46 | Jacques Guerin           | 2B      |   804 |
|           47 | Louis de Lignac          | 2B      |   800 |
|           48 | Jean-Dominique Daragnes  | 2B      |   800 |
|           49 | Jean-Philippe Louis      | 2B      |   792 |
|           50 | Olivier Matteoli         | 2B      |   791 |
|           51 | Axel Bonneville          | 2B      |   790 |
|           52 | Éric Dupuy               | 2B      |   787 |
|           53 | Pierre-Henri             | 2B      |   784 |
|           54 | Laurent Fiat             | 2B      |   783 |
|           55 | Stéphane Soulier         | 2B      |   776 |
|           56 | Guillaume Benoit         | 2B      |   771 |
|           57 | Florent Bartoli          | 2B      |   771 |
|           58 | Adrien Chamberon         | 2B      |   769 |
