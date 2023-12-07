var data = File.ReadLines("input.txt").ToList();

Calculate(data, false);
Calculate(data, true);

void Calculate(List<string> data, bool isJokerMode)
{
    var list = new List<HandAndBid>();
    var cards = isJokerMode 
        ? "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J".Split(", ") 
        : "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".Split(", ");
    
    var cardStrengthMap = new Dictionary<string, int>();

    for (var i = 0; i < cards.Length; i++)
    {
        cardStrengthMap[cards[i]] = cards.Length - i - 1;
    }

    data.ForEach(x =>
    {
        var hb = x.Split(" ");
        var handStrength = 0;
        var cardDict = new Dictionary<string, int>();

        for (var i = 0; i < hb[0].Length; i++)
        {
            var card = hb[0][i].ToString();
            if (!cardDict.ContainsKey(card))
            {
                cardDict[card] = 0;
            }

            cardDict[card]++;

            handStrength += cardStrengthMap[card] * (int)Math.Pow(cards.Length, hb[0].Length - 1 - i);
        }
        
        Console.WriteLine("-----------------");
        Console.WriteLine(hb[0]);
        
        Console.WriteLine("strength: {0}", handStrength);

        var handType = 0;

        var numberOfJokers = 0;
        if (isJokerMode && cardDict.Count > 1 && cardDict.TryGetValue("J", out numberOfJokers))
        {
            cardDict.Remove("J");
        }

        var cardFrequencyKvp = cardDict.OrderByDescending(x => x.Value).ToList();
        var highestOccurrence = (cardFrequencyKvp.Count != 0 ? cardFrequencyKvp[0].Value : 0) + numberOfJokers;

        switch (cardDict.Count)
        {
            case 1:
                handType = 6;
                Console.WriteLine("Five of a kind: {0}", handType);
                break;
            case 2 when highestOccurrence == 4:
                handType = 5;
                Console.WriteLine("Four of a kind: {0}", handType);
                break;
            case 2 when highestOccurrence == 3:
                handType = 4;
                Console.WriteLine("Full house: {0}", handType);
                break;
            case 3 when highestOccurrence == 3:
                handType = 3;
                Console.WriteLine("Three of a kind: {0}", handType);
                break;
            case 3 when highestOccurrence == 2:
                handType = 2;
                Console.WriteLine("Two pair: {0}", handType);
                break;
            case 4:
                handType = 1;
                Console.WriteLine("One pair: {0}", handType);
                break;
            default:
                Console.WriteLine("High card: {0}", handType);
                break;
        }
        
        list.Add(new HandAndBid
        {
            Hand = hb[0],
            Bid = int.Parse(hb[1]),
            Type = handType,
            HandStrength = handStrength
        });
    });

    var ordered = list.OrderByDescending(x => x.Type)
        .ThenByDescending(x => x.HandStrength).ToList();

    var sum = 0;

    for (var i = 0; i < ordered.Count; i++)
    {
        sum += ordered[i].Bid * (ordered.Count - i);
        Console.WriteLine(ordered[i].Hand);
    }
    
    Console.WriteLine(sum);
}

class HandAndBid
{
    public string Hand { get; set; }
    public int Bid { get; set; }
    
    public int Type { get; set; }

    public int HandStrength { get; set; }
}