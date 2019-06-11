
# This is a script that can be modified to your specific needs to
# be used to search access logs for possible sensitive information 

import time
import re 


start_time = time.time()


# insert your file name into the open() function 

file = open('access.log')

# filters file contents by line item  
log_contents = filter(None, file.read().split('\n'))

for line in (log_contents):
    entries = re.findall(r'"([^"])*)"',line)
    url = entries[0].split(' ')[1]
    url_parts = url.split('?')
    
    if(len(url_parts) >= 1):
        query = url_parts[1]
        # enter your keywords to search for here 
        if(query.find('password' OR 'login' OR 'admin') > -1):
            print("Possible Credentials Found!: ")
            print(query)
            print("\n")

elapsed_time = time.time() - start_time
print(elapsed_time) 