
number conversion library

## Usage
>>> import decimalize
>>> dec = decimalize.Decimalize('0123456789abcdef')
>>> dec.encode(255)
'ff'
>>> dec.decode('ff')
255


