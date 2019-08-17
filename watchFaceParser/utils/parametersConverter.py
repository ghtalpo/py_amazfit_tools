import logging
import os.path

from watchFaceParser.utils.elementsHelper import ElementsHelper
from watchFaceParser.models.textAlignment import TextAlignment
from watchFaceParser.models.color import Color
from watchFaceParser.models.parameter import Parameter


def ulong2long(n):
    if type(n) == int:
        if n >= 0x7fffffffffffffff:
            return -(0xffffffffffffffff - n + 1)
    return n


class ParametersConverter:
    @staticmethod
    def getValue(propertyInfo, serializable):
        propertyInfoName = propertyInfo['Name']
        if not propertyInfoName in serializable:
            return None
        return serializable[propertyInfoName]


    @staticmethod
    def build(T, serializable, path = ""):
        result = []

        properties = ElementsHelper.sortedProperties(T)
        for _id in properties:
            currentPath = str(_id) if path == None or path == '' else ''.join([path, '.', str(_id)])

            propertyInfo = properties[_id]
            propertyType = propertyInfo['Type']

            propertyValue = ParametersConverter.getValue(propertyInfo, serializable)

            if propertyValue is None:
                continue

            if propertyType == 'long' or propertyType == 'long?' or propertyType == TextAlignment  or propertyType == Color or propertyType == 'bool':
                value = propertyValue
                if propertyType == 'bool' or type(propertyValue) == bool:
                    value = 1 if propertyValue else 0
                elif propertyType == TextAlignment:
                    value = TextAlignment.fromJSON(propertyValue)
                elif propertyType == Color:
                    value = Color.fromJSON(propertyValue)
                elif propertyType == 'long' or propertyType == 'long?':
                    value = int(value)

                logging.debug(f"{currentPath} '{propertyInfo['Name']}': {value}")
                result.append(Parameter(_id, value))
            else:
                innerParameters = ParametersConverter.build(propertyType, propertyValue, currentPath)
                if len(innerParameters) > 0:
                    logging.debug(f"{currentPath} '{propertyInfo['Name']}'")
                    result.append(Parameter(_id, innerParameters))
                else:
                    logging.debug(f"{currentPath} '{propertyInfo['Name']}': Skipped because of empty")

        return result


    @staticmethod
    def parse(paramType, descriptor, path = ""):
        assert(type(descriptor) == type([]))
        assert(type(path) == type(""))
        properties = ElementsHelper.sortedProperties(paramType)
        result = paramType()
        currentType = paramType

        for parameter in descriptor:
            parameterId = parameter.getId()
            currentPath = str(parameterId) if not path else os.path.join(path, '.', str(parameterId))
            if parameterId not in properties:
                logging.warn(f"[ParamConv:parse] currentPath {currentPath} / Parameter {parameterId} isn't supported for {currentType}")
                raise IndexError(f"Parameter {parameterId} isn't supported for {currentType}")

            propertyInfo = properties[parameterId]
            propertyType = propertyInfo['Type']

            propertyInfoName = propertyInfo['Name']

            if propertyType == 'long' or propertyType == 'long?' or propertyType == TextAlignment  or propertyType == Color or propertyType == 'bool':
                if propertyType == TextAlignment:
                    setattr(result, propertyInfoName, TextAlignment(parameter.getValue()))
                elif propertyType == Color:
                    setattr(result, propertyInfoName, Color(parameter.getValue()))
                elif propertyType == 'bool':
                    setattr(result, propertyInfoName, parameter.getValue() > 0)
                elif propertyType == 'long':
                    setattr(result, propertyInfoName, ulong2long(parameter.getValue()))
                else:
                    setattr(result, propertyInfoName, ulong2long(parameter.getValue() or None))

            elif propertyType == '[]':
                assert(False) # not tested yet
            else:
                tmp = propertyType()
                for x in parameter.getChildren():
                    psd = ParametersConverter.parse(propertyType, [x], currentPath)
                    import json

                    for kk in psd.__dict__:
                        vv = psd.__dict__[kk]
                        setattr(tmp, kk, vv)
                setattr(result, propertyInfoName, tmp)
        return result
