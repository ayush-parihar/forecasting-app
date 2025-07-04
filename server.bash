# 1 · clone or copy these files
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
 
# 2 · train once (creates prophet_model.pkl)
python - <<'PY'
from forecaster.prophet_model import train
train()
print("✅ Model trained.")
PY
 
# 3 · run server
python manage.py runserver