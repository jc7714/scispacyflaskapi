from flask import Flask, request, jsonify
import spacy
import scispacy

app = Flask(__name__)
nlp = spacy.load("en_core_sci_sm")

@app.route('/extract_entities', methods=['POST'])
def extract_entities():
    text = request.json.get('text', '')
    doc = nlp(text)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    return jsonify(entities)

if __name__ == '__main__':
    app.run(debug=True)
