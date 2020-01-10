#REQUIREMENTS
import random
import os

from swagger_server.models.gene_info import GeneInfo  # noqa: E501
from swagger_server.models.gene_info import GeneInfoIdentifiers

from swagger_server.controllers.transformer import Transformer

#available at ftp://ftp.ncbi.nih.gov/gene/DATA/gene_info.gz
entrez_file = 'dat/entrez_ids.txt'
potential_id_files=[entrez_file]

#END REQUIREMENTS

class RandomProducer(Transformer):

    variables = ['number']

    def __init__(self):
        super().__init__(self.variables)
        self.potential_ids = set()
        for potential_id_file in potential_id_files:
            potential_id_fh = open(potential_id_file)
            for line in potential_id_fh:
                cols = line.strip().split()
                for col in cols:
                    self.potential_ids.add(col)
            potential_id_fh.close()

    def produce(self, controls):
        genes = []
        for gene_id in random.sample(self.potential_ids, controls['number']):
            genes.append(GeneInfo(
                         gene_id = 'NCBIGene:%s' % gene_id,
                         identifiers = GeneInfoIdentifiers(entrez='NCBIGene:%s' % gene_id),
                         attributes = [],
                         source = self.info.name))
        return genes



if __name__ == "__main__":
    os.system('wget -O %s.orig.gz ftp://ftp.ncbi.nih.gov/gene/DATA/gene_info.gz' % entrez_file)
    os.system('gunzip %s.orig.gz' % entrez_file)
    os.system("awk -F\"\t\" '$1 == 9606 && $10 == \"protein-coding\" {print $2}' %s.orig > %s" % (entrez_file, entrez_file))
