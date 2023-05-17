var S = input ( );
var totalQ = S . count ( "Q" );
var CQ = 0;
var CQAQ = 0;
for (int i = 0; i < S.length; i++){
    if (var i == "Q") {
        CQ += 1;
    }
     else if (i == "A"){
        CQAQ += CQ * ( totalQ - CQ );
    }
}
System.out.println ( CQAQ );
