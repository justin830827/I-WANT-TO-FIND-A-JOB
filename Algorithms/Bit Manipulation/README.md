# Bit Manipulation

Operations with bits are used in Data compression (data is compressed by converting it from one representation to another, to reduce the space) ,Exclusive-Or Encryption (an algorithm to encrypt the data for safety issues). In order to encode, decode or compress files we have to extract the data at bit level. Bitwise Operations are faster and closer to the system and sometimes optimize the program to a good level.

## Concepts

There are different bitwise operations used in the bit manipulation. These bit operations operate on the individual bits of the bit patterns. Bit operations are fast and can be used in optimizing time complexity. Some common bit operators are:

- NOT ( ~ ): Bitwise NOT is an unary operator that flips the bits of the number i.e., if the ith bit is 0, it will change it to 1 and vice versa. Bitwise NOT is nothing but simply the one’s complement of a number. Lets take an example.
```
N = 5 = (101)2
~N = ~5 = ~(101)2 = (010)2 = 2
```

- AND ( & ): Bitwise AND is a binary operator that operates on two equal-length bit patterns. If both bits in the compared position of the bit patterns are 1, the bit in the resulting bit pattern is 1, otherwise 0.
```
A = 5 = (101)2 , B = 3 = (011)2 A & B = (101)2 & (011)2= (001)2 = 1
```

- OR ( | ): Bitwise OR is also a binary operator that operates on two equal-length bit patterns, similar to bitwise AND. If both bits in the compared position of the bit patterns are 0, the bit in the resulting bit pattern is 0, otherwise 1.
```
A = 5 = (101)2 , B = 3 = (011)2
A | B = (101)2 | (011)2 = (111)2 = 7
```

- XOR ( ^ ): Bitwise XOR also takes two equal-length bit patterns. If both bits in the compared position of the bit patterns are 0 or 1, the bit in the resulting bit pattern is 0, otherwise 1.
```
A = 5 = (101)2 , B = 3 = (011)2
A ^ B = (101)2 ^ (011)2 = (110)2 = 6
```

- Left Shift ( << ): Left shift operator is a binary operator which shift the some number of bits, in the given bit pattern, to the left and append 0 at the end. Left shift is equivalent to multiplying the bit pattern with ( if we are shifting k bits ).
```
1 << 1 = 2 = 21
1 << 2 = 4 = 22 1 << 3 = 8 = 23
1 << 4 = 16 = 24
…
1 << n = 2n
```

- Right Shift ( >> ): Right shift operator is a binary operator which shift the some number of bits, in the given bit pattern, to the right and append 1 at the end. Right shift is equivalent to dividing the bit pattern with 2k ( if we are shifting k bits ).
```
4 >> 1 = 2
6 >> 1 = 3
5 >> 1 = 2
16 >> 4 = 1
```

Reference: [HackEarth](https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/tutorial/)
## Leetcode Problems

Clone the problem list [here](https://leetcode.com/list/x39dpzdr)

|  #  | Problem                                                                                     | Difficulty |                                         Solution                                          | Follow-up | Freq. |
| :-: | :------------------------------------------------------------------------------------------ | :--------: | :---------------------------------------------------------------------------------------: | :-------- | :---: |
| 201 | [Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/) |  `Medium`  | [Python](./python/bitwise_and_number_range.py), [Java](./java/BitwiseANDNumberRange.java) |           | `Low` |
