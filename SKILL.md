---
name: wp-fr-typo
description: >
  Traduit des textes anglais en français en respectant à 100% les règles typographiques
  officielles ET le glossaire officiel de l’équipe de traduction WordPress Francophone
  (translate.wordpress.org). Déclencher ce skill dès que l’utilisateur demande de
  traduire un texte, une chaîne, une interface, une extension ou un thème WordPress
  de l’anglais vers le français, ou qu’il mentionne : "traduis", "traduire",
  "traduction WordPress", "translate WP", "chaîne à traduire", "po/pot/mo",
  "GlotPress", ou "wordpress.org/translate".
  Ce skill est aussi utile pour vérifier ou corriger une traduction française existante.
---

> **Version du glossaire** : 19/08/2026 — Source : export officiel `translate.wordpress.org/locale/fr/default/glossary/` (604 termes).

# Skill : Traduction WordPress FR -- Typographie + Glossaire officiel

Traduction conforme à 100% aux règles Polyglots WordPress FR :
- Règles typo : https://fr.wordpress.org/team/handbook/polyglots/les-regles-typographiques-utilisees-pour-la-traduction-de-wp-en-francais/
- Glossaire : https://translate.wordpress.org/locale/fr/default/glossary/
- Glossaire format CSV: https://translate.wordpress.org/locale/fr/default/glossary/-export/

---

## 1. PROCESSUS DE TRADUCTION

Ordre impératif :

1. Commence par Pull le repo pour etre a jour.
2. Identifier et remplacer tous les termes du glossaire (section 3 et `references/glossaire.md`) dans le texte source.
3. Traduire le reste en français courant, voix active, phrases courtes. Appliquer la hiérarchie épicène (section 2.10) : neutre > combiné > point médian.
4. Appliquer toutes les règles typographiques (section 2).
5. Passer la checklist (section 4) point par point.
6. Livrer le texte final prêt à copier-coller dans GlotPress.
7. Signaler tout choix non évident (terme conservé, épicène retenu, etc.).

---

## 2. REGLES TYPOGRAPHIQUES OBLIGATOIRES

### 2.1 Espaces et ponctuation

#### Pas d’espace avant -- une espace après
| Signe | Remarque |
|-------|----------|
| Point . | |
| Virgule , | |
| Points de suspension ... | Caractère U+2026 unique -- jamais trois points |
| Parenthèse fermante ) | |
| Crochet fermant ] | |

#### Une espace avant -- pas d’espace après
| Signe |
|-------|
| Parenthèse ouvrante ( |
| Crochet ouvrant [ |

#### Espace insécable (U+00A0) avant -- espace ordinaire après
OBLIGATOIRE. Voir section 6 pour les contraintes d’encodage spécifiques aux fichiers .po.

| Signe |
|-------|
| Deux-points : |
| Point-virgule ; |
| Point d’interrogation ? |
| Point d’exclamation ! |
| Guillemet français fermant >> (U+00BB) |
| Pourcentage % |
| Unités de mesure (km, Mo, px, etc.) |
| Symboles monétaires (euro, $, etc.) |
| Signes mathématiques (=, <, >, ~, +) |

#### Espace ordinaire avant -- espace insécable (U+00A0) après
| Signe |
|-------|
| Guillemet français ouvrant << (U+00AB) |

Résultat attendu : << espace-insécable texte espace-insécable >>

#### Pas d’espace avant ni après
| Signe | Remarque |
|-------|----------|
| Barre oblique / | Aucune espace avant ni après |

Correct : Local/Environnement de test -- Oui/Non -- Précédent/Suivant
Incorrect : Local / Environnement de test (espaces autour de /)

Exception : une espace avant ET après UNIQUEMENT si l’un des éléments est un nom composé avec tiret ou une expression longue, pour la lisibilité (ex. : astuce / aide à l’utilisation). Ne pas appliquer cette exception aux libellés d’alternatives (Local/Staging, Oui/Non, etc.).

---

### 2.2 Apostrophe -- courbe obligatoire

Utiliser ' (U+2019) -- JAMAIS ' (U+0027, ASCII droit).

Correct : l’extension, c’est, j’ai
Incorrect : l'extension (apostrophe droite)

---

### 2.3 Points de suspension -- caractère unique

Utiliser le caractère unique U+2026 -- jamais trois points séparés

Correct : Chargement…
Incorrect : Chargement... (trois points ASCII)

---

### 2.4 Guillemets -- français obligatoires

<< et >> avec espaces insécables intérieures -- jamais guillemets anglais droits.

Correct : Un traducteur intervient : << Où se trouve le glossaire ? >>.
Incorrect : Un traducteur intervient: "Où se trouve le glossaire?".

---

### 2.5 Majuscules

Règle de base : beaucoup moins de majuscules qu’en anglais.
Majuscule UNIQUEMENT pour : début de phrase, noms propres, sigles.

Exemples de déclassement (anglais -> français) :
- Settings (milieu de phrase) -> réglages
- Add New Post -> Ajouter un article
- Media Library -> médiathèque
- Monday, March 30 -> lundi 30 mars

Majuscules accentuées obligatoires : É accent aigu, À accent grave, Ê accent circonflexe, etc.
Correct : Étant donné, Éditeur, À noter
Incorrect : Etant donne (sans accent), Editeur (sans accent)

---

### 2.6 Nombres

| Règle | Correct | Incorrect |
|-------|---------|-----------|
| Séparateur décimal | virgule , | point . |
| Séparateur de milliers | espace insécable | point ou virgule |
| Ordinaux | 1er, 1re, 2e, 3e | 1eme, 2eme, 1st, 2nd |
| Siècles | XXIe siècle | 21eme siècle |

Exemples : 1 234,56 euros -- 100 % -- 2e version

---

### 2.7 Abréviations

- Terminée par la DERNIÈRE LETTRE du mot -> pas de point : Mme, Dr, Pr, Me, bd
- NON terminée par la dernière lettre -> point : M., art., cat.
- Sigles : pas de point entre les lettres : ONU, CSS, API
- Mr est un ANGLICISME -> REFUSÉ, écrire M.

---

### 2.8 Accents sur les majuscules

Toujours accentuer les majuscules (sauf sigles).
Correct : Étiquette avec accent, Éditeur avec accent
Incorrect : Etiquette sans accent, Editeur sans accent

---

### 2.9 Ponctuation -- cas particuliers

- Fin de phrase : toujours ., ?, ! ou points de suspension
- Fin de titre / chapitre : PAS de ponctuation.
- Liste en une seule phrase : ; après chaque item, . après le dernier.
- Après etc. : pas de points de suspension.
- Entre les lettres d’un sigle : pas de point.

---

### 2.10 Rédaction épicène (écriture inclusive)

Hiérarchie **obligatoire** — toujours essayer le niveau supérieur avant de descendre :

1. **Formulation neutre** (prioritaire) — reformuler sans marque de genre.
2. **Formulation combinée** — mentionner les deux formes en toutes lettres.
3. **Point médian** (dernier recours) — UNIQUEMENT si contrainte d’espace (libellé de bouton, en-tête de colonne, cellule étroite).

| Anglais | Neutre (niveau 1) | Combiné (niveau 2) | Point médian (niveau 3) |
|---------|-------------------|---------------------|--------------------------|
| Administrator | personne administrant le site | administrateurs et administratrices | administrateur·rice |
| User | personne inscrite | utilisateurs et utilisatrices | utilisateur·rice |
| Author | personne ayant rédigé | auteurs et autrices | auteur·rice |
| Subscriber | personne abonnée | abonnés et abonnées | abonné·e |

Règles du point médian :
- Caractère : U+00B7 · (pas un point ordinaire ., pas un tiret -)
- Tout recours au point médian doit être signalé dans un bloc [DOUTE] (voir section 8)

---

## 3. GLOSSAIRE OFFICIEL WORDPRESS FR

Source : https://translate.wordpress.org/locale/fr/default/glossary/
Glossaire complet local : `references/glossaire.md` A utiliser en priorité.
ATTENTION : Ces termes sont OBLIGATOIRES. Toute déviation est un motif de rejet.

### 3.1 Règles générales

- Vouvoiement : toujours "vous", jamais "tu".
- Infinitif pour les boutons d’action : Save -> Enregistrer.
- Impératif pour conseils/aides : Click here -> Cliquez ici.
- WordPress : toujours W et P majuscules, sans exception.
- Ne pas traduire : noms de thèmes, noms d’extensions, URL, chemins de fichiers.
- Ne pas modifier : variables gettext (%s, %1$s, etc.) et balises HTML dans les chaînes.
- URL est FÉMININ : une URL (pas un URL).

---

### 3.2 Termes critiques — erreurs de rejet les plus fréquentes

| Anglais | ✅ Officiel | ❌ À rejeter / Notes |
|---------|------------|----------------------|
| `plugin` / `plug-in` | **extension** | plugin, plug-in, greffon |
| `post` (générique) | **publication** | post, billet ; « article » si contexte blog précis |
| `save` | **enregistrer** | sauvegarder (réservé backups) |
| `settings` | **réglages** | paramètres, configurations |
| `edit` (action) | **modifier** | éditer |
| `upload` | **téléverser** | uploader |
| `download` | **télécharger** | downloader |
| `dashboard` | **Tableau de bord** | dashboard (majuscule à Tableau) |
| `media library` | **médiathèque** | bibliothèque de médias |
| `featured image` | **image mise en avant** | image à la une |
| `template` | **modèle** (FSE/site editor) — **modèle de page** (classique) | template, modèle seul hors FSE |
| `template part` | **élément de modèle** | partie de gabarit |
| `pattern` / `block pattern` | **composition** | motif toléré si non-UI |
| `block theme` | **thème basé sur des blocs** | thème de blocs si manque de place |
| `full site editing` / `FSE` | **éditeur de site** / **édition de site** | |
| `global styles` | **styles globaux** | |
| `query loop` | **boucle de requête** | |
| `customize` | **personnaliser** | customiser |
| `Customizer` | **Outil de personnalisation** | |
| `sidebar` | **colonne latérale** | barre latérale |
| `tag` (taxonomie) | **étiquette** | tag |
| `tag` (HTML) | **balise** | |
| `slug` | **slug** | identifiant normalisé (nicename) |
| `permalink` | **permalien** | lien permanent |
| `trash` (nom) | **corbeille** | |
| `trash` (verbe) | **mettre à la corbeille** | |
| `remove` | **retirer** | supprimer (sauf users/extensions/thèmes) |
| `update` (nom) | **mise à jour** | |
| `update` (verbe) | **mettre à jour** | updater |
| `username` | **identifiant** | nom d’utilisateur |
| `widget` | **widget** | non traduit |
| `back-end` / `backend` | **interface d’administration** | |
| `front-end` / `frontend` | **interface publique** | |
| `hook` (action) | **crochet d’action** | |
| `hook` (filter) | **crochet de filtre** | |
| `add-on` / `addon` | **module** | module complémentaire si possible |
| `capabilities` | **permissions** | droits selon contexte |
| `shortcode` | **code court** | |
| `tooltip` | **infobulle** | |
| `breadcrumb` | **fil d’ariane** | |
| `changelog` | **journal des modifications** | |
| `thumbnail` | **miniature** | |
| `header` | **en-tête** | masculin |
| `footer` | **pied de page** | |
| `AI` | **IA** | Intelligence artificielle |
| `mu-plugin` | **extension indispensable** | must-use |
| `deprecated` | **obsolète** | |
| `popup` | **fenêtre surgissante** | fenêtre contextuelle selon type |
| `Mr` | **M.** | Mr = anglicisme refusé |
| `Are you sure` | **Confirmez-vous** | Êtes-vous sûr·e ? (neutre préféré au point médian) |
| `successfully` | **bien** | P. ex. : La mise à jour a bien été effectuée |

---

### 3.3 Interface — navigation et structure

| Anglais | Français officiel |
|---------|-------------------|
| Dashboard | tableau de bord |
| Admin bar / Toolbar | barre d’outils |
| Screen | écran |
| Screen Options | options de l’écran |
| Panel | panneau |
| Settings | réglages |
| General Settings | réglages généraux |
| Sidebar | colonne latérale |
| Widget area | zone de widgets |
| Block | bloc |
| Block editor | éditeur de blocs |
| Classic editor | éditeur classique |
| Block inserter | outil d’insertion de blocs |
| Inspector panel / Settings sidebar | panneau de réglages (colonne latérale des réglages) |
| Reusable block | bloc réutilisable |
| Preview | prévisualisation |
| Fullscreen mode | mode plein écran |
| Spotlight mode | mode focus |
| Top toolbar | barre d’outils supérieure |
| Document overview | vue d’ensemble du document |
| Publish | publier |
| Update (bouton) | Mettre à jour |
| Save draft | Enregistrer le brouillon |
| Discard | Ignorer les modifications |
| Duplicate | Dupliquer |

---

### 3.4 Contenus

| Anglais | Français officiel |
|---------|-------------------|
| Post (type blog) | article |
| Post (générique) | publication |
| Page | page |
| Custom post type | type de publication personnalisé |
| Attachment | fichier joint |
| Media | médias |
| Featured image | image mise en avant |
| Thumbnail | miniature |
| Gallery | galerie |
| Category | catégorie |
| Tag | étiquette |
| Taxonomy | taxonomie |
| Term | terme |
| Comment | commentaire |
| Excerpt | extrait |
| Revision | révision |
| Draft | brouillon |
| Pending review | en attente de relecture |
| Sticky post | article épinglé |
| Slug | identifiant |
| Permalink | permalien |
| Archive | archives |
| Feed | flux |
| Homepage / Front page | page d’accueil |
| Blog page | page des articles |

---

### 3.5 Éditeur de blocs / FSE / Gutenberg

| Anglais | Français officiel |
|---------|-------------------|
| Block | bloc |
| Pattern | composition |
| Template | modèle |
| Template part | partie de modèle |
| Global styles | styles globaux |
| Style variation | variation de style |
| Site editor | éditeur de site |
| Full site editing | édition de site |
| Navigation block | bloc Navigation |
| Query loop | boucle de requête |
| Block locking | verrouillage de bloc |
| Cover block | bloc Couverture |
| Group block | bloc Groupe |
| Columns block | bloc Colonnes |
| Spacer | espacement |
| Separator | séparateur |
| Embed | incorporation |
| Shortcode | code court (invariable) |
| Custom HTML | HTML personnalisé |
| theme.json | theme.json (ne pas traduire) |

---

### 3.6 Utilisateurs et rôles

Choisir le niveau le plus haut possible (neutre > combiné > point médian). Le point médian n’est acceptable qu’en cas de contrainte d’espace.

**Rôles (termes genrés) :**

| Anglais | Neutre (prioritaire) | Combiné | Point médian (dernier recours) |
|---------|---------------------|---------|-------------------------------|
| User | personne inscrite | utilisateurs et utilisatrices | utilisateur·rice |
| Administrator | personne administrant le site | administrateurs et administratrices | administrateur·rice |
| Editor | personne chargée de l’édition | éditeurs et éditrices | éditeur·rice |
| Author | personne ayant rédigé | auteurs et autrices | auteur·rice |
| Contributor | personne contribuant | contributeurs et contributrices | contributeur·rice |
| Subscriber | personne abonnée | abonnés et abonnées | abonné·e |
| Super Admin | personne en charge de la super-administration | super administrateurs et super administratrices | super administrateur·rice |

**Termes non genrés :**

| Anglais | Français officiel |
|---------|-------------------|
| Profile | profil |
| Role | rôle |
| Username | identifiant |
| Password | mot de passe |
| Log in | se connecter |
| Log out | se déconnecter |
| Register | s’inscrire |
| Account | compte |
| Avatar | avatar |

---

### 3.7 Extensions et thèmes

| Anglais | Français officiel |
|---------|-------------------|
| Plugin | extension |
| Theme | thème |
| Child theme | thème enfant |
| Block theme | thème de blocs |
| Classic theme | thème classique |
| Activate | activer |
| Deactivate | désactiver |
| Install | installer |
| Uninstall | désinstaller |
| Update (nom) | mise à jour |
| Update (verbe) | mettre à jour |
| Upgrade | mettre à niveau |
| Delete | supprimer |
| Customize | personnaliser |
| Customizer | Outil de personnalisation |
| Theme options | options du thème |
| Header | en-tête |
| Footer | pied de page |
| Logo | logo |
| Background | arrière-plan |

---

### 3.8 Réglages système

| Anglais | Français officiel |
|---------|-------------------|
| General | général |
| Writing | écriture |
| Reading | lecture |
| Discussion | commentaires |
| Permalinks | permaliens |
| Privacy | confidentialité |
| Site title | titre du site |
| Tagline | slogan |
| Timezone | fuseau horaire |
| Date format | format de date |
| Time format | format d’heure |
| Language | langue |
| Search engine visibility | visibilité pour les moteurs de recherche |
| Homepage display | page d’accueil |

---

### 3.9 Termes à NE PAS traduire

Conserver tels quels dans tous les contextes :
widget -- nonce -- transient -- cron -- Gutenberg -- WordPress --
noms d’extensions -- noms de thèmes -- URL -- chemins PHP --
fonctions/hooks (wp_head, the_content, etc.)

Variables gettext dans une chaîne (%s, %1$s, %2$d) : NE JAMAIS modifier ni déplacer.
Balises HTML dans une chaîne (<strong>, <a href="...">) : NE JAMAIS modifier.

---

## 4. CHECKLIST DE VALIDATION (avant livraison)

### Typographie
- [ ] Apostrophes courbes (U+2019) -- pas de droites (U+0027)
- [ ] Points de suspension U+2026 -- pas trois points ASCII
- [ ] Guillemets français << >> -- pas guillemets anglais
- [ ] Espace insécable avant : ; ? ! >> % et unités
- [ ] Espace insécable après <<
- [ ] Pas d’espace avant . , … ) ]
- [ ] Pas d’espace autour de la barre oblique / (Local/Environnement de test, pas Local / Environnement de test)
- [ ] Pas de majuscules inutiles (calque de l’anglais)
- [ ] Majuscules accentuées (É accent aigu, À accent grave, etc.)
- [ ] Séparateur décimal = virgule
- [ ] Séparateur de milliers = espace insécable
- [ ] Rédaction épicène : formulation neutre utilisée en priorité (niveau 1)
- [ ] Si neutre impossible : formulation combinée utilisée (niveau 2)
- [ ] Point médian utilisé UNIQUEMENT si contrainte d’espace empêche niveaux 1 et 2
- [ ] Abréviations correctes (point ou non selon la règle)
- [ ] Pas de point dans les sigles

### Glossaire
- [ ] Pas de "plugin" -> "extension"
- [ ] "post" générique -> "publication"
- [ ] "settings" -> "réglages"
- [ ] "save" -> "enregistrer"
- [ ] "upload" -> "téléverser"
- [ ] "featured image" -> "image mise en avant"
- [ ] "pattern" -> "composition"
- [ ] "template" -> "gabarit"
- [ ] "tag" -> "étiquette"
- [ ] "dashboard" -> "tableau de bord"
- [ ] "media library" -> "médiathèque"
- [ ] "Mr" -> "M."
- [ ] "WordPress" avec W et P majuscules
- [ ] Variables gettext (%s, etc.) non modifiées
- [ ] Balises HTML non modifiées
- [ ] Vouvoiement (vous) respecté
- [ ] Noms d’extensions/thèmes non traduits

---

## 5. EXEMPLES COMPLETS

| Anglais | Français conforme |
|---------|-------------------|
| Save Changes | Enregistrer les modifications |
| Add New Plugin | Ajouter une extension |
| Settings | Réglages |
| Media Library | Médiathèque |
| Are you sure? | Confirmez-vous ? |
| Error: invalid value. | Erreur : valeur non valide. |
| Loading... | Chargement… (U+2026) |
| 1 item found | 1 élément trouvé |
| 100% | 100 % |
| 2nd version | 2e version |
| Mr. Smith | M. Smith |
| "quoted text" | « texte entre guillemets » |
| it’s done | c’est terminé |
| Upload your file | Téléversez votre fichier |
| Edit post | Modifier la publication |
| Add new tag | Ajouter une étiquette |
| Block pattern | Composition |
| Site Editor | Éditeur de site |
| The plugin was deleted. | L’extension a été supprimée. |
| Featured image | Image mise en avant |
| Dashboard | Tableau de bord |
| Publish | Publier |
| Update (bouton) | Mettre à jour |
| Trash | Corbeille |
| Child theme | thème enfant |
| Full site editing | édition de site |
| The administrator has been notified. | La personne chargée de l’administration a été notifiée. |
| Contributors and Authors | Les contributeurs et contributrices, et les auteurs et autrices |
| User (en-tête de colonne) | Utilisateur·rice |
| Local / Staging | Local/Environnement de test |

---

## 6. NOTES POUR LES FICHIERS .PO / GETTEXT

Les règles typographiques de la section 2 (quels caractères utiliser, où placer les espaces)
s’appliquent intégralement aux fichiers .po. Cette section couvre uniquement les contraintes
**spécifiques au format .po** qui s’ajoutent aux règles générales.

### 6.1 RÈGLE CRITIQUE -- encodage des caractères dans les fichiers .po

Les fichiers .po sont du **texte brut UTF-8**. GlotPress et gettext ne font aucune
interprétation des séquences d’échappement Unicode ni des entités HTML.

**INTERDICTION ABSOLUE** d’écrire des séquences d’échappement dans les chaînes msgstr :
- Pas de \uXXXX (ex: \u2019, \u00a0, \u2026, \u00ab, \u00bb, \u2014, \u00b7, \u0153, etc.)
- Pas de &#xXXXX; ni &#NNN;
- Pas de &nbsp; ni &laquo; ni aucune entité HTML (sauf celles déjà présentes dans le msgid source)

**Toujours insérer le caractère réel UTF-8 directement dans la chaîne.**

Cela concerne TOUS les caractères typographiques décrits en section 2 :
apostrophe courbe, espace insécable, points de suspension, guillemets français,
tirets, point médian, ligatures oe/OE, majuscules accentuées, symbole multiplication, etc.

**Pourquoi** : les séquences non interprétées s’affichent telles quelles à l’écran.
Exemple : "Lu2019extension" au lieu de "L’extension".

**Méthode** : lors de l’écriture du fichier avec l’outil Write, insérer directement
le caractère Unicode dans la chaîne. Si l’outil sérialise des \uXXXX malgré tout,
appliquer un post-traitement Python pour remplacer les séquences par les vrais caractères.

### 6.2 Règles spécifiques au format .po

- Conserver la casse des variables gettext : %s, %1$s, %2$d.
- Ne jamais modifier, supprimer ni réordonner les variables gettext.
- Ne jamais modifier les balises HTML présentes dans une chaîne.
- Les seuls échappements autorisés dans un .po sont ceux du format gettext : \n (saut de ligne), \t (tabulation), \" (guillemet double littéral).

---

## 7. SOURCES DE REFERENCE

- Règles typographiques : https://fr.wordpress.org/team/handbook/polyglots/les-regles-typographiques-utilisees-pour-la-traduction-de-wp-en-francais/
- Glossaire officiel (en ligne) : https://translate.wordpress.org/locale/fr/default/glossary/
- Glossaire complet (local) : `references/glossaire.md`
- Erreurs fréquentes : https://fr.wordpress.org/team/handbook/polyglots/le-glossaire-et-les-erreurs-de-traduction-les-plus-frequentes/
- Recommandations : https://fr.wordpress.org/team/handbook/traduire-wordpress-en-francais/recommandations/

---

## 8. GARDE-FOUS EN CAS DE DOUTE

Ne jamais silencieusement choisir une traduction incertaine. Appliquer cette procédure :

### 8.1 Cas déclencheurs d’un signal de doute

Signaler explicitement (notation `[DOUTE]`) quand :
- Le terme n’est pas dans le glossaire officiel (section 3) ni dans la mémoire (section 9)
- Le contexte change la traduction : `post` blog vs `post` générique, `template` FSE vs classique
- Le terme est peut-être un nom propre (nom d’extension, nom de thème, nom de marque)
- La chaîne contient du jargon technique ambigu (API, CLI, UI/UX, slug de taxonomie)
- La ponctuation source est inhabituelle et pourrait être intentionnelle (ex : ellipse vs ...)
- Le genre grammatical n’est pas évident (acronyme, néologisme, emprunt)
- L’épicène : la formulation neutre (niveau 1) ou combinée (niveau 2) rend la phrase trop longue ou ambiguë — signaler si recours au point médian

### 8.2 Format du signal

Après la traduction proposée, ajouter un bloc de ce type :

```
[DOUTE] "terme source"
- Traduction retenue : "ma proposition"
- Alternatives : "option B" (raison) / "option C" (raison)
- Question : précisez le contexte si [X] ou [Y]
```

Ne jamais bloquer la livraison pour un doute : proposer la traduction la plus probable ET signaler.

### 8.3 Termes à ne JAMAIS traduire sans confirmation

Si le terme ressemble à un nom propre (extension, thème, service tiers, marque) :
- Le conserver tel quel dans la traduction
- Ajouter `[DOUTE - nom propre ?]` en fin de chaîne

---

## 9. MÉMOIRE D’APPRENTISSAGE

Le skill maintient une mémoire des corrections et des glossaires projet.
Tous les fichiers sont stockés dans `.claude/wp-fr-typo/memory/` (dans le répertoire de travail courant de l’utilisateur).

**Important :** ces fichiers ne font PAS partie du skill. Ils ne sont jamais écrasés lors d’une mise à jour.

### 9.1 Structure des fichiers

```
.claude/wp-fr-typo/memory/
├── corrections.md						# global — toutes les corrections, tous projets confondus
├── glossaire-mediapapa.md				# glossaire spécifique au projet « mediapapa »
├── glossaire-wearewp.md				# glossaire spécifique au projet « wearewp »
└── ...									# un fichier par projet
```

- `corrections.md` — historique global des corrections apportées par l’utilisateur (s’applique à tous les projets)
- `glossaire-<nom-du-projet>.md` — termes spécifiques à un projet donné (non couverts par le glossaire officiel)

### 9.2 Lecture au démarrage

AVANT de traduire :
1. Lire `.claude/wp-fr-typo/memory/corrections.md` s’il existe.
2. Demander à l’utilisateur le nom du projet en cours si ce n’est pas évident du contexte.
3. Lire `.claude/wp-fr-typo/memory/glossaire-<nom-du-projet>.md` s’il existe.

Les termes du glossaire projet ont PRIORITÉ sur les valeurs par défaut du skill
(sauf sur le glossaire officiel §3 qui reste non négociable).

### 9.3 Écriture

**Quand l’utilisateur corrige une traduction :**
1. Créer le dossier `.claude/wp-fr-typo/memory/` s’il n’existe pas.
2. Ajouter une ligne dans `corrections.md` avec le format :
   `| EN | FR proposé | FR corrigé | Raison | Date |`

**Quand l’utilisateur demande de mémoriser un terme ou de créer un glossaire projet :**
1. Créer le dossier `.claude/wp-fr-typo/memory/` s’il n’existe pas.
2. Créer ou compléter `glossaire-<nom-du-projet>.md` avec le template ci-dessous.
3. Le nom du fichier est en kebab-case (ex : `glossaire-wearewp.md`, `glossaire-flavor-flavor.md`).

### 9.4 Templates

**corrections.md** :
```
# Corrections de traduction

Corrections globales apportées par l’utilisateur. S’appliquent à tous les projets.

| Anglais | Proposé | Corrigé | Raison | Date |
|---------|---------|---------|--------|------|
```

**glossaire-<nom-du-projet>.md** :
```
# Glossaire projet — <Nom du projet>

Termes spécifiques à ce projet, prioritaires sur les valeurs par défaut.

| Anglais | Français retenu | Contexte / Note |
|---------|-----------------|-----------------|
```
