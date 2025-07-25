# Scripting

Pentesting tools.

## Encoding

[upperBypass.py](../main/upperBypass.py): tool that automates the encoding of characters as HTML, Unicode and URL entities for Uppercase filter evasion.

### Usage

You will be asked about the different encodings that you want to apply to the payload entered. 

In cases where you choose NOT to encode the special characters as URL, the space will be written as '+'. This is for HTTP POST requests of the type application/x-www-form-urlencoded.

```
python upperBypass.py
```

###### Space encoded as '+'

![alt text](https://github.com/daparicio8383/Scripting/blob/main/Images/upperBypass1.png "space encoded as '+'")


###### Space encoded as '%3D'

![alt text](https://github.com/daparicio8383/Scripting/blob/main/Images/upperBypass2.png "space encoded as '%3D'")

---

[HexToASCII_4byte.py](../main/HexToASCII_4byte.py): tool that takes a 4 byte Hexadecimal value, asks you if you want to rearrange bytes in order to change its endianess, and convert the resultant value into ASCII. To perform this conversion, a Bitwise NOT operator will be used. The tool was thought to replicate the deobfuscation function of an APK, which used this operator.

### How Bitwise NOT works

Bitwise NOT will invert any value you provide, bit by bit. It uses the **tilde symbol (~)**.

Consider you find this function:
```
bbb(~Var1[i]);
``` 

```
Var1[i] = 0x93; Var1[i] = 10010011
~Var1[i] = 01101100; ~Var1[i] = 0x6c
```

###### Usage with two 4 byte values provided, changing endianess.

![alt text](https://github.com/daparicio8383/Scripting/blob/main/Images/HexToASCII_Ghidra.png "Two 4 byte values provided, changing endianess")


---

## Brute force

[jwt-secret-comparer.py](../main/jwt-secret-comparer.py): tool that compares a JWT token with others generated from signatures with different secrets, obtained by using lists. Currently only the **HS256** signature algorithm is supported, although this will be updated.

### Usage

The first step is to import the *tqdm* module.

The file will then be edited to enter the path to the directory where the wordlists are stored.

Finally, when running jwt-secret-comparer, you will be prompted for the JWT token from which you want to extract the secret.

```
python jwt-secret-comparer.py
```

###### Editing the path

![alt text](https://github.com/daparicio8383/Scripting/blob/main/Images/jwt-secret-comparer1.png "Editing the path")

###### Usage

![alt text](https://github.com/daparicio8383/Scripting/blob/main/Images/jwt-secret-comparer2.png "Usage")

