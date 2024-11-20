## nlp-summarization-project

Le modèle que nous avons utilisé pour générer des résumés est basé sur une approche extractive et abstraite. Les résultats sont évalués en utilisant des métriques standards telles que ROUGE et BLEU, qui sont couramment utilisées pour mesurer la qualité des résumés générés par des modèles de traitement du langage naturel.

**Données d'entrée :**
- Ensemble de données : Contient 287113 articles pour l'entraînement, 13368 pour la validation, et 11490 pour le test.
- Articles traités : Les articles sont prétraités pour enlever le bruit textuel (mots inutiles, ponctuation excessive).

**Évaluation :**
- **ROUGE** : Évalue la similarité entre les résumés générés et les résumés de référence, avec une attention particulière à la précision, au rappel et à la F-mesure.
- **BLEU** : Évalue la similarité en termes de n-grammes, mais a montré de faibles scores dans ce cas.

**Problèmes rencontrés :**
- Le modèle a du mal à conserver les structures grammaticales dans les résumés extraits.
- Les scores BLEU faibles indiquent que le modèle a des difficultés à générer des résumés de manière cohérente.