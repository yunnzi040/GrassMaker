user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class Program:
    def __init__(self, id="codetree", level=10):
        self.id = id
        self.level = level

program1 = Program()
print(f"user {program1.id} lv {program1.level}")

program2 = Program(user2_id, user2_level)
print(f"user {program2.id} lv {program2.level}")