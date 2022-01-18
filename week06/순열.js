const arr = [1, 2, 3, 4]
const ans = []; // 순열이 저장될 배열
//
// isUsed[i] = i번째 요소를 사용중이라면 true.
const isUsed = [false, false, false, false];
for(let i=0; i<arr.length; i++){
    if(isUsed[i] === true) continue;
    isUsed[i] = true;

    for(let j=0; j<arr.length; j++){
        if(isUsed[j] === true) continue;
        isUsed[j] = true;

        for(let k=0; k<arr.length; k++) {
            if(isUsed[k] === true) continue;
            isUsed[k] = true;

            const current = [ arr[i], arr[j], arr[k] ];
            ans.push(current);
            isUsed[k] = false;
        }
        isUsed[j] = false;
    }
    isUsed[i] = false;
}