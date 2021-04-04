import typer
from tsp import travelling_salesman
from bullets import bullet_hell

app = typer.Typer()


@app.command()
def qwerty():
    print("Testing Commands")


@app.command()
def tsp(n_city: int = 30, border: int = 1000, saves: str = None):
    print("Executing Travelling Salesman Example")
    travelling_salesman(n_city, border, saves=saves)


@app.command()
def bullets(border: int = 1000, n_frames: int = 650, saves: str = None):
    print("Executing Bullet Hell Example")
    bullet_hell(border, n_frames, saves=saves)


if __name__ == "__main__":
    app()
