def rainfall(measurements):
    idx = 0
    rain_total = 0
    days = 0

    while True:
        rain_day = measurements[idx]

        if rain_day == 99999:
            break        
        elif rain_day > 0:
            rain_total += rain_day
            days += 1

        idx += 1

    if days == 0:
        return 0
    
    return rain_total / days