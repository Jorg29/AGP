import unittest


def is_pangram(s):
    greekletters = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
    solution = ()
    for c is s:
      if c in greekletters:
        ch = c.upper()
        if ch in greekletters:
          solution.add(ch)
    if len(solution)==24:
      return True
    else:
      return False


# Mην αλλάξετε κάτι από εδώ και κάτω
class TestPantogram(unittest.TestCase):
    def test(self):
        self.assertEqual(is_pangram("ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"), True)
        self.assertEqual(is_pangram("ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"[::-1]), True)
        self.assertEqual(is_pangram("ΞΕΣΚΕΠΑΖΩ ΤΗΝ ΨΥΧΟΦΘΟΡΟ ΒΔΕΛΥΓΜΙΑ"), True)
        self.assertEqual(
            is_pangram(
                "Ο ΚΑΛΥΜΝΙΟΣ ΣΦΟΥΓΓΑΡΑΣ ΨΙΘΥΡΙΣΕ ΠΩΣ ΘΑ ΒΟΥΤΗΞΕΙ ΧΩΡΙΣ ΝΑ ΔΙΣΤΑΖΕΙ"
            ),
            True,
        )
        self.assertEqual(is_pangram(""), False)
        self.assertEqual(is_pangram("A" * 24), False)
        self.assertEqual(is_pangram("ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨA"), False)


if __name__ == "__main__":
    unittest.main()
