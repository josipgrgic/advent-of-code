using System.Text.RegularExpressions;


namespace Day02
{
    class Program
    {
        static void Main(string[] args)
        {
            var lines = File.ReadAllLines("./input.txt");
            // var lines = File.ReadAllLines("./input.example");

            var commands = lines.Select(x =>
                {
                    var match = Regex.Matches(x, @"(\w*) (\d*)", RegexOptions.IgnoreCase);
                    return (Position: match[0].Groups[1].Value, Amount: int.Parse(match[0].Groups[2].Value));
                }).ToList();


            First(commands);
        }

        static void First(List<(string Position, int Amount)> commands)
        {
            var horizontal = 0;
            var depth = 0;
            var aim = 0;

            commands.ForEach(x =>
            {
                switch (x.Position)
                {
                    case "forward":
                        horizontal += x.Amount;
                        depth += aim * x.Amount;
                        break;
                    case "down":
                        aim += x.Amount;
                        break;
                    case "up":
                        aim -= x.Amount;
                        break;
                    default:
                        throw new Exception(x.Position);
                }

            });

            Console.WriteLine(horizontal * depth);
        }
    }
}