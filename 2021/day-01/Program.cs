
namespace Day01
{
    class Program
    {
        static void Main(string[] args)
        {
            var lines = File.ReadAllLines("./input.txt");
            // var lines = File.ReadAllLines("./input.example");

            var depths = lines.Select(x => int.Parse(x.Trim())).ToArray();

            Second(depths);


        }

        static void First(int[] depths)
        {
            var count = 0;

            for (var i = 0; i < depths.Count() - 1; i++)
            {
                var firstNumber = depths[i];
                var secondNumber = depths[i + 1];

                count += secondNumber > firstNumber ? 1 : 0;
            }

            Console.WriteLine(count);
        }

        static void Second(int[] depths)
        {
            var count = 0;

            for (var i = 0; i < depths.Count() - 3; i++)
            {
                var firstWindowSum = depths[i..(i + 3)].Sum();
                var secondWindowSum = depths[(i + 1)..(i + 4)].Sum();

                count += secondWindowSum > firstWindowSum ? 1 : 0;
            }

            Console.WriteLine(count);
        }
    }
}