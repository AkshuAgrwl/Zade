from helpers.router import route_params


@route_params(status_code=200)
def get() -> str:
    return "Pong!"
