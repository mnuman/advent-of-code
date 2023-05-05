import time

import day15a

if __name__ == "__main__":
    # runs under 50 seconds
    s = time.time()
    print(s)
    r = day15a.Recitation()
    r.start((10, 16, 6, 0, 1, 17))
    print(r.iterate(30000000))
    print(f"Elapsed time = {time.time() - s}")
