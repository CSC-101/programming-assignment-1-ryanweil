from data import *

# Write your functions for each part in the space below.

# Part 1
def vowel_count(input_string):
    # Define the vowels to look for
    vowels = "aeiou"

    # Initialize a counter for vowels
    count = 0

    # Loop through each character in the input string
    for char in input_string:
        # Check if the character is a vowel
        if char.lower() in vowels:

            count += 1  # Increment the count if it's a vowel

    # Return the total count of vowels
    return count

# Part 2
def short_lists(whole_list: list[list[int]])->list[list[int]]:

    shortlist = []

    for sublist in whole_list:
        if len(sublist) == 2:
            shortlist.append(sublist)

    return shortlist

# Part 3
def ascending_pairs(whole_list: list[list[int]])-> list[list[int]]:

    organized_list = []

    for sublist in whole_list:
        if len(sublist) == 2 and sublist[0] > sublist[1]:
            x = sublist[0]
            sublist[0] = sublist[1]
            sublist[1] = x
            organized_list.append(sublist)
        else:
            organized_list.append(sublist)
    return organized_list




# Part 4
def add_prices(price1: Price, price2: Price)-> Price:
    total_cents = price1.cents + price2.cents
    total_dollars = price1.dollars + price2.dollars + total_cents // 100
    remaining_cents = total_cents % 100
    return Price(total_dollars, remaining_cents)



# Part 5

def rectangle_area(rect: Rectangle)-> int:
    width=rect.bottom_right.x - rect.top_left.x
    height=rect.top_left.y - rect.bottom_right.y
    return width * height


# Part 6
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

def books_by_author(author_name: str, books: list[Book]) -> list[Book]:
    return [book for book in books if book.author == author_name]

# Part 7
import math


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, top_left: Point, bottom_right: Point):
        self.top_left = top_left
        self.bottom_right = bottom_right


class Circle:
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius


def circle_bound(rect: Rectangle) -> Circle:
    # Find the center of the rectangle
    center_x = (rect.top_left.x + rect.bottom_right.x) / 2
    center_y = (rect.top_left.y + rect.bottom_right.y) / 2
    center = Point(center_x, center_y)

    # Find the distance from the center to one of the corners (radius of the bounding circle)
    dx = center_x - rect.top_left.x
    dy = center_y - rect.top_left.y
    radius = math.sqrt(dx ** 2 + dy ** 2)

    # Return the Circle object
    return Circle(center, radius)

# Part 8
class Employee:
    def __init__(self, name: str, pay_rate: float):
        self.name = name
        self.pay_rate = pay_rate


def below_pay_average(employees: list[Employee]) -> list[str]:
    if not employees:
        return []

    total_pay = sum(employee.pay_rate for employee in employees)
    average_pay = total_pay / len(employees)

    return [employee.name for employee in employees if employee.pay_rate < average_pay]


