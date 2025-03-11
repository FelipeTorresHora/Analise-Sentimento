from transformers import pipeline
import json

# Carregar o modelo de análise de sentimentos
sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

# Função para mapear a pontuação do modelo para um rótulo de sentimento
def map_sentiment(score):
    if score == 1:
        return "Muito Negativo"
    elif score == 2:
        return "Negativo"
    elif score == 3:
        return "Neutro"
    elif score == 4:
        return "Positivo"
    elif score == 5:
        return "Muito Positivo"
    else:
        return "Desconhecido"

# Ler o arquivo JSON com os reviews
with open("reviews.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Lista para armazenar os reviews analisados
analyzed_reviews = []

# Analisar cada review
for review in data["reviews"]:
    product = review["product"]
    comment = review["comment"]
    
    # Fazer a análise de sentimento
    result = sentiment_analyzer(comment)[0]
    
    # Extrair a pontuação, o rótulo do sentimento e o nível de confiança
    sentiment_score = int(result["label"].split()[0])  # Extrai o número da label (1 a 5)
    sentiment_label = map_sentiment(sentiment_score)
    confidence_score = round(result["score"], 2)  # Arredonda o score de confiança para 4 casas decimais
    
    # Adicionar o resultado ao review
    analyzed_review = {
        "product": product,
        "comment": comment,
        "sentiment_score": sentiment_score,
        "confidence_score": confidence_score
    }
    analyzed_reviews.append(analyzed_review)

# Salvar os reviews analisados em um novo arquivo JSON
with open("analyzed_reviews.json", "w", encoding="utf-8") as file:
    json.dump({"analyzed_reviews": analyzed_reviews}, file, ensure_ascii=False, indent=4)

print("Análise de sentimentos concluída. Resultados salvos em 'analyzed_reviews.json'.")