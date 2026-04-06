# wakeword_service.py
import librosa
import numpy as np
from openwakeword.model import Model

import config

oww_model = Model(
    wakeword_models=[config.MODEL_PATH],
    melspec_model_path=config.SPECTROGRAM_PATH,
    embedding_model_path=config.EMBEDDINGS_PATH,
)


def process_audio(file_path):
    # 1. RESET: Fondamentale per pulire il buffer della predizione precedente
    oww_model.reset()

    # 2. Carica audio (float32, range -1 a 1)
    audio, sr = librosa.load(file_path, sr=16000, mono=True)

    # DEBUG: Stampa il picco massimo per assicurarti che il file non sia vuoto
    print(f"Max Amplitude (Float): {np.max(np.abs(audio))}")

    # 3. CONVERSIONE CRITICA: Da Float a Int16
    # Moltiplichiamo per 32767 e convertiamo in interi
    audio_int16 = (audio * 32767).astype(np.int16)

    # 4. Predizione
    predictions = oww_model.predict_clip(audio_int16)

    for frame_scores in predictions:
        for model_name, score in frame_scores.items():
            # Se vuoi vedere i nuovi score, decommenta:
            # print(f"{model_name}: {score}")
            if score > 0.5:
                return True

    return False
