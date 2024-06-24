def longest_time(h, m, s):
    hours = h * 3600
    minutes = m * 60
    seconds = s
    if hours > minutes and hours > seconds:
        return h
    elif minutes > hours and minutes > seconds:
        return m
    else:
        return s


print(longest_time(1, 59, 3598))
