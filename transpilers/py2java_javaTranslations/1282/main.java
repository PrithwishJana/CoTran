public void memo ( index , evenSum , oddSum , tight ) {
    if (var index == len ( v )) {
        if (evenSum > oddSum) {
            return 1;
        }
         else{
            return 0;
        }
    }
     if (dp { index } { evenSum } { oddSum } { tight } != - 1) {
        return dp { index } { evenSum } { oddSum } { tight };
    }
     var limit = v { index } if tight else 9;
    var ans = 0;
    for d in range ( limit + 1 ) :
        var currTight = 0;
        if (d == v { index }) {
            currTight = tight;
        }
         if (d % 2 != 0) {
            ans += memo ( index + 1 , evenSum , oddSum + d , currTight );
        }
         else{
            ans += memo ( index + 1 , evenSum + d , oddSum , currTight );
        }
    dp { index } { evenSum } { oddSum } { tight } = ans;
    return ans;
}
public void countNum ( n ) {
    global dp , v;
    v . clear ( );
    var num = {};
    while (n) {
        v . append ( n % 10 );
        n //= 10;
    }
     v . reverse ( );
    var dp = { [ [ [ - 1 , - 1 } for i in range ( 180 ) ] for j in range ( 180 ) ] for k in range ( 18 ) ];
    return memo ( 0 , 0 , 0 , 1 );
}
if (__name__ == "__main__") {
    dp = {};
    var v = {};
    var L = 2;
    var R = 10;
    System.out.println ( countNum ( R ) - countNum ( L - 1 ) );
}
 