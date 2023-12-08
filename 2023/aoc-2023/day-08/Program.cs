using System.Text.RegularExpressions;

var data = File.ReadLines("input.txt").ToList();

var nodeMap = new Dictionary<string, Node>();

for (var i = 2; i < data.Count; i++)
{
    var match = Regex.Match(data[i], "(.*) = \\((.*), (.*)\\)");

    nodeMap[match.Groups[1].ToString()] = new Node
    {
        Name = match.Groups[1].ToString(),
        Map = new Dictionary<string, string>
        {
            { "L", match.Groups[2].ToString() },
            { "R", match.Groups[3].ToString() },
        }
    };
}

//Part1();
Part2();

void Part1()
{
    var stepsNeeded = 0;
    var i = 0;
    var location = "AAA";
    while (true)
    {
        stepsNeeded++;
        location = nodeMap[location].Map[data[0][i++ % data[0].Length].ToString()];

        if (location == "ZZZ")
        {
            break;
        }
    }
    
    Console.WriteLine(stepsNeeded);
}

void Part2()
{
    var stepsNeeded = 0;
    var nodeLocations = new List<string>();
    var nodeSteps = new List<int>();
    
    foreach (var nodeMapKey in nodeMap.Keys)
    {
        if (nodeMapKey[2] == 'A')
        {
            nodeLocations.Add(nodeMapKey);
            nodeSteps.Add(0);
        }
    }
    
    var i = 0;
    while (true)
    {
        var stillGoing = false;
        for (var j = 0; j < nodeLocations.Count; j++)
        {

            if (nodeLocations[j][2] == 'Z')
            {
                continue;
            }

            stillGoing = true;
            nodeLocations[j] = nodeMap[nodeLocations[j]].Map[data[0][i % data[0].Length].ToString()];
            nodeSteps[j]++;
        }

        if (!stillGoing)
        {
            break;
        }
        
        i++;
        stepsNeeded++;
    }

    double result = nodeSteps[0];

    for (var j = 1; j < nodeSteps.Count; j++)
    {
        result = determineLCM(result, nodeSteps[j]);
    } 
    
    Console.WriteLine(result.ToString("F99").TrimEnd('0'));
}

double determineLCM(double a, double b)
{
    double num1, num2;
    if (a > b)
    {
        num1 = a; num2 = b;
    }
    else
    {
        num1 = b; num2 = a;
    }

    for (double i = 1; i < num2; i++)
    {
        var mult = num1 * i;
        if (mult % num2 == 0)
        {
            return mult;
        }
    }
    return num1 * num2;
}

class Node
{
    public string Name { get; set; }
    public Dictionary<string, string> Map { get; set; }
}