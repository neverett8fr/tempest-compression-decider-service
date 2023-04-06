from modules.decision_tree import Decider

from fastapi import FastAPI

deciderClass = Decider()

app = FastAPI()


@app.get("/compression/decide/{file_type}/{file_size}")
async def decider(file_type: int, file_size: int):
    # file data is in bits,
    # api url input in bytes - so * 8
    ext = deciderClass.get_best_method(file_type, file_size)

    return {"data": {
        "method_ext": deciderClass.get_comp_ext(ext),
        "method_num": ext
    }, "errors": []}


@app.get("/{text}")
async def test(text: str):
    return {"test": text}
