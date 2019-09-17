
def average(score1, score2, score3):
    NUMBER_TESTS = 3
    try:
        if score1 < 0:
            raise ValueError
        if score2 < 0:
            raise ValueError
        avg = (int(score1) + int(score2) + int(score3)) / NUMBER_TESTS
    except:
        raise ValueError
    print(str(avg));
    return avg


if __name__ == "__main__":
    fname = input("Your first name: ")
    lname = input("Your last name: ")
    age = input("Your age: ")
    score1 = input("First score: ")
    score2 = input("Second score: ")
    score3 = input("Third score: ")
    average(score1, score2, score3)

