# Problem link    : https://atcoder.jp/contests/abc362/tasks/abc362_a
# Submission link : https://atcoder.jp/contests/abc362/submissions/55587917

# input
read -r prices
read -r color
# Convert to list
price_lis=($prices)
# Determine the answer based on the color
if [ "$color" == "Red" ]; then
    ans=${price_lis[1]}
    if [ ${price_lis[2]} -lt $ans ]; then
        ans=${price_lis[2]}
    fi
elif [ "$color" == "Green" ]; then
    ans=${price_lis[0]}
    if [ ${price_lis[2]} -lt $ans ]; then
        ans=${price_lis[2]}
    fi
else
    ans=${price_lis[0]}
    if [ ${price_lis[1]} -lt $ans ]; then
        ans=${price_lis[1]}
    fi
fi

# Print the result
echo $ans
