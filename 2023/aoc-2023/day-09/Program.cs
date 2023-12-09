var data = File.ReadLines("input.txt").ToList();

var inputs = data.Select(x => x.Split(" ").Select(int.Parse).ToList()).ToList();

Part1And2();
void Part1And2()
{
    var sum = 0;
    var sum2 = 0;
    for (var i = 0; i < inputs.Count; i++)
    {
        Console.WriteLine("---------------------------");
        var numbers = inputs[i];

        var sequences = new List<List<int>>();
        
        sequences.Add(numbers);
        Console.WriteLine(string.Join(" ", numbers));

        while (sequences[^1].Any(x => x != 0))
        {
            var newSequence = new List<int>();
            for (var j = 1; j < sequences[^1].Count; j++)
            {
                newSequence.Add(sequences[^1][j] - sequences[^1][j- 1]);
            }
            
            sequences.Add(newSequence);
            Console.WriteLine(string.Join(" ", newSequence));
        }

        var diff = 0;
        var diff2 = 0;
        for (var j = sequences.Count - 2; j >= 0; j--)
        {
            diff = sequences[j][sequences[j].Count - 1] + diff;
            diff2 = sequences[j][0] - diff2;
        }

        sum += diff;
        sum2 += diff2;
        Console.WriteLine("next value: {0}", diff);
        Console.WriteLine("previous value: {0}", diff2);
    }

    Console.WriteLine(sum);
    Console.WriteLine(sum2);
}