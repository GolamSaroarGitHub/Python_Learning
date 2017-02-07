from textblob import TextBlob


wiki = TextBlob("Python is a high-level, general-purpose programming language.")

print(wiki.tags)

testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")
print(testimonial.sentiment)

print(testimonial.sentiment.polarity)

zen = TextBlob('''Beautiful is better than ugly. "
"Explicit is better than implicit.
"Simple is better than complex.''')
