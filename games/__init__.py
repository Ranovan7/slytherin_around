from games import bullet_hell, boids


def start_game(name: str = "bullet-hell"):
    if name == "bullet-hell":
        bullet_hell.main()
    elif name == "boids":
        boids.main()
    else:
        bullet_hell.main()
