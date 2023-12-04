using System.Text.RegularExpressions;

var data = File.ReadLines("input.txt").ToList();

//Part1(data);
Part2(data);

void Part1(IEnumerable<string> data)
{
    var sum = 0;

    foreach (var s in data)
    {
        var re = @"Card (.*): (.*) \| (.*)";
        var match = Regex.Match(s, re);

        var cardNumber = match.Groups[1].ToString();
        var winningNumbers = new HashSet<int>(match.Groups[2].ToString().Split(" ").Where(x => !string.IsNullOrEmpty(x)).Select(x => int.Parse(x.Trim())));
        var myNumbers = match.Groups[3].ToString().Split(" ").Where(x => !string.IsNullOrEmpty(x)).Select(x => int.Parse(x.Trim())).ToList();

        var score = 0;
        
        myNumbers.ForEach(x =>
        {
            if (winningNumbers.Contains(x))
            {
                score = score == 0 ? 1 : score << 1;
            }
        });

        Console.WriteLine("Card {0}: {1}", cardNumber, score + 1);
        sum += score;
    }
    
    Console.WriteLine(sum);
}

void Part2(List<string> data)
{
    var sum = 0;
    var copiesDict = new Dictionary<int, int>();

    for (var i = 0; i < data.Count; i++)
    {
        var numberOfInstances = 1 + (copiesDict.ContainsKey(i) ? copiesDict[i] : 0);
        sum += 1 + (copiesDict.ContainsKey(i) ? copiesDict[i] : 0);
        
        var re = @"Card (.*): (.*) \| (.*)";
        var match = Regex.Match(data[i], re);
        var cardNumber = match.Groups[1].ToString();
        
        Console.WriteLine("{0} instances of card {1}", numberOfInstances, cardNumber);
        
        var winningNumbers = new HashSet<int>(match.Groups[2].ToString().Split(" ").Where(x => !string.IsNullOrEmpty(x)).Select(x => int.Parse(x.Trim())));
        var myNumbers = match.Groups[3].ToString().Split(" ").Where(x => !string.IsNullOrEmpty(x)).Select(x => int.Parse(x.Trim())).ToList();

        var score = 0;
        
        myNumbers.ForEach(x =>
        {
            if (winningNumbers.Contains(x))
            {
                var index = i + ++score;
                copiesDict[index] = copiesDict.ContainsKey(index) ? copiesDict[index] + 1 * numberOfInstances : 1 * numberOfInstances;
                Console.WriteLine("Card {0}: {1}", cardNumber, index + 1);
            }
        });
        
        Console.WriteLine("");
    }


    Console.WriteLine(sum);
}