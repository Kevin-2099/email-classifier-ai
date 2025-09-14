# app.py
import gradio as gr
from transformers import pipeline
import re

# -----------------------------
# 1. Cargar pipeline de Hugging Face
# -----------------------------
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

# -----------------------------
# 2. Palabras clave por categoría
# -----------------------------
KEYWORDS = {
    "Urgente": ["urgente", "inmediato", "crítico", "fallo", "problema", "atención"],  # sin "ahora"
    "Importante pero no urgente": ["importante", "revisar", "feedback", "reunión", "documento", "contrato"],
    "Spam/Promoción": ["oferta", "promoción", "suscríbete", "compra", "descuento", "gana dinero", "ahora"],
    "Informativo": ["informativo", "recordatorio", "notificación", "aviso", "resumen"]
}

# Contexto: algunas palabras solo cuentan si aparecen cerca de otra palabra clave
CONTEXT_KEYWORDS = {
    "Urgente": [["responder", "urgente"], ["atención", "inmediato"]],
    # Ejemplo: "ahora" sola no es urgente, pero con "responder" podría ser
}

NEGATION_WORDS = ["no", "sin", "nunca", "jamás"]

# -----------------------------
# 3. Función para detectar negación
# -----------------------------
def has_negation_robust(text, keyword, window=5):
    text_clean = re.sub(r'[.,;!?]', ' ', text.lower())
    words = text_clean.split()
    for i, w in enumerate(words):
        if w == keyword.lower():
            start = max(0, i - window)
            context = words[start:i]
            if any(neg in context for neg in NEGATION_WORDS):
                return True
    return False

# -----------------------------
# 4. Función para verificar contexto de palabra clave
# -----------------------------
def check_context(text, keyword):
    text_clean = re.sub(r'[.,;!?]', ' ', text.lower())
    words = text_clean.split()
    for ctx_pair in CONTEXT_KEYWORDS.get("Urgente", []):
        if keyword in ctx_pair:
            # Chequear si ambas palabras aparecen en el texto
            if all(word in words for word in ctx_pair):
                return True
            else:
                return False
    return True  # si no hay regla de contexto, pasa

# -----------------------------
# 5. Función principal de clasificación
# -----------------------------
def classify_email(email_text):
    text_lower = email_text.lower()

    # 5a. Reglas con keywords, contexto y negaciones
    for category, words in KEYWORDS.items():
        for word in words:
            if re.search(r"\b" + re.escape(word) + r"\b", text_lower):
                if has_negation_robust(email_text, word):
                    continue  # ignorar palabra clave si está negada
                if not check_context(email_text, word):
                    continue  # ignorar si contexto no cumple
                explanation = f"Se detectó la palabra clave '{word}' asociada con la categoría '{category}'."
                return category, explanation

    # 5b. Fallback al modelo de Hugging Face
    pred = classifier(email_text)[0]
    label = pred['label']
    score = pred['score']

    if label == 'NEGATIVE' and score > 0.7:
        category = "Urgente"
        explanation = "El contenido del email sugiere urgencia según el modelo."
    elif label == 'POSITIVE' and score > 0.7:
        category = "Importante pero no urgente"
        explanation = "El email es relevante pero no urgente según el modelo."
    else:
        category = "Informativo"
        explanation = "El email parece ser solo informativo según el modelo."

    return category, explanation

# -----------------------------
# 6. Interfaz Gradio
# -----------------------------
iface = gr.Interface(
    fn=classify_email,
    inputs=gr.Textbox(lines=10, placeholder="Pega aquí el email..."),
    outputs=[gr.Label(num_top_classes=1), gr.Textbox()],
    title="Clasificador de Emails",
    description="Clasifica emails en: Urgente, Importante, Informativo, Spam. Evita falsos positivos con contexto y negaciones."
)

if __name__ == "__main__":
    iface.launch()
