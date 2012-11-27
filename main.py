pic = takePicture()
show(pic)

retake = askQuestion("Should I take a new picture?",["Yes","No"])

if retake == "Yes":
    pic = takePicture()
    show(pic)

pic = takePicture("blob")

choice = askQuestion("What color should I follow?",
["Red", "Blue", "Green", "Yellow"])

if choice == "Red":
    configureBlob(0,254,115,153,204,226)
    pic = takePicture("blob")
    def locateObject(pic):
        tot_x = 0
        count = 0
        for pixel in getPixels(pic):
            r, g, b = getRGB(pixel)
            if r == 255 and g == 255 and b == 255:
#            if r > 230 and b < 100 and b > 65 and g > 70 and g < 115:
                tot_x = tot_x + getX(pixel)
                count = count + 1
        if tot_x == 0:
            return -1
        else:
            return (tot_x/count)

    while 1:
         #take picture and locate the object
        pic = takePicture("blob")
        objectLocation = locateObject(pic)
        show(pic)
        if objectLocation == -1:
            turnRight(.04)
            pic = takePicture("blob")
            objectLocation = locateObject(pic)
            print objectLocation
        elif objectLocation <= 85:
            turnLeft(.04)
            pic = takePicture("blob")
            objectLocation = locateObject(pic)
            print objectLocation
        elif objectLocation <= 170:
            forward(.5)
            pic = takePicture("blob")
            objectLocation = locateObject(pic)
            print objectLocation
        else:
            turnRight(.04)
            pic = takePicture("blob")
            objectLocation = locateObject(pic)
            print objectLocation

if choice == "Blue":
    configureBlob(0,254,129,200,102,131)
    pic = takePicture("blob")
    def locateObject(pic):
        tot_x = 0
        count = 0
        for pixel in getPixels(pic):
            r, g, b = getRGB(pixel)
            if r == 255 and g == 255 and b == 255:
#            if b > 230 and r < 50 and r > 1 and g > 65 and g < 110:
                tot_x = tot_x + getX(pixel)
                count = count + 1
        if tot_x == 0:
            return -1
        else:
            return (tot_x/count)

    while 1:
         #take picture and locate the object
        pic = takePicture("blob")
        objectLocation = locateObject(pic)
        show(pic)
        if objectLocation == -1:
            pic = takePicture("blob")
            objectLocation = locateObject(pic)
            turnRight(.05)
            print objectLocation
        elif objectLocation <= 85:
            pic = takePicture("blob")
            objectLocation = locateObject(pic)
            turnLeft(.05)
            print objectLocation
        elif objectLocation <= 170:
            pic = takePicture("blob")
            objectLocation = locateObject(pic)
            forward(.5)
            print objectLocation
        else:
            pic = takePicture("blob")
            objectLocation = locateObject(pic)
            turnRight(.05)
            print objectLocation

if choice == "Green":
    configureBlob(0,254,124,169,30,168)
    pic = takePicture("blob")
    def locateObject(pic):
        tot_x = 0
        count = 0
        for pixel in getPixels(pic):
           r, g, b = getRGB(pixel)
           if r == 255 and g == 255 and b == 255:
#           if r > 110 and r < 160 and g > 230 and b > 120 and b < 145:
                tot_x = tot_x + getX(pixel)
                count = count + 1
        if tot_x == 0:
            return -1
        else:
            return (tot_x/count)

    while 1:
         #take picture and locate the object
        pic = takePicture("blob")
        objectLocation = locateObject(pic)
        show(pic)
#        if objectLocation == -1:
#            pic = takePicture("blob")
#            objectLocation = locateObject(pic)
#            turnRight(.05)
#            print objectLocation
        if objectLocation <= 85:
            pic = takePicture("blob")
            objectLocation = locateObject(pic)
            turnLeft(.005)
            print objectLocation
        elif objectLocation <= 170:
            pic = takePicture("blob")
            objectLocation = locateObject(pic)
            forward(.5)
            print objectLocation
        else:
            pic = takePicture("blob")
            objectLocation = locateObject(pic)
            turnRight(.005)
            print objectLocation

if choice == "Yellow":
    configureBlob(0,254,95,152,134,156)
    pic = takePicture("blob")
    def locateObject(pic):
        tot_x = 0
        count = 0
        for pixel in getPixels(pic):
           r, g, b = getRGB(pixel)
           if r == 255 and g == 255 and b == 255:
#           if r > 110 and r < 160 and g > 230 and b > 120 and b < 145:
                tot_x = tot_x + getX(pixel)
                count = count + 1
        if tot_x == 0:
            return -1
        else:
            return (tot_x/count)

    while 1:
         #take picture and locate the object
        pic = takePicture("blob")
        objectLocation = locateObject(pic)
        show(pic)
        if objectLocation == -1:
            pic = takePicture("blob")
            objectLocation = locateObject(pic)
            turnRight(.05)
            print objectLocation
        elif objectLocation <= 85:
            pic = takePicture("blob")
            objectLocation = locateObject(pic)
            turnLeft(.05)
            print objectLocation
        elif objectLocation <= 170:
            pic = takePicture("blob")
            objectLocation = locateObject(pic)
            forward(.5)
            print objectLocation
        else:
            pic = takePicture("blob")
            objectLocation = locateObject(pic)
            turnRight(.05)
            print objectLocation

