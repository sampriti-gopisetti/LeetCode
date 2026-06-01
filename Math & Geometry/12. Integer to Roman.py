class Solution:
    def intToRoman(self, num: int) -> str:
        symbol_dict={1: "I",5: "V",10: "X",50: "L",100: "C",500: "D",1000: "M",4: "IV",9: "IX",40: "XL",90: "XC",400: "CD",900: "CM"}
        roman=""
        digit=[]
        while num>0:
            digit.append(num%10)
            num=num//10
        for i in range(len(digit)-1,-1,-1):
            number=digit[i]*pow(10,i)
            if number in symbol_dict:
                roman=roman+symbol_dict[number]
                number=0
            elif number>(5*pow(10,i)):
                roman=roman+symbol_dict[5*pow(10,i)]
                number=number-(5*pow(10,i))
            if number!=0:
                count=number//pow(10,i)
                roman=roman+(count*symbol_dict[pow(10,i)])
        return roman

        