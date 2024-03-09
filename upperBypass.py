def code_html(text):
    htmlChars = {'0':'&#48;', '1':'&#49;', '2':'&#50;', '3':'&#51;', '4':'&#52;', '5':'&#53;', '6':'&#54;', 
                '7':'&#55;', '8':'&#56;', '9':'&#59;', 'A':'&#65;', 'B':'&#66;', 'C':'&#67;', 'D':'&#68;', 
                'E':'&#69;', 'F':'&#70;', 'G':'&#71;', 'H':'&#72;', 'I':'&#73;', 'J':'&#74;', 'K':'&#75;', 
                'L':'&#76;', 'M':'&#77;', 'N':'&#78;', 'Ñ':'&#209;', 'O':'&#79;', 'P':'&#80;', 'Q':'&#81;', 
                'R':'&#82;', 'S':'&#83;', 'T':'&#84;', 'U':'&#85;', 'V':'&#86;', 'W':'&#87;', 'X':'&#88;', 
                'Y':'&#89;', 'Z':'&#90;', 'a':'&#97;', 'b':'&#98;', 'c':'&#99;', 'd':'&#100;', 'e':'&#101;', 
                'f':'&#102;', 'g':'&#103;', 'h':'&#104;', 'i':'&#105;', 'j':'&#106;', 'k':'&#107;', 'l':'&#108;', 
                'm':'&#109;', 'n':'&#110;', 'ñ':'&#241;', 'o':'&#111;', 'p':'&#112;', 'q':'&#113;', 'r':'&#114;', 
                's':'&#115;', 't':'&#116;', 'u':'&#117;', 'v':'&#118;', 'w':'&#119;', 'x':'&#120;', 'y':'&#121;', 
                'z':'&#122;'}
    str_html = ''
    for char in text:
        str_html += htmlChars.get(char, char)
    return str_html

    # Converts alphanumeric characters to HTML entities.

def code_urlAll(text):
    asciiChars = {' ': '%20', '!': '%21', '"': '%22', '#': '%23', '$': '%24','%': '%25', '&': '%26', 
                "'": '%27', '(': '%28', ')': '%29', '*': '%2A', '+': '%2B', ',': '%2C', '.': '%2E', 
                '/': '%2F', '0': '%30', '1': '%31', '2': '%32', '3': '%33', '4': '%34', '5': '%35', 
                '6': '%36', '7': '%37', '8': '%38', '9': '%39', ':': '%3A', ';': '%3B', '<': '%3C', 
                '=': '%3D', '>': '%3E', '?': '%3F', '@': '%40', 'A': '%41', 'B': '%42', 'C': '%43', 
                'D': '%44', 'E': '%45', 'F': '%46', 'G': '%47', 'H': '%48', 'I': '%49', 'J': '%4A', 
                'K': '%4B', 'L': '%4C', 'M': '%4D', 'N': '%4E', 'O': '%4F', 'P': '%50', 'Q': '%51', 
                'R': '%52', 'S': '%53', 'T': '%54', 'U': '%55', 'V': '%56', 'W': '%57', 'X': '%58', 
                'Y': '%59', 'Z': '%5A', '[': '%5B', '\\': '%5C', ']': '%5D', '^': '%5E', '_': '%5F', 
                '`': '%60', 'a': '%61', 'b': '%62', 'c': '%63', 'd': '%64', 'e': '%65', 'f': '%66', 
                'g': '%67', 'h': '%68', 'i': '%69', 'j': '%6A', 'k': '%6B', 'l': '%6C', 'm': '%6D', 
                'n': '%6E', 'o': '%6F', 'p': '%70', 'q': '%71', 'r': '%72', 's': '%73', 't': '%74', 
                'u': '%75', 'v': '%76', 'w': '%77', 'x': '%78', 'y': '%79', 'z': '%7A', '{': '%7B', 
                '|': '%7C', '}': '%7D', '`': '%60', '~': '%7E', 'Ñ': '%D1', 'ñ': '%F1'}
    str_url = ''
    for char in text:
        str_url += asciiChars.get(char, char)
    return str_url

    # Encodes any printable character as URL.

def code_url(text):
    asciiChars = {'0': '%30', '1': '%31', '2': '%32', '3': '%33', '4': '%34', '5': '%35', 
                '6': '%36', '7': '%37', '8': '%38', '9': '%39', 'A': '%41', 'B': '%42', 'C': '%43', 
                'D': '%44', 'E': '%45', 'F': '%46', 'G': '%47', 'H': '%48', 'I': '%49', 'J': '%4A', 
                'K': '%4B', 'L': '%4C', 'M': '%4D', 'N': '%4E', 'O': '%4F', 'P': '%50', 'Q': '%51', 
                'R': '%52', 'S': '%53', 'T': '%54', 'U': '%55', 'V': '%56', 'W': '%57', 'X': '%58', 
                'Y': '%59', 'Z': '%5A', 'a': '%61', 'b': '%62', 'c': '%63', 'd': '%64', 'e': '%65', 
                'f': '%66', 'g': '%67', 'h': '%68', 'i': '%69', 'j': '%6A', 'k': '%6B', 'l': '%6C', 
                'm': '%6D', 'n': '%6E', 'o': '%6F', 'p': '%70', 'q': '%71', 'r': '%72', 's': '%73', 
                't': '%74', 'u': '%75', 'v': '%76', 'w': '%77', 'x': '%78', 'y': '%79', 'z': '%7A', 
                'Ñ': '%D1', 'ñ': '%F1', '&': '%26', '#': '%23', ';': '%3B', ' ': '+', '\\': '%5C'}

    str_url = ''
    for char in text:
        str_url += asciiChars.get(char, char)
    return str_url

    # Encodes any alphanumeric character as URL, plus the special characters that make up the html entities: '&', '#' and ';'.

def code_unicode(text):
    asciiChars = {'0': '\\u0030', '1': '\\u0031', '2': '\\u0032', '3': '\\u0033', '4': '\\u0034', '5': '\\u0035', 
                '6': '\\u0036', '7': '\\u0037', '8': '\\u0038', '9': '\\u0039', 'A': '\\u0041', 'B': '\\u0042', 'C': '\\u0043', 
                'D': '\\u0044', 'E': '\\u0045', 'F': '\\u0046', 'G': '\\u0047', 'H': '\\u0048', 'I': '\\u0049', 'J': '\\u004a', 
                'K': '\\u004b', 'L': '\\u004c', 'M': '\\u004d', 'N': '\\u004e', 'O': '\\u004f', 'P': '\\u0050', 'Q': '\\u0051', 
                'R': '\\u0052', 'S': '\\u0053', 'T': '\\u0054', 'U': '\\u0055', 'V': '\\u0056', 'W': '\\u0057', 'X': '\\u0058', 
                'Y': '\\u0059', 'Z': '\\u005a', 'a': '\\u0061', 'b': '\\u0062', 'c': '\\u0063', 'd': '\\u0064', 'e': '\\u0065', 
                'f': '\\u0066', 'g': '\\u0067', 'h': '\\u0068', 'i': '\\u0069', 'j': '\\u006a', 'k': '\\u006b', 'l': '\\u006c', 
                'm': '\\u006d', 'n': '\\u006e', 'o': '\\u006f', 'p': '\\u0070', 'q': '\\u0071', 'r': '\\u0072', 's': '\\u0073', 
                't': '\\u0074', 'u': '\\u0075', 'v': '\\u0076', 'w': '\\u0077', 'x': '\\u0078', 'y': '\\u0079', 'z': '\\u007a', 
                'Ñ': '\\u00d1', 'ñ': '\\u00f1'}

    str_uni = ''
    for char in text:
        str_uni += asciiChars.get(char, char)
    return str_uni

    # Encodes any alphanumeric character as Unicode, with the format '\u00xy'.

text = input("Enter the text you want to encode: \r\n")
choice = input("Do you want to encode the whole string to URL? Y or N\r\n")
if choice == 'Y' or choice == 'y':
    str_url = code_urlAll(text)
    print(str_url)
elif choice == 'N' or choice == 'n':
    choice1 = input("Do you want to encode alphanumeric characters as HTML entities or as Unicode characters? H or U\r\n")
    if choice1 == 'H' or choice1 == 'h':
        str_html = code_html(text)
        print("String without URL encode: " + str_html)
        choice2 = input("Do you want to encode special chars as URL? Y or N\r\n")
        if choice2 == 'Y' or choice2 == 'y':
            str_url = code_urlAll(str_html)
            print(str_url)
        elif choice2 == 'N' or choice2 == 'n':
            str_url = code_url(str_html)
            print(str_url)
        else:
            print("Begin again\r\n")
            exit()
    elif choice1 == 'U' or choice1 == 'u':
        str_uni = code_unicode(text)
        print("String without URL encode: " + str_uni)
        choice2 = input("Do you want to encode special chars as URL? Y or N\r\n")
        if choice2 == 'Y' or choice2 == 'y':
            str_url = code_urlAll(str_uni)
            print(str_url)
        elif choice2 == 'N' or choice2 == 'n':
            str_url = code_url(str_uni)
            print(str_url)
        else:
            print("Begin again\r\n")
            exit()
    else:
        print("begin again")
        exit()
else:
    print("Begin again")
    exit()
