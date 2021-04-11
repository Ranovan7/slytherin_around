import nimpy

proc add(a: int, b: int): int {.exportpy.} =
    return a + b

proc seq_int(): seq[int] {.exportpy.} =
    return @[]

proc looper(n: int): seq[int] {.exportpy.} =
    var result: seq[int] = @[]

    for i in 1..n:
        result.add(i*2)

    return result[^10..^1]
