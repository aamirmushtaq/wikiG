import sys
def main():
    print 'Hello : ' , sys.argv[1]
    

if __name__ == '__main__':
    main()
    

# OUT: Hello : Traceback (most recent call last):
# OUT:   File "<input>", line 2, in <module>
# OUT:   File "<input>", line 2, in main
# OUT: IndexError: list index out of range
