import time
import itertools

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
