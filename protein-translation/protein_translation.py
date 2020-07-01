import re

def proteins(value):

    uncoding = {
    'Methionine':['AUG'],
    'Phenylalanine':['UUU','UUC'],
    'Leucine':['UUA','UUG'],
    'Serine':['UCU','UCC','UCA','UCG'],
    'Tyrosine':['UAU','UAC'],
    'Cysteine':['UGU','UGC'],
    'Tryptophan':['UGG'],
    'STOP':['UAA','UAG','UGA'],
    }

    def chopper():
        '''
        Cuts RNA into chunks, and stops at the STOP codon.
        '''
        chunks = re.findall('.{3}', value)
        valids = []
        for i in chunks:
            if i not in uncoding['STOP']:
                valids.append(i)
            else:
                break
        return valids

    chunks_to_translate = chopper()
    translated = []

    def translator():
        '''
        Translates current codon into proteins:
        '''
        for chunk in chunks_to_translate:
            for protein, codon in uncoding.items():
                if chunk in codon:
                    translated.append(protein)

    translator()

    return translated
