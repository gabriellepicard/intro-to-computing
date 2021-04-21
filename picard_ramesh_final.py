# Set up function to open file
def open_file():
    while True:
        try:
            # Prompt user to input file
            file = input("Enter file name: ")
            fp = open(file,'r')
            #print('Open Success')
            break
        except:
            # Prompt user to re-enter file since it does not exist
            print('Error --', end='')
            pass
    return fp
    
# Function to read the file object
def read_data(fp):
        
    # IMPORT STRING MODULE FOR LATER
    import string
    
    # INITIALIZE LINE NUMBER TO 0
    line_num = 0
    
    # INITIALIZE DICTIONARY TO 0
    D = {}
        
    # DATA PRE-PROCESSING
    for line in fp:
        line = line.lower()
            
    # Split line to create a list
        words = line.split()
            
        # Remove punctuation
        for i in words:
            if i in string.punctuation:
                words.remove(i)
                    
        # Remove apostrophes, hyphens, and other punctuation from each word
        punctuation = str.maketrans('','',string.punctuation)
        words = [j.translate(punctuation) for j in words]
                
        # Use isalpha to remove words with special characters
        word_list = []
        for word in words:
            if word.isalpha() == False:
                word_list.append(word[:-1])
            else:
                word_list.append(word)
                    
        # Remove words with less than 2 characters
        for word in word_list:
            if len(word) < 2:
                word_list.remove(word)
        
        # Line number
        line_num += 1
        
        # Create dictionary
        for word in word_list:
            if word in D.keys():
                D[word].add(line_num)
            else:
                D[word] = set()
                D[word].add(line_num)
    
    return D
    
def find_cooccurance(D, inp_str):
    # Split inputted words into a list
    input_list = inp_str.split()
   
    # PRE-PROCESS TO MATCH FILE FORMAT
    # USE TRY STATEMENT IN CASE OF ERRORS
    try:
        # LOWER CASE
        for i in range(len(input_list)):
            input_list[i] = input_list[i].lower()
            
        # PRINT CO-OCCURENCE WORDS
        print('The co-occurence for: ', end='')
        print(*input_list, sep=', ')
        
        # REMOVE PUNCTUATION
        import string
        for i in input_list:
            if i in string.punctuation:
                input_list.remove(i)
                    
        # REMOVE APOSTROPHES, HYPHENS, ETC FROM WORDS
        punctuation = str.maketrans('','',string.punctuation)
        words = [j.translate(punctuation) for j in input_list]
                
        # USE ISALPHA TO REMOVE WORDS WITH SPECIAL VARIABLES
        input_list = []
        for word in words:
            if word.isalpha() == False:
                input_list.append(word[:-1])
            else:
                input_list.append(word)
                    
        # REMOVE WORDS WITH LESS THAN TWO VARIABLES
        for word in input_list:
            if len(word) < 2:
                input_list.remove(word)
                
        # CHECK IF INPUTS ARE IN FILE
        for word in input_list:
            if not word in D:
                input_list.remove(word)
        
        # CONVERT INPUTTED VALUES INTO SET TO USE FOR INTERSECTION
        set2 = set(input_list)
        
        # CONVERT VALUES IN D INTO SET TO USE FOR INTERSECTION
        D_2 = set(D)
        
        # CREATE LIST OF LINE NUMBERS THAT INCLUDES BOTH set2 & D_2
        Int = set2 & D_2
        line_num = []
        for word in D_2:
            if word in Int:
                line_num.append(D[word])
                
        # USE INTERSECTION OPERATOR TO SEE WHERE THE TWO LISTS INTERSECT    
        line_num_int = line_num[0].intersection(*line_num)
        line_num_final = list(line_num_int)
        
        # PRINT LINE NUMBERS OF CO-OCCURENCE
        if line_num_final == []:
            print('Lines: None.')
        else:
            print('Lines: ', end='') 
            print(*line_num_final, sep = ', ')
   
    # IF ERROR OCCURS, PRINT "Lines: None."
    except:
        print('Lines: None.')

# MAIN FUNCTION        
def main():
    
    #CALL OPEN_FILE
    fp = open_file()
    
    #CALL READ_DATA
    D = read_data(fp)
    
    # ASK TO ENTER WORDS TO CHECK FOR CO-OCCURENCE
    inp_str = input('Enter space separated words: ')
    
    # STOP FUNCTION IF INPUT IS: Q or q
    while inp_str.lower() != 'q':
        
        # CALL CO-OCCURENCE
        find_cooccurance(D, inp_str)
        
        # REPEAT CO-OCCURENCE UNTIL Q OR q INPUTTED
        inp_str = input('Enter space separated words: ')

if __name__ == "__main__":
    main()
