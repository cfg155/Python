mTitleArr = []
mGenreArr = []
mRatingArr = []
mPriceArr = []


def calculateTotalPrice(movieLength, additionalPrice):
    return (movieLength*500) + additionalPrice


def addNewMovie():
    try:
        mTitle = input("Input Movie Title \n")
        while len(mTitle) < 3 or len(mTitle) > 10:
            mTitle = input("Input Movie Title \n")

        mGenre = input("Input Movie Genre [Comedy | Action] \n")
        while mGenre != "Comedy" and mGenre != "Action":
            mGenre = input("Input Movie Genre [Comedy | Action] \n")

        additionalPrice = 0
        if(mGenre == "Comedy"):
            additionalPrice = 3000
        elif(mGenre == "Action"):
            additionalPrice = 4000

        tmp = input("Input Rating [1-10]\n")
        mRating = int(tmp)
        while mRating < 1 or mRating > 10:
            tmp = input("Input Rating [1-10]\n")
            mRating = int(tmp)

        mTitleArr.append(mTitle)
        mGenreArr.append(mGenre)
        mRatingArr.append(mRating)
        mPriceArr.append(calculateTotalPrice(len(mTitle), additionalPrice))
    except:
        print("something wrong with your input, please try again")
        addNewMovie()


def viewMovie():
    print("====================================================")
    print("| No | Title | Genre | Rating | Price")
    print("====================================================")
    for index in range(0, len(mRatingArr)):
        no = index + 1
        print("| " + str(no) + " | " + mTitleArr[index] + " | " +
              mGenreArr[index] + " | " + str(mRatingArr[index]) + " | " + str(mPriceArr[index]))


def menu():
    print("=============")
    print("Movie Rental")
    print("=============")
    print("1. Add new Movie")
    print("2. View Movie")
    print("3. Exit")
    tmp = input(">> ")

    choose = int(tmp)

    if choose == 1:
        addNewMovie()

    if choose == 2:
        viewMovie()

    if choose == 3:
        print("Thank You for using this software")
        exit()


while True:
    menu()
