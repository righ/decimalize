**`decimalize`** is a package to convert radix flexibly.

Requirements
============
* Python 2.5 or later.

Install
=======
```sh
$ pip install decimalize
```

History
=======
1.0.x
-----
- First release.

Usage
=====

Basic Example
-------------

```python
>>> import decimalize
>>> manager = decimalize.Decimalize('0123456789abcdef')
>>> manager.encode(255)
'ff'
>>> manager.decode('ffff')
65535
```

Multi Byte Example
------------------
Please specify a unicode-string if you use multibyte charset.

```python
>>> import decimalize
>>> manager = decimalize.Decimalize(
...    u'あいうえおかきくけこさしすせそたちつてとなにぬねの'
...    u'はひふへほまみむめもやゆよらりるれろわをん'
... )  # 46進数
>>> print(manager.encode(500))
さる
>>> manager.decode(u'いぬ')
68
>>> # print(manager.encode(7308313824848881))
>>> # print(manager.encode(2811963241313541391200))
```
