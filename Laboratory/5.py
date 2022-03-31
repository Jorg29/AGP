import unittest


def hamming_distance(s, t):
    if len(s) != len(t):
      return -1
    distance = 0
    for i in range (0,len(s)):
      if t[i] != s[i]:
        distance+=1
        return distance


# Mην αλλάξετε κάτι από εδώ και κάτω
class TestHammingDistance(unittest.TestCase):
    def test_HD(self):
        self.assertEqual(hamming_distance("G", ""), -1)
        self.assertEqual(hamming_distance("", "G"), -1)
        self.assertEqual(hamming_distance("G", "A"), 1)
        self.assertEqual(hamming_distance("G", "G"), 0)
        self.assertEqual(hamming_distance("GA", "GA"), 0)
        self.assertEqual(hamming_distance("GA", "AG"), 2)
        self.assertEqual(hamming_distance("AGCT", "AGCT"), 0)
        self.assertEqual(hamming_distance("AGCT", "TCGA"), 4)
        self.assertEqual(hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"), 7)


if __name__ == "__main__":
    unittest.main()
