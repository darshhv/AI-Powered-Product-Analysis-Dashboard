import os
import requests
import tensorflow as tf

model_urls = {
    "master": "https://drive.google.com/uc?id=19JTau3vko39Bs8fDDEUlA7VGri1p-9Gk",
    "morph": "https://drive.google.com/uc?id=1v63XBBN6H11p0ZcbTVbpFegD7SOsvHE4",
    "subtype": "https://drive.google.com/uc?id=1s7A7S5bjm4toSCZNhkTcG8w7J6OrHvQ-",
    "factors": "https://drive.google.com/uc?id=1NfqRYKlTMDpEOgQ_vij8YCNfRN6UO4qU",
    "realworld": "https://drive.google.com/uc?id=1-kSSr7QwCzwP0Djbf8adxQpnHH58qaWU"
}

def download_model(model_name, save_path):
    if not os.path.exists(save_path):
        print(f"Downloading {model_name} model...")
        response = requests.get(model_urls[model_name])
        with open(save_path, 'wb') as f:
            f.write(response.content)
    else:
        print(f"{model_name} model already exists.")

def load_model(model_name):
    filename = f"{model_name}_model.keras"
    download_model(model_name, filename)
    return tf.keras.models.load_model(filename)
