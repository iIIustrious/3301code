from binascii import unhexlify, hexlify
import sys

"""
Written by Onecool, Surtri and (some) iIIustrious
"""

hexadecimal = {' ' : "Spacebar", '0' : "0000", '1' : "0001", '2' : "0010", '3' : "0011", '4' : "0100", '5' : "0101", '6' : "0110", '7' : "0111", '8' : "1000", '9' : "1001", 'a' : "1010", 'b' : "1011", 'c' : "1100", 'd' : "1101", 'e' : "1110", 'f' : "1111", 'A' : "1010", 'B' : "1011", 'C' : "1100", 'D' : "1101", 'E' : "1110", 'F' : "1111"}
binary_4bit = {y:x for x, y in hexadecimal.items()}

def ConvertToBinary(strHex):
    newlist = []
    for i in strHex:
        if i in hexadecimal:
            newlist.append(hexadecimal[i])
        else:
            newlist.append("X")
    return ''.join(newlist)

def ConvertBinaryToHex(strBinary):
    newlist = []
    step = 4 #4 bit hex
    for i in [strBinary[i:i+step] for i in range(0,len(strBinary),step)]:
        if i in binary_4bit:
            newlist.append(binary_4bit[i])
    return ''.join(newlist)

def ConvertHexToASCII(strHex):
    
    return ''

def ConvertToAscii(bits):
    chars = []
    for b in range(int(len(bits) / 8)):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)


def bitwiseXOR(str1, str2):

    newlist = []
    for i in range(0,len(str1)):
        s1 = int(str1[i])
        s2 = int(str2[i])
        s3 = s1 ^ s2
        newlist.append(str(s3))
        
    return ''.join(newlist)

def main():
    # Open files.
    hex1 = "test message"
    hex2 = "648244116d8e8f0bf11ab92993f57dc05faa351dbaee6b05f38afb695ec682516c8e7d0b6ed9c2d9885ffd5ae94d35b371751953f143b0a2634f4376dc120ab29acb5b6d87bbefa595fc74b7230dc863e3e3157f5653bab9cf18a1e84dc42792bad129659938791e627f2da2d476af82fb94ba8f7b7975c72f490e64f9d8f0a7389595c51044c534afabf89fc0695776fc9d84967c07d369c0837504e6310411121bc37d0fc9f192edfc5d0726c21efdfe27c4b0c01dc334c8d8efd66605952bcf01fde3b3f5dfa912c5a90625a590ba5491cdca900c02fc2ed9bdb9832cdffba67f89efe50ccd29b4deabb8c21ce2c533a45043a977adade633ef94ab292436"
    hex3 = "87de5b7fa26ab85d2256c453e7f5bc3ac7f25ee743297817febd7741ededf07ca0c7e8b1788ea4131441a8f71c63943d8b56aea6a45159e2f59f9a194af23eaabf9de0f3123c041c882d5b7e03e17ac49be67cef29fbc7786e3bda321a176498835f6198ef22e81c30d44281cd217f7a46f58c84dd7b29b941403ecd75c0c735d20266121f875aa8dec28f32fc153b1393e143fc71616945eea3c10d6820bd631cf775cf3c1f27925b4a2da655f783f7616f3359b23cff6fb5cb69bcb745c55dff439f7eb6a4094bd302b65a84360a62f94c8b010250fcc431c190d6ed8cc8a3bfce37dddb24b93f502ad83c5fa21923189d8be7a6127c4105fcf0e5275286f2"
    hex4 = "bf1d5574ca36efd524e6c34c26cbd628b19aa835aceb94ea7f2ca7f33d1b8f51476bc597d4bf9ad5111d8f39ef5351b3b090bce47f023002fe69928e79f6f8147f6fe051f2f159041f932f5190308d7441fc3cecead0851662d3217485827e640a4183fa5bc8cef5ff7d1473d2746a37fbc8b94318ff0d3aeb467017c0ea5cb33b3e6967453986e1450b35ad47861f679cf7db5a6c170bcfb67544983ec1e36b27ee8c5721da39d27dbfa0cdc15ba3cbaa425e8a8b96b81ab665f3ebc41563a0e9270695d3d68887cfab2c07b290718307f764afba684b17fcfd71323f64206e5fa378b4ee89e80885733080065dd34a5c838898906b8d43de9f1d8eb6922bad"
    s2 = ConvertToBinary(hex2)
    s3 = ConvertToBinary(hex3)
    s4 = ConvertToBinary(hex4)
    
    bitwise_s2s3 = bitwiseXOR(s2,s3)
    bitwise_s2s4 = bitwiseXOR(s2,s4)
    bitwise_s3s4 = bitwiseXOR(s3,s4)

    s2s3Out = ConvertBinaryToHex(bitwise_s2s3)
    s2s4Out = ConvertBinaryToHex(bitwise_s2s4)
    s3s4Out = ConvertBinaryToHex(bitwise_s3s4)
    # XOR everything.


    sys.stdout.write('\n---------------------------Onion 2--------------------------\n')
    sys.stdout.write('Hex : ' + hex2 + '\n')
    sys.stdout.write('Bin : ' + s2 + '\n')
    sys.stdout.write('\n---------------------------Onion 3--------------------------\n')
    sys.stdout.write('Hex : ' + hex3 + '\n')
    sys.stdout.write('Bin : ' + s3 + '\n')
    sys.stdout.write('\n--------------------------Onion 4----------------------------\n')
    sys.stdout.write('Hex : ' + hex4 + '\n')
    sys.stdout.write('Bin : ' + s4 + '\n')
        
    sys.stdout.write('\n\n\n\n--------------------------Bitwise XOR Onion2 and Onion 3----------------------------\n')
    sys.stdout.write('Hex : ' + s2s3Out + '\n')
    sys.stdout.write('Bin : ' + bitwise_s2s3 + '\n')    
    sys.stdout.write('\n--------------------------Bitwise XOR Onion2 and Onion 4----------------------------\n')
    sys.stdout.write('Hex : ' + s2s4Out + '\n')
    sys.stdout.write('Bin : ' + bitwise_s2s4 + '\n')    
    sys.stdout.write('\n--------------------------Bitwise XOR Onion3 and Onion 4----------------------------\n')
    sys.stdout.write('Hex : ' + s3s4Out + '\n')
    sys.stdout.write('Bin : ' + bitwise_s3s4 + '\n')  
    crib_drag()

def crib_drag():
    f = open(sys.argv[1], 'r')
    for line in f:
        sys.stdout.write('\n' + line + '\n')
        crib = ''.join(hex(ord(x))[2:] for x in line)
        crib = ConvertToBinary(crib)
        string = 'E35C1F6ECFE43756D34C7D7A7400C1FA98586BFAF9C713120D378C28B32B722DCC4995BA165766CA9C1E55ADF52EA18EFA23B7F55512E94096D0D96F96E034182556BB9E9587EBB91DD12FC920ECB2A7780569907FA87DC1A1237BDA57D3430A398E48FD761A910252AB6F231957D0F8BD61360BA6025C7E6E0930A98C183792EA97F3D70FC39F9C716977AD3C7C6C656F7CC76A0D66BA2C2E20B4098E11B9720EECB6B233D6D600B6B670A173359D0A9F48F7E972213C5B7D13866AD14050763042629D0551D6E2C1C71F5CA1939AD8ADDD46CB925CFE381F182D6F6EA0175819B1BE323E287416E4F473849DBEFBE62B39DBA40F65D1ECE3CF1F718C7BA2C4'
        string = ConvertToBinary(string)
        n = string
        while len(n) >= len(crib):
            xor = bitwiseXOR(crib, n)
            sys.stdout.write(str(len(n)) + ':' + ConvertToAscii(xor) + '\n')
            n= n[1:]

    
main()