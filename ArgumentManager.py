import argparse


def generate_argument_parser(argv):
    parser = argparse.ArgumentParser(description='Generate test reports')
    parser.add_argument('-s', '--single-file', help='analyze single file', action='store_true')
    parser.add_argument('-r', '--recurrent',
                        help='resolve included files recurrently, only #include "" is recognised',
                        action='store_true')
    return parser.parse_args(argv)
