import time
import itertools

class startup:
    def __init__(self):
        pass

    def run(self):
        print("Brute startup running...")
        user = user_input()
        user.get_input()
        brute = brute_force(user.password, user.password_length, user.password_type)
        return brute.execute()

class user_input:
    def __init__(self):
        self.password = ""
        self.password_length = 0
        self.password_type = 0

    def get_input(self):
        self.password = self.get_password()
        self.password_length = len(self.password)
        self.password_type = self.determine_password_type(self.password)

    def get_password(self):
        input_password = input("Enter the password to brute-force: ")
        return input_password

    def determine_password_type(self, password):
        if password.isdigit():
            return 1  # Numeric
        else:
            return 2  # String

class brute_force:
    def __init__(self, password, password_length, password_type):
        self.password = password
        self.password_length = password_length
        self.password_type = password_type

    def execute(self):
        print(f"Brute-forcing password...")
        if self.password_type == 1:
            print(f"Brute-forcing numeric password of length {self.password_length}...")
            return self.pin_breaker(self.password, self.password_length)
        elif self.password_type == 2:
            print(f"Brute-forcing string password of length {self.password_length}...")
            return self.string_breaker(self.password, self.password_length)

    def pin_breaker(self, password, length):
        start_time = time.time()
        for i in range(0, 10**length):
            attempt = str(i).zfill(length)
            print(f"Trying: {attempt}", end='\r')
            if attempt == password:  # Compare as strings
                print(f"Password found: {attempt}")
                end_time = time.time()
                print(f"Brute-force completed in {end_time - start_time:.4f} seconds.")
                return end_time - start_time
        print("\nPassword not found.")
        return None
    
    def string_breaker(self, password, length):
        start_time = time.time()
        chars = [chr(i) for i in range(33, 127)]  # Printable ASCII
        for attempt_tuple in itertools.product(chars, repeat=length):
            attempt = ''.join(attempt_tuple)
            print(f"Trying: {attempt}", end='\r')
            if attempt == password:
                print(f"\nPassword found: {attempt}")
                end_time = time.time()
                print(f"Brute-force completed in {end_time - start_time:.4f} seconds.")
                return end_time - start_time
        print("\nPassword not found.")
        return None

start = startup()
start.run()
