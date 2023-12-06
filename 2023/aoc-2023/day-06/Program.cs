using System.Text.RegularExpressions;

var data = File.ReadLines("input.txt").ToList();

var timeString = Regex.Match(data[0], "Time: (.*)").Groups[1].ToString();
var distanceString = Regex.Match(data[1], "Distance: (.*)").Groups[1].ToString();

var times = timeString.Trim().Split(" ").Where(x => !string.IsNullOrEmpty(x)).Select(x => double.Parse(x.Trim())).ToList();
var distances = distanceString.Trim().Split(" ").Where(x => !string.IsNullOrEmpty(x)).Select(x => double.Parse(x.Trim())).ToList();

Part1(times, distances);

var bigTime = double.Parse(string.Join("", times));
var bigDistance = double.Parse(string.Join("", distances));

Part1(new List<double> {bigTime}, new List<double> {bigDistance});

void Part1(List<double> times, List<double> distances)
{
    double result = 1;

    for (var i = 0; i < times.Count; i++)
    {
        var timeAvailable = (double)times[i];
        var distanceToBeat = (double)distances[i];

        var x1 = timeAvailable / 2 - Math.Sqrt(timeAvailable * timeAvailable - 4 * distanceToBeat) / 2;
        var x2 = timeAvailable / 2 + Math.Sqrt(timeAvailable * timeAvailable - 4 * distanceToBeat) / 2;
        
        Console.WriteLine("x1: {0}", x1);
        Console.WriteLine("x2: {0}", x2);

        var x1Int = Math.Ceiling(x1);
        var x2Int = Math.Floor(x2);

        var raceResult = x2Int - x1Int + 1 - (Math.Abs(x1 - x1Int) < Double.Epsilon ? 1 : 0) - (Math.Abs(x2 - x2Int) < Double.Epsilon ? 1 : 0);
        
        Console.WriteLine(raceResult);
        result *= raceResult;
    }
    
    Console.WriteLine(result);
}
