import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
resume = '''Path I (Shorter, Applied):
555-123-1234
    Learn Python.

        Because in my opinion its very easy to learn and you can learn to code in no time.
        There are hundreds of dedicated websites, video courses, tutorials out there to learn Python.
        Some sources - Learn Python, Programming for Everybody (Getting Started with Python) | Coursera, Python 3.4 Programming Tutorials - YouTube .

    Go through some machine learning tutorial.

        An Introduction to Machine Learning .
        Python Programming Tutorials .
        Machine Learning Recipes with Josh Gordon - YouTube .

    Start experimenting with scikit-learn: machine learning in Python .
    Start experimenting with TensorFlow .

There you go. With above steps you can build your first machine learning solution within a month.

Only problem with this approach is that you won’t have deep understanding of the ML concepts.

Path II (Longer, Theory and Practice): 567-234-3244

    Theory:

        Linear Algebra - Strang.
        Multivariable Calculus - Apostol.
        Convex Optimization - Boyd.
        Probability - Ross.
        Mathematical Statistics - Rice.
        Data Structures and Algorithms - Cormen.
        Databases - Silberschatz.
        Elements of Statistical Learning - Hastie.
        Machine Learning - Bishop.
        Deep Learning - Goodfellow.
515-333-3456
    Practice:

        Learn Python.
        Implement machine learning algorithms yourself to gain better understanding of theory.
        Start using available machine learning library like - scikit-learn, theano, tensorflow, pybrain etc.
        Apply your learning on Kaggle projects.'''

#finall does not return an object but a list, one list item per object that has 0 or 1 group in them
mo = phoneRegex.findall(resume)
print(mo)

#where there are multiple objects returned it will return a list of tuples
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneRegex.findall(resume)
print(mo)

lyrics ='12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree'

xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall(lyrics)
print(mo)

vowelRegex = re.compile(r'[aeiouAEIOU]') #r'(a|e|i|o|u)'
mo = vowelRegex.findall('Robocop eats baby food')
print(mo)

#finding 2 in a row
vowelRegex = re.compile(r'[aeiouAEIOU]{2}') #r'(a|e|i|o|u)'
mo = vowelRegex.findall('Robocop eats baby food')
print(mo)

#negative character class using ^
vowelRegex = re.compile(r'[^aeiouAEIOU]') #r'(a|e|i|o|u)'
mo = vowelRegex.findall('Robocop eats baby food')
print(mo)

