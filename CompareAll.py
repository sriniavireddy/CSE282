import kmers

from BruteForceMatching import brute_force_mapping


def main():

    sequence_kmer_list = kmers.get_random_sequence_kmers(1000)

    design_kmer_list = kmers.get_design_kmers()

    brute_force_mapping_list = brute_force_mapping(sequence_kmer_list, design_kmer_list)

    print(len(brute_force_mapping_list))


if __name__ == "__main__":

    main()
