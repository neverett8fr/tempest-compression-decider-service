from modules.decision_tree import get_best_method, get_type_ext, get_comp_ext

from fastapi import FastAPI

app = FastAPI()


@app.get("/compression/decide/{file_type}/{file_size}")
async def decider(file_type: int, file_size: int):
    # file data is in bits,
    # api url input in bytes - so * 8
    ext = get_best_method(file_type, file_size * 8)

    return {"data": {
        "method_ext": get_comp_ext(ext),
        "method_num": ext
    }, "errors": []}


@app.get("/{text}")
async def root(text: str):
    return {"test": text}
