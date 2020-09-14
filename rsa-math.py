import sys
import os
import random 

banner = """                                                   
     _____ _____ _____    _____ _____ _____ _____
    | __  |   __|  _  |  |     |  _  |_   _|  |  |
    |    -|__   |     |  | | | |     | | | |     |
    |__|__|_____|__|__|  |_|_|_|__|__| |_| |__|__|

       Script that aim teach how RSA math works
"""

sys.setrecursionlimit(10000)

print_red       = lambda *args, **kwargs : print("\u001b[31;1m", *args, "\u001b[0m", **kwargs)
print_green     = lambda *args, **kwargs : print("\u001b[32;1m", *args, "\u001b[0m", **kwargs)
print_yellow    = lambda *args, **kwargs : print("\u001b[33;1m", *args, "\u001b[0m", **kwargs)
print_blue      = lambda *args, **kwargs : print("\u001b[34;1m", *args, "\u001b[0m", **kwargs)
print_magenta   = lambda *args, **kwargs : print("\u001b[35;1m", *args, "\u001b[0m", **kwargs)
print_cyan      = lambda *args, **kwargs : print("\u001b[36;1m", *args, "\u001b[0m", **kwargs)

class Helper:
    @staticmethod
    def print_banner():
        print_green(banner)

    @staticmethod
    def clear():
        if os.name == "nt" : os.system("cls")
        else: os.system("clear")

    @classmethod
    def go_on(cls):
        print_yellow("\nContinue...", end="")
        input()
        cls.clear()
        print("", end="\n\n")

class Algorithms:

    @classmethod
    def gcd(cls, a, b):
        """ Greatest common divisor """
        if b == 0:
            return a
        return cls.gcd(b, a % b)

    @staticmethod
    def get_prime_list(n = 100):
        prime_list = []
        for i in range(2, n):
            for j in range (2, i):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
        return prime_list

    @staticmethod
    def get_coprime_numbers(integer):
        coprime_list = []
        for i in range(1, integer):
            if Algorithms.gcd(i, integer) == 1:
                coprime_list.append(i)
        return coprime_list

    @staticmethod
    def get_encryption_keys(n, phi):
        keys = []
        for i in range(2,phi):
            if Algorithms.gcd(n, i) == 1 and Algorithms.gcd(phi, i) == 1:
                keys.append(i)
        return keys

    @staticmethod
    def get_decryption_keys(e, phi, start = 1, finish=1000):
        keys = []
        for i in range (1000):
            for i in range(phi + start, phi + finish):
                if i * e % phi == 1:
                    keys.append(i)
            if len(keys) >= 5:
                break
            else:
                start += 1000
                finish += 1000
        return keys

    @staticmethod
    def encrypt_number(number, e, n):
        return number ** e % n

    @staticmethod
    def decrypt_number(number, d, n):
        return number ** d % n

    @classmethod
    def encrypt_string(cls, string, e, n):
        ascii_list = [ord(k) for k in string]
        return ascii_list, [cls.encrypt_number(k, e, n) for k in ascii_list]

    @classmethod
    def decrypt_string(cls, crypt_list, d, n):
        dec_list = [cls.decrypt_number(k, d, n) for k in crypt_list]
        return dec_list, "".join([chr(k) for k in dec_list])

class RsaMath:
    def __init__(self):
        self.p = ""
        self.q = ""
        self.n = ""
        self.phi = ""
        self.e = ""
        self.d = ""

    def print_information(self):
        information = f"""
        -----------
        p   : {self.p}
        q   : {self.q}
        n   : {self.n}
        phi : {self.phi}
        e   : {self.e}
        d   : {self.d}
        -----------
        """
        print_cyan(information)

    def set_p(self, prime_numbers):
        while True:
            try:
                print_blue("\n--- What is 'p' number going to be : ", end="")
                p = int(input())
                if p in prime_numbers:
                    self.p = p
                    break
                else:
                    print_red("!!! 'p' is not prime number!")
            except KeyboardInterrupt:
                sys.exit()
            except ValueError:
                print_red("!!! 'p' must be number!")

    def set_q(self, prime_numbers):
        while True:
            try:
                print_blue("\n--- What is 'q' number going to be : ", end="")
                q = int(input())
                if q in prime_numbers:
                    self.q = q
                    break
                else:
                    print_red("!!! 'p' is not prime number!")
            except KeyboardInterrupt:
                sys.exit()
            except ValueError:
                print_red("!!! 'q' must be number!")

    def set_n(self):
        if self.p and self.q:
            self.n = self.p * self.q
        else:
            print_red("!!! Define 'p' and 'q' first!")

    def set_phi(self):
        if self.n:
            self.phi = len(Algorithms.get_coprime_numbers(self.n))
        else:
            print_red("!!! Define 'n' first!")
    
    def set_e(self, key_list):
        while True:
            try:
                print_blue("\n--- What is 'e' number going to be : ", end="")
                e = int(input())
                if e in key_list:
                    self.e = e
                    break
                else:
                    print_red("!!! 'e' must be chosen from the list!")
            except KeyboardInterrupt:
                sys.exit()
            except ValueError:
                print_red("!!! 'e' must be number!")

    def set_d(self, key_list):
        while True:
            try:
                print_blue("\n--- What is 'd' number going to be : ", end="")
                d = int(input())
                if d in key_list:
                    self.d = d
                    break
                else:
                    print_red("!!! 'd' must be chosen from the list!")
            except KeyboardInterrupt:
                sys.exit()
            except ValueError:
                print_red("!!! 'd' must be number!")

    def number_example(self):
        while True:
            try:
                print_blue("\n--- Give a number to encrypt : ", end="")
                number = int(input())
                break
            except KeyboardInterrupt:
                sys.exit()
            except ValueError:
                print_red("!!! Number must be given!")
        print_green(f">>> Number is {number}")
        
        encrypted = Algorithms.encrypt_number(number, self.e, self.n)
        print_green(f">>> Encryption : {number} ^ {self.e} % {self.n} = {encrypted}")
        
        decrypted = Algorithms.decrypt_number(encrypted, self.d, self.n)
        print_green(f">>> Decryption : {encrypted} ^ {self.d} % {self.n} = {decrypted}")

        print_blue("Try again? (y/n) : ", end="")
        answer = input()
        if answer == "y":
            self.number_example()

    def string_example(self):
        print_blue("\n--- Give a string to encrypt : ", end="")
        value = input()

        ascii_list, enc_list = Algorithms.encrypt_string(value, self.e, self.n)
        dec_list, dec_string = Algorithms.decrypt_string(enc_list, self.d, self.n)

        print_green(f">>> String Value  : ", value)
        print_green(f">>> ASCII Values  : ", ascii_list)       
        print_green(f">>> Encryption    : ", enc_list)
        print_green(f">>> Encrypted Str : ", "".join([chr(k) for k in enc_list]))
        print_green(f">>> Decryption    : ", dec_list)
        print_green(f">>> Decrypted Str : ", dec_string)

        print_blue("Try again? (y/n) : ", end="")
        answer = input()
        if answer == "y":
            self.string_example()

if __name__ == "__main__":
    r = RsaMath()
    Helper.clear()

    #Banner
    Helper.print_banner()
    Helper.go_on()

    # Introduction
    print_green(">>> RSA encryption based on some math formulas such as mod.")
    print_green(">>> First of all, we must define the following variables:")
    r.print_information()
    print_green(">>> All variables will be selected step by step and will give information about how.")
    Helper.go_on()

    # p and q numbers
    print_green(">>> 'p' and 'q' are two prime number which can be random choosen.")
    print_green(">>> They can be any prime number.")
    print_green(">>> Here is a list which shows prime numbers less than 100:")

    prime_numbers = Algorithms.get_prime_list()
    print_magenta("\n",prime_numbers, end="\n\n")

    print_green(">>> Let's select 'p' and 'q' from the list above...")
    r.set_p(prime_numbers)
    r.set_q(prime_numbers)
    r.print_information()
    Helper.go_on()

    # n number
    print_green(">>> 'n' number is simply 'p' and 'q' multipilied together.")
    r.set_n()
    r.print_information()
    Helper.go_on()

    # phi number
    print_green(">>> Let's look at 'phi' number...")
    print_green(">>> 'phi' is the number of integers that are coprime to 'n'.")
    print_green(">>> If two integers are coprime, then they do not share a common divider, except 1.")
    print_green(">>> Here is the numbers coprime with 'n'")

    coprime_list = Algorithms.get_coprime_numbers(r.n)
    if len(coprime_list) > 16:
        print_magenta("\n", "[" + " , ".join([str(k) for k in coprime_list[:10]]) + " ... " + " , ".join([str(k) for k in coprime_list[-5:]]) + "]\n")
    else:
        print_magenta("\n", coprime_list, end="\n")
    print_magenta(f"Total : {len(coprime_list)}", end="\n\n")

    print_green(f">>> So, there are {len(coprime_list)} numbers that fits the formula and our 'phi' number is {len(coprime_list)}")
    print_green(">>> The basic way to find 'phi' number is : (p-1) * (q-1)")
    r.set_phi()
    r.print_information()
    Helper.go_on()

    # e number (Encryption key)
    print_green(">>> 'e' is an encryption number.")
    print_green(">>> We need to find a number that is less than 'phi' (2 < e < phi), and coprime to BOTH 'n' and 'phi'.")
    print_green(">>> Here is the possible 20 POSSIBLE encryption numbers:")

    encryption_keys = Algorithms.get_encryption_keys(r.n, r.phi)
    print_magenta("\n", random.choices(encryption_keys, k = 20), end="\n\n")
    
    print_green(">>> As you can see, there is more than one encryption number option.")
    print_green(">>> Let's select 'e' from the list above...")
    r.set_e(encryption_keys)
    r.print_information()
    Helper.go_on()

    # d number (Decryption key)
    print_green(">>> The last thing we need to found is decryption number 'd'.")
    print_green(">>> 'd' is a number which follow the following rule : ( d * e % phi == 1 )")
    print_green(">>> As encryption number, there is more than one decrpytion number options.")
    print_green(">>> Here is the SOME POSSIBLE decryption numbers (There is countless of them):")

    decryption_keys = Algorithms.get_decryption_keys(r.e, r.phi)
    print_magenta("\n", decryption_keys, end="\n\n")

    print_green(">>> Let's select 'd' number from list above...")
    r.set_d(decryption_keys)
    r.print_information()
    Helper.go_on()

    # Public & Private Key
    print_green(">>> Great! Now we have public and private keys!")
    r.print_information()
    print_magenta(f"\n >>> Public Key  : {(r.e, r.n)}")
    print_magenta(f">>> Private Key : {(r.d, r.n)}\n")

    print_green(f">>> To encrypt data, use following equation :", end="")
    print_red("data ^ e % n = encrypted-data")
    print_green(f">>> To decrypt data, use following equation :", end="")
    print_red("encrypted-data ^ d % n = data\n")
    Helper.go_on()

    # Number Examples
    print_green(">>> EXAMPLES:")
    r.print_information()
    print_green(">>> Let's encrypt and decrypyt some numbers.")
    print_green(f">>> NOTE : Given number must be less than 'n' ({r.n}) number.")
    r.number_example()
    Helper.go_on()

    # String Examples
    print_green(">>> STRING ENCRYPTION", end="\n\n")
    print_green(">>> Strings are converted to ASCII first.")
    print_green(">>> Then ASCII number list will be encrypt and decrypt.")
    print_green("\n >>> EXAMPLES :")
    print_green(f">>> NOTE : 'n' number is ({r.n}), so bigger ASCII numbers than 'n' cannot convert properly.")
    r.string_example()
    Helper.go_on()

    # Bye
    print_magenta(">>> That was all.")
    print_magenta(">>> Bye.", end = "\n")
