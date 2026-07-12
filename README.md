# 🤖 AI Email Classifier

Clasificador inteligente de correos electrónicos basado en Inteligencia Artificial que combina procesamiento semántico del lenguaje (NLP), análisis de documentos y heurísticas inteligentes para clasificar emails, generar resúmenes automáticos, detectar posibles intentos de phishing y priorizar los mensajes según su nivel de urgencia.

La aplicación utiliza modelos de **Transformers**, **Sentence Transformers**, **Gradio** y una base de datos **SQLite** para ofrecer una solución completa para la gestión inteligente de correos electrónicos.

---

# 📧 Categorías Detectadas

- 🔴 **Urgente** — requiere acción inmediata.
- 🟡 **Importante pero no urgente** — necesita revisión posterior.
- 📄 **Informativo** — solo requiere lectura.
- 🚫 **Spam / Promoción** — publicidad o contenido promocional.

---

# ✨ Funcionalidades

## 🧠 Clasificación Semántica

Analiza el significado completo del correo utilizando embeddings multilingües, evitando depender únicamente de palabras clave.

---

## 📊 Score de Urgencia (0–100)

Cada correo recibe una puntuación de urgencia calculada a partir de:

- clasificación semántica
- confianza del modelo
- palabras clave de urgencia
- fechas límite detectadas
- categoría asignada

Esto permite priorizar automáticamente los correos más importantes.

---

## 🛡️ Detección de Spam y Phishing

El sistema incorpora diversas heurísticas para detectar posibles intentos de phishing, incluyendo:

- frases sospechosas habituales
- enlaces acortados
- uso excesivo de mayúsculas
- exceso de signos de exclamación
- diferencias entre el dominio del remitente y el de los enlaces

Las alertas detectadas se muestran junto al análisis.

---

## 🌍 Detección Automática de Idioma

Detecta automáticamente el idioma predominante del correo, incluso cuando el contenido mezcla varios idiomas.

---

## 📝 Resumen Automático mediante IA

Genera un resumen automático utilizando modelos de Hugging Face Transformers.

El resumen considera tanto el contenido del correo como el de los archivos adjuntos.

---

## 📎 Análisis de Adjuntos

Permite analizar varios archivos simultáneamente.

Formatos compatibles:

- PDF
- DOCX
- TXT

El contenido extraído se incorpora automáticamente al análisis.

---

## 🗄️ Historial Inteligente

Cada análisis se almacena automáticamente en una base de datos SQLite.

Se conserva información como:

- fecha
- idioma
- categoría
- score de urgencia
- resumen
- explicación
- indicadores de phishing
- existencia de adjuntos

---

## 📥 Exportación

El historial puede exportarse en:

- CSV
- JSON
- Excel (.xlsx)

---

## 🎨 Interfaz Web

Aplicación desarrollada con **Gradio** que permite:

- pegar el contenido del email
- subir múltiples archivos
- visualizar el progreso del análisis
- consultar el historial
- borrar el historial
- limpiar los campos
- descargar las exportaciones

---

# ⚙️ Instalación

```bash
git clone https://github.com/Kevin-2099/ai-email-classifier.git

cd ai-email-classifier

pip install -r requirements.txt

python app.py
```

La interfaz web se abrirá automáticamente en el navegador.

---

# 🚀 Uso

1. Pegue el contenido del correo electrónico.
2. (Opcional) Suba uno o varios archivos adjuntos.
3. Pulse **Analizar Email**.

El sistema mostrará:

- idioma detectado
- categoría asignada
- score de urgencia
- resumen automático
- explicación de la clasificación
- indicadores de spam o phishing (si existen)

---

# 🎯 Casos de Uso

- Gestión inteligente de bandejas de entrada.
- Helpdesk y soporte técnico.
- Priorización automática de correos.
- Automatización de procesos empresariales.
- Asistentes personales basados en IA.
- Clasificación documental.
- Organización automática de comunicaciones internas.

---

# 📄 Licencia

Este proyecto se distribuye bajo una **licencia propietaria con acceso al código (source-available)**.

El código fuente se pone a disposición únicamente para fines de **visualización, evaluación y aprendizaje**.

❌ No está permitido copiar, modificar, redistribuir, sublicenciar, ni crear obras derivadas del software o de su código fuente sin autorización escrita expresa del titular de los derechos.

❌ El uso comercial del software, incluyendo su oferta como servicio (SaaS), su integración en productos comerciales o su uso en entornos de producción, requiere un **acuerdo de licencia comercial independiente**.

📌 El texto **legalmente vinculante** de la licencia es la versión en inglés incluida en el archivo `LICENSE`. 

Se proporciona una traducción al español en `LICENSE_ES.md` únicamente con fines informativos. En caso de discrepancia, prevalece la versión en inglés.

---

# Autor
Kevin-2099
