import matplotlib.pyplot as plt

def plot_results():
    # Charger les résultats d'évaluation
    with open("results/evaluation.txt") as f:
        lines = f.readlines()

    rouge_scores = []
    bleu_scores = []

    # Parse les scores depuis le fichier
    for line in lines:
        if "ROUGE (Extractif)" in line:
            rouge_ext = float(line.split(":")[1].split(",")[0].strip())
            rouge_scores.append(rouge_ext)
        elif "BLEU (Extractif)" in line:
            bleu_ext = float(line.split(":")[1].split(",")[0].strip())
            bleu_scores.append(bleu_ext)

    # Graphique des scores ROUGE
    plt.figure(figsize=(8, 6))
    plt.bar(range(1, len(rouge_scores) + 1), rouge_scores, color='skyblue')
    plt.title("Scores ROUGE pour les Articles")
    plt.xlabel("Articles")
    plt.ylabel("Score ROUGE")
    plt.savefig("captures/ROUGE_scores.png")

    # Graphique des scores BLEU
    plt.figure(figsize=(8, 6))
    plt.bar(range(1, len(bleu_scores) + 1), bleu_scores, color='lightgreen')
    plt.title("Scores BLEU pour les Articles")
    plt.xlabel("Articles")
    plt.ylabel("Score BLEU")
    plt.savefig("captures/BLEU_scores.png")

if __name__ == "__main__":
    plot_results()
