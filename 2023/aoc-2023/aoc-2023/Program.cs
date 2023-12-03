var data = File.ReadLines("day-01/input.txt");

void Part1(IEnumerable<string> data)
{
    var sum = 0;

    foreach (var s in data)
    {
        var first = -1;
        var last = -1;

        foreach (var t in s)
        {
            if (!char.IsNumber(t))
            {
                continue;
            }

            var number = t - '0';

            if (first == -1)
            {
                first = number;
            }

            last = number;
        }

        var calibrationValue = 10 * first + last;
    
        Console.WriteLine(calibrationValue);
    
        sum += calibrationValue;
    }

    Console.WriteLine(sum);
}

//Part1(data);

void Part2(IEnumerable<string> data)
{
    // one, two, three, four, five, six, seven, eight, and nine
    var numbers = new List<string> { "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };
    var numbersMap = numbers.Select((x, i) => new { x, i }).ToDictionary(kv => kv.x, kv => kv.i + 1);
    
    var numbersReversed = new List<string> { "eno", "owt", "eerht", "ruof", "evif", "xis", "neves", "thgie", "enin" };
    var numbersReversedMap = numbersReversed.Select((x, i) => new { x, i }).ToDictionary(kv => kv.x, kv => kv.i + 1);
    
    var sum = 0;

    foreach (var s in data)
    {
        var first = -1;
        var substrings = new List<string>();
        for (var i = 0; i < s.Length; i++)
        {
            if (char.IsNumber(s[i]))
            {
                first = s[i] - '0';
                break;
            }

            var charString = s[i].ToString();
            for (var j = 0; j < substrings.Count; j++)
            {
                substrings[j] += charString;
                if (numbersMap.TryGetValue(substrings[j], out var value))
                {
                    first = value;
                    break;
                }
            }

            if (first != -1)
            {
                break;
            }
            
            substrings.Add(charString);
        }
        
        substrings.Clear();
        var last = -1;
        for (var i = s.Length-1; i >= 0; i--)
        {
            if (char.IsNumber(s[i]))
            {
                last = s[i] - '0';
                break;
            }

            var charString = s[i].ToString();
            for (var j = 0; j < substrings.Count; j++)
            {
                substrings[j] += charString;
                if (numbersReversedMap.TryGetValue(substrings[j], out var value))
                {
                    last = value;
                    break;
                }
            }
            
            if (last != -1)
            {
                break;
            }
            
            substrings.Add(charString);
        }

        var calibrationValue = 10 * first + last;
    
        Console.WriteLine(calibrationValue);
    
        sum += calibrationValue;
    }

    Console.WriteLine(sum);
}

Part2(data);