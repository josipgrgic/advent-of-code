using System.Diagnostics;
using System.Text.RegularExpressions;

namespace Day04
{
    class Program
    {
        static int width;
        static int height;

        static void Main(string[] args)
        {
            var input = File.ReadAllLines("./input.txt");
            // var input = File.ReadAllLines("./input.example");

            var lines = input.Select(x =>
            {
                var match = Regex.Matches(x, @"(\d+),(\d+) -> (\d+),(\d+)", RegexOptions.IgnoreCase);
                var line = new Line(
                    int.Parse(match[0].Groups[1].Value),
                    int.Parse(match[0].Groups[2].Value),
                    int.Parse(match[0].Groups[3].Value),
                    int.Parse(match[0].Groups[4].Value)
                );

                width = Math.Max(width, Math.Max(line.Start.X, line.End.X));
                height = Math.Max(height, Math.Max(line.Start.Y, line.End.Y));

                return line;
            })
            .ToList();

            CountOverlaps(lines.Where(l => l.Start.X == l.End.X || l.Start.Y == l.End.Y));
            CountOverlaps(lines);
        }

        private static void CountOverlaps(IEnumerable<Line> lines)
        {
            var s = new Stopwatch();
            s.Start();
            var result = 0;

            var matrix = new int[width + 1, height + 1];
            foreach (var line in lines)
            {
                foreach (var point in line.ProducePoints())
                {
                    matrix[point.Item1, point.Item2]++;

                    if (matrix[point.Item1, point.Item2] == 2)
                    {
                        result++;
                    }
                }
            }

            s.Stop();

            Console.WriteLine($"Result: {result}");
            Console.WriteLine($"Elapsed: {s.ElapsedMilliseconds}ms");
        }
    }

    struct Point
    {
        public int X;
        public int Y;

        public Point(int x, int y)
        {
            this.X = x;
            this.Y = y;
        }
    }

    struct Line
    {
        public Point Start;
        public Point End;

        public Line(int x1, int y1, int x2, int y2)
        {
            var p1 = new Point(x1, y1);
            var p2 = new Point(x2, y2);

            if (p1.X < p2.X)
            {
                Start = p1;
                End = p2;
            }
            else
            {
                Start = p2;
                End = p1;
            }
        }

        public Tuple<int, int>[] ProducePoints()
        {
            var numberOfPoints = Math.Max(
                    Math.Abs(Start.X - End.X),
                    Math.Abs(Start.Y - End.Y))
                + 1;

            var xIncrement = Math.Sign(End.X - Start.X);
            var yIncrement = Math.Sign(End.Y - Start.Y);

            var points = new Tuple<int, int>[numberOfPoints];

            for (var i = 0; i < numberOfPoints; i++)
            {
                points[i] = Tuple.Create(Start.X + i * xIncrement, Start.Y + i * yIncrement);
            }

            return points;
        }
    }
}