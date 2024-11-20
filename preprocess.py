from datasets import load_dataset

def preprocess_data():
    # Charger le jeu de données CNN/Daily Mail
    dataset = load_dataset("cnn_dailymail", "3.0.0")
    
    # Diviser en ensembles d'entraînement, validation et test
    train_data = dataset['train']
    val_data = dataset['validation']
    test_data = dataset['test']
    
    # Exemple de prétraitement : Suppression des caractères spéciaux
    def clean_text(text):
        return text.replace('\n', ' ').strip()

    train_data = train_data.map(lambda x: {'article': clean_text(x['article']), 'highlights': clean_text(x['highlights'])})
    val_data = val_data.map(lambda x: {'article': clean_text(x['article']), 'highlights': clean_text(x['highlights'])})
    test_data = test_data.map(lambda x: {'article': clean_text(x['article']), 'highlights': clean_text(x['highlights'])})

    # Sauvegarder les ensembles prétraités
    train_data.save_to_disk("data/train_data")
    val_data.save_to_disk("data/val_data")
    test_data.save_to_disk("data/test_data")

if __name__ == "__main__":
    preprocess_data()
