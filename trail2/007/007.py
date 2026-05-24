secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class Meeting:
    def __init__(self, s_code, m_point, time):
        self.s = s_code
        self.m = m_point
        self.t = time

meeting = Meeting(secret_code, meeting_point, time)
print(f"secret code : {meeting.s}")
print(f"meeting point : {meeting.m}")
print(f"time : {meeting.t}")