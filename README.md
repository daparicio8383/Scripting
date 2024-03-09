# Scripting

Web application pentesting tools.

## Encoding

- [upperBypass.py](../blob/main/upperBypass.py): tool that automates the encoding of characters as HTML, Unicode and URL entities for Uppercase filter evasion.

### Usage

You will be asked about the different encodings that you want to apply to the payload entered. 

In cases where you choose NOT to encode the special characters as URL, the space will be written as '+'. This is for HTTP POST requests of the type application/x-www-form-urlencoded.

```
python upperBypass.py
```

![alt text](https://github.com/daparicio8383/Scripting/blob/main/Images/upperBypass1.png "space encoded as '+'")
![alt text](https://github.com/daparicio8383/Scripting/blob/main/Images/upperBypass2.png "space encoded as '%3D'")
