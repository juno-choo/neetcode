public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length)
        {
            return false;
        }

        Dictionary<int, int> charCounts = new Dictionary<int, int>();

        foreach (char c in s)
        {
            if (charCounts.ContainsKey(c))
            {
                charCounts[c]++;
            }
            else
            {
                charCounts[c] = 1;
            }
        }

        foreach (char c in t)
        {
            if (!charCounts.ContainsKey(c) || charCounts[c] == 0)
            {
                return false;
            }
            charCounts[c]--;
        }

        return true;
    }
}
