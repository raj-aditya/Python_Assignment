class Time():
    def __init__(self, hr, min):
        self.hr = hr
        self.min = min

def addtime(time1,time2):
    total_hours = time1.hr + time1.hr
    total_mins = time2.min + time2.min
    extra_hours = total_hours // 60
    total_mins = total_mins % 60
    total_hours = total_hours + extra_hours
    print(f"Hour: {total_hours}  Min: {total_mins}")



time1 = Time(2,50)
time2 = Time(1, 20)

addtime(time1, time2)