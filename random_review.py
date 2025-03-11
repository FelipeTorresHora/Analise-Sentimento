import json
import random

products = [
    "Geladeira FrostFree (EletroD)",
    "Fogão 4 Bocas (EletroD)",
    "Máquina de Lavar TurboWash (EletroD)",
    "Micro-ondas QuickHeat (EletroD)"
]

positive_comments = [
    "Produto excelente! Superou minhas expectativas.",
    "Muito bom, recomendo a todos.",
    "Funciona perfeitamente, estou muito satisfeito.",
    "Qualidade impecável e entrega rápida.",
    "Adorei! Vale cada centavo.",
    "Ótimo desempenho e design moderno.",
    "Facilidade de uso incrível, estou impressionado.",
    "Produto de alta qualidade, recomendo.",
    "Atendeu todas as minhas necessidades.",
    "Melhor compra que já fiz!"
]

neutral_comments = [
    "Produto bom, mas poderia ser melhor.",
    "Funciona bem, mas não é nada extraordinário.",
    "Custo-benefício razoável.",
    "Atende às expectativas, mas não me surpreendeu.",
    "Bom, mas o design poderia ser mais moderno.",
    "Funciona, mas o manual de instruções é confuso.",
    "Não é ruim, mas também não é excelente.",
    "Produto decente, mas esperava mais.",
    "Faz o que promete, mas sem grandes diferenciais.",
]

negative_comments = [
    "Péssima qualidade, não recomendo.",
    "Produto veio com defeito, muito decepcionado.",
    "Não funciona como esperado, muito frustrante.",
    "Atendimento ao cliente horrível, não comprem.",
    "Pior produto que já adquiri.",
    "Muito barulhento e ineficiente.",
    "Quebra facilmente, não vale o investimento.",
    "Produto de baixa qualidade, não compre.",
    "Totalmente insatisfeito com a compra.",
    "Arrependido da compra, não atendeu minhas expectativas."
]

def generate_random_review():
    product = random.choice(products)
    rating = random.randint(1, 5)
    
    if rating >= 4:
        comment = random.choice(positive_comments)
    elif rating == 3:
        comment = random.choice(neutral_comments)
    else:
        comment = random.choice(negative_comments)
    
    return {
        "product": product,
        "comment": comment,
    }

reviews = [generate_random_review() for _ in range(500)]

with open("reviews.json", "w", encoding="utf-8") as file:
    json.dump({"reviews": reviews}, file, ensure_ascii=False, indent=4)

print("Arquivo 'reviews.json' criado com sucesso!")