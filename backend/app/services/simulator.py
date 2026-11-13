import random

def normal_value(low, high):
    """A value near the middle of the safe range, with a small random wobble."""
    middle = (low + high) / 2
    spread = (high - low) / 2
    value = random.gauss(middle, spread * 0.25)
    # Keep normal readings inside the safe range, so only real faults get flagged
    return max(low, min(high, value))

def faulty_value(low, high):
    """A value pushed just outside the safe range, either below or above it."""
    width = high - low
    overshoot = random.uniform(0.1, 0.3) * width
    if random.random() < 0.5:
        return low - overshoot
    return high + overshoot

def generate_reading(segment, fault_chance=0.05):
    """Make up one sensor reading for a segment: (pressure, temperature, flow_rate)."""
    pressure = normal_value(segment.pressure_min, segment.pressure_max)
    temperature = normal_value(segment.temperature_min, segment.temperature_max)
    flow_rate = normal_value(segment.flow_min, segment.flow_max)

    # Now and then, break exactly one of the three values
    if random.random() < fault_chance:
        fault = random.choice(["pressure", "temperature", "flow"])
        if fault == "pressure":
            pressure = faulty_value(segment.pressure_min, segment.pressure_max)
        elif fault == "temperature":
            temperature = faulty_value(segment.temperature_min, segment.temperature_max)
        else:
            flow_rate = faulty_value(segment.flow_min, segment.flow_max)

    return round(pressure, 2), round(temperature, 2), round(flow_rate, 2)