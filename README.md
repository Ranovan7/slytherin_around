# Python Implementation Examples (SlytherinAround)

## Installation

- `# mkdir .venv`

- `# pipenv install`

- `# pipenv shell`

## Projects/Implementations

### Boids Simulation

- Bird Flock (Boids) Simulation
- default command
</br>`# python main.py boids`
- options
</br>`# --n-birds <int>` number of birds
</br>`# --border <int>` how large the graph border will be
</br>`# --n-frames <int>` number of frames
</br>`# --saves <filename>` save result to ./boids/examples/<filename>.gif
- result example
<p align="center">
  <img width="600" height="600" src="https://github.com/ranovan7/slytherin_around/blob/master/boids/examples/100_birds.gif">
</p>

### Travelling Salesman Problem

- Edges Swap implementation for Travelling Salesman Problem (TSP)
- default command
    </br>`# python main.py tsp`
- options
    </br>`# --n-city <int>` number of cities generated
    </br>`# --border <int>` how large the graph border will be
    </br>`# --saves <filename>` save result to ./tsp/examples/<filename>.gif
- result example
    <p align="center">
      <img width="600" height="600" src="https://github.com/ranovan7/slytherin_around/blob/master/tsp/examples/30_cities.gif">
    </p>

### Bullet Hell

- Practice for Bullet Hell movements
- default command
    </br>`# python main.py bullets`
- options
    </br>`# --border <int>` how large the graph border will be
    </br>`# --n-frames <int>` number of frames
    </br>`# --saves <filename>` save result to ./bullets/examples/<filename>.gif
- result example
    <p align="center">
      <img width="600" height="600" src="https://github.com/ranovan7/slytherin_around/blob/master/bullets/examples/prototype.gif">
    </p>

### Games

- Python Game using pygame
- default command
    </br>`# python main.py game`
