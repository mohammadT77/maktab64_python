def range(start, end: int = None, step=1):
    if end is None:
        start, end = 0, start

    assert step != 0, "Step cannot be 0 (inf loop)"
    i = start
    while i < end:
        yield i
        i += step
