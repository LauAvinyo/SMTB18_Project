charge = {
    'positive' : set(('R','H', 'K')),
    'negative' : set(('D', 'E')),
    'neutral'  : set(('A', 'N', 'C', 'Q', 'G', 'I', 'L', 'M', 
                     'F', 'P', 'S', 'T', 'W', 'Y', 'U'))
    }

polarity = {
    'polar'  : set(('R', 'N', 'D', 'C', 'Q', 'E', 
                   'G', 'H', 'K', 'S', 'T', 'Y')),
    'apolar' : set(('A', 'I', 'L', 'M',
                  'F', 'F', 'W', 'V'))
}

polarityVolume = {
    'special'      : set('C',),
    'neutralSmall' : set(('A', 'G', 'P', 'S', 'T')),
    'polarSmall'   : set(('N', 'D', 'Q', 'E')),
    'polarLarge'   : set(('R', 'H', 'K')),
    'apolarSmall'  : set(('I', 'L', 'M', 'V')),
    'apolarLarge'  : set(('F', 'W', 'Y'))
}