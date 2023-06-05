counter = 0
while counter < 10:
    # try:
    #     age = int(input("How old are you?"))
    #     break
    # except:
    #         print("Invalid Input")
    try:
        counter +=1
        if counter == 5:
            # raise Exception("Counter shoukd not be 5")
            raise RuntimeWarning("Count is now 5")
    # except (RuntimeWarning, EncodingWarning) as err:
    except  RuntimeWarning as err:
        print("Wahala cast:", err)
    else:
        print("else block")
    # finally:
    #     print("read eye")
