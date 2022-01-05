def loadImagesData(dataFileName, labelFileName):
    labels = []
    images = []

    with open(dataFileName, 'rb') as dataFile:
        # Read file header
        dataFile.read(4) # "magic number"
        itemsCount = int.from_bytes(dataFile.read(4), "big")
        height = int.from_bytes(dataFile.read(4), "big")
        width = int.from_bytes(dataFile.read(4), "big")


        if((height != 28) | (width != 28)):
            raise ValueError("Unsupported file format: " + dataFileName)

        while(itemsCount > len(images)):
            images.append([x for x in dataFile.read(784)])
        
    with open(labelFileName, 'rb') as labelFile:
        # Read file header
        labelFile.read(4) # "magic number"
        itemsCount = int.from_bytes(labelFile.read(4), "big")

        labels = [int.from_bytes(labelFile.read(1), "big") for _ in range(0, itemsCount)]

    return (images, labels)