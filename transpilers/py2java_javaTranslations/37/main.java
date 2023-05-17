var N = 3;
public void MaxTraceSub ( mat ) {
    var max_trace = 0;
    for i in range ( N ) :
        for j in range ( N ) :
            r = i;
            s = j;
            trace = 0;
            while (( r < N and s < N )) {
                trace += mat { r } { s };
                r += 1;
                s += 1;
                max_trace = max ( trace , max_trace );
            }
     return max_trace;
}
if (var __name__ == '__main__') {
    var mat = { [ 10 , 2 , 5 } , { 6 , 10 , 4 } , { 2 , 7 , -10 } ];
    System.out.println ( MaxTraceSub ( mat ) );
}
 