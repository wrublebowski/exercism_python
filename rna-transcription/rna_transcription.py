def to_rna(dna_strand):

    transcript = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}

    rna_list = [transcript[i] for i in dna_strand]
    rna = ''
    for i in rna_list:
        rna += i

    return rna
