
namespace Day03
{
    class Program
    {
        static void Main(string[] args)
        {
            var lines = File.ReadAllLines("./input.txt");
            // var lines = File.ReadAllLines("./input.example");

            Part2(lines);
        }

        static void Part1(string[] lines)
        {
            var totalLines = lines.Count();
            var lineLength = lines[0].Length;

            var zeroesPerColumn = new int[lineLength];
            foreach (var line in lines)
            {
                var bits = line.ToCharArray();

                for (var i = 0; i < lineLength; i++)
                {
                    zeroesPerColumn[i] += bits[i] == '0' ? 1 : 0;
                }
            }

            var gammaRate = new int[lineLength];
            var epsilonRate = new int[lineLength];

            var gammaDecimal = 0;
            var epsilonDecimal = 0;

            for (var i = 0; i < lineLength; i++)
            {
                var zeroesAtColumn = zeroesPerColumn[i];

                var value = zeroesAtColumn > (totalLines / 2) ? 0 : 1;

                gammaDecimal += value * (int)Math.Pow(2, lineLength - i - 1);
                epsilonDecimal += (1 - value) * (int)Math.Pow(2, lineLength - i - 1);

                gammaRate[i] = value;
                epsilonRate[i] = 1 - gammaRate[i];
            }

            Console.WriteLine($"{gammaDecimal} x {epsilonDecimal} = {gammaDecimal * epsilonDecimal}");
        }

        static void Part2(string[] lines)
        {
            var oxygenList = lines;

            var j = 0;
            while (oxygenList.Length != 1)
            {
                var numberOfOnes = oxygenList.Sum(x => x[j] - '0');
                if (numberOfOnes >= oxygenList.Count() - numberOfOnes)
                {
                    oxygenList = oxygenList.Where(x => x[j] == '1').ToArray();
                }
                else
                {
                    oxygenList = oxygenList.Where(x => x[j] == '0').ToArray();
                }

                j++;
            }

            var co2List = lines;
            j = 0;
            while (co2List.Length != 1)
            {
                var numberOfOnes = co2List.Sum(x => x[j] - '0');

                if (numberOfOnes >= co2List.Count() - numberOfOnes)
                {
                    co2List = co2List.Where(x => x[j] == '0').ToArray();
                }
                else
                {
                    co2List = co2List.Where(x => x[j] == '1').ToArray();
                }

                j++;
            }

            var oxgen = Convert.ToInt32(oxygenList.First(), 2);
            var co2 = Convert.ToInt32(co2List.First(), 2);

            Console.WriteLine($"{oxgen} x {co2} = {oxgen * co2}");
        }
    }
}