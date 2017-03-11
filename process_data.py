import json
import argparse
import string

def get_parser():
    """Get parser for command line arguments."""
    parser = argparse.ArgumentParser(description="Twitter Parser")
    parser.add_argument("-q",
                        "--query",
                        dest="query",
                        help="Query/Filter",
                        default='-')
    parser.add_argument("-d",
                        "--data-dir",
                        dest="data_dir",
                        help="Output/Data Directory")
    return parser

def format_filename(fname):
    """Convert file name into a safe string.

    Arguments:
        fname -- the file name to convert
    Return:
        String -- converted file name
    """
    return ''.join(convert_valid(one_char) for one_char in fname)


def convert_valid(one_char):
    """Convert a character into '_' if invalid.

    Arguments:
        one_char -- the char to convert
    Return:
        Character -- converted char
    """
    valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)
    if one_char in valid_chars:
        return one_char
    else:
        return '_'

def get_data(data_dir, query):
  query_fname = format_filename(query)
  outfile = "%s/stream_%s.json" % (data_dir, query_fname)

  with open(outfile, 'r') as f:
    line = f.readline();
    tweet = json.loads(line);
    print(json.dumps(tweet, indent=4))

if __name__ == '__main__':
  parser = get_parser()
  args = parser.parse_args()

  get_data(args.data_dir, args.query)