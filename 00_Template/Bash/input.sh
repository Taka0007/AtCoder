#!/bin/bash

# 文字列を1つ入力
read S

# 整数を1つ入力
read a

# 小数を1つ入力
read af

# 整数を2つ入力
read b c

# 整数リストを1行で入力
read -a num_list

# 出力確認
echo "$S"
echo "$a"
echo "$af"
echo "$b $c"
echo "${num_list[@]}"
