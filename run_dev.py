import uvicorn
from livereload import Server


def run_uvicorn() -> None:
    uvicorn.run("main:app", host="127.0.0.1", reload=True, port=52000)


server = Server()


server.watch("app/views/")


server.serve(host="127.0.0.1", port=53000, root=".")


