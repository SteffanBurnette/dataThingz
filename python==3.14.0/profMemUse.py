"""
This will be a basic script that profiles memory usage
"""
import tracemalloc

def create_list(n):
    return [i for i in range(n)]

def main():
    tracemalloc.start()

    x = create_list(1000)

    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics("lineno")

    print("[Top 10]")
    for stat in top_stats[:10]:
        print(stat)
    
    tracemalloc.stop()

main()