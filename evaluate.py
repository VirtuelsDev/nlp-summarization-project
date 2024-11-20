from rouge_score import rouge_scorer
from nltk.translate.bleu_score import sentence_bleu

def evaluate():
    # Charger les résumés générés et les références
    with open("results/extractive_summaries.txt") as f:
        extractive_summaries = f.readlines()
    with open("results/abstractive_summaries.txt") as f:
        abstractive_summaries = f.readlines()
    
    from datasets import load_from_disk
    test_data = load_from_disk("data/test_data")
    references = test_data['highlights'][:10]  # Correspondance avec les 10 articles testés

    # Évaluation des scores ROUGE et BLEU
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    rouge_results = []
    bleu_results = []

    for ref, ext, absr in zip(references, extractive_summaries, abstractive_summaries):
        # Calcul ROUGE
        rouge_ext = scorer.score(ref, ext)
        rouge_abs = scorer.score(ref, absr)
        rouge_results.append((rouge_ext, rouge_abs))

        # Calcul BLEU
        bleu_ext = sentence_bleu([ref.split()], ext.split())
        bleu_abs = sentence_bleu([ref.split()], absr.split())
        bleu_results.append((bleu_ext, bleu_abs))
    
    # Sauvegarder les résultats
    with open("results/evaluation.txt", "w") as f:
        for i, (r, b) in enumerate(zip(rouge_results, bleu_results)):
            f.write(f"Article {i+1}:\n")
            f.write(f"ROUGE (Extractif): {r[0]}, ROUGE (Abstrait): {r[1]}\n")
            f.write(f"BLEU (Extractif): {b[0]}, BLEU (Abstrait): {b[1]}\n\n")

if __name__ == "__main__":
    evaluate()
