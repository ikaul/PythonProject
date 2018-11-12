import unittest


class Tag(object):
    """
    Given a input string and a list of sub strings,
    for each substring found in the input string,
    add <b></b> tags to it.
    """

    def __init__(self, input_string=None, sub_strings=[]):
        self.input_string = input_string
        self.sub_strings = sub_strings

    def tagged(self):
        tag_arr = []
        # Check where in the input string sub strings are found.
        # Store indices in array.
        for sub_str in self.sub_strings:
            index = 0
            while self.input_string.find(sub_str, index) != -1:
                start = self.input_string.find(sub_str, index)
                index = start + len(sub_str) - 1
                tag_arr.append([start, index])

        if not tag_arr:
            return self.input_string

        # Sort the tag array so that we can infuse overlaps.
        tag_arr.sort()
        last = 0
        tags = []
        for index, tag in enumerate(tag_arr):
            if last + 1 >= tag[0] and index > 0:
                tags[-1][1] = tag[1]
            else:
                tags.append(tag)
            last = tag[1]

        ret = self.input_string

        start = 0
        for tag in tags:
            prefix = ret[:tag[0]+start]
            data = ret[tag[0]+start:tag[1]+1+start]
            postfix = ret[tag[1]+1+start:]
            start += 7
            ret = '{}<b>{}</b>{}'.format(prefix, data, postfix)
        return ret


class TestTag(unittest.TestCase):
    def test_tagged(self):
        # Generic Case
        self.assertEqual(Tag('abcxxx123', ['abc']).tagged(), '<b>abc</b>xxx123')
        # Empty Case
        self.assertEqual(Tag('abcxxx123abc').tagged(), 'abcxxx123abc')
        # Overlap Case
        self.assertEqual(Tag('abcxxx123abc', ['abc', '123']).tagged(), '<b>abc</b>xxx<b>123abc</b>')
        # Complex Case
        self.assertEqual(Tag('abcxxx123abc', ['abc', '123', 'xx']).tagged(), '<b>abcxxx123abc</b>')
        self.assertEqual(Tag('abcxxx12345abc', ['abc', '123', 'xx']).tagged(), '<b>abcxxx123</b>45<b>abc</b>')

unittest.main()
