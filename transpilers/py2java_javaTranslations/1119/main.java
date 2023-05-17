public void getOddOccurrence ( arr ) {
    var res = 0;
    for (int element = 0; element < arr.length; element++){
        res = res ^ element;
    }
    return res;
}
var arr = { 2 , 3 , 5 , 4 , 5 , 2 , 4 , 3 , 5 , 2 , 4 , 4 , 2 };
System.out.println ( "%d" % getOddOccurrence ( arr ) );
