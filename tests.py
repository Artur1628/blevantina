import unittest

from tasks import replace_substring, strip_spaces, join_with_space, split_by_space, capitalize_string, to_lower, \
    to_upper, get_length, contains_substring, count_occurrences, substring_by_index, starts_with, ends_with, \
    reverse_string, remove_all_spaces


class TestStringTasks(unittest.TestCase):
    def test_get_length(self):
        self.assertEqual(get_length("hello"), 5)

    def test_to_upper(self):
        self.assertEqual(to_upper("hello"), "HELLO")

    def test_to_lower(self):
        self.assertEqual(to_lower("HELLO"), "hello")

    def test_capitalize_string(self):
        self.assertEqual(capitalize_string("hello"), "Hello")

    def test_split_by_space(self):
        self.assertEqual(split_by_space("hello world"), ["hello", "world"])

    def test_join_with_space(self):
        self.assertEqual(join_with_space(["hello", "world"]), "hello world")

    def test_strip_spaces(self):
        self.assertEqual(strip_spaces("  hello  "), "hello")

    def test_replace_substring(self):
        self.assertEqual(replace_substring("hello world", "world", "Python"), "hello Python")

    def test_contains_substring(self):
        self.assertTrue(contains_substring("hello", "ell"))
        self.assertFalse(contains_substring("hello", "xyz"))

    def test_count_occurrences(self):
        self.assertEqual(count_occurrences("hello hello", "hello"), 2)

    def test_substring_by_index(self):
        self.assertEqual(substring_by_index("hello", 1, 4), "ell")

    def test_starts_with(self):
        self.assertTrue(starts_with("hello", "he"))
        self.assertFalse(starts_with("hello", "lo"))

    def test_ends_with(self):
        self.assertTrue(ends_with("hello", "lo"))
        self.assertFalse(ends_with("hello", "he"))

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_remove_all_spaces(self):
        self.assertEqual(remove_all_spaces(" h e l l o "), "hello")

if __name__ == '__main__':
    unittest.main()
