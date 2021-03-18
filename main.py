import typer
from tsp import travelling_salesman

app = typer.Typer()


@app.command()
def qwerty():
    print("Testing Commands")


@app.command()
def tsp(n_city: int = 30, border: int = 1000, saves: str = None):
    print("Executing Travelling Salesman Example")
    travelling_salesman(n_city, border, saves=saves)


if __name__ == "__main__":
    app()
