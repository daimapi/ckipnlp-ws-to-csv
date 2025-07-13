# ckipnlp ws to csv

[![python](https://img.shields.io/badge/Python-3.12-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![tensorflow](https://img.shields.io/badge/TensorFlow-1.12-FF6F00.svg?style=flat&logo=tensorflow)](https://www.tensorflow.org)
[![License: GPLv3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## how to use
### local data requirements
- `tar.txt`for words that need to be count
```txt
word1
word2
word3
...
```
- `/src` for files that are going to be progressed(available: .txt )
```txt
时代少年团《lemon》中文版歌词.txt
AiScReam Official Lyric.txt
...
```
### output
- data will be output to `output_data.csv`.This file will be generated otherwise rewrote if already exist.
- example:

  | 0   | 时代少年团《lemon》中文版歌词.txt | AiScReam Official Lyric.txt | ... |
    |:----|:---------------------:|:---------------------------:|:---:|
  | 的   |          11           |              0              | ... |
  | one |           0           |              4              | ... |
  | ... |          ...          |             ...             | ... |
- delimiter using : ","

### codec
- UTF-8