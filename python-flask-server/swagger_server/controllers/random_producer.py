#REQUIREMENTS
import random
import os

from swagger_server.models.gene_info import GeneInfo  # noqa: E501
from swagger_server.models.transformer_info import TransformerInfo  # noqa: E501
from swagger_server.models.parameter import Parameter
from swagger_server.models.gene_info import GeneInfoIdentifiers
from swagger_server.models.attribute import Attribute

#available at http://software.broadinstitute.org/gsea/downloads.jsp
entrez_file = 'dat/entrez_ids.txt'
potential_id_files=[entrez_file]

#END REQUIREMENTS

transformer_name = 'Random gene list'
valid_controls = ['number']
default_control_values = {'number': 32}
default_control_types = {'number': 'int'}

def get_control(controls, control):
    value = controls[control] if control in controls else default_control_values[control]
    if default_control_types[control] == 'double':
        return float(value)
    elif default_control_types[control] == 'Boolean':
        return bool(value)
    elif default_control_types[control] == 'int':
        return int(value)
    else:
        return value

def get_genes(controls):

    potential_ids = set()
    for potential_id_file in potential_id_files:
        potential_id_fh = open(potential_id_file)
        for line in potential_id_fh:
            cols = line.strip().split()
            for col in cols:
                potential_ids.add(col)
        potential_id_fh.close()

    genes = []
    for gene_id in random.sample(potential_ids, get_control(controls, 'number')):
        genes.append(GeneInfo(
                     gene_id = 'NCBIGene:%s' % gene_id,
                     identifiers = GeneInfoIdentifiers(entrez='NCBIGene:%s' % gene_id),
                     attributes = [
                        Attribute(
                          name = 'source',
                          value = 'random gene',
                          source = transformer_name
                        )]))
    return genes

def get_info():
    return TransformerInfo(
        name = transformer_name,
        function = 'producer',
        #operation = 'enrichment',
        #ui_label = 'HyperGeomEnrich',
        #source_url = 'http://software.broadinstitute.org/gsea/downloads.jsp',
        description = 'Random gene list producer',
        parameters = [Parameter(x, default_control_types[x], default_control_values[x]) for x in valid_controls],
        required_attributes = []
    )


if __name__ == "__main__":
    os.system('wget -O %s.orig.gz ftp://ftp.ncbi.nih.gov/gene/DATA/gene_info.gz' % entrez_file)
    os.system('gunzip %s.orig.gz' % entrez_file)
    os.system("awk -F\"\t\" '$1 == 9606 && $10 == \"protein-coding\" {print $2}' %s.orig > %s" % (entrez_file, entrez_file))
