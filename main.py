import os

import boto3
from fastapi import FastAPI

BUCKET = os.environ['BUCKET']

app = FastAPI()


@app.get("/")
def get_root():
    return "Hello, welcome to this API about animals."


@app.get("/sound")
def get_sound(animal: str):
    s3 = boto3.client('s3')
    try:
        response = s3.get_object(Bucket=BUCKET, Key=f"{animal}.txt")
    except s3.exceptions.NoSuchKey:
        return f"Could not find the sound of {animal}."
    sound = response["Body"].read().decode()
    return f"The {animal} goes {sound}."
