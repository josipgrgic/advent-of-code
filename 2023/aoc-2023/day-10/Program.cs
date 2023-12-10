var data = File.ReadLines("input.txt").ToList();

var tileTypeLookup = new Dictionary<char, IPipeConnection>
{
    { '|', new PipeConnection(-1, 0, 1, 0, '|')},  // north and south
    { '-', new PipeConnection(0, 1, 0, -1, '-')},  // east and west
    { 'L', new PipeConnection(-1, 0, 0, 1, 'L')},  // north and east
    { 'J', new PipeConnection(-1, 0, 0, -1, 'J')}, // north and west
    { '7', new PipeConnection(1, 0, 0, -1, '7')},  // south and west
    { 'F', new PipeConnection(1, 0, 0, 1, 'F')},   // south and east
    {'.', new NoPipeConnection()},
    {'S', new AnimalPipeConnection()}
};

var pipeElements = new HashSet<(int, int)>();


Part1();

var newMap = TransformMap();

Part2(newMap);

// Process the input, print the solution, and fill the pipeElements collection with all pipes that form the loop we seek
void Part1()
{
    var startI = 0;
    var startJ = 0;

    for (var i = 0; i < data.Count; i++)
    {
        for (var j = 0; j < data[i].Length; j++)
        {
            if (data[i][j] != 'S')
            {
                continue;
            }

            startI = i;
            startJ = j;
            break;
        }
    }

    var pipeLenght = 0;

    var currentI = startI;
    var currentJ = startJ;
    var lastI = startI;
    var lastJ = startJ;
    
    pipeElements.Add((currentI, currentJ));

    do
    {
        pipeLenght++;

        for (var i = currentI - 1; i <= currentI + 1; i++)
        {
            var foundNext = false;
            if (i < 0 || i > data.Count - 1)
            {
                continue;
            }

            for (var j = currentJ - 1; j <= currentJ + 1; j++)
            {

                if (j < 0 || j > data[i].Length - 1)
                {
                    continue;
                }

                if (i == currentI && j == currentJ)
                {
                    continue;
                }
                
                if (i == lastI && j == lastJ)
                {
                    continue;
                }
                
                var nextPipe = tileTypeLookup[data[i][j]];
                var currentPipe = tileTypeLookup[data[currentI][currentJ]];

                if (currentPipe.ConnectsPipe(currentI, currentJ, i, j) 
                    && nextPipe.ConnectsPipe(i, j , currentI, currentJ))
                {
                    lastI = currentI;
                    lastJ = currentJ;

                    currentI = i;
                    currentJ = j;
                    foundNext = true;
                    break;
                }
                
            }

            if (foundNext)
            {
                Console.WriteLine("Next pipe: {0}, ({1}, {2})", data[currentI][currentJ], currentI, currentJ);
                pipeElements.Add((currentI, currentJ));
                break;
            }
        }
    } while (currentI != startI || currentJ != startJ);
    
    Console.WriteLine(pipeLenght / 2);
}

// First, clear all the junk pipes (the ones that do not belong to the loop)
// Then, enlarge the pipe. For example:
// ..........
// .F------7.
// .|F----7|.
// .||....||.
// .||....||.
// .|L-7F-J|.
// .|..||..|.
// .L--JL--J.
// ..........
// becomes 
//,,,,,,,,,,,,,,,,,,,
//.,F-------------7,.
//,,|,,,,,,,,,,,,,|,,
//.,|,F---------7,|,.
//,,|,|,,,,,,,,,|,|,,
//.,|,|,.,.,.,.,|,|,.
//,,|,|,,,,,,,,,|,|,,
//.,|,|,.,.,.,.,|,|,.
//,,|,|,,,,,,,,,|,|,,
//.,|,L---7,F---J,|,.
//,,|,,,,,|,|,,,,,|,,
//.,|,.,.,|,|,.,.,|,.
//,,|,,,,,|,|,,,,,|,,
//.,L-----J,L-----J,.
//,,,,,,,,,,,,,,,,,,,
//.,.,.,.,.,.,.,.,.,.
// the comma (,) characters are empty spaces we added
char[,] TransformMap()
{
    var pipeList = pipeElements.ToList();
    var newMap = new char[data.Count,data[0].Length];
    
    for (var i = 0; i < data.Count; i++)
    {
        for (var j = 0; j < data[i].Length; j++)
        {
            if (pipeElements.Contains((i, j)))
            {
                newMap[i,j] = data[i][j];

                if (newMap[i, j] == 'S')
                {
                    var x = (pipeList.Last().Item1 - i, pipeList.Last().Item2 - j, pipeList[1].Item1 - i, pipeList[1].Item2 - j);
                
                    if (x == (-1, 0, 1, 0))
                    {
                        newMap[i, j] = '|';
                    }
                    if (x == (0, 1, 0, -1))
                    {
                        newMap[i, j] = '-';
                    }
                    if (x == (-1, 0, 0, 1))
                    {
                        newMap[i, j] = 'L';
                    }
                    if (x == (-1, 0, 0, -1))
                    {
                        newMap[i, j] = 'J';
                    }
                    if (x == (1, 0, 0, -1))
                    {
                        newMap[i, j] = '7';
                    }
                    if (x == (1, 0, 0, 1))
                    {
                        newMap[i, j] = 'F';
                    }
                }
            }
            else
            {
                newMap[i, j] = '.';
            }
        }
    }
    
    PrintMap(newMap);
    
    var enlargedMap = new char[newMap.GetLength(0) * 2 - 1, newMap.GetLength(1) * 2 - 1];

    for (var i = 0; i < newMap.GetLength(0); i++)
    {
        for (var j = 0; j < newMap.GetLength(1); j++)
        {
            enlargedMap[i*2, j * 2] = newMap[i, j];

            if (j == newMap.GetLength(1) - 1)
            {
                continue;
            }
        
            if (newMap[i, j] == '.' || newMap[i, j+1] == '.')
            {
                enlargedMap[i*2, j * 2 + 1] = ',';
                continue;
            }
        
            var currentPipe = tileTypeLookup[newMap[i, j]];

            if (currentPipe.ConnectsPipe(i,j,i, j+1))
            {
                enlargedMap[i*2, j * 2 + 1] = '-';
            }
            else
            {
                enlargedMap[i*2, j * 2 + 1] = ',';
            }
        }
    }

    for (var j = 0; j < enlargedMap.GetLength(1); j++)
    {
        for (var i = 0; i < enlargedMap.GetLength(0); i += 2)
        {
            if (i+1 >= enlargedMap.GetLength(0))
            {
                continue;
            }
        
            if (enlargedMap[i, j] == '.' || enlargedMap[i+2, j] == '.' || enlargedMap[i, j] == ',' || enlargedMap[i+2, j] == ',')
            {
                enlargedMap[i+1, j] = ',';
                continue;
            }
        
            var currentPipe = tileTypeLookup[enlargedMap[i, j]];

            if (currentPipe.ConnectsPipe(i,j,i+1, j))
            {
                enlargedMap[i+1, j] = '|';
            }
            else
            {
                enlargedMap[i+1, j] = ',';
            }
        }
    }

    PrintMap(enlargedMap);

    return enlargedMap;
}

// start from the sides of the map
// "color" all empty spaces that are reachable with "O"
// finally, the number of the "." characters that remain are the desired answer
void Part2(char[,] map)
{
    var enqueueHistory = new HashSet<(int, int)>();
    var queue = new Queue<(int, int)>();
    for (var i = 0; i < map.GetLength(0); i++)
    {
        for (var j = 0; j < map.GetLength(1); j++)
        {
            if (map[i, j] != '.' && map[i, j] != ',')
            {
                continue;
            }
            
            if (i == 0 || i == map.GetLength(0) - 1)
            {
                queue.Enqueue((i,j));
                enqueueHistory.Add((i, j));
            }
            
            if (j == 0 || j == map.GetLength(1) - 1)
            {
                queue.Enqueue((i,j));
                enqueueHistory.Add((i, j));
            }
        }
    }

    while (queue.TryDequeue(out var el))
    {
        if (map[el.Item1, el.Item2] == '.' || map[el.Item1, el.Item2] == ',')
        {
            map[el.Item1, el.Item2] = 'O';
        }

        for (var i = el.Item1 - 1; i <= el.Item1 + 1; i++)
        {
            if (i < 0 || i > map.GetLength(0) - 1)
            {
                continue;
            }

            for (var j = el.Item2 - 1; j <= el.Item2 + 1; j++)
            {
                if (j < 0 || j > map.GetLength(1) - 1)
                {
                    continue;
                }

                if ((map[i, j] == '.' || map[i, j] == ',') && !enqueueHistory.Contains((i, j)))
                {
                    enqueueHistory.Add((i, j));
                    queue.Enqueue((i,j));
                }
            }
        }
    }
    
    PrintMap(map);

    var count = 0;
    
    for (var i = 0; i < map.GetLength(0); i++)
    {
        for (var j = 0; j < map.GetLength(1); j++)
        {
            if (map[i, j] == '.')
            {
                count++;
            }
        }
    }
    Console.WriteLine();
    Console.WriteLine(count);
}

void PrintMap(char[,] map)
{
    Console.WriteLine();
    Console.WriteLine("----------------------");
    for (var i = 0; i < map.GetLength(0); i++)
    {
        Console.WriteLine();
        for (var j = 0; j < map.GetLength(1); j++)
        {
            Console.Write(map[i, j]);
        }
    }
    
    Console.WriteLine();
}

interface IPipeConnection
{
    bool ConnectsPipe(int pipeI, int pipeJ, int currentI, int currentJ);
}

class PipeConnection : IPipeConnection
{
    public char Character { get; set; }
    public (int, int) From { get; set; }
    public (int, int) To { get; set; }

    public PipeConnection(int fromI, int fromJ, int toI, int toJ, char character)
    {
        From = (fromI, fromJ);
        To = (toI, toJ);
        Character = character;
    }

    private bool FromConnects(int pipeI, int pipeJ, int currentI, int currentJ)
    {
        return currentI == pipeI + From.Item1 && currentJ == pipeJ + From.Item2;
    }
    
    private bool ToConnects(int pipeI, int pipeJ, int currentI, int currentJ)
    {
        return currentI == pipeI + To.Item1 && currentJ == pipeJ + To.Item2;
    }

    public virtual bool ConnectsPipe(int pipeI, int pipeJ, int currentI, int currentJ)
    {
        return FromConnects(pipeI, pipeJ, currentI, currentJ) || ToConnects(pipeI, pipeJ, currentI, currentJ);
    }
}

class NoPipeConnection : IPipeConnection
{
    public bool ConnectsPipe(int pipeI, int pipeJ, int currentI, int currentJ)
    {
        return false;
    }
}

class AnimalPipeConnection : IPipeConnection
{
    public bool ConnectsPipe(int pipeI, int pipeJ, int currentI, int currentJ)
    {
        return true;
    }
}