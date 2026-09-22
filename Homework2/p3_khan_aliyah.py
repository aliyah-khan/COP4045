#aliyah khan
#3

import csv

def add_user(sn: dict, username: str, fullname: str) -> bool:
    """adds a new user with no friends to sn, returns false if the user already exists"""
    try:
        if username in sn:
            return False
        sn[username] = (fullname, [])
        return True

    except Exception as e:
        print("something went wrong adding the user:", e)
        raise


def add_friend(sn: dict, user1: str, user2: str) -> bool:
    """adds a mutual friend link between user1 and user2, returns false if either user is missing"""
    try:
        if user1 not in sn or user2 not in sn:
            return False

        #getting the current friend lists so we can add to them
        user1Name = sn[user1][0]
        user1Friends = sn[user1][1]
        user2Name = sn[user2][0]
        user2Friends = sn[user2][1]

        if user2 not in user1Friends:
            user1Friends.append(user2)
        if user1 not in user2Friends:
            user2Friends.append(user1)

        sn[user1] = (user1Name, user1Friends)
        sn[user2] = (user2Name, user2Friends)
        return True

    except Exception as e:
        print("something went wrong adding the friend link:", e)
        raise


def get_friends(sn: dict, user1: str, distance: int) -> list:
    """returns all friends of user1 up to the given link distance, avoiding cycles"""
    try:
        if user1 not in sn:
            return []

        #keeping track of everyone already seen so we don't loop back around
        visited = [user1]
        currentLevel = [user1]
        result = []
        level = 0

        while level < distance:
            nextLevel = []

            #going through every user in the current level and checking
            #their friends list for anyone new
            for user in currentLevel:
                friendsList = sn[user][1]
                for friend in friendsList:
                    if friend not in visited:
                        visited.append(friend)
                        nextLevel.append(friend)
                        result.append(friend)

            currentLevel = nextLevel
            level = level + 1

        return result

    except Exception as e:
        print("something went wrong getting the friends list:", e)
        raise


def save_network(filename: str, sn: dict) -> None:
    """saves a social network dictionary to a csv file"""
    try:
        f = open(filename, "w", newline="")
        writer = csv.writer(f)

        for username in sn:
            fullname = sn[username][0]
            friendsList = sn[username][1]

            row = [username, fullname]
            for friend in friendsList:
                row.append(friend)

            writer.writerow(row)

        f.close()

    except Exception as e:
        print("something went wrong saving the network:", e)
        raise


def load_network(filename: str) -> dict:
    """loads a social network dictionary from a csv file saved with save_network"""
    try:
        f = open(filename, "r", newline="")
        reader = csv.reader(f)

        sn = {}
        for row in reader:
            username = row[0]
            fullname = row[1]

            friendsList = []
            for i in range(2, len(row)):
                friendsList.append(row[i])

            sn[username] = (fullname, friendsList)

        f.close()
        return sn

    except Exception as e:
        print("something went wrong loading the network:", e)
        raise

#testif module
def testif(b, testname, msgOK="", msgFailed=""):
    """Function used for testing.
    param b: boolean, normally a tested condition: true if test passed, false
    otherwise
    param testname: the test name
    param msgOK: string to be printed if param b==True ( test condition true)
    param msgFailed: string to be printed if param b==False
    returns b
    """
    if b:
        print("Success: " + testname + "; " + msgOK)
    else:
        print("Failed: " + testname + "; " + msgFailed)
    return b


def test():
    #building a fresh copy of the network so the tests don't mess with main
    sn = {'alice': ('Alice Smith', ['maria']),
          'maria': ('Maria Cortez', ['alice', 'joe', 'david']),
          'joe': ('Joseph Adams', ['maria', 'eve']),
          'eve': ('Evelyn Cooper', ['joe']),
          'david': ('David Benson', ['maria'])}

    #testing add_user
    result = add_user(sn, "frank", "Frank Miller")
    testif(result == True, "add_user new user", "frank was added", "frank was not added")

    result = add_user(sn, "alice", "Alice Again")
    testif(result == False, "add_user existing user", "alice was correctly rejected", "alice should have been rejected")

    #testing add_friend
    result = add_friend(sn, "frank", "alice")
    testif(result == True, "add_friend valid users", "frank and alice are linked", "frank and alice were not linked")

    result = add_friend(sn, "frank", "nobody")
    testif(result == False, "add_friend invalid user", "nobody was correctly rejected", "nobody should have been rejected")

    #testing get_friends
    friends1 = get_friends(sn, "alice", 1)
    testif(set(friends1) == {"maria", "frank"}, "get_friends distance 1", "got the right friends", "got the wrong friends: " + str(friends1))

    friends2 = get_friends(sn, "alice", 2)
    testif(set(friends2) == {"maria", "joe", "david", "frank"}, "get_friends distance 2", "got the right friends", "got the wrong friends: " + str(friends2))

    #testing save_network and load_network
    save_network("testnetwork.csv", sn)
    loadedsn = load_network("testnetwork.csv")
    testif(loadedsn == sn, "save and load network", "network matches after save and load", "network did not match after save and load")

def main():
    print("aliyah khan z23556724\n")
    #building the example social network from the assignment
    sn = {'alice': ('Alice Smith', ['maria']),
          'maria': ('Maria Cortez', ['alice', 'joe', 'david']),
          'joe': ('Joseph Adams', ['maria', 'eve']),
          'eve': ('Evelyn Cooper', ['joe']),
          'david': ('David Benson', ['maria'])}

    print("starting network:")
    print(sn)

    #testing add_user
    print("\nadd_user frank:", add_user(sn, "frank", "Frank Miller"))
    print("add_user alice again:", add_user(sn, "alice", "Alice Again"))
    print(sn)

    #testing add_friend
    print("\nadd_friend frank and alice:", add_friend(sn, "frank", "alice"))
    print("add_friend frank and nobody:", add_friend(sn, "frank", "nobody"))
    print(sn)

    #testing get_friends
    print("\nfriends of alice at distance 1:", get_friends(sn, "alice", 1))
    print("friends of alice at distance 2:", get_friends(sn, "alice", 2))
    print("friends of nobody at distance 1:", get_friends(sn, "nobody", 1))

    #testing save_network and load_network
    save_network("network.csv", sn)
    loadedsn = load_network("network.csv")
    print("\nnetwork loaded back from csv:")
    print(loadedsn)
    print("loaded network matches original:", loadedsn == sn)

if __name__ == "__main__":
    main()
    print("\nrunning extra credit tests:\n")
    test()
