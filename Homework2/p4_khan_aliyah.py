#aliyah khan
#4

import csv

def read_csv_rows(filename):
    #opens a csv file and returns all of its rows as a list of lists
    try:
        f = open(filename, "r", encoding="utf-8")
        reader = csv.reader(f)

        rows = []
        for row in reader:
            rows.append(row)

        f.close()
        return rows

    except Exception as e:
        print("something went wrong reading", filename, ":", e)
        raise


def parse_box_office(text):
    #converts a box office string into a plain number
    cleaned = text.replace("$", "")
    cleaned = cleaned.replace(",", "")
    return int(cleaned)


def load_ranking_csv(filename, isboxoffice):
    #both the top rated and top grossing files have the same layout,
    #rank, title, year, value, so this one function handles either file
    #isboxoffice tells us whether to parse the value as money or as a rating
    #returns a dict mapping (title, year) to the value
    try:
        rows = read_csv_rows(filename)
        rows = rows[1:]  #skipping header row

        rankingDict = {}
        for row in rows:
            title = row[1]
            year = row[2]
            valuetext = row[3]

            if isboxoffice:
                value = parse_box_office(valuetext)
            else:
                value = float(valuetext)

            rankingDict[(title, year)] = value

        return rankingDict

    except Exception as e:
        print("something went wrong loading the ranking from", filename, ":", e)
        raise


def load_casts_csv(filename):
    #reads the casts file, which has no header, and returns a dict
    #mapping (title, year) to a tuple (director, list of actors)
    try:
        rows = read_csv_rows(filename)

        castsDict = {}
        for row in rows:
            title = row[0]
            year = row[1]
            director = row[2]

            actorsList = []
            for i in range(3, len(row)):
                if row[i] != "":
                    actorsList.append(row[i])

            castsDict[(title, year)] = (director, actorsList)

        return castsDict

    except Exception as e:
        print("something went wrong loading the casts from", filename, ":", e)
        raise


def sort_by_index_descending(datalist, index):
    #sorts a list of tuples in place by the value at position index,
    #highest first, using a simple selection sort
    n = len(datalist)
    for x in range(n):
        largest = x
        for y in range(x + 1, n):
            if datalist[y][index] > datalist[largest][index]:
                largest = y
        if largest != x:
            temp = datalist[x]
            datalist[x] = datalist[largest]
            datalist[largest] = temp


def print_ranking(rankinglist, limit):
    #prints a list of tuples one per line, cut off at limit entries if
    #limit is given, otherwise prints everything
    if limit is None:
        entriesToShow = rankinglist
    else:
        entriesToShow = rankinglist[:limit]

    for entry in entriesToShow:
        print(entry)


def display_top_collaborations(toprated_file, casts_file, limit=None):
    #displays director/actor pairs ranked by how many top rated movies
    #they worked on together
    try:
        topratedDict = load_ranking_csv(toprated_file, False)
        castsDict = load_casts_csv(casts_file)

        #counting how many top rated movies each director and actor
        #pair worked on together
        collabCounts = {}
        for movieKey in castsDict:
            if movieKey in topratedDict:
                director = castsDict[movieKey][0]
                actorsList = castsDict[movieKey][1]

                for actor in actorsList:
                    pair = (director, actor)
                    if pair in collabCounts:
                        collabCounts[pair] = collabCounts[pair] + 1
                    else:
                        collabCounts[pair] = 1

        #turning the dictionary into a list of tuples so it can be sorted
        collabList = []
        for pair in collabCounts:
            director = pair[0]
            actor = pair[1]
            count = collabCounts[pair]
            collabList.append((director, actor, count))

        sort_by_index_descending(collabList, 2)

        print("\ntop director and actor collaborations:")
        print_ranking(collabList, limit)

    except Exception as e:
        print("something went wrong displaying the top collaborations:", e)
        raise


def display_top_actors(topgrossing_file, casts_file, limit=None):
    #displays actors ranked by the total box office of their top
    #grossing movies
    try:
        grossingDict = load_ranking_csv(topgrossing_file, True)
        castsDict = load_casts_csv(casts_file)

        #adding up the box office for every actor across their top
        #grossing movies
        actorTotals = {}
        for movieKey in grossingDict:
            if movieKey in castsDict:
                boxoffice = grossingDict[movieKey]
                actorsList = castsDict[movieKey][1]

                for actor in actorsList:
                    if actor in actorTotals:
                        actorTotals[actor] = actorTotals[actor] + boxoffice
                    else:
                        actorTotals[actor] = boxoffice

        actorList = []
        for actor in actorTotals:
            total = actorTotals[actor]
            actorList.append((actor, total))

        sort_by_index_descending(actorList, 1)

        print("\ntop grossing actors:")
        print_ranking(actorList, limit)

    except Exception as e:
        print("something went wrong displaying the top actors:", e)
        raise


def main():
    print("aliyah khan z23556724")
    display_top_collaborations("imdb-top-rated.csv", "imdb-top-casts.csv", 10)
    display_top_actors("imdb-top-grossing.csv", "imdb-top-casts.csv", 10)


if __name__ == "__main__":
    main()
