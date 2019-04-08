# Diffie-Hellman-Algorithm
The Diffie-Hellman algorithm is a key exchange protocol. This project implements the basic flow of the DH algorithm and the DH attack algorithm for small prime numbers p.

## 1.1 DH algorithm flow

### 1.1.1 Overview of the DH Algorithm Process

DH is an acronym for Diffie-Hellman, a key exchange algorithm proposed by Whitefield and Martin Hellman in 1976 . The flow of the DH algorithm is specifically described by the net red characters Alice and Bob in cryptography.

Suppose Alice needs to negotiate a secret key with Bob. The secret key is essentially a sequence of bits, which is a large number from a computational point of view.

(1)   Alice shares a prime p with Bob and the primitive root g of the prime. These two numbers can be sent from one party to the other without encryption. It is not important to send to whom, as long as both parties know that p is known. And g can be.

(2)   Alice produces a private random number A that satisfies 1<= A <= p-1 and then calculates g^A mod p = Ya Will result Ya. It is sent to Bob through the public network; at the same time, Bob also generates a private random number B, which satisfies 1<= B <= p-1, and calculates g^B mod p = Yb Will result Yb Send to Alice via the public network.

(3)   The information that Alice knows is p, g, A, Ya, where the number A is Alice is private; likewise, Bob knows that the information is p, g, B, Yb, where the number B is private to Bob. Alice through calculation Ka=(Yb)^A mod p and get the secret key Ka , Bob through calculation Kb=(Ya)^B mod p and get the secret key Kb At this time, it can be proved that it must meet Ka = Kb . Therefore, after the two parties negotiated, they obtained the same secret key and achieved the purpose of secret key negotiation.

### 1.1.2 DH algorithm flow code implementation
see `DH.py`

### 1.1.3 DH algorithm running test

Run the executable command format:

`DH.exe -g <base> -p <prime>`

-g: the original root

-p: shared prime number

## 1.2 DH attack system

### 1.2.1 DH attack system flow

The DH algorithm does not have identity verification when transmitting the primitive root g and the prime number p, and thus has the opportunity to be implemented by a man-in-the-middle attack to replace the data transmitted by both parties. The basic flow of cracking the private key of both parties in the DH algorithm is elaborated. Specifically, an example is given. Suppose a binary group (g, p) = (7, 15), the middleman gets the public key of both parties, A is 13 and B is 4.

Formula based on public key g^A mod p = Ya , traverse the value of A one by one, as follows:

7^A mod 15 calculation process:

7^1 mod 15 = 7

7^ 2 mod 15 = 4

7^ 3 mod 15 = 13

7^ 4 mod 15 = 1

7^ 5 mod 15 = 7

7^ 6 mod 15 = 4

7^ 7 mod 15 = 13

7^ 8 mod 15 = 1

.......

Through the above example, we can find that there are 4 kinds of results of 7^A mod 15 , and it is a cyclical cycle. If the middleman gets A or B, just choose one between [1, p-1] to satisfy 7^A mod 15 = 13 . You can get the shared secret key.

### 1.2.2 DH attack system code implementation
see `DHAttack.py`

### 1.2.3 DH attack system running test

Run the executable command format:

`DHAttack.exe -A <A_public_key> -B <B_public_key> -g <base> -p <prime>`

-A: A public key of A

-B:B's public key

-g: the original root

-p: shared prime number

