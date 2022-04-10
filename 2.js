//1到100的质数之和

var sum = 0;
for (var i = 2; i <= 100; i++) {
    var isPrime = true;
    for (var j = 2; j < i; j++) {
        if (i % j == 0) {
            isPrime = false;
            break;
        }
    }
    if (isPrime) {
        sum += i;
    }
}   console.log(sum);
1.
var sum = 0;
for (var i = 2; i <= 100; i++) {
    var isPrime = true;
    for (var j = 2; j < i; j++) {
        if (i % j == 0) {
            isPrime = false;
            break;
        }
    }
    if (isPrime) {
        sum += i;
    }
}
false
var sum = 0;
for (var i = 2; i <= 100; i++) {
    var isPrime = true;
    for (var j = 2; j < i; j++) {
        if (i % j == 0) {
            isPrime = false;
            break;
        }
    }
    if (isPrime) {
        sum += i;
    }
}