import os

import openwakeword

# Definisci la tua cartella locale
custom_dir = os.path.join(os.getcwd(), "my_models")

# Crea la cartella se non esiste
if not os.path.exists(custom_dir):
    os.makedirs(custom_dir)

# Scarica i modelli nella cartella locale
openwakeword.utils.download_models(target_directory=custom_dir)

print(f"Modelli scaricati in: {custom_dir}")
