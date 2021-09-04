#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(const char* s) {
    
    // 문자열 길이 strlen() 함수 사용
    bool answer = true;
    
    if(strlen(s) != 4 && strlen(s) != 6) {
        return false;
    }
    
    // 숫자 여부 판단 isdigit()함수 사용
    for (int i=0; i<strlen(s); i++) {
        if(isdigit(s[i]) == false)
           return false;           
    }
    return answer;
}