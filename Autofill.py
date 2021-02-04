#!/usr/bin/env python
# coding: utf-8



# In[2]:


#to load the file in the variable "filename"
filename = "liste_magazine.txt"
with open(filename) as f:              #open() --> opens the file
    pre_list = f.read().splitlines()   #read() -> reads the file splitlines()-> returns a list with all the lines in string
    org_list = [x for x in pre_list]   # org_list to keep the original list of contents
    list = [x.lower() for x in pre_list]  #list to keep the converted lower case strings 
    print(list)

list.sort()                              #sort() -> to sort alphabeitcally so that the output is sorted
# for elements in list:
#     print(elements)


# In[7]:


#class Trie has __init__() method as constructor to initialize the attributes of the class
words = []
class Trie:
    def __init__(self):
        self.next = {}   
        #next has empty dictionary which is used to keep track of child node(character/s) as the key value pair through link
        self.leaf = False #leaf is the end node when true. 
    
    
 #add_item() method is used to insert all the items of the sorted list in the format of Trie. Each item is passed
 #through this method till the end of the list

    def add_item(self, word):
        count = 0                        #counter to keep track of number of iterations of each item.
        while count < len(word):         #while loop executes till the counter is less than the length of an item
            letter = word[count]         #assigns the content of the word based on index or position
            if not letter in self.next:  #if the character of that word is not in Trie 
                node = Trie()            #inittilize the attributes self.next = {} and self.leaf = false
                self.next[letter] = node
            self = self.next[letter]     #add the character in a trie
            if count == len(word) - 1:   #if all the characters of a word is added to a trie then exit the method else keep adding
                self.leaf = True
            else:
                self.leaf = False
            count += 1


#autofill method() takes the input which user has entered. The entered string can be of any length. If the entered characters
#matches those many characters then it calls the traverse() method and all the words will appear as output
#if the entered characters doesn't match the Trie at any level then it returns "Nothing"

    def autofill(self, word):
        count = 0                          #counter initialized to 0
        add_node = ''                      #to store the entered characters
        while count < len(word):           #run the loop till counter exceeds the length of the entered character
            letter = word[count]           #each character is assigned to letter
            add_node += letter             #assign that character to add_node to store
            if letter in self.next:        #if the entered character is in Trie, get that character      
                self = self.next[letter]   
            else:
                return 'NOTHING'           #else display "Nothing"
            count += 1
        self.traverse(add_node)            #after the successful while, it comes out and calls traverse() to get all the 
        return "\n"                        #possible matching words

#traverse() method -> if no input then all the items of the list are printed else it traverses to all the possible 
#nodes which is beginning from the passed characters as an attribute in word.

    def traverse(self, word):
        if self.leaf:                       #if it reached the end of the node
            for i in org_list:              #to print the original format as I changed the list to lower case above
                if i.lower()==word:
                    #print(i)
                    words.append(i)
                    
        for count in self.next:            #get the next character from the the trie -> linking to next node or character
            add_node = word + count        #current character/s + next character/s is stored in add_node
            self.next[count].traverse(add_node) #intitialize the attribute and do it recuresively



x = Trie()
for i in list:         
    x.add_item(i)           #add_item() is called for each word in the list
    
input_string = input("Enter the character: ")   #user input to search 
user_input = input_string.lower()               #convert the user input to lowercase to match
print(x.autofill(user_input))                   
for i in words[0:3]:
    print(i)


#         
#         
