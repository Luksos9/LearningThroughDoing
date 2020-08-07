import time,sys
indient = 0
indientDirection = True

#Program prints a Zigzag with certain speed, it changes indient to imitate Zigzag
try:
    #main loop that is always True so it won't stop until we exit program
    while True:
        print(" " * indient, end="")
        print("********")
        #Set time until next line of * is printed
        time.sleep(0.1)

        #Increasing indient
        if indientDirection:
            indient += 1

            #Changing direction when reached certain indient(20 spaces)
            if indient == 20:
                indientDirection = False

        #Decreasing indient
        else:
            indient -= 1

            #Changing direction again
            if indient == 0:
                indientDirection = True

except KeyboardInterrupt:
    sys.exit()