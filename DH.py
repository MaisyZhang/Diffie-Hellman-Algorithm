from argparse import ArgumentParser


def calc_key(key, g, p):
    return (g ** key) % p


def main():
    parser = ArgumentParser()
    parser.add_argument("-A", "--A_private_key", required=True)
    parser.add_argument("-B", "--B_private_key", required=True)
    parser.add_argument("-g", "--base", required=True)
    parser.add_argument("-p", "--prime", required=True)
    args = parser.parse_args()

    A = int(args.A_private_key)
    B = int(args.B_private_key)
    g = int(args.base)
    p = int(args.prime)

    A_public_key = calc_key(A, g, p)
    B_public_key = calc_key(B, g, p)

    A_shared_key = calc_key(A, B_public_key, p)
    B_shared_key = calc_key(B, A_public_key, p)

    print('Shared secret: {}'.format(A_shared_key))
    pass


if __name__ == '__main__':
    main()
