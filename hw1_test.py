from hw1 import*
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1


        def test_one_vowel(self):
            word = "abc"
            self.assertEqual(vowel_count(word), 1)

        def test_one_vowel1_Upper_(self):
            word = "AbC"
            self.assertEqual(vowel_count(word), 1)

        def test_one_vowel1_Upper_1_lower(self):
            word = "hEllo"
            self.assertEqual(vowel_count(word), 2)
    # Part 2
        def test_shortlist(self):
            list=[[0,8,7,9], [1,2]]
            self.assertEqual(short_lists(list),[[1,2]])

        def test_empty_list(self):
            list=[]
            self.assertEqual(short_lists(list),[])

        def test_odd_list(self):
            list=[[1,4,6,8],[1]]
            self.assertEqual(short_lists(list),[])
    # Part 3
        def test_ascending_list(self):
            list=[[2,1]]
            self.assertEqual(ascending_pairs(list), [[1,2]])

        def test_ascending_list1(self):
            list= [[2,1],[3,4],[1],[3,2,1]]
            self.assertEqual(ascending_pairs(list), [[1,2],[3,4],[1],[3,2,1]])

        def test_ascending_list2(self):
            list=[]
            self.assertEqual(ascending_pairs(list), [])

    # Part 4
        def test_add_prices_basic(self):
            price1=Price(5,75)
            price2=Price(4,50)
            self.assertEqual(add_prices(price1, price2).dollars, 10)
            self.assertEqual(add_prices(price1, price2).cents, 25)

        def test_add_prices_no_overflow(self):
            price1=Price(10,20)
            price2=Price(4,30)
            self.assertEqual(add_prices(price1, price2).dollars, 14)
            self.assertEqual(add_prices(price1, price2).cents, 50)

        def test_add_prices_with_overflow(self):
            price1 = Price(7,90)
            price2 = Price(5,20)
            self.assertEqual(add_prices(price1, price2,).dollars, 13)
            self.assertEqual(add_prices(price1,price2).cents, 10)


    # Part 5

        def test_rectangle_area_basic(self):
            rect=Rectangle(Point(1,5),Point(4,1))
            self.assertEqual(rectangle_area(rect),12)

        def test_rectangle_area_line(self):
            rect=Rectangle(Point(3,7), Point(3,1))
            self.assertEqual(rectangle_area(rect), 0)

        def test_rectangle_area_square(self):
            rect=Rectangle(Point(3,7), Point(3,1))
            self.assertEqual(rectangle_area(rect),0)


    # Part 6
        def test_books_by_author_basic(self):
            book_list = [Book("Book1", "Author A"), Book("Book2", "Author B"), Book("Book3", "Author A")]
            result = books_by_author("Author A", book_list)
            self.assertEqual([book.title for book in result], ["Book1", "Book3"])


        def test_books_by_author_none(self):
            book_list = [Book("Book1", "Author A"), Book("Book2", "Author B")]
            result = books_by_author("Author C", book_list)
            self.assertEqual(result, [])


        def test_books_by_author_one_match(self):
            book_list = [Book("Book1", "Author A"), Book("Book2", "Author B"), Book("Book3", "Author C")]
            result = books_by_author("Author C", book_list)
            self.assertEqual([book.title for book in result], ["Book3"])

    # Part 7
class TestCircleBound(unittest.TestCase):

        def test_circle_bound_basic(self):
            rect = Rectangle(Point(0, 4), Point(4, 0))
            circle = circle_bound(rect)
            self.assertEqual(circle.center.x, 2)
            self.assertEqual(circle.center.y, 2)
            self.assertAlmostEqual(circle.radius, 2.828, places=3)  # sqrt(8) = 2.828

        def test_circle_bound_large_rectangle(self):
            rect = Rectangle(Point(-5, 5), Point(5, -5))
            circle = circle_bound(rect)
            self.assertEqual(circle.center.x, 0)
            self.assertEqual(circle.center.y, 0)
            self.assertAlmostEqual(circle.radius, 7.071, places=3)  # sqrt(50) = 7.071

        def test_circle_bound_small_rectangle(self):
            rect = Rectangle(Point(1, 2), Point(2, 1))
            circle = circle_bound(rect)
            self.assertEqual(circle.center.x, 1.5)
            self.assertEqual(circle.center.y, 1.5)
            self.assertAlmostEqual(circle.radius, 0.707, places=3)  # sqrt(0.5) = 0.707


    # Part 8

import unittest

class TestBelowPayAverage(unittest.TestCase):

    def test_below_pay_average_basic(self):
        employees = [Employee("Alice", 50000), Employee("Bob", 60000), Employee("Charlie", 55000)]
        result = below_pay_average(employees)
        self.assertEqual(result, ["Alice", "Charlie"])

    def test_below_pay_average_no_one_below(self):
        employees = [Employee("Alice", 60000), Employee("Bob", 60000)]
        result = below_pay_average(employees)
        self.assertEqual(result, [])

    def test_below_pay_average_empty_list(self):
        employees = []
        result = below_pay_average(employees)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()







if __name__ == '__main__':
    unittest.main()
