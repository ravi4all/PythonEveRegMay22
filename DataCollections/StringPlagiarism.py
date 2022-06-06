text_1 = """
Python is a multiparadigm, general-purpose, interpreted, high-level programming language. Python allows programmers to use different programming styles to create simple or complex programs, get quicker results and write code almost as if speaking in a human language. Some of the popular systems and applications that have employed Python during development include Google Search, YouTube, BitTorrent, Google App Engine, Eve Online, Maya and iRobot machines.
"""
text_2 = """
Python is a high-level, general-purpose, interpreted object-oriented programming language. Similar to PERL, Python is a programming language popular among experienced C++ and Java programmers.
Working in Python, users can interpret statements in several operating systems, including UNIX-based systems, Mac OS, MS-DOS, OS/2 and various versions of Microsoft Windows 10 and Windows 11.
"""

# 1. Perform Tokenization - using split
# 2. Remove stopwords and punctuations
#   stopwords = [is, am, are, a, in, of, and, if, but, to, by...]
#   punctuations = '!@#$%^&*()_+-=][;'/.,<>?
# 3. Convert list of words to set data type
# 4. Use jaccard distance to find similarity between two strings
