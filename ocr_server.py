from flask import Flask, request, jsonify
import keras_ocr
import base64
import io
from PIL import Image

app = Flask(__name__)
pipeline = keras_ocr.pipeline.Pipeline()

@app.route('/process_captcha', methods=['POST'])
def process_captcha():
    data = request.json
    if 'image' not in data:
        return jsonify({'error': 'No image provided'}), 400

    # Decode the base64 image
    image_data = base64.b64decode(data['image'])
    image = Image.open(io.BytesIO(image_data))

    # Use Keras OCR to extract text
    prediction_groups = pipeline.recognize([image])
    text = ''.join([word for word, box in prediction_groups[0]])

    return jsonify({'text': text})

if __name__ == '__main__':
    import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use the PORT environment variable or default to 5000
    app.run(host='0.0.0.0', port=port)

