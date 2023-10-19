from fastapi import FastAPI
from joblib import load
import pandas as pd
import uvicorn
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
instrumentator = Instrumentator()

# Initialisez l'instrumentateur
instrumentator.instrument(app)

# Load the model
model = load('TwitterstockMarket.joblib')

df = pd.read_csv('Twitter Stock Market Dataset.csv')
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get_close_price/")
async def get_close_price(date: str):
    try:
        date = pd.to_datetime(date, format='%Y-%m-%d')
        close_price = df[df['Date'] == date]['Close'].values[0]
        return {"close_price": close_price}
    except IndexError:
        raise HTTPException(status_code=404, detail="Date not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/predict_close_price/")
async def predict_close_price(Open: float, High: float, Low: float, Volume: float):
    try:
        data = pd.DataFrame({
            'Open': [Open],
            'Feature2': [High],
            'Feature3': [Low],
            'Feature4': [Volume]
        })
        prediction = model.predict(data)
        return {"predicted_close_price": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
