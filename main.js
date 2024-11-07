// Find inversion count in array algorithm
function countInversions(arr) {
    let invCount = 0;
    for (let i = 0; i < arr.length - 1; i++) {
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[i] > arr[j]) {
                invCount++;
            }
        }
    }
    return invCount;
}

const arr = [2, 4, 1, 3, 5];
console.log("Inversiyalar soni: " + countInversions(arr));
