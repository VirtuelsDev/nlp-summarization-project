from transformers import pipeline

def summarize_extractive():
    # Charger le modèle extractif
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    
    # Charger les données de test
    from datasets import load_from_disk
    test_data = load_from_disk("data/test_data")

    # Générer des résumés pour les articles de test
    results = []
    for article in test_data['article'][:10]:  # Limiter à 10 articles pour l'exemple
        summary = summarizer(article, max_length=130, min_length=30, do_sample=False)
        results.append(summary[0]['summary_text'])
    
    # Sauvegarder les résumés
    with open("results/extractive_summaries.txt", "w") as f:
        for res in results:
            f.write(res + "\n")

if __name__ == "__main__":
    summarize_extractive()
