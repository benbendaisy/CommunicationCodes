from typing import List

class Food:
        def __init__(self, food_rating, food_name):
            # Store the food's rating.
            self.food_rating = food_rating
            # Store the food's name.
            self.food_name = food_name
        def __lt__(self, other):
            # Overload the less than operator for comparison.
            # If food ratings are the same, sort based on their name (lexicographically smaller name food will be on top).
            if self.food_rating == other.food_rating:
                return self.food_name < other.food_name
            # Sort based on food rating (bigger rating food will be on top).
            return self.food_rating > other.food_rating

class FoodRatings1:
    """
    Design a food rating system that can do the following:

    Modify the rating of a food item listed in the system.
    Return the highest-rated food item for a type of cuisine in the system.
    Implement the FoodRatings class:

    FoodRatings(String[] foods, String[] cuisines, int[] ratings) Initializes the system. The food items are described by foods, cuisines and ratings, all of which have a length of n.
    foods[i] is the name of the ith food,
    cuisines[i] is the type of cuisine of the ith food, and
    ratings[i] is the initial rating of the ith food.
    void changeRating(String food, int newRating) Changes the rating of the food item with the name food.
    String highestRated(String cuisine) Returns the name of the food item that has the highest rating for the given type of cuisine. If there is a tie, return the item with the lexicographically smaller name.
    Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.

    Example 1:

    Input
    ["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
    [[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]
    Output
    [null, "kimchi", "ramen", null, "sushi", null, "ramen"]

    Explanation
    FoodRatings foodRatings = new FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]);
    foodRatings.highestRated("korean"); // return "kimchi"
                                        // "kimchi" is the highest rated korean food with a rating of 9.
    foodRatings.highestRated("japanese"); // return "ramen"
                                        // "ramen" is the highest rated japanese food with a rating of 14.
    foodRatings.changeRating("sushi", 16); // "sushi" now has a rating of 16.
    foodRatings.highestRated("japanese"); // return "sushi"
                                        // "sushi" is the highest rated japanese food with a rating of 16.
    foodRatings.changeRating("ramen", 16); // "ramen" now has a rating of 16.
    foodRatings.highestRated("japanese"); // return "ramen"
                                        // Both "sushi" and "ramen" have a rating of 16.
                                        // However, "ramen" is lexicographically smaller than "sushi".
    """
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_rating_map = {}
        self.food_cuisine_map = {}
        self.cuisine_food_map = defaultdict(list)
        for i in range(len(foods)):
            # Store 'rating' and 'cuisine' of the current 'food' in 'food_rating_map' and 'food_cuisine_map' maps.
            self.food_rating_map[foods[i]] = ratings[i]
            self.food_cuisine_map[foods[i]] = cuisines[i]
            heapq.heappush(self.cuisine_food_map[cuisines[i]], Food(ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_rating_map[food] = newRating
        cuisine_name = self.food_cuisine_map[food]
        heapq.heappush(self.cuisine_food_map[cuisine_name], Food(newRating, food))

    def highestRated(self, cuisine: str) -> str:
        highest_rated = self.cuisine_food_map[cuisine][0]
        # If the latest rating of 'food' doesn't match with the 'rating' on which it was sorted in the priority queue,
        # then we discard this element from the priority queue.
        while self.food_rating_map[highest_rated.food_name] != highest_rated.food_rating:
            heapq.heappop(self.cuisine_food_map[cuisine])
            highest_rated = self.cuisine_food_map[cuisine][0]
        return highest_rated.food_name

from sortedcontainers import SortedSet
class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_rating_map = {}
        self.food_cuisine_map = {}
        self.cuisine_food_map = defaultdict(SortedSet)
        for i in range(len(foods)):
            # Store 'rating' and 'cuisine' of the current 'food' in 'food_rating_map' and 'food_cuisine_map' maps.
            self.food_rating_map[foods[i]] = ratings[i]
            self.food_cuisine_map[foods[i]] = cuisines[i]
            self.cuisine_food_map[cuisines[i]].add((-ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine_name = self.food_cuisine_map[food]
        old_element= (-self.food_rating_map[food], food)
        self.cuisine_food_map[cuisine_name].remove(old_element)
        self.food_rating_map[food] = newRating
        self.cuisine_food_map[cuisine_name].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        highest_rated = self.cuisine_food_map[cuisine][0]
        return highest_rated[1]