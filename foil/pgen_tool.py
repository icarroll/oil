#!/usr/bin/env python3
"""
pgen_tool.py
"""

import sys

from foil.pgen2 import pgen


def main(argv):
  try:
    grammar_path = argv[1]
  except IndexError:
    f = sys.stdin
  else:
    f= open(grammar_path)

  p = pgen.PgenParser(f)
  t, start_symbol = p.parse()
  print(t)
  print(start_symbol)

  # TODO: Now interpret the grammar somehow.


if __name__ == '__main__':
  try:
    main(sys.argv)
  except RuntimeError as e:
    print('FATAL: %s' % e, file=sys.stderr)
    sys.exit(1)
