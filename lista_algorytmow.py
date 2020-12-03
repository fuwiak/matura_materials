def decimalToBinary(num):
    num_=""
    if num > 1:
        decimalToBinary(num // 2)
        num_+=str(num % 2)
    
    return num_
