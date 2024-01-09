#include <stdio.h>

typedef struct pairs {
    char *key;
    char *value;
} pairs;

pairs e2c[] = {{"a","一"}, {"dog","狗"}};

int main() {
    printf("%s:%s\n", e2c[0].key, e2c[0].value);
}