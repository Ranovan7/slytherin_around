import math
import random
import nimpy
import sugar

type Vector3 = ref object of RootObj
    x: float
    y: float
    z: float

method show(self: Vector3): void =
    echo "(", self.x, ",", self.y, ",", self.z, ")"

method add(self: Vector3, vec: Vector3): void =
    self.x += vec.x
    self.y += vec.y
    self.z += vec.z

method subtract(self: Vector3, vec: Vector3): void =
    self.x -= vec.x
    self.y -= vec.y
    self.z -= vec.z

method divide(self: Vector3, vec: Vector3): void =
    self.x /= vec.x
    self.y /= vec.y
    self.z /= vec.z

method set_mag(self: Vector3, new_mag: float): void =
    let mag = sqrt(self.x*self.x + self.y*self.y + self.z*self.z)
    if mag == 0.0:
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
    else:
        self.x = self.x * new_mag / mag
        self.y = self.y * new_mag / mag
        self.z = self.z * new_mag / mag

method euclidean_distance(self: Vector3, target: Vector3): float =
    var x = target.x - self.x
    var y = target.y - self.y
    var z = target.z - self.z
    return math.sqrt(x*x + y*y + z*z)

method clip(self: Vector3, a_min: float, a_max: float): void =
    self.x = min(a_max, max(a_min, self.x))
    self.y = min(a_max, max(a_min, self.y))
    self.z = min(a_max, max(a_min, self.z))

proc newVector3(x: float = 0.0, y: float = 0.0, z: float = 0.0): Vector3 =
    Vector3(x: x, y: y, z: z)

type Bird = ref object of RootObj
    id: int
    position: Vector3
    velocity: Vector3
    acceleration: Vector3
    alignment_rad: float
    cohesion_rad: float
    separation_rad: float
    min_speed: float
    max_speed: float
    acc_limit: float

method set_attr(self: Bird): void =
    self.alignment_rad = 100.0
    self.cohesion_rad = 150.0
    self.separation_rad = 100.0
    self.min_speed = 10.0
    self.max_speed = 15.0
    self.acc_limit = 3.0

method info(self: Bird): void =
    # if self.id == 20:
    # if true:
    #     echo "Bird ", self.id, " (", self.position.x, ",", self.position.y, ")"
    discard

method get_position(self: Bird, dim: string): seq[float] =
    if dim == "2d":
        return @[self.position.x, self.position.y]
    else:
        return @[self.position.x, self.position.y, self.position.z]

method wrap(self: Bird, width: float, height: float, depth: float): void =
    if self.position.x > width:
        self.position.x = 0.0
    elif self.position.x < 0.0:
        self.position.x = width

    if self.position.y > height:
        self.position.y = 0.0
    elif self.position.y < 0.0:
        self.position.y = height

    if self.position.z > depth:
        self.position.z = 0.0
    elif self.position.z < 0.0:
        self.position.z = depth

method border_evasion(self: Bird, width: float, height: float, depth: float): void =
    let offset: float = 50.0

    if self.position.x > width - offset:
        self.acceleration.x = -(self.acceleration.x.abs())
    elif self.position.x < 0.0 + offset:
        self.acceleration.x = self.acceleration.x.abs()

    if self.position.y > height - offset:
        self.acceleration.y = -(self.acceleration.y.abs())
    elif self.position.y < 0.0 + offset:
        self.acceleration.y = self.acceleration.y.abs()

    if self.position.z > depth - offset:
        self.acceleration.z = -(self.acceleration.z.abs())
    elif self.position.z < 0.0 + offset:
        self.acceleration.z = self.acceleration.z.abs()

method reset_acceleration(self: Bird): void =
    self.acceleration = newVector3()

method add_force(self: Bird, force: Vector3): void =
    self.acceleration.add(force)

method update(self: Bird): void =
    self.velocity.add(self.acceleration)
    self.velocity.clip(a_min= -self.max_speed, a_max= self.max_speed)
    self.position.add(self.velocity)

method emergence(self: Bird, birds: seq[Bird]): void =
    var steer_align = newVector3()
    var steer_cohesion = newVector3()
    var steer_separation = newVector3()
    var count_align = 0
    var count_cohesion = 0
    var count_separation = 0

    for bird in birds:
        if bird == self:
            continue

        let distance = self.position.euclidean_distance(bird.position)
        if distance <= self.alignment_rad:
            count_align += 1
            steer_align.add(bird.velocity)

        if distance <= self.cohesion_rad:
            count_cohesion += 1
            steer_cohesion.add(bird.position)

        if distance <= self.separation_rad:
            count_separation += 1
            var diff = Vector3(x: self.position.x, y: self.position.y, z: self.position.z)
            diff.subtract(bird.position)
            diff.x /= distance
            diff.y /= distance
            diff.z /= distance
            steer_separation.add(diff)

    if count_align > 0:
        steer_align.x /= count_align.float
        steer_align.y /= count_align.float
        steer_align.z /= count_align.float
        steer_align.set_mag(self.min_speed)
        steer_align.subtract(self.velocity)

    if count_cohesion > 0:
        steer_cohesion.x /= count_cohesion.float
        steer_cohesion.y /= count_cohesion.float
        steer_cohesion.z /= count_cohesion.float
        steer_cohesion.subtract(self.position)
        steer_cohesion.set_mag(self.min_speed)
        steer_cohesion.subtract(self.velocity)

    if count_separation > 0:
        steer_separation.x /= count_separation.float
        steer_separation.y /= count_separation.float
        steer_separation.z /= count_separation.float
        steer_separation.set_mag(self.min_speed)
        steer_separation.subtract(self.velocity)

    steer_align.clip(a_min= -self.acc_limit, a_max=self.acc_limit)
    self.add_force(steer_align)

    steer_cohesion.clip(a_min= -self.acc_limit, a_max=self.acc_limit)
    self.add_force(steer_cohesion)

    steer_separation.clip(a_min= -self.acc_limit, a_max=self.acc_limit)
    self.add_force(steer_separation)

proc newBird(id: int, position: Vector3, velocity: Vector3): Bird =
    return Bird(
        id: id,
        position: position,
        velocity: velocity,
        acceleration: Vector3(x:0.0, y:0.0, z:0.0),
        alignment_rad: 100.0,
        cohesion_rad: 150.0,
        separation_rad: 100.0,
        min_speed: 10.0,
        max_speed: 15.0,
        acc_limit: 3.0
    )

type Flock = ref object of RootObj
    n_birds: int
    border: float
    birds: seq[Bird]

method update(self: Flock): void =
    for bird in self.birds:
        # bird.wrap(self.border, self.border, self.border)
        bird.reset_acceleration()
        bird.emergence(self.birds)
        bird.border_evasion(self.border, self.border, self.border)
        bird.update()

method get_frame(self: Flock, dim: string): seq[seq[float]] =
    var results: seq[seq[float]] = @[]
    for i, bird in self.birds:
        results.add(bird.get_position(dim))
    return results

method set_attr(self: Flock): void =
    for i, bird in self.birds:
        bird.set_attr()

method info(self: Flock): void =
    for i, bird in self.birds:
        bird.info()

proc simulation(
    n_birds: int,
    dim: string = "2d",
    border: int = 2000,
    n_frames: int = 700
): seq[seq[seq[float]]] {.exportpy.} =
    if dim != "2d" and dim != "3d":
        return @[]

    var frames: seq[seq[seq[float]]] = @[]
    var flock = Flock(
        n_birds: n_birds,
        border: border.float,
        birds: @[]
    )
    var z_pos = 1.0
    var z_vel = 0.0
    for i in 1..n_birds:
        if dim == "3d":
            z_pos = float(rand(1..border))
            z_vel = float(rand(-10..10))

        let pos = newVector3(
            float(rand(1..border)),
            float(rand(1..border)),
            z_pos
        )
        let vel = newVector3(
            float(rand(-10..10)),
            float(rand(-10..10)),
            z_vel
        )
        flock.birds.add(
            Bird(
                id: i,
                position: pos,
                velocity: vel
            )
        )

    for i in 1..n_frames:
        if i == 1:
            flock.set_attr()
        flock.update()
        flock.info()

        frames.add(flock.get_frame(dim))

    return frames
