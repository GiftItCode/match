def gen_timeslots(gran, start_hour, end_hour):
    """
    :param gran: granularity of timeslots in minutes.
    :param start_hour: starting hour
    :param end_hour: ending hour
    """
    slots = []
    for day in range(1,8):
        for slot in range(int(start_hour*60/gran),int(end_hour*60/gran)):
            hb = int(slot*gran/60)
            mb = int(slot*gran%60)
            he = int((slot+1)*gran/60)
            me = int((slot+1)*gran%60)
            slots.append((f"'{hb:02}:{mb:02}'",f"'{he:02}:{me:02}'",day))
    return slots

if __name__ == '__main__':
    slots = gen_timeslots(15, 6, 23)
    print("""insert into timeslot (begin_time, end_time, day_of_week)
values""")
    for s in slots:
        print(f'({s[0]},{s[1]},{s[2]}),')
