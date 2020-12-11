import logging

from watchFaceParser.utils.elementsHelper import ElementsHelper


class ResourcesLoader:
    # redundancy
    @staticmethod
    def getValue(propertyInfo, serializable):
        propertyInfoName = propertyInfo['Name']
        if not propertyInfoName in serializable:
            return None
        return serializable[propertyInfoName]

    # private static readonly Logger Logger = LogManager.GetCurrentClassLogger();
    # private readonly string _imagesDirectory;

    # private readonly Dictionary<long, long> _mapping;

    def __init__(self, imagesDirectory):
        self._resources = [] # List<IResource>();
        self._mapping = {} # Dictionary<long, long>();
        self._imagesDirectory = imagesDirectory

    # public ResourcesLoader(string imagesDirectory)
    # {
    #     Resources = new List<IResource>();
    #     _mapping = new Dictionary<long, long>();
    #     _imagesDirectory = imagesDirectory;
    # }

    def resources(self):
        return self._resources


    def getImages(self):
        from resources.models.image import Image
        t = []
        for resource in self._resources:
            if type(resource) == Image:
                t.append(resource)
        return t


    def process(self, T, serializable, path = ''):
        assert(type(path) == str)
        if path != None and path != '':
            logging.debug(f"Loading resources for {path} '{T}'")
#        print (f"Loading resources for {path} '{T}'")

        lastImageIndexValue = None
        properties = ElementsHelper.sortedProperties(T)
        for _id in properties:
            currentPath = str(_id) if path == None or path == '' else ''.join([path, '.', str(_id)])

            propertyInfo = properties[_id]
            #propertyType = propertyInfo['Type']
            if isinstance(propertyInfo['Type'],list):
                propertyType = propertyInfo['Type'][0]
            else:
                propertyType = propertyInfo['Type']
            propertyValue = ResourcesLoader.getValue(propertyInfo, serializable) # propertyInfo.getValue(serializable, None)

            imageIndexAttribute = ElementsHelper.getCustomAttributeFor('ImageIndex', propertyInfo)
            imagesCountAttribute = ElementsHelper.getCustomAttributeFor('ImagesCount', propertyInfo)
#            print("INDEX",imageIndexAttribute,propertyInfo['Name'],propertyValue)

            if imagesCountAttribute != None and imageIndexAttribute != None:
                raise IndexError(
                    f"Property {propertyInfo} can't have both ParameterImageIndexAttribute and ParameterImagesCountAttribute")

            if propertyType == 'long' or propertyType == 'long?' or propertyType == list or propertyType == type:
                if imageIndexAttribute != None:
                    if propertyValue == None:
                        continue
                    imageIndex = propertyValue

                    lastImageIndexValue = imageIndex
 #                   print("INDEX",imageIndexAttribute,propertyInfo['Name'],propertyValue,imageIndex)
                    mappedIndex = self.loadImage(imageIndex)
                    propertyInfoName = propertyInfo['Name']
                    serializable[propertyInfoName] = mappedIndex

                elif imagesCountAttribute != None:
                    if lastImageIndexValue == None:
                        raise IndexError(
                            f"Property {propertyInfo} can't be processed because ImageIndex isn't present or it is zero")

                    if propertyType == type:
                        imagesCount = propertyValue.getValue()
                    elif propertyType == list:
                        imagesCount = propertyValue.Count
                    else:
                        imagesCount = propertyValue

                    for i in range(lastImageIndexValue + 1, lastImageIndexValue + imagesCount):
                        self.loadImage(i)
            else:
                if lastImageIndexValue and isinstance(propertyValue,list):
                    print ("DEBUG",lastImageIndexValue,lastImageIndexValue,propertyValue)
                    for i in range(lastImageIndexValue+1, lastImageIndexValue+len(propertyValue)):
                        self.loadImage(i)
                if imagesCountAttribute == None and imageIndexAttribute == None:
                    if propertyValue != None:
                        self.process(propertyType, propertyValue, currentPath)
                else:
                    raise IndexError(
                        f"Property {propertyInfo} with type {propertyType} can't have ParameterImageIndexAttribute or ParameterImagesCountAttribute")


    def loadImage_working(self, index):
        assert(type(index) == int)
        if index in self._mapping:
            return self._mapping[index]

        if index >= len(self._resources):
            self._resources.extend([None ] * (index + 1 - len(self._resources)))
        newImageIndex = index
        #else:
        #newImageIndex = len(self._resources)
#        print (self._resources)
 #       print ("xxINDEX",index, newImageIndex, len(self._resources))
        logging.debug(f"Loading image {newImageIndex}...")
        print(f"Loading image {newImageIndex}...")
        from resources.imageLoader import ImageLoader
        resource = ImageLoader.loadResourceForNumber(self._imagesDirectory, index)
#        if len(self._resources) > index:
#        print (len(self._resources))
        self._resources[index] = resource
 #       else:
        #self._resources.append(resource)
        self._mapping[index] = newImageIndex
#        print (self._resources)
        return newImageIndex

    def loadImage(self, index):
        assert(type(index) == int)
        if index in self._mapping:
            return self._mapping[index]

        logging.debug(f"Request image index {index}...")
        newImageIndex = None
        for i in range(len(self._resources),index+1):
 
            newImageIndex = i
            logging.debug(f"Loading image {newImageIndex}...")
#            print(f"Loading image {newImageIndex}...")
            from resources.imageLoader import ImageLoader
            resource = ImageLoader.loadResourceForNumber(self._imagesDirectory, i)
            self._resources.append(resource)
            self._mapping[i] = newImageIndex
#        print ("XXXX",index,newImageIndex)
        return newImageIndex
 
    def loadImage_orig(self, index):
        assert(type(index) == int)
        if index in self._mapping:
            return self._mapping[index]

        newImageIndex = len(self._resources)
        logging.debug(f"Loading image {newImageIndex}...")
        from resources.imageLoader import ImageLoader
        resource = ImageLoader.loadResourceForNumber(self._imagesDirectory, index)
        self._resources.append(resource)
        self._mapping[index] = newImageIndex
        return newImageIndex
