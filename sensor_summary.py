readings = [72.1, 74.0, 120.5, 73.2]
threshold = 100.0

def summarize(readings: list[float], threshold: float) -> dict:
    count = len(readings)

    if count == 0:
        return {
            "sample_count": 0,
            "minimum": None,
            "maximum": None,
            "average": None,
            "above_threshold": 0,
        }

    minimum = min(readings)
    maximum = max(readings)
    average = sum(readings) / count
    above_threshold = sum(1 for value in readings if value > threshold)

    return {
        "sample_count": count,
        "minimum": minimum,
        "maximum": maximum,
        "average": average,
        "above_threshold": above_threshold,
    }

if __name__ == "__main__":
    summary = summarize(readings, threshold)

    print(f"Samples: {summary['sample_count']}")
    print(f"Minimum: {summary['minimum']}")
    print(f"Maximum: {summary['maximum']}")
    print(f"Average: {summary['average']:.2f}")
    print(f"Alerts: {summary['above_threshold']}")