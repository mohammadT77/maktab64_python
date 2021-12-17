function singleDigitRecursive(n) {
    n = String(n)
    sum = 0
    for (let i of n) {
        sum += Number(i)
    }
    return sum < 10? sum:singleDigitRecursive(sum)
}

function singleDigit(n) {
    while (Number(n) >= 10) {
        n = String(n)
        sum = 0
        for (let i of n) {
            sum += Number(i)
        }
        n = sum
    }
    return n
}


