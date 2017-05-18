import sys
def repeat(s,exclaim):
    result = s + s + s
    if exclaim:
        result = result + '!!!'
        
    return result
    

def main():
    print repeat('YAY', False)
    print repeat('Woohoo', True)
    


if __name__ == '__main__':
    main()
    

# OUT: YAYYAYYAY
# OUT: WoohooWoohooWoohoo!!!
