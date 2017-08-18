import unittest


class Solution(object):
    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        i, j, res = 0, 0, ''
        while i < len(s) - len(res):
            end_odd = 2 * j - i
            end_even = end_odd - 1
            if end_even < len(s) and s[i: j] == s[end_even : j - 1: -1]:
                res = s[i: end_even + 1]
            if end_odd < len(s) and s[i: j] == s[end_odd: j: -1]:
                res = s[i: end_odd + 1]
            if end_odd < len(s):
                j += 1
            else:
                i += 1
                j = i + (len(res) + 1) / 2
        return res

    def longestPalindrome(self, s):
        start, end, res = 0, 0, ''
        while start < len(s) - len(res):
            sub = s[start: end]
            if end <= len(s) and sub == sub[::-1]:
                res = sub
            if end < len(s):
                end += 1
            else:
                start += 1
                end = start + len(res) + 1
        return res



class TestSolution(unittest.TestCase):

    def test_multi_solution(self):
        self.assertIn(Solution().longestPalindrome("babad"), ['bab', 'aba'])

    def test_single_character(self):
        self.assertEqual(Solution().longestPalindrome('a'), 'a')

    def test_even_palindrome(self):
        self.assertEqual(Solution().longestPalindrome('aa'), 'aa')

    def test_super_long_input(self):
        self.assertEqual(Solution().longestPalindrome(
            "jglknendplocymmvwtoxvebkekzfdhykknufqdkntnqvgfbahsljkobhbxkvyictzkqjqydczuxjkgecdyhixdttxfqmgks"
            "rkyvopwprsgoszftuhawflzjyuyrujrxluhzjvbflxgcovilthvuihzttzithnsqbdxtafxrfrblulsakrahulwthhbjcslc"
            "eewxfxtavljpimaqqlcbrdgtgjryjytgxljxtravwdlnrrauxplempnbfeusgtqzjtzshwieutxdytlrrqvyemlyzolhbkzhy"
            "fyttevqnfvmpqjngcnazmaagwihxrhmcibyfkccyrqwnzlzqeuenhwlzhbxqxerfifzncimwqsfatudjihtumrtjtggzleovi"
            "hifxufvwqeimbxvzlxwcsknksogsbwwdlwulnetdysvsfkonggeedtshxqkgbhoscjgpiel"
        ), 'sknks')
        self.assertEqual(Solution().longestPalindrome(
            "ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwi"
            "usngkbdhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddzn"
            "wumxosomfbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagi"
            "sdmsokeznjsnwpxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycooj"
            "wwgtklypicgkyaboqjfivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxugh"
            "whvlsxsgttbcyrlkaarngeoaldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvz"
            "todbfnjhbtwpjlzuajnlzfmmujhcggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsuk"
            "vzflcuxxzvxzravzznpxttduajhbsyiywpqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgj"
            "wudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcudlzfzutplbycejmkpxcygsafzkgudy"
        ), 'fklkf')

    def test_empty_input(self):
        self.assertEqual(Solution().longestPalindrome(''), '')


if __name__ == '__main__':
    unittest.main()
