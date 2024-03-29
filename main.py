import uvicorn
from fastapi import FastAPI, Body

app = FastAPI()


@app.post("/")
def read_item(data=Body()):
    print(data)

if __name__ == "__main__":
    uvicorn.run(app, host="1.0.0.0", port=80)

