import random

class DH():
    def __init__(self, public_key1, public_key2, private_key):
        self.public_key1 = public_key1
        self.public_key2 = public_key2
        self.private_key = private_key
        self.full_key = None

    def generate_partial_key(self):
        partial_key = pow(self.public_key1, self.private_key) % self.public_key2
        return partial_key

    def generate_full_key(self, partial_key_r):
        full_key = pow(partial_key_r, self.private_key) % self.public_key2
        self.full_key = full_key
        return full_key



def make_primes(n):
    primes = [2]
    nextPrime = 3
    while nextPrime < n:
        isPrime = True
        i = 0
        squareRoot = int(nextPrime ** 0.5)
        while primes[i] <= squareRoot:
            if nextPrime % primes[i] == 0:
                isPrime = False
            i += 1
        if isPrime:
            primes.append(nextPrime)

        nextPrime += 1
    return primes

def recieve_prime():

    while True:
        num = random.randint(2, 1000)
        if num in make_primes(1000):
            return num


public_alice = recieve_prime()
private_alice = recieve_prime()
public_bob = recieve_prime()
private_bob = recieve_prime()
private_eva = recieve_prime()

alice = DH(public_alice, public_bob, private_alice)
bob = DH(public_alice, public_bob, private_bob)
eva = DH(public_alice, public_bob, private_eva)


partial_alice = alice.generate_partial_key()
partial_bob = bob.generate_partial_key()
partial_eva = eva.generate_partial_key()

full_alice = alice.generate_full_key(partial_bob)
full_bob = bob.generate_full_key(partial_alice)
full_eva = eva.generate_full_key(partial_alice)


if __name__ == "__main__":
    print("Alice: ")
    print("Public: " + str(public_alice))
    print('Private: ' + str(private_alice))
    print('Partial: ' + str(partial_alice) )
    print('Full: ' + str(full_alice) + '\n')

    print('Bob: ')
    print("Public: " + str(public_bob))
    print('Private: ' + str(private_bob))
    print('Partial: ' + str(partial_bob))
    print('Full: ' + str(full_bob) + '\n')

    print('Eva: ')
    print('Private: ' + str(private_eva))
    print('Partial: ' + str(partial_eva))
    print('Full: ' + str(full_eva) + '\n')