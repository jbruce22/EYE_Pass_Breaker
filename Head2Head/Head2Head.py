import subprocess
import time
import os

class startup:
    def __init__(self):
        pass

    def run(self):
        print("Head2Head startup running...")
        user = user_input()
        user.get_input()
        
        head2head_dir = os.path.dirname(os.path.abspath(__file__))
        strat_path = os.path.join(head2head_dir, "Head_StratBrute.py")
        brute_path = os.path.join(head2head_dir, "Head_Brute.py")

        start_time = time.time()
        strat_proc = subprocess.run(["python", strat_path, user.password])
        strat_time = time.time() - start_time

        start_time = time.time()
        brute_proc = subprocess.run(["python", brute_path, user.password, str(user.determine_password_type(user.password))])
        brute_time = time.time() - start_time

        if strat_time < brute_time:
            print(f"StratBrute was faster by {brute_time - strat_time} seconds.")
            return [user.password, strat_time]
        elif brute_time < strat_time:
            print(f"Brute was faster by {strat_time - brute_time} seconds.")
            return [user.password, brute_time]
        else:
            print("Both methods took the same time!")
            return [user.password, strat_time]

    
class user_input:
    def __init__(self):
        self.password = ""
        self.password_length = 0
        self.password_type = 0

    def get_input(self):
        self.password = self.get_password()
        self.password_length = len(self.password)

    def get_password(self):
        input_password = input("Enter the password to brute-force: ")
        return input_password
    
    def determine_password_type(self, password):
        if password.isdigit():
            return 1  # Numeric
        else:
            return 2  # String
        
start = startup()
info = start.run()
if info[1] > 45:
    with open("H2H_" + str(info[0]) + ".txt", "w") as f:
        f.write(f"Password: {info[0]}\nTime Taken: {info[1]} seconds\n")
    print("Info written to file.")