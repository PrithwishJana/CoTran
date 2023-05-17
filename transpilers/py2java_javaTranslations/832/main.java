var target = input ( );
var list_abc = { "A" , "B" , "C" };
var old = {};
new = {};
check = {};
flag = false;
if ("ABC" in target) {
    old . append ( { target , [ } ] );
}
 while (old != {} and flag == false) {
    for (int i = 0; i < old.length; i++){
        if (i { 0 } == "ABC") {
            check . append ( i { 1 } );
            flag = true;
            break;
        }
         for (int j = 0; j < list_abc.length; j++){
            element = i { 0 } . replace ( "ABC" , j );
            if ("ABC" in element) {
                new . append ( { element , i [ 1 } + { j } ] );
            }
         }
    }
     else{
        old = new { : };
        var new = {};
    }
}
 var flag = false;
for (int i = 0; i < check.length; i++){
    abc = "ABC";
    li = i;
    li . reverse ( );
    for (int j = 0; j < li.length; j++){
        abc = abc . replace ( j , "ABC" );
    }
    if (abc == target) {
        flag = true;
    }
}
 System.out.println ( "Yes" if flag == true else "No" );
