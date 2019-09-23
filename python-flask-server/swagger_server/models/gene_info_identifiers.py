# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class GeneInfoIdentifiers(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, entrez: str=None, hgnc: str=None, mim: str=None, ensembl: List[str]=None, mygene_info: str=None):  # noqa: E501
        """GeneInfoIdentifiers - a model defined in Swagger

        :param entrez: The entrez of this GeneInfoIdentifiers.  # noqa: E501
        :type entrez: str
        :param hgnc: The hgnc of this GeneInfoIdentifiers.  # noqa: E501
        :type hgnc: str
        :param mim: The mim of this GeneInfoIdentifiers.  # noqa: E501
        :type mim: str
        :param ensembl: The ensembl of this GeneInfoIdentifiers.  # noqa: E501
        :type ensembl: List[str]
        :param mygene_info: The mygene_info of this GeneInfoIdentifiers.  # noqa: E501
        :type mygene_info: str
        """
        self.swagger_types = {
            'entrez': str,
            'hgnc': str,
            'mim': str,
            'ensembl': List[str],
            'mygene_info': str
        }

        self.attribute_map = {
            'entrez': 'entrez',
            'hgnc': 'hgnc',
            'mim': 'mim',
            'ensembl': 'ensembl',
            'mygene_info': 'mygene_info'
        }

        self._entrez = entrez
        self._hgnc = hgnc
        self._mim = mim
        self._ensembl = ensembl
        self._mygene_info = mygene_info

    @classmethod
    def from_dict(cls, dikt) -> 'GeneInfoIdentifiers':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The gene_info_identifiers of this GeneInfoIdentifiers.  # noqa: E501
        :rtype: GeneInfoIdentifiers
        """
        return util.deserialize_model(dikt, cls)

    @property
    def entrez(self) -> str:
        """Gets the entrez of this GeneInfoIdentifiers.

        Entrez gene id (CURIE).  # noqa: E501

        :return: The entrez of this GeneInfoIdentifiers.
        :rtype: str
        """
        return self._entrez

    @entrez.setter
    def entrez(self, entrez: str):
        """Sets the entrez of this GeneInfoIdentifiers.

        Entrez gene id (CURIE).  # noqa: E501

        :param entrez: The entrez of this GeneInfoIdentifiers.
        :type entrez: str
        """

        self._entrez = entrez

    @property
    def hgnc(self) -> str:
        """Gets the hgnc of this GeneInfoIdentifiers.

        HGNC gene id (CURIE).  # noqa: E501

        :return: The hgnc of this GeneInfoIdentifiers.
        :rtype: str
        """
        return self._hgnc

    @hgnc.setter
    def hgnc(self, hgnc: str):
        """Sets the hgnc of this GeneInfoIdentifiers.

        HGNC gene id (CURIE).  # noqa: E501

        :param hgnc: The hgnc of this GeneInfoIdentifiers.
        :type hgnc: str
        """

        self._hgnc = hgnc

    @property
    def mim(self) -> str:
        """Gets the mim of this GeneInfoIdentifiers.

        OMIM gene id (CURIE).  # noqa: E501

        :return: The mim of this GeneInfoIdentifiers.
        :rtype: str
        """
        return self._mim

    @mim.setter
    def mim(self, mim: str):
        """Sets the mim of this GeneInfoIdentifiers.

        OMIM gene id (CURIE).  # noqa: E501

        :param mim: The mim of this GeneInfoIdentifiers.
        :type mim: str
        """

        self._mim = mim

    @property
    def ensembl(self) -> List[str]:
        """Gets the ensembl of this GeneInfoIdentifiers.

        ENSEMBL gene id (CURIE).  # noqa: E501

        :return: The ensembl of this GeneInfoIdentifiers.
        :rtype: List[str]
        """
        return self._ensembl

    @ensembl.setter
    def ensembl(self, ensembl: List[str]):
        """Sets the ensembl of this GeneInfoIdentifiers.

        ENSEMBL gene id (CURIE).  # noqa: E501

        :param ensembl: The ensembl of this GeneInfoIdentifiers.
        :type ensembl: List[str]
        """

        self._ensembl = ensembl

    @property
    def mygene_info(self) -> str:
        """Gets the mygene_info of this GeneInfoIdentifiers.

        myGene.info primary id.  # noqa: E501

        :return: The mygene_info of this GeneInfoIdentifiers.
        :rtype: str
        """
        return self._mygene_info

    @mygene_info.setter
    def mygene_info(self, mygene_info: str):
        """Sets the mygene_info of this GeneInfoIdentifiers.

        myGene.info primary id.  # noqa: E501

        :param mygene_info: The mygene_info of this GeneInfoIdentifiers.
        :type mygene_info: str
        """

        self._mygene_info = mygene_info