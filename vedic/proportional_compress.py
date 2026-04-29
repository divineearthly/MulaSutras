def proportional_compress(data: str, tolerance: float = 0.1) -> tuple:
    """
    Find substrings that are approximately proportional (ratio near an integer).
    Works well for numbers that are scaled versions, e.g., 100,200,300...
    Not a full implementation, but demonstrates the Vedic principle.
    """
    # For data consisting of comma-separated numbers, we try to find a base ratio.
    # Simplified: look for pairs where the ratio is within tolerance of an integer.
    try:
        nums = [float(x) for x in data.split(',') if x.strip()]
    except ValueError:
        return data, {}  # not numeric
    if len(nums) < 4:
        return data, {}
    # Compute average ratio between consecutive elements
    ratios = [nums[i+1]/nums[i] for i in range(len(nums)-1) if nums[i] != 0]
    if not ratios:
        return data, {}
    mean_ratio = sum(ratios) / len(ratios)
    # If all ratios are close to the same integer, we can compress.
    int_ratio = round(mean_ratio)
    if all(abs(r - int_ratio) < tolerance for r in ratios):
        # Compress by storing first value and ratio
        compressed = f"{nums[0]}:x{int_ratio}"
        dictionary = {"pattern": f"proportional with ratio {int_ratio}"}
        return compressed, dictionary
    return data, {}
