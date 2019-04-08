from argparse import ArgumentParser


def calc_shared_key(A, B, p, g):
    a, b = None, None
    for x in range(1, p):
        if (g ** x) % p == A:
            a = x
        if (g ** x) % p == B:
            b = x
    return a, b


def main():
    parser = ArgumentParser()
    parser.add_argument("-A", "--A_public_key", required=True)
    parser.add_argument("-B", "--B_public_key", required=True)
    parser.add_argument("-g", "--base", required=True)
    parser.add_argument("-p", "--prime", required=True)
    args = parser.parse_args()

    A = int(args.alice)
    B = int(args.bob)
    g = int(args.base)
    p = int(args.prime)

    a, b = calc_shared_key(A, B, p, g)
    
    if a != None:
        print('A private key is {}'.format(a))
    else:
        print("Could not find the A's private key :(")

    if b != None:
        print('B private key is {}'.format(b))
    else:
        print("Could not find the B's private key :(")

    if a != None and b != None:
        k = (B ** a) % p
        print('A and B shared secret key is {}'.format(k))
    else:
        print('Could not find the shared key :(')
    pass


if __name__ == '__main__':
    main()
