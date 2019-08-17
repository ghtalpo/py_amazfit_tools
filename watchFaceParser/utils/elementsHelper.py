import logging

from watchFaceParser.watchFace import WatchFace
from watchFaceParser.attributes.parameterIdAttribute import ParameterIdAttribute


class ElementsHelper:
    @staticmethod
    def sortedProperties(typeInfo):
        try:
            getattr(typeInfo, 'definitions')
        except AttributeError:
            return []

        properties = {}
        for propertyInfo in typeInfo.definitions:
            parameterIdAttribute = ParameterIdAttribute(propertyInfo)
            if parameterIdAttribute is None:
                raise IndexError(
                    f"Class {typeInfo.Name} doesn't have ParameterIdAttribute on property {propertyInfo['Name']}"
                )
            if parameterIdAttribute.getId() in properties:
                raise IndexError(
                    f"Class {typeInfo.Name} already has ParameterIdAttribute with Id {parameterIdAttribute.Id}"
                )
            properties[parameterIdAttribute.getId()] = typeInfo.definitions[propertyInfo]
        return properties


    @staticmethod
    def getCustomAttributeFor(T, propertyInfo):
        if T in propertyInfo['Name']:
            return propertyInfo['Type']
        return None
