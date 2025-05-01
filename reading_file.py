# Use the file name mbox-short.txt as the file name
#Prompting a message to the user
user_input = input("Enter a text file : ")

try:
    #Handling the file 
    fhandle = open(user_input)
    
except:
    #Handling error cases related to the file avalability
    print("The file is not available for reading! Check your file directory.")
    quit()

#Initialising my counter variables
count = 0
float_value = 0

#Iterating through the file
for lines in fhandle:
    
    #Conditionnal statement
    if lines.startswith("X-DSPAM-Confidence:"):
        
        #Incremeting the counter
        count += 1
        
        #Finding a starting point in the lines
        search_position = lines.find(":")
        
        #Getting a substring from the lines
        substring_value = lines[search_position+1:]
        
        try:
            #Tryint to converting the substring into a float
            float_conv = float(substring_value)
            
        except:
            #Handling error cases
            print("problem fount at", lines)
            
            #Quitting if the file is invalid or unreachable 
            quit()
        
        #Calculating the sum of the cumulated float
        float_value += float_conv
    
    else:
        #Skyping lines not starting by X-DSPAM-Confidence:
        continue

#Calculating the average 
average = float_value/count

#Final print statement
print("Average spam confidence:", average)
        
