using System.Diagnostics;
using System.Text.RegularExpressions;

var data = File.ReadLines("input.txt").ToList();

var almanac = GetAlmanac(data);
var stopwatch = Stopwatch.StartNew();
Part2(almanac);
stopwatch.Stop();
Console.WriteLine(stopwatch.Elapsed.TotalMilliseconds);

var seeds = new List<double>();

for (var i = 0; i < almanac.Seeds.Count; i += 2)
{
    for (var j = 0; j < almanac.Seeds[i + 1]; j++)
    {
        seeds.Add(almanac.Seeds[i] + j);
    }
}

almanac.Seeds = seeds;

stopwatch = Stopwatch.StartNew();
Part1(almanac);
stopwatch.Stop();
Console.WriteLine(stopwatch.Elapsed.TotalMilliseconds);

void Part1(Almanac almanac)
{
    var closestLocation = double.MaxValue;

    var seedToLocationMappings = new Dictionary<double, List<double>>();
    
    almanac.Seeds.ForEach(x =>
    {
        seedToLocationMappings[x] = new List<double> { x };
        var mappedNumber = x;

        foreach (var almanacMap in almanac.Maps)
        {
            foreach (var mapEntry in almanacMap.MapEntries)
            {
                if (mappedNumber >= mapEntry.SourceRangeStart &&
                    mappedNumber <= mapEntry.SourceRangeStart + mapEntry.RangeLength - 1)
                {
                    mappedNumber = mapEntry.DestinationRangeStart + mappedNumber - mapEntry.SourceRangeStart;
                    break;
                }
            }
            
            seedToLocationMappings[x].Add(mappedNumber);
        }

        if (mappedNumber < closestLocation)
        {
            closestLocation = mappedNumber;
        }
    });
    
    Console.WriteLine(closestLocation);
}

void Part2(Almanac almanac)
{
    var ranges = new List<(double, double)>();

    for (int i = 0; i < almanac.Seeds.Count; i+= 2)
    {
        ranges.Add((almanac.Seeds[i], almanac.Seeds[i] + almanac.Seeds[i+1] - 1));
    }
    
    foreach (var almanacMap in almanac.Maps)
    {
        var newRanges = new List<(double, double)>();

        for (var i = 0; i < ranges.Count; i++)
        {
            var (rangeFrom, rangeTo) = ranges[i];
            var rangeMapped = false;
            
            foreach (var almanacMapEntry in almanacMap.MapEntries)
            {
                if (rangeFrom >= almanacMapEntry.SourceRangeStart + almanacMapEntry.RangeLength)
                {
                    continue;
                }

                if (rangeTo < almanacMapEntry.SourceRangeStart)
                {
                    continue;
                }

                rangeMapped = true;

                var intersectRangeStart = Math.Max(rangeFrom, almanacMapEntry.SourceRangeStart);
                var intersectRangeEnd = Math.Min(rangeTo,
                    almanacMapEntry.SourceRangeStart + almanacMapEntry.RangeLength - 1);
                
                var mappedRangeStart = almanacMapEntry.DestinationRangeStart + intersectRangeStart - almanacMapEntry.SourceRangeStart;
                var mappedRangeEnd = almanacMapEntry.DestinationRangeStart + intersectRangeEnd - almanacMapEntry.SourceRangeStart;
                
                newRanges.Add((mappedRangeStart, mappedRangeEnd));

                // add the parts of the original range that are not contained in the matched range
                if (rangeFrom < almanacMapEntry.SourceRangeStart)
                {
                    ranges.Add((rangeFrom, almanacMapEntry.SourceRangeStart-1));
                }
                
                if (rangeTo > almanacMapEntry.SourceRangeStart + almanacMapEntry.RangeLength - 1)
                {
                    ranges.Add((almanacMapEntry.SourceRangeStart + almanacMapEntry.RangeLength, rangeTo));
                }

                break;
            }

            if (!rangeMapped)
            {
                newRanges.Add((rangeFrom, rangeTo));
            }
        }

        ranges = newRanges;
    }

    var smallestLocation = double.MaxValue;
    
    ranges.ForEach(x =>
    {
        if (x.Item1 < smallestLocation)
        {
            smallestLocation = x.Item1;
        }
    });
    
    Console.WriteLine(smallestLocation);
}

Almanac GetAlmanac(List<string> data)
{
    var almanac = new Almanac();

    almanac.Seeds = Regex.Match(data[0], "seeds: (.*)")
        .Groups[1]
        .ToString()
        .Split(" ")
        .Select(x => double.Parse(x.Trim()))
        .ToList();

    var currentMap = new Map();
    var re = new Regex("(\\d+) (\\d+) (\\d+)");
    
    for (var i = 3; i < data.Count; i++)
    {
        if (string.IsNullOrEmpty(data[i]))
        {
            almanac.Maps.Add(currentMap);
            currentMap = new Map();
            continue;
        }

        if (data[i].Contains("map"))
        {
            continue;
        }

        var mapEntryMatch = re.Match(data[i]);
        currentMap.MapEntries.Add(new MapEntry
        {
            DestinationRangeStart = double.Parse(mapEntryMatch.Groups[1].ToString()),
            SourceRangeStart = double.Parse(mapEntryMatch.Groups[2].ToString()),
            RangeLength = double.Parse(mapEntryMatch.Groups[3].ToString())
        });
    }
    almanac.Maps.Add(currentMap);

    return almanac;
}


class Almanac
{
    public List<double> Seeds { get; set; } = new();
    public List<Map> Maps { get; set; } = new();
}

class Map
{
    public List<MapEntry> MapEntries { get; set; } = new();
}

class MapEntry
{
    public double DestinationRangeStart { get; set; }
    public double SourceRangeStart { get; set; }
    public double RangeLength { get; set; }
}