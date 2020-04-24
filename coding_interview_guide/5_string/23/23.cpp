#include <iostream>
#include <cstring>
using namespace std;

struct TrieNode {
    int end;
    int path;
    TrieNode *map[26];
};

class Trie {
public:
    Trie() {
        root = alloc_node();
    }

    TrieNode* alloc_node() {
        TrieNode *node = (TrieNode *) malloc(sizeof(TrieNode));
        for (int i = 0; i < 26; i++) {
            node->map[i] = nullptr;
        }
        node->end = 0;
        node->path = 0;
        return node;
    }

    void insert(char *s) {
        if (s == nullptr) {
            return;
        }
        TrieNode *node = root;
        for (unsigned int i = 0; i < strlen(s); i++) {
            int index = s[i] - 'a';
            if (node->map[index] == nullptr) {
                node->map[index] = alloc_node();
            }

            node = node->map[index];
            node->path++;
        }
        node->end += 1;
    }

    void del(char *s) {
        if (s == nullptr) {
            return;
        }

        TrieNode *node = root;
        for (unsigned int i = 0; i < strlen(s); i++) {
            int index = s[i] - 'a';
            if (node->map[index] == nullptr) {
                return;
            }

            node = node->map[index];
            node->path--;
        }
        if (node->end != 0) {
            node->end -= 1;
        }
    }

    bool search(char *s) {
        if (s == nullptr) {
            return false;
        }

        TrieNode *node = root;
        for (unsigned int i = 0; i < strlen(s); i++) {
            int index = s[i] - 'a';
            if (node->map[index] == nullptr) {
                return false;
            }
            node = node->map[index];
        }
        return node->end != 0;
    }

    int prefix(char *s) {
        if (s == nullptr) {
            return 0;
        }

        TrieNode *node = root;
        for (unsigned int i = 0; i < strlen(s); i++) {
            int index = s[i] - 'a';
            if (node->map[index] == nullptr) {
                return 0;
            }
            node = node->map[index];
        }
        return node->path;
    }
private:
    TrieNode *root;
};


int main()
{
    Trie trie;
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        int op;
        char word[21];
        scanf("%d %s", &op, word);
        if (op == 1) {
            trie.insert(word);
        }
        else if (op == 2) {
            trie.del(word);
        }
        else if (op == 3) {
            if (trie.search(word)) {
                printf("YES\n");
            }
            else {
                printf("NO\n");
            }
        }
        else if (op == 4) {
            printf("%d\n", trie.prefix(word));
        }
    }
    return 0;
}
