// See https://aka.ms/new-console-template for more information

var lines = File.ReadAllLines("./Day08/input.txt").ToList();
//var lines = File.ReadAllLines("./Day08/example.txt").ToList();

var matrix = new int[lines.Count,lines[0].Length];

var i = 0;
lines.ForEach(line =>
{
    var j = 0;
    foreach (var c in line.ToCharArray())
    {
        matrix[i, j++] = c - '0';
    }

    i++;
});

First();

void First()
{
    var visibleTreeLocations = new HashSet<(int, int)>();
    
    var iterate = 
        ((int, int) start, (int, int) end, (int, int) increment) =>
        {
            var max = -1;
            var current = start;

            var last = (end.Item1 + increment.Item1, end.Item2 + increment.Item2);
            while (current != last)
            {
                var treeHeight = matrix[current.Item1, current.Item2];

                if (treeHeight > max)
                {
                    visibleTreeLocations.Add(current);
                    max = treeHeight;
                }
                
                current = (current.Item1 + increment.Item1, current.Item2 + increment.Item2);
            }
        };

    for (var i = 0; i < matrix.GetLength(0); i++)
    {
        iterate((i, 0), (i, matrix.GetLength(1)-1), (0, 1));
        iterate((i, matrix.GetLength(1)-1), (i, 0), (0, -1));
    }
    
    for (var j = 0; j < matrix.GetLength(1); j++)
    {
        iterate((0, j), (matrix.GetLength(0)-1, j), (1, 0));
        iterate((matrix.GetLength(0)-1, j), (0, j), (-1, 0));
    }
    
    Console.WriteLine(visibleTreeLocations.Count);
}

Second();

void Second()
{
    var leftMatrix = new int[matrix.GetLength(0), matrix.GetLength(1)];

    for (var i = 0; i < matrix.GetLength(0); i++)
    {
        var latestOccurrences = Enumerable.Repeat(0, 10).ToArray();
        for (var j = 0; j < matrix.GetLength(1); j++)
        {
            calculateViewingDistance(leftMatrix, i, j, j, latestOccurrences);
        }
    }
    
    var rightMatrix = new int[matrix.GetLength(0), matrix.GetLength(1)];
    for (var i = 0; i < matrix.GetLength(0); i++)
    {
        var latestOccurrences = Enumerable.Repeat(matrix.GetLength(1)-1, 10).ToArray();
        for (var j = matrix.GetLength(1) - 1; j >= 0; j--)
        {
            calculateViewingDistance(rightMatrix, i, j, j, latestOccurrences);
        }
    }
    
    var topMatrix = new int[matrix.GetLength(0), matrix.GetLength(1)];
    for (var j = 0; j < matrix.GetLength(1); j++)
    {
        var latestOccurrences = Enumerable.Repeat(0, 10).ToArray();
        for (var i = 0; i < matrix.GetLength(0); i++)
        {
            calculateViewingDistance(topMatrix, i, j, i, latestOccurrences);
        }
    }
    
    var bottomMatrix = new int[matrix.GetLength(0), matrix.GetLength(1)];
    for (var j = 0; j < matrix.GetLength(1); j++)
    {
        var latestOccurrences = Enumerable.Repeat(matrix.GetLength(0)-1, 10).ToArray();
        for (var i = matrix.GetLength(0) - 1; i >= 0; i--)
        {
            calculateViewingDistance(bottomMatrix, i, j, i, latestOccurrences);
        }
    }

    var maxScenicScore = 0;
    
    for (var i = 0; i < matrix.GetLength(0); i++)
    {
        for (var j = 0; j < matrix.GetLength(1); j++)
        {
            var scenicScore = leftMatrix[i,j] * rightMatrix[i,j] * topMatrix[i,j] * bottomMatrix[i, j];
            if (scenicScore > maxScenicScore)
            {
                maxScenicScore = scenicScore;
            }
        }
    }
    
    Console.WriteLine(maxScenicScore);
}

void calculateViewingDistance(int[,] m, int i, int j, int position, int[] latestOccurrences)
{
    var treeHeight = matrix[i, j];

    var viewingDistance = Int32.MaxValue;

    for (var k = treeHeight; k < 10; k++)
    {
        viewingDistance = Math.Min(viewingDistance, Math.Abs(position - latestOccurrences[k]));
    }
            
    latestOccurrences[treeHeight] = position;
    m[i, j] = viewingDistance;
}



