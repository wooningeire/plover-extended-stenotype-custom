from plover.system.english_stenotype import *

KEYS = (
  '#', '_', '^-', '+-', '&-', '.-', 
  'S-', 'T-', 'K-', 'P-', 'W-', 'H-', 'R-',
  'A-', 'O-',
  '*',
  '-E', '-U',
  '-F', '-R', '-P', '-B', '-L', '-G', '-T', '-S', '-D', '-Z',
)

IMPLICIT_HYPHEN_KEYS = ('A-', 'O-', '-E', '-U', '*')

ORTHOGRAPHY_RULES.append(
  # panic +ed = panicked (*panicced)
  (r'^(.+)ic \^ (ed|ing|y|ier|iest|er)$', r'\1ick\2'),
)