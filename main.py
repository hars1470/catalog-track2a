from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI(title='SSIP 2.0 Participle Assistant')

# Serve static frontend files
app.mount('/frontend', StaticFiles(directory='frontend'), name='frontend')

@app.get('/')
def serve_frontend():
    return FileResponse(os.path.join('frontend', 'index.html'))

@app.get('/participle/{word}')
def analyze_participle(word: str):
    return {
        'word': word,
        'type': 'Present Participle (-ing)' if word.endswith('ing') else 'Past Participle (-ed/V3)',
        'gujarati_context': 'ચાલુ વર્તમાન દર્શાવતું રૂપ' if word.endswith('ing') else 'પૂર્ણ થયેલી ક્રિયા દર્શાવતું રૂપ'
    }
