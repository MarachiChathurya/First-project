a1={}
a2={}
def anagrams(str1,str2):
        if len(str1)!=len(str2):
                return False
        else:
                num=0
                for x in str1:
                        a1[num]=x
                        num+=1
                num=0
                for x in str2:
                        a2[num]=x
                        num+=1
                b=sorted(a1.values())
                c=sorted(a2.values())
                if b==c:
                        return True
                else:
                        return False
string1=input("Enter the string")
string2=input("Enter the string to find wheather it is anagram")
print(anagrams(string1,string2))
                
