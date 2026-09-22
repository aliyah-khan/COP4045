#aliyah khan
#5

from datetime import datetime

import sys
import os
import math
import tempfile
import unittest


def read_observations(filename):
    #reads the station observations file and returns a dict of valid data plus a list of errors
    observations = {}
    errors = []
    seen = set()

    with open(filename, "r", encoding="utf-8") as f:
        lineNum = 0
        for line in f:
            lineNum += 1
            line = line.strip()

            if line == "":
                errors.append((lineNum, "malformed line"))
                continue

            fields = line.split(",")
            if len(fields) != 3:
                errors.append((lineNum, "malformed line"))
                continue

            station = fields[0].strip()
            datetext = fields[1].strip()
            temptext = fields[2].strip()

            if station == "" or datetext == "" or temptext == "":
                errors.append((lineNum, "malformed line"))
                continue

            try:
                #going with this exact format since it matches the example given
                dateobj = datetime.strptime(datetext, "%I:%M:%S %p %m/%d/%Y")
            except Exception:
                errors.append((lineNum, "invalid date"))
                continue

            try:
                temp = float(temptext)
            except Exception:
                errors.append((lineNum, "invalid temperature"))
                continue

            #float() also accepts "nan" and "inf", so catching those here too
            if not math.isfinite(temp):
                errors.append((lineNum, "invalid temperature"))
                continue

            if temp < -100.0 or temp > 150.0:
                errors.append((lineNum, "invalid temperature"))
                continue

            key = (station, dateobj)
            if key in seen:
                errors.append((lineNum, "duplicate observation"))
                continue
            seen.add(key)

            if station in observations:
                observations[station].append((dateobj, temp))
            else:
                observations[station] = [(dateobj, temp)]

    #sorting each station's observations by date
    for station in observations:
        observations[station].sort(key=lambda entry: entry[0])

    return (observations, errors)


def station_statistics(observations):
    #calculates min, max, and mean temperature for each station
    statsDict = {}
    for station in observations:
        temps = []
        for entry in observations[station]:
            temps.append(entry[1])

        minTemp = min(temps)
        maxTemp = max(temps)
        meanTemp = sum(temps) / len(temps)

        statsDict[station] = (minTemp, maxTemp, meanTemp)

    return statsDict


def station_outliers(observations):
    #finds stations whose latest temperature is above their mean
    statsDict = station_statistics(observations)

    outliers = {
        station: (
            observations[station][-1][0],
            observations[station][-1][1],
            statsDict[station][2],
        )
        for station in observations
        if observations[station][-1][1] > statsDict[station][2]
    }

    return outliers


def write_statistics(filename, statistics):
    #writes each station's stats to the output file in alphabetical order
    #format used: Station A: min=60.0, max=80.0, mean=70.0
    stationNames = list(statistics.keys())
    stationNames.sort()

    with open(filename, "w", encoding="utf-8") as f:
        for station in stationNames:
            minTemp, maxTemp, meanTemp = statistics[station]
            line = f"{station}: min={minTemp:.1f}, max={maxTemp:.1f}, mean={meanTemp:.1f}\n"
            f.write(line)


def main():
    if len(sys.argv) != 3:
        print("usage: python p5_khan_aliyah.py input.txt output.txt")
        return

    inputFile = sys.argv[1]
    outputFile = sys.argv[2]

    try:
        observations, errors = read_observations(inputFile)
    except (FileNotFoundError, OSError) as e:
        print("something went wrong reading", inputFile, ":", e)
        return

    if errors:
        print("\nerrors found:")
        for lineNum, message in errors:
            print("line", lineNum, ":", message)

    statsDict = station_statistics(observations)
    outliersDict = station_outliers(observations)

    print("\nstation statistics:")
    stationNames = list(statsDict.keys())
    stationNames.sort()
    for station in stationNames:
        minTemp, maxTemp, meanTemp = statsDict[station]
        print(f"{station}: min={minTemp:.1f}, max={maxTemp:.1f}, mean={meanTemp:.1f}")

    print("\nstation outliers:")
    outlierStationNames = list(outliersDict.keys())
    outlierStationNames.sort()
    for station in outlierStationNames:
        latestDate, latestTemp, meanTemp = outliersDict[station]
        print(station, ":", latestDate, latestTemp, meanTemp)

    try:
        write_statistics(outputFile, statsDict)
    except (FileNotFoundError, OSError) as e:
        print("something went wrong writing to", outputFile, ":", e)
        return


class TestWeatherStats(unittest.TestCase):

    def setUp(self):
        #tracking every temp file made during a test so tearDown can clean them up
        self.tempPaths = []

    def tearDown(self):
        for path in self.tempPaths:
            if os.path.exists(path):
                os.remove(path)

    def make_temp_file(self, content):
        #writes content to a temp file and returns its path
        tempFile = tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False)
        tempFile.write(content)
        tempFile.close()
        self.tempPaths.append(tempFile.name)
        return tempFile.name

    def test_multiple_stations(self):
        content = (
            "Station A, 09:00:00 AM 04/20/2026, 70.0\n"
            "Station B, 09:00:00 AM 04/20/2026, 60.0\n"
            "Station A, 10:00:00 AM 04/20/2026, 75.0\n"
        )
        path = self.make_temp_file(content)
        observations, errors = read_observations(path)

        self.assertEqual(len(errors), 0)
        self.assertIn("Station A", observations)
        self.assertIn("Station B", observations)
        self.assertEqual(len(observations["Station A"]), 2)

    def test_negative_temperatures(self):
        content = "Station A, 09:00:00 AM 04/20/2026, -20.5\n"
        path = self.make_temp_file(content)
        observations, errors = read_observations(path)

        self.assertEqual(len(errors), 0)
        self.assertEqual(observations["Station A"][0][1], -20.5)

    def test_duplicate_observation(self):
        content = (
            "Station A, 09:00:00 AM 04/20/2026, 70.0\n"
            "Station A, 09:00:00 AM 04/20/2026, 72.0\n"
        )
        path = self.make_temp_file(content)
        observations, errors = read_observations(path)

        self.assertEqual(len(observations["Station A"]), 1)
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0][0], 2)

    def test_invalid_temperature_range(self):
        content = (
            "Station A, 09:00:00 AM 04/20/2026, 200.0\n"
            "Station A, 09:00:00 AM 04/21/2026, -150.0\n"
        )
        path = self.make_temp_file(content)
        observations, errors = read_observations(path)

        self.assertEqual(len(errors), 2)
        self.assertNotIn("Station A", observations)

    def test_station_statistics(self):
        content = (
            "Station A, 09:00:00 AM 04/20/2026, 60.0\n"
            "Station A, 09:00:00 AM 04/21/2026, 80.0\n"
        )
        path = self.make_temp_file(content)
        observations, errors = read_observations(path)

        statsDict = station_statistics(observations)
        minTemp, maxTemp, meanTemp = statsDict["Station A"]
        self.assertEqual(minTemp, 60.0)
        self.assertEqual(maxTemp, 80.0)
        self.assertEqual(meanTemp, 70.0)

    def test_sorted_observations_or_output(self):
        content = (
            "Station A, 09:00:00 AM 04/21/2026, 80.0\n"
            "Station A, 09:00:00 AM 04/20/2026, 60.0\n"
        )
        path = self.make_temp_file(content)
        observations, errors = read_observations(path)

        #checking the observations themselves are sorted by date
        dates = [entry[0] for entry in observations["Station A"]]
        self.assertEqual(dates, sorted(dates))

        #and checking write_statistics puts stations in lexicographic order
        statsDict = {
            "Station B": (60.0, 80.0, 70.0),
            "Station A": (50.0, 90.0, 70.0),
        }
        outPath = self.make_temp_file("")
        write_statistics(outPath, statsDict)

        with open(outPath, "r", encoding="utf-8") as f:
            lines = f.readlines()

        firstStation = lines[0].split(":")[0]
        secondStation = lines[1].split(":")[0]
        self.assertLess(firstStation, secondStation)

    def test_missing_input_file(self):
        with self.assertRaises((FileNotFoundError, OSError)):
            read_observations("thisfiledoesnotexist.txt")


if __name__ == "__main__":
    print("aliyah khan z23556724")
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        unittest.main(argv=[sys.argv[0]])
    else:
        main()