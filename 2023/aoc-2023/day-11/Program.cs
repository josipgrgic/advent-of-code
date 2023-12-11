var data = File.ReadLines("input.txt").ToList();

var galaxyLocations = new List<(int, int)>();

var emptyRows = new HashSet<int>(Enumerable.Range(0, data.Count - 1));
var emptyColumns = new HashSet<int>(Enumerable.Range(0, data[0].Length - 1));

for (var i = 0; i < data.Count; i++)
{
    for (var j = 0; j < data[i].Length; j++)
    {
        if (data[i][j] == '.')
        {
            continue;
        }
        
        galaxyLocations.Add((i,j));
        emptyRows.Remove(i);
        emptyColumns.Remove(j);
    }
}

Part1(1000000);
void Part1(int emptySpaceDistanceValue = 2)
{
    double sum = 0;
    for (var i = 0; i < galaxyLocations.Count; i++)
    {
        var (g1i, g1j) = galaxyLocations[i];
        for (var j = i + 1; j < galaxyLocations.Count; j++)
        {
            var (g2i, g2j) = galaxyLocations[j];

            double result = 0;

            for (var k = Math.Min(g1i, g2i) + 1; k <= Math.Max(g1i, g2i); k++)
            {
                if (emptyRows.Contains(k))
                {
                    result += emptySpaceDistanceValue;
                }
                else
                {
                    result++;
                }
            }
            
            for (var k = Math.Min(g1j, g2j) + 1; k <= Math.Max(g1j, g2j); k++)
            {
                if (emptyColumns.Contains(k))
                {
                    result += emptySpaceDistanceValue;
                }
                else
                {
                    result++;
                }
            }

            Console.WriteLine("Between galaxy {0} and galaxy {1}: {2}", i + 1, j + 1, result);
            sum += result;
        }
    }
    
    Console.WriteLine(sum);
}