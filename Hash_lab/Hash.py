"""Hash Class"""
class Pair:
    def __init__(self,word):
        self.word = word
        self.count = 1

    def get_word(self):
        return self.word

    def get_count(self):
        return self.count

    def add_count(self):
        self.count += 1
    
    def __str__(self):
        return f"{self.word}, {self.count}"

class Hash:
    def __init__(self, mod):
        self.mod = mod
        self.col = 0
        self.buck = mod
        self.ary = [None] * mod
        self.add_call_count = 0

    def print_hash(self):
        yo = []
        for i in self.ary:
            sm = []
            if i:
                for j in i:
                    sm.append(str(j))
                yo.append(sm)
            else:
                yo.append(None)
        return yo
    
    def good_print_hash(self):
        yo = []
        for i in self.ary:
            if i:
                yo.append(str(i))
            else:
                yo.append(None)
        return yo
    
    def get_mod(self):
        return self.mod
    
    def get_add_call_count(self):
        return self.add_call_count

    def get_col(self):
        return self.col
    
    def get_buck(self):
        return self.buck
    
    def get_ary(self):
        return self.ary

        
    def make_key(self, item):
        base36 = 0
        chars = "0123456789abcdefghijklmnopqrstuvwxyz"
        item = item.lower()
        key = int.from_bytes(item.encode(), "big")
        while key:
            key, rem = divmod(key,36)
            base36 += ord(chars[rem])
        return base36

        """for i in range(len(item)):
            key += ord(item[i]) * i """
        
        return key
    
    def add(self, item):
        self.add_call_count += 1
        key = self.make_key(item)
        place = key % self.get_mod()
        if not self.ary[place]:
            self.ary[place] = [Pair(item)]
        
        else:
            found = False
            cat = self.ary[place]
            for buk in range(len(cat)):
                if cat[buk].word == item:
                    cat[buk].add_count()
                    cat.sort(key = lambda x:x.get_count(), reverse = True)
                    found = True
                    break
                self.col += 1
            if found == False:
                cat.append(Pair(item))
                self.buck += 1
            self.ary[place] = cat

    def find(self, item):
        item = item.lower()
        key = self.make_key(item)
        look = 0
        place = key % self.get_mod()
        cat = self.ary[place]
        for i in cat:
            look += 1
            if i.get_word() == item:
                return i.get_count(), look
            
    def good_find(self, item):
        item = item.lower()
        key = self.make_key(item)
        look = 0
        place = key % self.get_mod()
        cat = self.ary[place]
        while not cat.get_word() == item:
            look += 1
            place += 1
            if place == len(self.ary):
                place = 0
            cat = self.ary[place]
        look += 1
        return cat.get_word(), look
            
    def good_add(self,item):
        self.add_call_count += 1
        key = self.make_key(item)
        place = key % self.get_mod()

        if not self.ary[place]:
            self.ary[place] = Pair(item)

        elif self.ary[place].get_word() == item:
            self.ary[place].add_count()
        else:
            self.col += 1
            place += 1 
            if place >= len(self.ary):
                place = 0
            while self.ary[place]:
                if self.ary[place].get_word() == item:
                    self.ary[place].add_count()
                    return
                place += 1
                if place >= len(self.ary):
                    place = 0
                self.col
            self.ary[place] = Pair(item)

def words_in(word_list):
    # return num of buck, num of colisions
    global ha
    print(int(len(set(word_list)) * 1.2))
    ha = Hash(int(len(set(word_list)) * 1))
    print("here")
    for word in word_list:
        ha.good_add(word)
    print(ha.good_print_hash())
    return ha.get_buck(), ha.get_col()

def lookup_word_count(item):
    # return how many, num of lookups
    return ha.good_find(item)
                
            
            











def main():
    ha = Hash(10)
    ha.add("ti1")
    ha.add("me1")
    ha.add("ho1")
    ha.add("ti1")
    ha.add("it1")
    ha.add("it1")
    ha.add("it1")
    ha.add("it1")
    ha.add("1it")
    print(ha.print_hash())
    print(ha.find("1it"))

if __name__ == "__main__":
    main()
        


        