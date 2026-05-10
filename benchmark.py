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


def find_fastest_algorithms(results):
    scenarios = {
        "Стаття 1, існуючий підрядок": "text1_exists",
        "Стаття 1, вигаданий підрядок": "text1_missing",
        "Стаття 2, існуючий підрядок": "text2_exists",
        "Стаття 2, вигаданий підрядок": "text2_missing",
    }

    fastest = {}

    for scenario, key in scenarios.items():
        fastest[scenario] = min(
            results,
            key=lambda algorithm_name: results[algorithm_name][key],
        )

    article1_average = {
        algorithm_name: (
            data["text1_exists"] + data["text1_missing"]
        ) / 2
        for algorithm_name, data in results.items()
    }
    article2_average = {
        algorithm_name: (
            data["text2_exists"] + data["text2_missing"]
        ) / 2
        for algorithm_name, data in results.items()
    }
    overall_average = {
        algorithm_name: sum(data.values()) / len(data)
        for algorithm_name, data in results.items()
    }

    fastest["Стаття 1, середній результат"] = min(
        article1_average,
        key=article1_average.get,
    )
    fastest["Стаття 2, середній результат"] = min(
        article2_average,
        key=article2_average.get,
    )
    fastest["Загалом"] = min(overall_average, key=overall_average.get)

    return fastest
