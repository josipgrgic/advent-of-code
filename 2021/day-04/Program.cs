namespace Day04
{
    class Program
    {
        static void Main(string[] args)
        {
            var lines = File.ReadAllLines("./input.txt");
            // var lines = File.ReadAllLines("./input.example");

            var numbersLookup = new Dictionary<int, int>();
            var numbersToDraw = lines[0]
                .Split(",", StringSplitOptions.RemoveEmptyEntries)
                .Select((x, i) =>
                {
                    var number = int.Parse(x);
                    numbersLookup[number] = i;
                    return number;
                }).ToList();

            var boards = new List<int[]>();

            for (var i = 1; i < lines.Length; i += 6)
            {
                var boardStrings = lines[(i + 1)..(i + 6)];

                var parsed = boardStrings
                    .SelectMany(x => x.Split(" ", StringSplitOptions.RemoveEmptyEntries)
                        .Select(int.Parse))
                    .ToArray();

                boards.Add(parsed);
            }

            BoardData? minBoard = null;
            BoardData? maxBoard = null;

            foreach (var board in boards)
            {
                var boardData = new BoardData();
                var numbers = new HashSet<int>();
                var sum = 0;
                var roundWhenCompleted = new int[10];

                for (var i = 0; i < 5; i++)
                {
                    for (var j = 0; j < 5; j++)
                    {
                        var num = board[5 * i + j];
                        sum += num;
                        numbers.Add(num);

                        roundWhenCompleted[i] = Math.Max(roundWhenCompleted[i], numbersLookup[num]);
                        roundWhenCompleted[5 + j] = Math.Max(roundWhenCompleted[5 + j], numbersLookup[num]);
                    }
                }

                boardData.SolvedAtRound = roundWhenCompleted.Min();

                var pickedNumbersSum = numbersToDraw.Take(boardData.SolvedAtRound + 1).Sum(x => numbers.Contains(x) ? x : 0);
                boardData.FinalResult = (sum - pickedNumbersSum) * numbersToDraw[boardData.SolvedAtRound];

                if (minBoard == null || boardData.SolvedAtRound < minBoard.SolvedAtRound)
                {
                    minBoard = boardData;
                }

                if (maxBoard == null || boardData.SolvedAtRound > maxBoard.SolvedAtRound)
                {
                    maxBoard = boardData;
                }
            }

            Console.WriteLine(minBoard.FinalResult);
            Console.WriteLine(maxBoard.FinalResult);
        }
    }

    class BoardData
    {
        public int FinalResult;
        public int SolvedAtRound;
    }
}