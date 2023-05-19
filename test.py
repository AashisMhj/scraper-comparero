import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', help='output file')
    args = parser.parse_args()
    return args

args = parse_args()
if args.output:
    # The output argument was provided
    output_file = args.output
    print('yes')
    # Perform the necessary actions with the output file
else:
    # The output argument was not provided
    # Handle the case when the argument is missing
    print('no')
