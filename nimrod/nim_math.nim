import nimpy
import times, strutils

proc strstr(haystack, needle: cstring): cstring {.importc, header: "<string.h>".}

proc contains(haystack, needle: string): bool = strstr(cstring(haystack), cstring(needle)) != nil

proc add(a: int, b: int): int {.exportpy.} =
    return a + b

proc seq_int(): seq[int] {.exportpy.} =
    return @[]

proc looper(n: int): seq[int] {.exportpy.} =
    var result: seq[int] = @[]

    for i in 1..n:
        result.add(i*2)

    return result[^10..^1]

proc looper_str(text: string, subtext: string, n_iter: int): void {.exportpy.} =
    let time = cpuTime()
    for i in 0..n_iter:
        discard subtext in text
    echo "Time taken: ", cpuTime() - time
