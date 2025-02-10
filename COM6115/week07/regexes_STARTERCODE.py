
# COM6115: Text Processing
# Regular Expressions Lab Class

import sys, re

#------------------------------

testRE = re.compile('(logic|sicstus)', re.I)

#------------------------------

with open('RGX_DATA.html') as infs:
    linenum = 0
    for line in infs:
        linenum += 1
        if line.strip() == '':
            continue
        print('  ', '-' * 100, '[%d]' % linenum, '\n   TEXT:', line, end='')
    
        m = testRE.search(line)
        if m:
            print('** TEST-RE:', m.group(1))

        # Regex pattern to find matches Option1 : But its not working well with < , > in text
        #pattern = "<.*>"
        # Find all matches
        #matches = re.findall(pattern, line)
        #print('** RegEx:', matches)

        # Regex pattern to find matches , Option 2 to find matches
        pattern = r"</?([a-zA-Z0-9]+)>"
        mm = testRE.finditer(line)
        m = testRE.finditer(line)
        #for m in mm:
        #    print('** TEST-RE:', m.group(1))

        # Use re.finditer to get match objects
        matches = re.finditer(pattern, line)

        # Process each match
        for match in matches:
            tag_name = match.group(1)  # Extract the tag name
            if match.group(0).startswith("</"):
                print(f"CLOSETAG: {tag_name}")
            else:
                print(f"OPENTAG: {tag_name}")

# Step3 : open-tags works for tags both with and without parameters

