# Auto generated from minimal_metab.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-08-02T20:04:40
# Schema: minimal_metab
#
# id: https://w3id.org/microbiomedata/minimal-metab
# description: A LinkML cookiecutter repo for modelling metabolomics from the ground up
# license: MIT

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Double, Float, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
UO = CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MINIMAL_METAB = CurieNamespace('minimal_metab', 'https://w3id.org/microbiomedata/minimal-metab/')
QUD = CurieNamespace('qud', 'http://qudt.org/1.1/schema/qudt#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = MINIMAL_METAB


# Types
class Unit(str):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "unit"
    type_model_uri = MINIMAL_METAB.Unit


# Class references
class NamedThingId(URIorCURIE):
    pass


class SampleOperationsId(NamedThingId):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Thing
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = MINIMAL_METAB.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class SampleOperations(NamedThing):
    """
    Represents a SampleOperations
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MINIMAL_METAB.SampleOperations
    class_class_curie: ClassVar[str] = "minimal_metab:SampleOperations"
    class_name: ClassVar[str] = "SampleOperations"
    class_model_uri: ClassVar[URIRef] = MINIMAL_METAB.SampleOperations

    id: Union[str, SampleOperationsId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SampleOperationsId):
            self.id = SampleOperationsId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class AttributeValue(YAMLRoot):
    """
    The value for any value of a attribute for a sample. This object can hold both the un-normalized atomic value and
    the structured value
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MINIMAL_METAB.AttributeValue
    class_class_curie: ClassVar[str] = "minimal_metab:AttributeValue"
    class_name: ClassVar[str] = "AttributeValue"
    class_model_uri: ClassVar[URIRef] = MINIMAL_METAB.AttributeValue

    has_raw_value: Optional[str] = None
    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_raw_value is not None and not isinstance(self.has_raw_value, str):
            self.has_raw_value = str(self.has_raw_value)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass
class QuantityValue(AttributeValue):
    """
    A simple quantity, e.g. 2cm
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MINIMAL_METAB.QuantityValue
    class_class_curie: ClassVar[str] = "minimal_metab:QuantityValue"
    class_name: ClassVar[str] = "QuantityValue"
    class_model_uri: ClassVar[URIRef] = MINIMAL_METAB.QuantityValue

    has_unit: str = None
    has_numeric_value: float = None
    has_raw_value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.has_unit):
            self.MissingRequiredField("has_unit")
        if not isinstance(self.has_unit, str):
            self.has_unit = str(self.has_unit)

        if self._is_empty(self.has_numeric_value):
            self.MissingRequiredField("has_numeric_value")
        if not isinstance(self.has_numeric_value, float):
            self.has_numeric_value = float(self.has_numeric_value)

        if self.has_raw_value is not None and not isinstance(self.has_raw_value, str):
            self.has_raw_value = str(self.has_raw_value)

        super().__post_init__(**kwargs)


@dataclass
class SampleOperationsCollection(YAMLRoot):
    """
    A holder for SampleOperations objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MINIMAL_METAB.SampleOperationsCollection
    class_class_curie: ClassVar[str] = "minimal_metab:SampleOperationsCollection"
    class_name: ClassVar[str] = "SampleOperationsCollection"
    class_model_uri: ClassVar[URIRef] = MINIMAL_METAB.SampleOperationsCollection

    entries: Optional[Union[Dict[Union[str, SampleOperationsId], Union[dict, SampleOperations]], List[Union[dict, SampleOperations]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="entries", slot_type=SampleOperations, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=MINIMAL_METAB.id, domain=None, range=URIRef,
                   pattern=re.compile(r'[a-zA-Z0-9_]+:[a-zA-Z0-9_]+'))

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=MINIMAL_METAB.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=MINIMAL_METAB.description, domain=None, range=Optional[str])

slots.has_input = Slot(uri=MINIMAL_METAB.has_input, name="has_input", curie=MINIMAL_METAB.curie('has_input'),
                   model_uri=MINIMAL_METAB.has_input, domain=None, range=Union[str, NamedThingId])

slots.has_output = Slot(uri=MINIMAL_METAB.has_output, name="has_output", curie=MINIMAL_METAB.curie('has_output'),
                   model_uri=MINIMAL_METAB.has_output, domain=None, range=Union[str, NamedThingId])

slots.has_raw_value = Slot(uri=MINIMAL_METAB.has_raw_value, name="has_raw_value", curie=MINIMAL_METAB.curie('has_raw_value'),
                   model_uri=MINIMAL_METAB.has_raw_value, domain=AttributeValue, range=Optional[str])

slots.has_unit = Slot(uri=MINIMAL_METAB.has_unit, name="has_unit", curie=MINIMAL_METAB.curie('has_unit'),
                   model_uri=MINIMAL_METAB.has_unit, domain=None, range=str, mappings = [QUD.unit, SCHEMA.unitCode])

slots.has_numeric_value = Slot(uri=MINIMAL_METAB.has_numeric_value, name="has_numeric_value", curie=MINIMAL_METAB.curie('has_numeric_value'),
                   model_uri=MINIMAL_METAB.has_numeric_value, domain=None, range=float, mappings = [QUD.quantityValue, SCHEMA.value])

slots.sampleOperationsCollection__entries = Slot(uri=MINIMAL_METAB.entries, name="sampleOperationsCollection__entries", curie=MINIMAL_METAB.curie('entries'),
                   model_uri=MINIMAL_METAB.sampleOperationsCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, SampleOperationsId], Union[dict, SampleOperations]], List[Union[dict, SampleOperations]]]])

slots.type = Slot(uri=MINIMAL_METAB.type, name="type", curie=MINIMAL_METAB.curie('type'),
                   model_uri=MINIMAL_METAB.type, domain=None, range=Optional[str])

slots.AttributeValue_type = Slot(uri=MINIMAL_METAB.type, name="AttributeValue_type", curie=MINIMAL_METAB.curie('type'),
                   model_uri=MINIMAL_METAB.AttributeValue_type, domain=AttributeValue, range=Optional[str])

slots.QuantityValue_has_raw_value = Slot(uri=MINIMAL_METAB.has_raw_value, name="QuantityValue_has_raw_value", curie=MINIMAL_METAB.curie('has_raw_value'),
                   model_uri=MINIMAL_METAB.QuantityValue_has_raw_value, domain=QuantityValue, range=Optional[str])

slots.QuantityValue_has_unit = Slot(uri=MINIMAL_METAB.has_unit, name="QuantityValue_has_unit", curie=MINIMAL_METAB.curie('has_unit'),
                   model_uri=MINIMAL_METAB.QuantityValue_has_unit, domain=QuantityValue, range=str, mappings = [QUD.unit, SCHEMA.unitCode])

slots.QuantityValue_has_numeric_value = Slot(uri=MINIMAL_METAB.has_numeric_value, name="QuantityValue_has_numeric_value", curie=MINIMAL_METAB.curie('has_numeric_value'),
                   model_uri=MINIMAL_METAB.QuantityValue_has_numeric_value, domain=QuantityValue, range=float, mappings = [QUD.quantityValue, SCHEMA.value])