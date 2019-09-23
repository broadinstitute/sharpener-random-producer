# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.gene_info import GeneInfo  # noqa: F401,E501
from swagger_server.models.model_property import ModelProperty  # noqa: F401,E501
from swagger_server import util


class TransformerQuery(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, genes: List[GeneInfo]=None, controls: List[ModelProperty]=None):  # noqa: E501
        """TransformerQuery - a model defined in Swagger

        :param genes: The genes of this TransformerQuery.  # noqa: E501
        :type genes: List[GeneInfo]
        :param controls: The controls of this TransformerQuery.  # noqa: E501
        :type controls: List[ModelProperty]
        """
        self.swagger_types = {
            'genes': List[GeneInfo],
            'controls': List[ModelProperty]
        }

        self.attribute_map = {
            'genes': 'genes',
            'controls': 'controls'
        }

        self._genes = genes
        self._controls = controls

    @classmethod
    def from_dict(cls, dikt) -> 'TransformerQuery':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The transformer_query of this TransformerQuery.  # noqa: E501
        :rtype: TransformerQuery
        """
        return util.deserialize_model(dikt, cls)

    @property
    def genes(self) -> List[GeneInfo]:
        """Gets the genes of this TransformerQuery.

        List of genes that will be transformed. Required for expanders and filters; should be omitted for producers.  # noqa: E501

        :return: The genes of this TransformerQuery.
        :rtype: List[GeneInfo]
        """
        return self._genes

    @genes.setter
    def genes(self, genes: List[GeneInfo]):
        """Sets the genes of this TransformerQuery.

        List of genes that will be transformed. Required for expanders and filters; should be omitted for producers.  # noqa: E501

        :param genes: The genes of this TransformerQuery.
        :type genes: List[GeneInfo]
        """

        self._genes = genes

    @property
    def controls(self) -> List[ModelProperty]:
        """Gets the controls of this TransformerQuery.

        Values that control the behavior of the transformer. Names of the controls must match the names specified in the transformer's definition and values must match types (and possibly  allowed_values) specified in the transformer's definition.  # noqa: E501

        :return: The controls of this TransformerQuery.
        :rtype: List[ModelProperty]
        """
        return self._controls

    @controls.setter
    def controls(self, controls: List[ModelProperty]):
        """Sets the controls of this TransformerQuery.

        Values that control the behavior of the transformer. Names of the controls must match the names specified in the transformer's definition and values must match types (and possibly  allowed_values) specified in the transformer's definition.  # noqa: E501

        :param controls: The controls of this TransformerQuery.
        :type controls: List[ModelProperty]
        """
        if controls is None:
            raise ValueError("Invalid value for `controls`, must not be `None`")  # noqa: E501

        self._controls = controls