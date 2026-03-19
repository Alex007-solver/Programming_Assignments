#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define N 70

typedef struct {
    int x, y;
    int g, h, f;
    int parent_x, parent_y;
} Node;

int grid[N][N];
int closed[N][N];

Node openList[N*N];
int openCount = 0;

int heuristic(int x1, int y1, int x2, int y2) {
    return abs(x1 - x2) + abs(y1 - y2);
}

void addToOpen(Node n) {
    openList[openCount++] = n;
}

int getBestNode() {
    int best = 0;
    for (int i = 1; i < openCount; i++) {
        if (openList[i].f < openList[best].f)
            best = i;
    }
    return best;
}

void removeNode(int index) {
    openList[index] = openList[--openCount];
}

void generateGrid(int density) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (rand() % 100 < density)
                grid[i][j] = 1;
            else
                grid[i][j] = 0;
            closed[i][j] = 0;
        }
    }
}

void printPath(int parent[N][N][2], int sx, int sy, int gx, int gy) {
    int x = gx, y = gy;
    int path[N][N] = {0};

    while (!(x == sx && y == sy)) {
        path[x][y] = 1;
        int px = parent[x][y][0];
        int py = parent[x][y][1];
        x = px;
        y = py;
    }

    path[sx][sy] = 1;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (grid[i][j] == 1)
                printf("# ");
            else if (path[i][j])
                printf("* ");
            else
                printf(". ");
        }
        printf("\n");
    }
}

void Astar(int sx, int sy, int gx, int gy) {

    int parent[N][N][2];
    int nodesExpanded = 0;

    Node start = {sx, sy, 0, heuristic(sx, sy, gx, gy), 0, -1, -1};
    start.f = start.g + start.h;

    addToOpen(start);

    clock_t startTime = clock();

    while (openCount > 0) {

        int bestIndex = getBestNode();
        Node current = openList[bestIndex];
        removeNode(bestIndex);

        int x = current.x;
        int y = current.y;

        if (closed[x][y])
            continue;

        closed[x][y] = 1;
        nodesExpanded++;

        parent[x][y][0] = current.parent_x;
        parent[x][y][1] = current.parent_y;

        if (x == gx && y == gy) {
            clock_t endTime = clock();

            printf("\n✅ Path Found!\n");
            printf("Path Length: %d\n", current.g);
            printf("Nodes Expanded: %d\n", nodesExpanded);
            printf("Time: %lf sec\n",
                   (double)(endTime - startTime) / CLOCKS_PER_SEC);

            printPath(parent, sx, sy, gx, gy);
            return;
        }

        int dx[] = {-1, 1, 0, 0};
        int dy[] = {0, 0, -1, 1};

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && ny >= 0 && nx < N && ny < N &&
                grid[nx][ny] == 0 && !closed[nx][ny]) {

                Node neighbor;
                neighbor.x = nx;
                neighbor.y = ny;
                neighbor.g = current.g + 1;
                neighbor.h = heuristic(nx, ny, gx, gy);
                neighbor.f = neighbor.g + neighbor.h;
                neighbor.parent_x = x;
                neighbor.parent_y = y;

                addToOpen(neighbor);
            }
        }
    }

    printf("\n❌ No Path Found\n");
}

int main() {
    srand(time(NULL));

    int sx = 0, sy = 0;
    int gx = 69, gy = 69;

    int density;

    printf("Enter obstacle density (10 low, 30 medium, 50 high): ");
    scanf("%d", &density);

    generateGrid(density);

    grid[sx][sy] = 0;
    grid[gx][gy] = 0;

    Astar(sx, sy, gx, gy);

    return 0;
}
