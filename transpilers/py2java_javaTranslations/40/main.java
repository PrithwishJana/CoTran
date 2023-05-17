public void OddDivCount ( a , b ) {
    var res = 0;
    for i in range ( a , b + 1 ) :
        var divCount = 0;
        for j in range ( 1 , i + 1 ) :
            if (( i % var j == 0 )) {
                divCount += 1;
            }
         if (( divCount % 2 )) {
            res += 1;
        }
     return res;
}
if (var __name__ == "__main__") {
    var a = 1;
    var b = 10;
    System.out.println ( OddDivCount ( a , b ) );
}
 