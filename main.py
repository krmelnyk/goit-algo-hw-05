# main.py

from benchmark import find_fastest_algorithms, run_benchmarks


def load_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def print_results(results):
    print("\nBenchmark results (average seconds per run):\n")

    for algo, data in results.items():
        print(f"{algo}:")
        for key, value in data.items():
            print(f"  {key}: {value:.6f}")
        print()


def print_fastest_algorithms(results):
    fastest = find_fastest_algorithms(results)

    print("Fastest algorithms:\n")
    for scenario, algorithm_name in fastest.items():
        print(f"  {scenario}: {algorithm_name}")


if __name__ == "__main__":
    text1 = load_text("стаття 1.txt")
    text2 = load_text("стаття 2.txt")

    pattern_exists = "алгоритм"
    pattern_missing = "superoptimizedquantumsearch"

    results = run_benchmarks(
        text1,
        text2,
        pattern_exists,
        pattern_missing,
    )

    print_results(results)
    print_fastest_algorithms(results)
