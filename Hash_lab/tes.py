from Hash import *
def words_in(word_list):
    # return num of buck, num of colisions
    global ha
    ha = Hash(200) 
    for word in word_list:
        ha.good_add(word)
    #print(ha.print_hash())
    return f"buk {ha.get_buck()} col {ha.get_col()}"

def lookup_word_count(item):
    # return how many, num of lookups
    return ha.find(item)



def main():
    
    word_list = ["Once", "upon", "a", "time", "in", "a", "small", "village", "there", "lived", "a", "young", "girl", "named", "Alice", "Alice", "was", "known", "for", "her", "curiosity", "and", "adventurous", "spirit", "One", "day", "while", "exploring", 
    "the", "forest", "nearby", "she", "stumbled", "upon", "a", "path", "The", "path", "was", "overgrown", "with", 
    "vines", "and", "looked", "like", "it", "had", "not", "been", "used", "in", "years", "Alice", "decided", "to", "follow", 
    "the", "path", "to", "see", "where", "it", "led", "After", "walking", "for", "a", "while", "she", "came", "across", "an", 
    "old", "abandoned", "cottage", "The", "cottage", "was", "covered", "in", "ivy", "and", "looked", "like", "it", "had", 
    "been", "empty", "for", "a", "long", "time", "Alice", "was", "intrigued", "and", "decided", "to", "explore", "inside", 
    "Inside", "the", "cottage", "she", "found", "a", "dusty", "old", "book", "on", "a", "shelf", "The", "book", "was", "filled", 
    "with", "stories", "about", "magical", "creatures", "and", "faraway", "lands", "Alice", "was", "fascinated", "and", 
    "spent", "hours", "reading", "the", "stories", "She", "noticed", "that", "one", "of", "the", "stories", "mentioned", 
    "a", "treasure", "in", "the", "forest", "Determined", "to", "find", "the", "treasure", "Alice", "set", "out", 
    "on", "a", "new", "adventure", "She", "followed", "the", "clues", "in", "the", "book", "which", "led", "her", "to", "a", 
    "clearing", "in", "the", "forest", "In", "the", "center", "of", "the", "clearing", "was", "a", "large", "tree", "with", 
    "a", "hollow", "trunk", "Alice", "reached", "inside", "the", "hollow", "trunk", "and", "pulled", "out", "a", "small", 
    "wooden", "box", "Inside", "the", "box", "was", "a", "beautiful", "golden", "necklace", "with", "a", "sparkling", "gem", 
    "Alice", "was", "thrilled", "with", "her", "discovery", "and", "rushed", "back", "to", "the", "village", "to", "show", 
    "everyone", "The", "villagers", "were", "amazed", "by", "the", "treasure", "and", "praised", "Alice", "for", "her", 
    "bravery", "and", "determination", "From", "that", "day", "on", "Alice", "was", "known", "as", "the", "girl", "who", 
    "found", "the", "treasure", "in", "the", "forest", "She", "continued", "to", "go", "on", "many", "more", 
    "adventures", "always", "following", "her", "curiosity", "and", "never", "afraid", "to", "explore", "the", "unknown", 
    "And", "so", "Alice's", "legend", "grew", "and", "she", "became", "an", "inspiration", "to", "all", "the", "children", 
    "in", "the", "village", "who", "dreamed", "of", "going", "on", "their", "own", "adventures", "and", "discovering", 
     "treasures", "of", "their", "own", "The", "end", "but", "the", "adventures", "never", "really", "ended", 
    "for", "Alice", "who", "always", "foFund", "new", "paths", "to", "explore", "and", "new", "stories", "to", "tell", "She", 
    "knew", "that", "the", "world", "was", "full", "of", "mysteries", "and", "she", "was", "determined", "to", "uncover", 
    "them", "all", "one", "adventure", "at", "a", "time", "Alice's", "story", "is", "a", "reminder", "to", "us", "all", "to", 
    "never", "lose", "our", "sense", "of", "wonder", "and", "to", "always", "be", "curious", "about", "the", "world", 
    "around", "us", "For", "it", "is", "through", "curiosity", "and", "adventure", "that", "we", "find", "the", "true", 
    "magic", "in", "life", "And", "so", "the", "story", "of", "Alice", "and", "her", "adventures", "lives", "on", "in", 
    "the", "hearts", "and", "minds", "of", "all", "who", "hear", "it", "inspiring", "them", "to", "go", "on", "their", 
    "own", "journeys", "and", "find", "their","own"]
    #print(len(set(word_list)))
    print(words_in(word_list))
    #print(lookup_word_count("find"))
if __name__ == "__main__":
    main()