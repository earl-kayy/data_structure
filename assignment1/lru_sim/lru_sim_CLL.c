#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    char page[1024]; 
    struct Node *next;
} Node;

typedef struct {
    Node *tail;//
    int size;
} CircularLinkedList;

typedef struct {
    int cache_slots;
    int cache_hit;
    int tot_cnt;
    CircularLinkedList *cache;
} CacheSimulator;

CircularLinkedList *createCircularLinkedList() {
    CircularLinkedList *list = (CircularLinkedList *)malloc(sizeof(CircularLinkedList));
    Node *dummy = (Node *)malloc(sizeof(Node));
    strcpy(dummy->page, "");
    dummy->next = dummy;
    list->tail = dummy;
    list->size = 0;
    return list;
}

void insertAtHead(CircularLinkedList *list, const char *page);
void removeNode(CircularLinkedList *list, const char *page);
int isInList(CircularLinkedList *list, const char *page);
void popTail(CircularLinkedList *list);
int listSize(CircularLinkedList *list);

CacheSimulator *createCacheSimulator(int cache_slots) {
    CacheSimulator *sim = (CacheSimulator *)malloc(sizeof(CacheSimulator));
    sim->cache_slots = cache_slots;
    sim->cache_hit = 0;
    sim->tot_cnt = 0;
    sim->cache = createCircularLinkedList();
    return sim;
}

void do_sim(CacheSimulator *sim, const char *page) {
    sim->tot_cnt++;
    if (isInList(sim->cache, page)) {
        sim->cache_hit++;
        removeNode(sim->cache, page);
        insertAtHead(sim->cache, page);
    } else {
        if (listSize(sim->cache) < sim->cache_slots) {
            insertAtHead(sim->cache, page);
        } else {
            popTail(sim->cache);
            insertAtHead(sim->cache, page);
        }
    }
}

void print_stats(CacheSimulator *sim) {
    printf("Cache Slots: %d, Cache Hits: %d, Hit Ratio: %.5f\n",
           sim->cache_slots, sim->cache_hit, (float)sim->cache_hit / sim->tot_cnt);
}

int main() {
    FILE *data_file = fopen("./linkbench.trc", "r");
    char line[1024];
    int cache_slots;

    for (cache_slots = 100; cache_slots <= 1000; cache_slots += 100) {
        CacheSimulator *cache_sim = createCacheSimulator(cache_slots);
        
        while (fgets(line, sizeof(line), data_file)) {
            char *page = strtok(line, " \n");
            do_sim(cache_sim, page);
        }
        
        print_stats(cache_sim);
        fseek(data_file, 0, SEEK_SET); 
    }

    fclose(data_file);
    return 0;
}
#include <stdbool.h>

// 원형 연결 리스트의 헤드에 노드를 삽입
void insertAtHead(CircularLinkedList *list, const char *page) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    strcpy(newNode->page, page);
    newNode->next = list->tail->next->next;
    list->tail->next->next = newNode;
    list->size++;
}

// 원형 연결 리스트에서 특정 페이지를 가진 노드 제거
void removeNode(CircularLinkedList *list, const char *page) {
    if (list->size == 0) return; // 비어 있는 리스트면 아무것도 하지 않음

    Node *current = list->tail->next; // 더미 노드
    do {
        // 다음 노드가 찾고자 하는 페이지를 가지고 있는지 확인
        if (strcmp(current->next->page, page) == 0) {
            Node *toDelete = current->next;
            // 삭제하려는 노드가 마지막 노드인 경우 tail을 업데이트
            if (toDelete == list->tail) {
                list->tail = (list->size == 1) ? list->tail->next : current;
            }
            // 삭제 로직
            current->next = toDelete->next;
            free(toDelete);
            list->size--;
            
            // 리스트에 노드가 하나도 없게 되면 tail을 더미 노드로 설정
            if (list->size == 0) {
                list->tail->next = list->tail;
            }
            return;
        }
        current = current->next;
    } while (current != list->tail->next); // 더미 노드로 돌아올 때까지 반복
}

// 특정 페이지를 가진 노드가 리스트에 있는지 확인
int isInList(CircularLinkedList *list, const char *page) {
    if (list->size == 0) return 0;

    Node *current = list->tail->next->next; // 더미 노드의 다음 노드부터 시작
    do {
        if (strcmp(current->page, page) == 0) {
            return 1; // 찾았다면 1 반환
        }
        current = current->next;
    } while (current != list->tail->next->next); // 더미 노드의 다음 노드로 다시 돌아올 때까지 반복
    return 0; // 못 찾았다면 0 반환
}


// 원형 연결 리스트의 마지막 노드를 제거
void popTail(CircularLinkedList *list) {
    if (list->size == 0) return; // 리스트에 데이터 노드가 없는 경우

    if (list->size == 1) {
        // 데이터 노드가 하나뿐인 경우
        free(list->tail->next->next); // 첫 번째 실제 데이터 노드(더미 노드의 다음 노드) 삭제
        list->tail->next->next = list->tail->next; // 더미 노드의 next를 자기 자신으로 설정
    } else {
        // 데이터 노드가 두 개 이상인 경우
        Node *current = list->tail->next;
        while (current->next != list->tail) {
            current = current->next;
        }
        // current는 이제 tail 바로 이전의 노드
        current->next = list->tail->next; // tail의 다음 노드(더미 노드)를 가리킵니다.
        free(list->tail); // 마지막 실제 데이터 노드 삭제
        list->tail = current; // 새로운 tail 업데이트
    }
    list->size--;
}

// 원형 연결 리스트의 크기를 반환
int listSize(CircularLinkedList *list) {
    return list->size;
}
