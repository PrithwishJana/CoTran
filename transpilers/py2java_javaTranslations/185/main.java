public void wastedWater ( V , M , N ) {
    var amt_per_min = M - N;
    var time_to_fill = V / amt_per_min;
    var wasted_amt = N * time_to_fill;
    return wasted_amt;
}
var V = 700;
M = 10;
N = 3;
System.out.println ( wastedWater ( V , M , N ) );
V = 1000;
var M = 100;
var N = 50;
System.out.println ( wastedWater ( V , M , N ) );
