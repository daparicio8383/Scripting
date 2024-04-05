# Scripting

Web application pentesting tools.

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

