fun main() {
    // 文字列を1つ入力
    val S = readLine()!!

    // 整数を1つ入力
    val a = readLine()!!.toInt()

    // 小数を1つ入力
    val af = readLine()!!.toDouble()

    // 整数を2つ入力
    val (b, c) = readLine()!!.split(" ").map { it.toInt() }

    // 整数をリスト形式で入力
    val num_list = readLine()!!.split(" ").map { it.toInt() }

    // 出力
    println(S)
}