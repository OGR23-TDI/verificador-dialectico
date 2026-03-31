import argparse
import json
import os
import sys

class CLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Dialectical Verifier CLI')
        self.parser.add_argument('-o', '--output', type=str, choices=['json', 'markdown', 'text'], 
                                 help='Output format (json, markdown, or text)')
        self.parser.add_argument('-e', '--export', type=str, 
                                 help='File path to export results')
        self.parser.add_argument('-v', '--verbose', action='store_true', 
                                 help='Enable verbose output')
        self.parser.add_argument('--version', action='version', version='%(prog)s 1.0')
        self.args = self.parser.parse_args()

    def run(self):
        self.check_args()
        # Implementation of CLI functionalities
        if self.args.verbose:
            print('Verbose mode enabled')
        print('Running CLI with output format:', self.args.output)
        #... Additional CLI logic here

    def check_args(self):
        if not self.args.output:
            print('Error: Output format is required.')
            self.parser.print_help()
            sys.exit(1)
        if self.args.export and not os.path.exists(os.path.dirname(self.args.export)):
            print('Error: Export directory does not exist.')
            sys.exit(1)

if __name__ == '__main__':
    cli = CLI()
    cli.run()