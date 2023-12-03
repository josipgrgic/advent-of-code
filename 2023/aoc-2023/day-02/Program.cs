using System.Text.RegularExpressions;

var data = File.ReadLines("input.txt");

var totalCubesLookup = new Dictionary<string, int>
{
    {"red", 12},
    {"green", 13},
    {"blue", 14}
};

List<Game> parseGames(IEnumerable<string> data)
{
    var games = new List<Game>();

    foreach (var s in data)
    {
        var re = @"Game (\d+): (.*)";
        var match = Regex.Match(s, re);

        var gameId = match.Groups[1].ToString();
        var subsets = match.Groups[2].ToString();

        var game = new Game
        {
            Id = int.Parse(gameId),
            Subsets = new List<Subset>()
        };
        
        games.Add(game);

        var subsetList = subsets.Split(";");
        
        foreach (var subset in subsetList)
        {
            var subsetResult = new Subset
            {
                CubeCounts = new List<CubeCount>()
            };
            game.Subsets.Add(subsetResult);
            
            var diceCounts = subset.Split(",");

            foreach (var diceCount in diceCounts)
            {
                var dcs = diceCount.Trim().Split(" ");
                var cubeCount = new CubeCount
                {
                    Count = int.Parse(dcs[0]),
                    Color = dcs[1]
                };
                
                subsetResult.CubeCounts.Add(cubeCount);
            }
        }
    }

    return games;
}

var games = parseGames(data);
Part1(games, totalCubesLookup);
Part2(games, totalCubesLookup);

void Part1(List<Game> games, Dictionary<string, int> totalCubesLookup)
{
    var sum = 0;
    
    games.ForEach(game =>
    {
        var isvalid = true;
        
        foreach (var cubeCount in game.Subsets.SelectMany(x => x.CubeCounts))
        {
            if (totalCubesLookup[cubeCount.Color] < cubeCount.Count)
            {
                isvalid = false;
                Console.WriteLine("Game {0} is not valid: {1} : {2}", game.Id, cubeCount.Color, cubeCount.Count);
                break;
            }
        }

        if (isvalid)
        {
            sum += game.Id;
        }
    });
    
    Console.WriteLine(sum);
}

void Part2(List<Game> games, Dictionary<string, int> totalCubesLookup)
{
    var sum = 0;
    
    games.ForEach(game =>
    {
        var minCubesNeededDict = new Dictionary<string, int>();
        
        foreach (var cubeCount in game.Subsets.SelectMany(x => x.CubeCounts))
        {
            if (!minCubesNeededDict.ContainsKey(cubeCount.Color) ||
                minCubesNeededDict[cubeCount.Color] < cubeCount.Count)
            {
                minCubesNeededDict[cubeCount.Color] = cubeCount.Count;
            }
        }
        
        

        Console.WriteLine("Game {0}", game.Id);
        minCubesNeededDict.Keys.ToList().ForEach(x =>
        {
            Console.WriteLine("{0}:{1}", x, minCubesNeededDict[x]);
        });
        
        Console.WriteLine(minCubesNeededDict.Values.Aggregate(1, (total, next) => total * next));
        sum += minCubesNeededDict.Values.Aggregate(1, (total, next) => total * next);
        Console.WriteLine("");
    });
    
    Console.WriteLine(sum);
}

class Game
{
    public int Id;
    public List<Subset> Subsets;
}

class Subset
{
    public List<CubeCount> CubeCounts;
}

class CubeCount
{
    public string Color;
    public int Count;
}


