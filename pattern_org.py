class patterns:
    def box(self,n):     #n=3,5
        # for i in range(10): print("-", end=" ")              # ------------
        # print(f"\n 1 \t n={n} \n")                           #   1   n=3
        # for i in range(n):                                   # * * *
        #     for j in range(n): print("*", end=" ")           # * * *
        #     print()     
        
        print("\n" .join("*"*n for _ in range(n)))                                     # * * *
        for i in range(10): print("-", end=" ")              # ------------
        print()

    def patternSet1(self,n):


        # 1️⃣ Simple star triangle
        def patternStarTriangle(n):
            print(f"\nPattern Star Triangle \t n={n}")
            print("\n".join("*"*(i+1) for i in range(n)))
            print("- "*10)

        # 2️⃣ Number triangle
        def patternNumberTriangle(n):
            print(f"\nPattern Number Triangle \t n={n}")
            print("\n".join(str(i+1)*(i+1) for i in range(n)))
            print("- "*10)

        # 3️⃣ Index triangle
        def patternIndexTriangle(n):
            print(f"\nPattern Index Triangle \t n={n}")
            for i in range(1,n+1):
                for j in range(i):
                    print(j, end=" ")
                print()
            print("- "*10)

        # 4️⃣ Binary alternating triangle
        def patternBinaryAlternating(n):
            print(f"\nPattern Binary Alternating \t n={n}")
            for i in range(n):
                star = 0 if i % 2 == 0 else 1
                for j in range(i):
                    print(star, end=" ")
                    star = 1 - star
                print()
            print("- "*10)

        # 5️⃣ Continuous number triangle
        def patternContinuousNumber(n):
            print(f"\nPattern Continuous Number \t n={n}")
            num = 1
            for i in range(n):
                for j in range(i):
                    print(num, end=" ")
                    num += 1
                print()
            print("- "*10)

        # 6️⃣ Alphabet triangle
        def patternAlphabetTriangle(n):
            print(f"\nPattern Alphabet Triangle \t n={n}")
            for i in range(n):
                for j in range(ord('A'), ord('A')+i+1):
                    print(chr(j), end=" ")
                print()
            print("- "*10)

        # 7️⃣ Alphabet repeated triangle
        def patternAlphabetRepeated(n):
            print(f"\nPattern Alphabet Repeated \t n={n}")
            for i in range(n):
                ch = ord('A') + i
                for j in range(i+1):
                    print(chr(ch), end=" ")
                print()
            print("- "*10)

        # 8️⃣ Reverse-starting alphabet triangle
        def patternReverseAlphabet(n):
            print(f"\nPattern Reverse-start Alphabet \t n={n}")
            ch = 'E'
            for i in range(1, n+1):
                for j in range(i):
                    print(chr(ord(ch)+j), end=" ")
                ch = chr(ord(ch)-1)
                print()
            print("- "*10)

        # ✅ Call all patterns for different n
        for n in [3,5]:
            patternStarTriangle(n)
            patternNumberTriangle(n)
            patternIndexTriangle(n)
        for n in [4,5]:
            patternBinaryAlternating(n)
            patternContinuousNumber(n)
            patternAlphabetTriangle(n)
            patternAlphabetRepeated(n)
            patternReverseAlphabet(n)

        print("\nAll patterns printed successfully!\n")


    def equilateralTriangle(self,n):

        def pattern8(n):     #n=4,5
            print(f"\n 8 \t n={n} \n")    
            for i in range(n):
                #for j in range(n-i):
                #    print("*",end=" ")
                for j in range(n-i-1):
                    print(" ",end=" ")
                for j in range(2*i+1):
                    print("*",end=" ")
                print()
            for i in range(10):
                print("-",end=" ")

        def pattern18(n):    #n=4,5
            print(f"\n 18 \t n={n} \n")
            for i in range(n):
                ch='A'
                breakthr = (2*i+1)//2
                for j in range(n-i-1):
                    print(" ",end=" ")
                for j in range(2*i+1):
                    print((ch),end=" ")
                    if j<= breakthr: ch = chr(ord(ch)+1)
                    else: ch = chr(ord(ch)-1)
                print()
            for i in range(10):
                    print("-",end=" ")  

        pattern8(4)
        print()
        pattern8(5)
        print()

        pattern18(4)
        print()
        pattern18(5)
        print()

    def invertedRightangleTriangle(self,n):

        def pattern5(n):     #n=3,5
            print(f"\n 5 \t n={n} \n")    
            for i in range (n):
                for j in range(n-i):
                    print("*",end=" ")
                print()
            for i in range(10):
                print("-",end=" ")
        
        def pattern6(n):     #n=3,5
            print(f"\n 6 \t n={n} \n")     
            for i in range(n):
                for j in range(n-i):
                    print(j+1,end=" ")
                print()
            for i in range(10):
                print("-",end=" ")

        def pattern16(n):    #n=4,5
            print(f"\n 16 \t n={n} \n")                     #  A B C D                      
            for i in range(n):                              #  A B C
                for j in range(ord('A'),ord('A')+n-i):      #  A B
                    print(chr(j),end=" ")                   #  A
                print()

            for i in range(10):
                    print("-",end=" ")

        pattern5(3)
        print()
        pattern5(5)
        print()

        pattern6(3)
        print()
        pattern6(5)
        print()

        pattern16(4)
        print()
        pattern16(5)
        print()
  
    def Center_AlignedRightTriangle(self, n):    # n=4,5
        print(f"\n 7 \t n={n} \n")                           #   7   n=4
        for i in range(n):
            for j in range(n-i-1): print(" ", end=" ")       #       *
            for j in range(i+1): print("*", end=" ")         #     * *
            print()                                          #   * * *
        for i in range(10): print("-", end=" ")              # * * * *
        print()
  
    def InvertedPyramidStarPattern(self,n):     #n=4,5
        print(f"\n 9 \t n={n} \n")    
        for i in range(n):
            for j in range(i):
                print(" ",end=" ")
            for j in range(2*n-(2*i+1)):
                print("*",end=" ")
            print()
        for i in range(10):
            print("-",end=" ")
    
    def Left_AlignedDiamondPattern(self,n):    #n=4,5
        print(f"\n 10 \t n={n} \n")    
        for i in range(2*n+1):
            star=i
            if i>n:
                 star=2*n-i
            for j in range(star):
                print("*",end=" ")
            print()
        for i in range(10):
            print("-",end=" ")
   
    def DiamondStarPattern(self,n):    #n=4,5
        print(f"\n 12 \t n={n} \n") 
        for i in range(n):
            #for j in range(n-i):
            #    print("*",end=" ")
            for j in range(n-i-1):
                print(" ",end=" ")
            for j in range(2*i+1):
                print("*",end=" ")
            print()
        for i in range(n):
            for j in range(i):
                print(" ",end=" ")
            for j in range(2*n-(2*i+1)):
                print("*",end=" ")
            print()
        for i in range(10):
            print("-",end=" ")
    
    def PalindromicNumberPyramid(self,n):    #n=4,5,6
        print(f"\n 13 \t n={n} \n")                 #1             1
        for i in range(1,n+1):                      #1 2         2 1
            for j in range(1,i+1):                  #1 2 3     3 2 1
                print(j,end=" ")                    #1 2 3 4 4 3 2 1
            for j in range(2*(n-i)):
                print(" ",end=" ")
        # Last row: repeat last number
            for j in range(i, 0, -1):
                    print(j, end=" ")
            print()
           
        for i in range(10):
            print("-",end=" ") 

    def pattern20(self,n):    #n=4,5
        print(f"\n 20 \t n={n} \n")
        for i in range(10):
                print("-",end=" ")  

    def pattern21(self,n):    #n=4,5
        print(f"\n 21 \t n={n} \n")
        for i in range(10):
                print("-",end=" ")  

    def extraction_of_digits(self, n):

        # 1️⃣ Sum of digits
        def sumOfDigits(n):
            total = 0
            temp = n
            while temp != 0:
                rem = temp % 10
                total += rem
                temp //= 10
            print(f"Sum of digits of {n} is: {total}")

        # 2️⃣ Check if number is palindrome
        def checkPalindrome(n):
            n1 = n
            rev = 0
            temp = n
            while temp != 0:
                rem = temp % 10
                rev = rev * 10 + rem
                temp //= 10
            if rev == n1:
                print(f"{n} is a palindrome: True")
            else:
                print(f"{n} is a palindrome: False")

        # 3️⃣ Check if number is Armstrong (for 3-digit numbers)
        def checkArmstrong(n):
            n1 = n
            total = 0
            temp = n
            while temp != 0:
                rem = temp % 10
                total += rem ** 3
                temp //= 10
            if total == n1:
                print(f"{n1} is an Armstrong number")
            else:
                print(f"{n1} is NOT an Armstrong number")

        # 4️⃣ Find length of number
        def findLengthOfNum(n):
            if n == 0:
                length = 1
            else:
                length = 0
                temp = n
                while temp != 0:
                    temp //= 10
                    length += 1
            print(f"Length of {n} is: {length}")

        # 5️⃣ Call all functions
        def callExteactopm_of_digits_function(n):
            print("\nDigit Extraction and Number Checks:\n")
            sumOfDigits(n)
            checkPalindrome(n)
            checkArmstrong(n)
            findLengthOfNum(n)

        callExteactopm_of_digits_function(n)


    def recursionProblem(self, n):

        # 1️⃣ Print numbers from 1 to n
        def PrintTheNumUptoN(n):
            if n == 0:
                return
            PrintTheNumUptoN(n - 1)
            print(n, end=" ")

        # 2️⃣ Print numbers from n to 1
        def PrintTheNumFromN(n):
            if n == 0:
                return
            print(n, end=" ")
            PrintTheNumFromN(n - 1)

        # 3️⃣ Find factorial of n
        def findFactorialOfN(n):
            if n == 0 or n == 1:
                return 1
            return n * findFactorialOfN(n - 1)

        # 4️⃣ Find sum of first n numbers (Parameterized recursion)
        def sumOfN(n, s=0):
            if n == 0:
                return s
            return sumOfN(n - 1, s + n)

        # 5️⃣ Find nth Fibonacci number
        def getFibonacciOfN(n):
            if n <= 1:
                return n
            return getFibonacciOfN(n - 1) + getFibonacciOfN(n - 2)

        # 6️⃣ Print all recursive results neatly
        def callRecursionFuncion(n):
            print("\nUsing recursion:\n")

            print(f"\tPrintTheNumUptoN\t: ", end="")
            PrintTheNumUptoN(n)
            print()

            print(f"\tPrintTheNumFromN\t: ", end="")
            PrintTheNumFromN(n)
            print()

            print(f"\tfindFactorialOfN\t: {findFactorialOfN(n)}")
            print(f"\tsumOfN\t\t\t: {sumOfN(n)}")

            print(f"\tgetFibonacciOfN\t\t: {getFibonacciOfN(n)}")

            print(f"\tgetFibonacciSeriesOfN\t: ", end="")
            for i in range(n):
                print(getFibonacciOfN(i), end=" ")
            print("\n")

        # Call everything
        callRecursionFuncion(n)

            
        

    def print_Pattern(self):

        self.box(3)
        print()
        self.box(5)
        print()

        self.patternSet1(3)
        print()

        self.equilateralTriangle(3)
        print()

        self.invertedRightangleTriangle(4)
        print()

        self.Center_AlignedRightTriangle(4)
        print()
        self.Center_AlignedRightTriangle(5)
        print()

        self.InvertedPyramidStarPattern(4)
        print()
        self.InvertedPyramidStarPattern(5)
        print()

        self.Left_AlignedDiamondPattern(4)
        print()
        self.Left_AlignedDiamondPattern(5)
        print()

        self.DiamondStarPattern(4)
        print()
        self.DiamondStarPattern(5)
        print()

        self.PalindromicNumberPyramid(4)
        print()
        self.PalindromicNumberPyramid(5)
        print()
        self.PalindromicNumberPyramid(6)
        print()

        self.pattern20(4)
        print()
        self.pattern20(5)
        print()

        self.pattern21(4)
        print()
        self.pattern21(5)
        print()

        self.extraction_of_digits(434)
        print()

        self.recursionProblem(6)
        print()



a= patterns()
a.print_Pattern()
