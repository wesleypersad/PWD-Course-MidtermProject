# functions defined for midterms all in one place

# Function to read data from a file
def read_lyrics(filename):
    # Read the text file containing the words into a string
    f= open(filename, "r")
    lyrics = f.read()
    f.close()
    return lyrics

# Function to read data from file and convert all words to lower case
def read_lyrics_lower(filename):
    # Read the text file containing the words into a string
    f= open(filename, "r")
    lyrics = f.read()
    f.close()
    lyrics = lyrics.lower()
    return lyrics

# Function to tokenise the string into a list of words
# Problem with this for some reason !!!
def tokenize(data):
    # Tokenize the data to split it into a list of words
    wordlist = word_tokenize(data)
    return wordlist

# Function to remove the stop words from a list
def remove_stop(words):
    #This will remove the defined stop words from the words list
    words = [w for w in words if not w in stop]
    return words

# Function to create a dictionary and count the occurance of each word in the list
def count_words(words):
    # Count each word and create a dictionary containing the count
    counter = {}
    for word in words:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    return counter

# Function to create a word cloud form a list of words
#def make_cloud(words):
#    # Find the fequency of the words
#    data_analysis = nltk.FreqDist(words)
#    wcloud = WordCloud().generate_from_frequencies(data_analysis)
#    return wcloud

# Function to draw the word cloud
#def draw_cloud(wcloud):
#    # Plot the wordcloud for the dictionary
#    plt.imshow(wcloud, interpolation="bilinear")
#    plt.axis("off")
#    (-1.5, 200, 100, -2.5)
#    plt.show()

# Function to return a soup object from a webpage
#def get_soup(URL, jar=None):
#    request_headers = {"update-insecure-requests":"1",
#                       "user-agent":"Chrome",
#                       "accept":"text/html",
#                       "accept-encoding":"gzip, deflate, br",
#                       "accept-language":"en-US,en;q=0.8"        
#                        }
#    if jar:
#        r = requests.get(URL, cookies=jar, headers=request_headers)
#    else:
#        r = requests.get(URL, headers=request_headers)
#        jar = requests.cookies.RequestsCookieJar()
#    #print(r.url)
#    data = r.text
#    soup = BeautifulSoup(data, "html.parser")
#    return soup, jar

# Function to display all the div elements in a soup object
#def page_data(soup):
#    print(rootsoup.find_all('div'))

# Function to extract all the album data
#def album_data(soup):
#    # return a list of albums and tracks
#    return soup.find_all('div', {'class': ['album', 'listalbum-item']})
