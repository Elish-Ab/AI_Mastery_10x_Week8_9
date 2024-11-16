from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()

# Pydantic model for input data
class Transaction(BaseModel):
    transaction_id: str
    amount: float
    customer_id: str
    product_category: str

@app.get("/")
def read_root():
    return {"message": "Fraud Detection API is running"}



# Load the trained model
model = pickle.load(open("random_forest_model.pkl", "rb"))

@app.post("/predict")
def predict_fraud(transaction: Transaction):
    # Prepare input data for the model
    input_data = [[
        transaction.amount,
        transaction.customer_id,
        transaction.product_category
    ]]
    # Predict using the model
    prediction = model.predict(input_data)
    return {"transaction_id": transaction.transaction_id, "fraud": bool(prediction[0])}
