var data = File.ReadLines("input.txt").ToList();

//Part1(data);

Part2(data);

void Part1(List<string> data)
{
    var sum = 0;

    for (var i = 0; i < data.Count; i++)
    {
        for (var j = 0; j < data[i].Length; j++)
        {
            if (!char.IsNumber(data[i][j]))
            {
                continue;
            }

            var numberLenght = 0;
            var digits = new List<int>();
            for (var k = j; k < data[i].Length; k++)
            {
                if (char.IsNumber(data[i][k]))
                {
                    numberLenght++;
                    digits.Add(data[i][k] - '0');
                }
                else
                {
                    break;
                }
            }

            var isAdjecentToSymbol = false;
            var minI = Math.Max(i - 1, 0);
            var maxI = Math.Min(i + 1, data.Count-1);
            var minJ = Math.Max(j - 1, 0);
            var maxJ = Math.Min(j + numberLenght, data[i].Length-1);

            for (var k = minI; k <= maxI; k++)
            {
                for (var l = minJ; l <= maxJ; l++)
                {
                    if (char.IsNumber(data[k][l]))
                    {
                        continue;
                    }

                    if (data[k][l] != '.')
                    {
                        isAdjecentToSymbol = true;
                        break;
                    }
                }

                if (isAdjecentToSymbol)
                {
                    break;
                }
            }

            var number = 0;
            digits.Reverse();
            digits.Select((x, index) =>
            {
                number += (int)(x * Math.Pow(10, index));
                return 0;
            }).ToList();
            
            if (isAdjecentToSymbol)
            {
                Console.WriteLine("{0} is adjecent to a symbol", number);
                sum += number;
            }
            else
            {
                Console.WriteLine("{0} is not adjecent to a symbol", number);
            }

            j += numberLenght - 1;
        }
    }
    
    Console.WriteLine(sum);
}

void Part2(List<string> data)
{
    var sum = 0;

    var gearLookup = new Dictionary<(int, int), List<int>>();
    
    for (var i = 0; i < data.Count; i++)
    {
        for (var j = 0; j < data[i].Length; j++)
        {
            if (!char.IsNumber(data[i][j]))
            {
                continue;
            }

            var numberLenght = 0;
            var digits = new List<int>();
            for (var k = j; k < data[i].Length; k++)
            {
                if (char.IsNumber(data[i][k]))
                {
                    numberLenght++;
                    digits.Add(data[i][k] - '0');
                }
                else
                {
                    break;
                }
            }
            
            var number = 0;
            digits.Reverse();
            digits.Select((x, index) =>
            {
                number += (int)(x * Math.Pow(10, index));
                return 0;
            }).ToList();

            var isAdjecentToSymbol = false;
            var minI = Math.Max(i - 1, 0);
            var maxI = Math.Min(i + 1, data.Count-1);
            var minJ = Math.Max(j - 1, 0);
            var maxJ = Math.Min(j + numberLenght, data[i].Length-1);

            for (var k = minI; k <= maxI; k++)
            {
                for (var l = minJ; l <= maxJ; l++)
                {
                    if (data[k][l] == '*')
                    {
                        isAdjecentToSymbol = true;
                        if (!gearLookup.ContainsKey((k, l)))
                        {
                            gearLookup[(k, l)] = new List<int>();
                        }
                        gearLookup[(k, l)].Add(number);
                    }
                }

                if (isAdjecentToSymbol)
                {
                    break;
                }
            }

            j += numberLenght - 1;
        }
    }
    
    gearLookup.Values.ToList().ForEach(x =>
    {
        if (x.Count == 2)
        {
            sum += x[0] * x[1];
        }
    });
    
    Console.WriteLine(sum);
}