import datetime
import math
import re

from typing import Tuple
from hashlib import sha1

from src.factorization import prime_factors, multiples, num_divisors, divisors
from src.fibonacci import fibonacci_sequence
from src.primes import Primes
from textwrap import dedent
from unittest import TestCase


class Point(object):
    def __init__(self, x: int, y: int):
        self.x, self.y = x, y

    def __str__(self):
        return "{}".format(self.position)

    def __eq__(self, other):
        return self.position == other.position

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(abs(self.x - other.x), abs(self.y - other.y))

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y

    @property
    def position(self) -> Tuple[int, int]:
        return (self.x, self.y)

    @property
    def right(self):
        return Point(self.x + 1, self.y)

    @property
    def down(self):
        return Point(self.x, self.y + 1)


class Node(Point):
    def __init__(self, x, y, value=0):
        self.value = value
        self.parents = set()
        super(Node, self).__init__(x, y)

    def __hash__(self):
        return sha1("{}.{}".format(self.position, self.value).encode("utf-8")).hexdigest().__hash__()

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __ge__(self, other):
        return self.value >= other.value

    def add_parent(self, parent) -> None:
        if len(self.parents) == 2:
            raise ValueError("Already have maximum number of parents")
        self.parents.add(parent)

    def max_sum(self) -> int:
        max_sum = self.value
        for _p in self.parents:
            max_sum = max(self.value + _p.max_sum(), max_sum)
        return max_sum


class Collatz(object):
    def __init__(self):
        """
        Creates an iterable of the Collatz function starting at n

        :param n: Starting integer
        """
        self.len_cache = {}

    def chain_length(self, n):
        if 1 <= n <= 2:
            return n
        if n in self.len_cache:
            return self.len_cache[n]
        if n % 2 == 0:
            _l = 1 + self.chain_length(n / 2)
        else:
            _l = 2 + self.chain_length((3 * n + 1) / 2)
        self.len_cache[n] = _l
        return _l


class TestProblem1(TestCase):

    def test_problem_1(self):

        def func(n: list, m: int) -> int:
            results = set()
            for _n in n:
                results.update(multiples(_n, m))
            return sum(results)

        self.assertEqual(func([3, 5], 10), 23)
        print(func([3, 5], 1000))


class TestProblem2(TestCase):

    def test_problem_2(self):
        self.assertEqual(fibonacci_sequence(89), [1, 2, 3, 5, 8, 13, 21, 34, 55, 89])

        total = 0
        for x in fibonacci_sequence(4000000):
            if x % 2 == 0:
                total += x

        print(total)

    def test_fibonacci_sequence(self):
        self.assertEqual(fibonacci_sequence(89), [1, 2, 3, 5, 8, 13, 21, 34, 55, 89])


class TestProblem3(TestCase):

    def test_prime_factors(self):
        self.assertEqual(prime_factors(13195), [5, 7, 13, 29])

    def test_problem_3(self):
        print(max(prime_factors(600851475143)))


class TestProblem4(TestCase):

    def test_problem_4(self):
        def gen_palindromes(n: int) -> list:
            """
            Generates palindromes of length `n`
            """
            if n % 2 != 0:
                n = n - 1
                spacer = True
            else:
                spacer = False
            for x in range(10 ** (int(n / 2) - 1), 10 ** int(n / 2)):
                x_str = str(x)
                if not spacer:
                    yield int("{}{}".format(x_str, x_str[::-1]))
                else:
                    for y in range(10 ** (n - 2), 10 ** (n - 1)):
                        yield int("{}{}{}".format(x_str, y, x_str[::-1]))

        def func(n: int) -> int:
            """
            Finds the largest palindrome that's the product of n-digit numbers.
            """
            m = 0
            for x in range(0, n):
                m *= 10
                m += 9
            max_product = m ** 2
            pal_len = math.ceil(math.log10(max_product))

            results = []
            for pal in gen_palindromes(pal_len):
                for i in range(10 ** (n - 1), 10 ** n):
                    j = pal / i
                    if j.is_integer() and len(str(int(j))) == n:
                        results.append(pal)
                        break
            return max(results)

        self.assertEqual(func(2), 9009)
        print(func(3))


class TestProblem5(TestCase):

    def test_problem_5(self):
        def func(n: int) -> int:
            primes = Primes()
            i = 1

            primes.is_prime(n)
            m = 1
            for p in primes:
                if p <= n:
                    m *= p
                else:
                    break

            match = False
            while not match:
                match = True
                num = m * i
                for j in range(n, 2, -1):
                    if num % j != 0:
                        match = False
                        i += 1
                        break
            return i * m

        self.assertEqual(func(10), 2520)
        print(func(20))


class TestProblem6(TestCase):

    def test_problem_6(self):
        def func(n: int) -> int:
            return sum([x for x in range(1, n + 1)])**2 - sum([x ** 2 for x in range(1, n + 1)])

        self.assertEqual(func(10), 2640)
        print(func(100))


class TestProblem7(TestCase):

    def test_problem_7(self):
        def func(n: int) -> int:
            primes = Primes()
            i = 0
            for p in primes:
                i += 1
                if i == n:
                    return p

        self.assertEqual(func(6), 13)
        print(func(10001))


class TestProblem8(TestCase):
    digit_str = dedent("""
        73167176531330624919225119674426574742355349194934
        96983520312774506326239578318016984801869478851843
        85861560789112949495459501737958331952853208805511
        12540698747158523863050715693290963295227443043557
        66896648950445244523161731856403098711121722383113
        62229893423380308135336276614282806444486645238749
        30358907296290491560440772390713810515859307960866
        70172427121883998797908792274921901699720888093776
        65727333001053367881220235421809751254540594752243
        52584907711670556013604839586446706324415722155397
        53697817977846174064955149290862569321978468622482
        83972241375657056057490261407972968652414535100474
        82166370484403199890008895243450658541227588666881
        16427171479924442928230863465674813919123162824586
        17866458359124566529476545682848912883142607690042
        24219022671055626321111109370544217506941658960408
        07198403850962455444362981230987879927244284909188
        84580156166097919133875499200524063689912560717606
        05886116467109405077541002256983155200055935729725
        71636269561882670428252483600823257530420752963450""")

    def test_problem_8(self):
        def func(n: int) -> int:
            digits = [int(x) for x in self.digit_str if x != "\n"]
            result = 0
            for i in range(0, len(digits) - n):
                product = 1
                for j in range(i, i+n):
                    product *= digits[j]
                result = max(product, result)
            return result

        self.assertEqual(func(4), 5832)
        print(func(13))


class TestProblem9(TestCase):

    def test_problem_9(self):
        for i in range(1, 1000):
            for j in range(1, 1000):
                if i + j > 1000:
                    break
                k = 1000 - i - j
                if i ** 2 + j ** 2 == k ** 2:
                    print(i * j * k)
                    return


class TestProblem10(TestCase):

    def test_problem_10(self):
        primes = Primes()

        self.assertEqual(primes.sum_below(10), 17)
        print(primes.sum_below(2000000))


class TestProblem11(TestCase):

    def setUp(self):
        grid_str = """
                      08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
                      49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
                      81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
                      52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
                      22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
                      24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
                      32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
                      67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
                      24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
                      21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
                      78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
                      16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
                      86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
                      19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
                      04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
                      88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
                      04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
                      20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
                      20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
                      01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""
        grid_list = [int(x) for x in dedent(grid_str).split()]
        max_index = math.sqrt(len(grid_list))
        max_index = int(max_index) if max_index.is_integer() else self.fail("Oopsie")
        self.grid = [[]]
        for i in range(0, max_index):
            row = []
            for j in range(0, max_index):
                row.append(grid_list.pop(0))
            self.grid.append(row)
        if len(grid_list) > 0:
            self.fail("Huh?")

    def get(self, point: tuple, default: int=1) -> int:
        try:
            result = self.grid[point[0]][point[1]]
        except IndexError:
            result = default
        finally:
            return result

    def test_problem_11(self):
        def product(factors: list) -> float:
            result = 1
            for x in factors:
                result = result * x
            return result


        max_product = 0

        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid[i])):
                row = []
                col = []
                diag_right = []
                diag_left = []
                for _x in range(0, 4):
                    row.append(self.get((i, j+_x)))
                    col.append(self.get((i+_x, j)))
                    diag_right.append(self.get((i+_x, j+_x)))
                    diag_left.append(self.get((i-_x, j+_x)))
                max_product = max(max_product, product(row), product(col), product(diag_right), product(diag_left))

        self.assertEqual(max_product, 70600674)


class TestProblem12(TestCase):
    def test_divisors(self):
        self.assertEqual(num_divisors(28), 6)

    def test_divisor_funcs(self):
        for x in range(0, 200):
            if len(divisors(x)) != num_divisors(x):
                self.fail("len({}) != {}".format(divisors(x), num_divisors(x)))

    def triangle_number(self, n):
        return sum([x for x in range(0, n+1)])

    def test_problem_12(self):
        n = 1
        l_1 = num_divisors(n)
        l_2 = num_divisors(n + 1)
        try:
            max_divisors = l_1 * l_2
            _d = max_divisors
            while _d < 500:
                n += 1
                l_1 = l_2
                if n % 2 != 0:
                    l_2 = num_divisors((n + 1) / 2)
                else:
                    l_2 = num_divisors(n + 1)
                _d = l_1 * l_2
                if _d > max_divisors:
                    max_divisors = _d
                    print("{}: {}".format(_d, n))
        finally:
            self.assertEqual(n, 12375)


class TestProblem13(TestCase):

    def setUp(self):
        num_str = dedent("""
            37107287533902102798797998220837590246510135740250
            46376937677490009712648124896970078050417018260538
            74324986199524741059474233309513058123726617309629
            91942213363574161572522430563301811072406154908250
            23067588207539346171171980310421047513778063246676
            89261670696623633820136378418383684178734361726757
            28112879812849979408065481931592621691275889832738
            44274228917432520321923589422876796487670272189318
            47451445736001306439091167216856844588711603153276
            70386486105843025439939619828917593665686757934951
            62176457141856560629502157223196586755079324193331
            64906352462741904929101432445813822663347944758178
            92575867718337217661963751590579239728245598838407
            58203565325359399008402633568948830189458628227828
            80181199384826282014278194139940567587151170094390
            35398664372827112653829987240784473053190104293586
            86515506006295864861532075273371959191420517255829
            71693888707715466499115593487603532921714970056938
            54370070576826684624621495650076471787294438377604
            53282654108756828443191190634694037855217779295145
            36123272525000296071075082563815656710885258350721
            45876576172410976447339110607218265236877223636045
            17423706905851860660448207621209813287860733969412
            81142660418086830619328460811191061556940512689692
            51934325451728388641918047049293215058642563049483
            62467221648435076201727918039944693004732956340691
            15732444386908125794514089057706229429197107928209
            55037687525678773091862540744969844508330393682126
            18336384825330154686196124348767681297534375946515
            80386287592878490201521685554828717201219257766954
            78182833757993103614740356856449095527097864797581
            16726320100436897842553539920931837441497806860984
            48403098129077791799088218795327364475675590848030
            87086987551392711854517078544161852424320693150332
            59959406895756536782107074926966537676326235447210
            69793950679652694742597709739166693763042633987085
            41052684708299085211399427365734116182760315001271
            65378607361501080857009149939512557028198746004375
            35829035317434717326932123578154982629742552737307
            94953759765105305946966067683156574377167401875275
            88902802571733229619176668713819931811048770190271
            25267680276078003013678680992525463401061632866526
            36270218540497705585629946580636237993140746255962
            24074486908231174977792365466257246923322810917141
            91430288197103288597806669760892938638285025333403
            34413065578016127815921815005561868836468420090470
            23053081172816430487623791969842487255036638784583
            11487696932154902810424020138335124462181441773470
            63783299490636259666498587618221225225512486764533
            67720186971698544312419572409913959008952310058822
            95548255300263520781532296796249481641953868218774
            76085327132285723110424803456124867697064507995236
            37774242535411291684276865538926205024910326572967
            23701913275725675285653248258265463092207058596522
            29798860272258331913126375147341994889534765745501
            18495701454879288984856827726077713721403798879715
            38298203783031473527721580348144513491373226651381
            34829543829199918180278916522431027392251122869539
            40957953066405232632538044100059654939159879593635
            29746152185502371307642255121183693803580388584903
            41698116222072977186158236678424689157993532961922
            62467957194401269043877107275048102390895523597457
            23189706772547915061505504953922979530901129967519
            86188088225875314529584099251203829009407770775672
            11306739708304724483816533873502340845647058077308
            82959174767140363198008187129011875491310547126581
            97623331044818386269515456334926366572897563400500
            42846280183517070527831839425882145521227251250327
            55121603546981200581762165212827652751691296897789
            32238195734329339946437501907836945765883352399886
            75506164965184775180738168837861091527357929701337
            62177842752192623401942399639168044983993173312731
            32924185707147349566916674687634660915035914677504
            99518671430235219628894890102423325116913619626622
            73267460800591547471830798392868535206946944540724
            76841822524674417161514036427982273348055556214818
            97142617910342598647204516893989422179826088076852
            87783646182799346313767754307809363333018982642090
            10848802521674670883215120185883543223812876952786
            71329612474782464538636993009049310363619763878039
            62184073572399794223406235393808339651327408011116
            66627891981488087797941876876144230030984490851411
            60661826293682836764744779239180335110989069790714
            85786944089552990653640447425576083659976645795096
            66024396409905389607120198219976047599490197230297
            64913982680032973156037120041377903785566085089252
            16730939319872750275468906903707539413042652315011
            94809377245048795150954100921645863754710598436791
            78639167021187492431995700641917969777599028300699
            15368713711936614952811305876380278410754449733078
            40789923115535562561142322423255033685442488917353
            44889911501440648020369068063960672322193204149535
            41503128880339536053299340368006977710650566631954
            81234880673210146739058568557934581403627822703280
            82616570773948327592232845941706525094512325230608
            22918802058777319719839450180888072429661980811197
            77158542502016545090413245809786882778948721859617
            72107838435069186155435662884062257473692284509516
            20849603980134001723930671666823555245252804609722
            53503534226472524250874054075591789781264330331690""")
        self.num_list = [int(x) for x in num_str.split()]

    def test_problem_13(self):
        num_sum = sum(self.num_list)
        self.assertEqual("5537376230", str(num_sum)[0:10])


class TestProblem14(TestCase):
    def test_problem_14(self):
        try:
            collatz_cache = Collatz()
            max_n, max_length = 0, 0
            for n in range(500000, 1000000):
                length = collatz_cache.chain_length(n)
                if length > max_length:
                    max_n, max_length = n, length
        finally:
            self.assertEqual(837799, max_n)


class TestProblem15(TestCase):
    def central_binomial_coef(self, n: int) -> int:
        return (math.factorial(2 * n)/(math.factorial(n)) ** 2)


    def test_num_paths(self):
        self.assertEqual(self.central_binomial_coef(2), 6)

    def test_problem_15(self):
        self.assertAlmostEqual(137846528820, self.central_binomial_coef(20))


class TestProblem16(TestCase):
    def test_problem_16(self):
        x_str = "{}".format(2 ** 15)
        self.assertEqual(26, sum([int(x) for x in x_str]))
        x_str = "{}".format(2 ** 1000)
        self.assertEqual(1366, sum([int(x) for x in x_str]))


class TestProblems17(TestCase):
    pattern = re.compile("\w")
    single_digits = {
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 0: ""
    }
    teen_digits = {
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
        16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
    }
    second_digits = {
        2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy",
        8: "eighty", 9: "ninety", 0: "hundred"
    }

    def num_alphabetic(self, test_str: str) -> int:
        try:
            results = len(self.pattern.findall(test_str))
        finally:
            return results

    def long_form(self, n) -> str:
        if n in self.teen_digits:
            return self.teen_digits[n]
        elif n in self.single_digits:
            return self.single_digits[n]
        n_str = "{}".format(n)
        if len(n_str) == 2:
            return self.second_digits[int(n_str[0])] + self.single_digits[int(n_str[1])]
        if len(n_str) == 3:
            results = self.single_digits[int(n_str[0])] + "hundred"
            if int(n_str[1:]) > 0:
                results += "and" + self.long_form(int(n_str[1:]))
            return results
        if len(n_str) == 4:
            results = self.single_digits[int(n_str[0])] + "thousand"
            if int(n_str[1:]) > 0:
                results += "and" + self.long_form(int(n_str[1:]))
            return results

    def num_long_form(self, n: int) -> int:
        _l = self.long_form(n)
        _c = self.num_alphabetic(_l)
        return _c

    def test_problem_17(self):
        self.assertEqual(19, sum([self.num_long_form(n) for n in range(1, 6)]))
        self.assertEqual(23, self.num_long_form(342))
        self.assertEqual(20, self.num_long_form(115))
        result = sum([self.num_long_form(n) for n in range(1, 1001)])
        self.assertEqual(21124, result)


class TestProblems18_Naive(TestCase):
    def setUp(self):
        self.triangle = []
        self.triangle_str = dedent("""
                                        75
                                        95 64
                                        17 47 82
                                        18 35 87 10
                                        20 04 82 47 65
                                        19 01 23 75 03 34
                                        88 02 77 73 07 63 67
                                        99 65 04 28 06 16 70 92
                                        41 41 26 56 83 40 80 70 33
                                        41 48 72 33 47 32 37 16 94 29
                                        53 71 44 65 25 43 91 52 97 51 14
                                        70 11 33 28 77 73 17 78 39 68 17 57
                                        91 71 52 38 17 14 91 43 58 50 27 29 48
                                        63 66 04 68 89 53 67 30 73 16 69 87 40 31
                                        04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""").strip()
        row = 0
        for line in self.triangle_str.split("\n"):
            col = 0
            row_list = []
            for value in line.split(" "):
                n = Node(row, col, int(value))
                if row > 0:
                    try:
                        n.add_parent(self.triangle[row - 1][col])
                    except IndexError:
                        pass
                    try:
                        n.add_parent(self.triangle[row - 1][col - 1])
                    except IndexError:
                        pass
                row_list.append(n)
                col += 1
            self.triangle.append(row_list)
            row += 1

    def test_problem_18(self):
        max_sum = 0
        for n in self.triangle[-1]:
            max_sum = max(n.max_sum(), max_sum)
        self.assertEqual(1074, max_sum)


class TestProblems18(TestCase):
    def setUp(self):
        self.triangle = []
        self.triangle_str = dedent("""
                                        75
                                        95 64
                                        17 47 82
                                        18 35 87 10
                                        20 04 82 47 65
                                        19 01 23 75 03 34
                                        88 02 77 73 07 63 67
                                        99 65 04 28 06 16 70 92
                                        41 41 26 56 83 40 80 70 33
                                        41 48 72 33 47 32 37 16 94 29
                                        53 71 44 65 25 43 91 52 97 51 14
                                        70 11 33 28 77 73 17 78 39 68 17 57
                                        91 71 52 38 17 14 91 43 58 50 27 29 48
                                        63 66 04 68 89 53 67 30 73 16 69 87 40 31
                                        04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""").strip()

        row_pos = 0
        for row in self.triangle_str.split("\n"):
            col_pos = 0
            self.triangle.append([])
            for col in row.split(" "):
                value = int(col)
                if row_pos > 0:
                    max_parent = 0
                    starting_pos = col_pos - 1 if col_pos > 0 else 0
                    ending_pos = min(col_pos + 1, len(self.triangle[row_pos - 1]))
                    for parent_value in self.triangle[row_pos - 1][starting_pos:ending_pos]:
                        max_parent = max(max_parent, parent_value)
                    value += max_parent
                self.triangle[row_pos].append(value)
                col_pos += 1
            row_pos += 1
                # Only store greatest sum

    def test_problem_18(self):
        self.assertEqual(1074, max(self.triangle[len(self.triangle) - 1]))


class TestProblem19(TestCase):
    def test_problem_19(self):
        start_date = datetime.datetime(year=1901, month=1, day=1)
        end_date = datetime.datetime(year=2000, month=12, day=31)
        duration = 0
        while start_date < end_date:
            start_date = start_date + datetime.timedelta(days=1)
            duration += 1 if start_date.day == 1 and start_date.isoweekday() == 7 else 0
        self.assertEqual(171, duration)


class TestProblem20(TestCase):
    def test_problem_20(self):
        self.assertEqual(-1, sum([int(x) for x in str(math.factorial(100))]))

