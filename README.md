# 📧 Clasificador de Emails con IA

Este proyecto es un **clasificador inteligente de correos electrónicos** construido en **Python + Hugging Face + Gradio**.  
El sistema analiza el texto de un email y lo clasifica en una de las siguientes categorías:

- 🟥 **Urgente** (requiere atención inmediata)  
- 🟨 **Importante pero no urgente**  
- 🟦 **Informativo**  
- 🟩 **Spam / Promoción**  

---

## 🚀 Tecnologías utilizadas
- [Transformers (Hugging Face)](https://huggingface.co/transformers/) → modelo base `distilbert-base-uncased-finetuned-sst-2-english`  
- [Gradio](https://gradio.app/) → interfaz web interactiva  
- [scikit-learn](https://scikit-learn.org/) → soporte para reglas y posible entrenamiento futuro  

---

## ⚙️ Instalación

Clona el repositorio e instala las dependencias:

git clone https://github.com/Kevin-2099/email-classifier-ai.git

cd email-classifier-ai

pip install -r requirements.txt

Ejecuta la aplicación:

python app.py

Esto abrirá una interfaz web local con Gradio en http://127.0.0.1:7860/.

## 🧠 Cómo funciona
1. Reglas basadas en palabras clave

. El sistema busca keywords típicas de cada categoría (ej. “urgente”, “inmediato”, “oferta”, “recordatorio”).

. Se aplican reglas de contexto y detección de negaciones para reducir falsos positivos.

2. Fallback con modelo de Hugging Face

. Si no encuentra coincidencias claras, usa distilBERT fine-tuned en clasificación de texto.

. Según el sentimiento detectado, asigna la categoría más probable.
