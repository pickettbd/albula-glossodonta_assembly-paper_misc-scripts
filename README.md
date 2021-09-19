# albula-glossodonta_assembly-paper_misc-scripts
Misc. scripts referenced in our genome assembly paper for _Albula glossodonta_

## Usage
`python3 generateBedForMrnaExtraction.py maker.gff assembly.fa candidate_genes.bed`
`python3 renameVcfChrs.py sequence_ids.tsv variants.vcf > variants.renamed.vcf`

## Note
These scripts are not necessarily connected to eachother. No order is implied about how/when they should be run. This is simply a convenient way to make this code available for anyone who wishes to see it after reading our paper.

## Citation
If you use this code in some part or way, please cite our paper:
>Pickett BD, Talma S, Glass JR, Ence D, Cowley PD, Ridge PG, Kauwe JSK. 2021. Genome Assembly of the Roundjaw Bonefish (_Albula glossodonta_), a Vulnerable Circumtropical Sportfish. _bioRxiv_. DOI: [10.1101/2021.09.10.458299](https://doi.org/10.1101/2021.09.10.458299).
<!-- >Name. Name. ... Name. 2020. Title. _journal_. Vol.(Iss.):pages.-->
