# benchmark.py

import timeit
from search_algorithms import (
    kmp_search,
    rabin_karp_search,
    boyer_moore_search,
)


def benchmark_algorithm(algorithm, text, pattern, runs=100):
    timer = timeit.Timer(lambda: algorithm(text, pattern))
    return timer.timeit(number=runs) / runs


def run_benchmarks(text1, text2, pattern_exists, pattern_missing):
    algorithms = {
        "KMP": kmp_search,
        "Rabin-Karp": rabin_karp_search,
        "Boyer-Moore": boyer_moore_search,
    }

    results = {}

    for name, algo in algorithms.items():
        results[name] = {
            "text1_exists": benchmark_algorithm(algo, text1, pattern_exists),
            "text1_missing": benchmark_algorithm(algo, text1, pattern_missing),
            "text2_exists": benchmark_algorithm(algo, text2, pattern_exists),
            "text2_missing": benchmark_algorithm(algo, text2, pattern_missing),
        }

    return results