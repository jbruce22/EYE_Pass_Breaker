import time
import itertools

class brute_force:
    def __init__(self, password, password_length):
        self.password = password
        self.password_length = password_length

    def execute(self):
        start_time = time.time()
        print(f"Brute-forcing password...\nStarting number hack...")
        if self.pin_breaker(self.password, self.password_length) == None:
            print(f"Number hack failed.\nStarting letter hack...")
            if self.let_breaker(self.password, self.password_length) == None:
                print(f"Letter hack failed.\nStarting letter+number hack...")
                if self.letnum_breaker(self.password, self.password_length) == None:
                    print(f"Letter+Number hack failed.\nStarting string hack...")
                    if self.string_breaker(self.password, self.password_length) == None:
                        print("String hack failed. Password not found.")
        end_time = time.time()
        print(f"Brute-force completed in {end_time - start_time:.4f} seconds.")
        return end_time - start_time
    
    def pin_breaker(self, password, length):
        for i in range(0, 10**length):
            attempt = str(i).zfill(length)
            print(f"Trying: {attempt}", end='\r')
            if attempt == password:  # Compare as strings
                print(f"Password found: {attempt}")
                return attempt
        print("\nPassword not found.")
        return None
    
    def let_breaker(self, password, length):
        chars = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
        for attempt_tuple in itertools.product(chars, repeat=length):
            attempt = ''.join(attempt_tuple)
            print(f"Trying: {attempt}", end='\r')
            if attempt == password:
                print(f"\nPassword found: {attempt}")
                return attempt
        print("\nPassword not found.")
        return None
        
    def letnum_breaker(self, password, length):
        chars = [chr(i) for i in range(48, 58)] + [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
        for attempt_tuple in itertools.product(chars, repeat=length):
            attempt = ''.join(attempt_tuple)
            print(f"Trying: {attempt}", end='\r')
            if attempt == password:
                print(f"\nPassword found: {attempt}")
                return attempt
        print("\nPassword not found.")
        return None
    
    def string_breaker(self, password, length):
        chars = [chr(i) for i in range(33, 127)]  # Printable ASCII
        for attempt_tuple in itertools.product(chars, repeat=length):
            attempt = ''.join(attempt_tuple)
            print(f"Trying: {attempt}", end='\r')
            if attempt == password:
                print(f"\nPassword found: {attempt}")
                return attempt
        print("\nPassword not found.")
        return None
