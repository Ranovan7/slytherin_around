import typer
from tsp import travelling_salesman
from bullets import bullet_hell
from boids import bird_flocks
from games import start_game
from nimrod import try_nim

app = typer.Typer()


@app.command()
def qwerty():
    print("Testing Commands")


@app.command()
def nim_test():
    try_nim()


@app.command()
def tsp(n_city: int = 30, border: int = 1000, saves: str = None):
    print("Executing Travelling Salesman Example")
    travelling_salesman(n_city, border, saves=saves)


@app.command()
def bullets(border: int = 1000, n_frames: int = 700, saves: str = None):
    print("Executing Bullet Hell Example")
    bullet_hell(border, n_frames, saves=saves)


@app.command()
def boids(
    n_birds: int = 50,
    border: int = 1500,
    n_frames: int = 600,
    saves: str = None
):
    print("Executing Boids (Bird Flock) Simulation")
    bird_flocks(n_birds, border, n_frames, saves=saves)


@app.command()
def game(name: str = "bullet-hell"):
    print(f"Initiating Game : {name}")
    start_game(name)


if __name__ == "__main__":
    app()
