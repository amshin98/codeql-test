def rainfall(measurements):
    rain_total = 0
    days = 0

    for idx in range(len(measurements)):
        rain_day = measurements[idx]

        if rain_day == 99999:
            break
        elif rain_day > 0:
            rain_total += rain_day
            days += 1

    if days == 0:
        return 0
    
    return rain_total / days