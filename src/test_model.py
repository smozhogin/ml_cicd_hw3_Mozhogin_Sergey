import os
import sys
import subprocess
import joblib

MODEL_PATH = os.path.join('models', 'model.pkl')

def test_model_file_created():
    subprocess.check_call([sys.executable, 'src/train.py'])
    assert os.path.exists(MODEL_PATH), f'Файл с моделью {MODEL_PATH} не был создан'

def test_model_can_predict():
    model = joblib.load(MODEL_PATH)
    pred = model.predict([[5.2, 4.5, 1.5, 1.2]])
    assert pred is not None