def check_reading(segment, pressure, temperature, flow_rate):
    """Compare one reading to a segment's safe limits.

    Returns two things:
    - is_anomaly: True if any value is out of range
    - problems: a list of messages, one for each value out of range
    """
    problems = []

    if pressure < segment.pressure_min:
        problems.append("Pressure too low")
    elif pressure > segment.pressure_max:
        problems.append("Pressure too high")

    if temperature < segment.temperature_min:
        problems.append("Temperature too low")
    elif temperature > segment.temperature_max:
        problems.append("Temperature too high")

    if flow_rate < segment.flow_min:
        problems.append("Flow rate too low")
    elif flow_rate > segment.flow_max:
        problems.append("Flow rate too high")

    is_anomaly = len(problems) > 0
    return is_anomaly, problems