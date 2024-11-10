#task 1
reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

words_to_highlight = ["good","excellent","bad","poor","average"]

def highlight_words(review,words_to_highlight):
    for words in words_to_highlight:
       review = review.replace(words, words.upper())
    return review

for review in reviews:
    print(highlight_words(review, words_to_highlight))

#task 2
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def counting_positive_words(reviews):
   
    count = 0
    for review in reviews:
       words= review.split()
    for words in positive_words:
          count += 1
    return count
counts=counting_positive_words(reviews)
#counting_negative_words()
print(f"there are {counts} positive words in review ")

def counting_negative_words(reviews):
  count = 0
  for review in reviews:
       words= review.split()
  for words in negative_words:
          count += 1
  return count
counts=counting_negative_words(reviews)
#counting_negative_words()
print(f"there are {counts} negative words in review ")


#task 3

def create_summary(review, max_length=30):
    
    if len(review) <= max_length:
        return review
    end = review.rfind(' ', 0, max_length)
    
    if end == -1:
        return review[:max_length] + "…"
    else:
        return review[:end] + "…"
for review in reviews:
    print(create_summary(review))


#question 2
def validate_name_length():
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()
    
    if len(first_name) < 2:
        print("Error: First name must be at least 2 characters long.")
    elif len(last_name) < 2:
        print("Error: Last name must be at least 2 characters long.")
    else:
        print("Name validated successfully.")

validate_name_length()