#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define N 20   

typedef struct {
    int x, y;
    int g, h, f;
    int parent_x, parent_y;
} Node;

int grid[N][N];
int closed[N][N];

Node openList[N*N];
int openCount;

int heuristic(int x1, int y1, int x2, int y2) {
    return abs(x1 - x2) + abs(y1 - y2);
}

void resetSearch() {
    openCount = 0;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            closed[i][j] = 0;
}

void addToOpen(Node n) {
    openList[openCount++] = n;
}

int getBestNode() {
    int best = 0;
    for (int i = 1; i < openCount; i++)
        if (openList[i].f < openList[best].f)
            best = i;
    return best;
}

void removeNode(int idx) {
    openList[idx] = openList[--openCount];
}

void generateGrid(int density) {
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            grid[i][j] = (rand() % 100 < density) ? 1 : 0;
}

int AstarStep(int sx, int sy, int gx, int gy, int *nx, int *ny) {

    resetSearch();

    int parent[N][N][2];

    Node start = {sx, sy, 0, heuristic(sx, sy, gx, gy), 0, -1, -1};
    start.f = start.g + start.h;

    addToOpen(start);

    while (openCount > 0) {

        int idx = getBestNode();
        Node cur = openList[idx];
        removeNode(idx);

        int x = cur.x, y = cur.y;

        if (closed[x][y]) continue;
        closed[x][y] = 1;

        parent[x][y][0] = cur.parent_x;
        parent[x][y][1] = cur.parent_y;

        if (x == gx && y == gy) {

            int tx = gx, ty = gy;

            while (!(parent[tx][ty][0] == sx && parent[tx][ty][1] == sy)) {
                int px = parent[tx][ty][0];
                int py = parent[tx][ty][1];
                tx = px;
                ty = py;
            }

            *nx = tx;
            *ny = ty;
            return 1;
        }

        int dx[] = {-1,1,0,0};
        int dy[] = {0,0,-1,1};

        for (int i = 0; i < 4; i++) {
            int xx = x + dx[i];
            int yy = y + dy[i];

            if (xx >= 0 && yy >= 0 && xx < N && yy < N &&
                grid[xx][yy] == 0 && !closed[xx][yy]) {

                Node n;
                n.x = xx;
                n.y = yy;
                n.g = cur.g + 1;
                n.h = heuristic(xx, yy, gx, gy);
                n.f = n.g + n.h;
                n.parent_x = x;
                n.parent_y = y;

                addToOpen(n);
            }
        }
    }

    return 0; 
}

void printGrid(int cx, int cy, int gx, int gy) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {

            if (i == cx && j == cy)
                printf("U "); // UGV
            else if (i == gx && j == gy)
                printf("G ");
            else if (grid[i][j] == 1)
                printf("# ");
            else
                printf(". ");
        }
        printf("\n");
    }
    printf("\n");
}

void dynamicUGV(int sx, int sy, int gx, int gy) {

    int cx = sx, cy = sy;
    int steps = 0, replans = 0;

    clock_t start = clock();

    while (!(cx == gx && cy == gy)) {

        printGrid(cx, cy, gx, gy);

        if (rand() % 100 < 20) {
            int ox = rand() % N;
            int oy = rand() % N;

            if ((ox != cx || oy != cy) && (ox != gx || oy != gy)) {
                grid[ox][oy] = 1;
                printf("⚠ New obstacle at (%d,%d)\n", ox, oy);
            }
        }

        int nx, ny;

        if (!AstarStep(cx, cy, gx, gy, &nx, &ny)) {
            printf("❌ No Path Available!\n");
            return;
        }

        replans++;

        cx = nx;
        cy = ny;
        steps++;
    }

    clock_t end = clock();

    printf("\n✅ Goal Reached!\n");
    printf("Steps (Path Length): %d\n", steps);
    printf("Replans: %d\n", replans);
    printf("Time: %lf sec\n",
           (double)(end - start) / CLOCKS_PER_SEC);
}

int main() {

    srand(time(NULL));

    int sx = 0, sy = 0;
    int gx = N-1, gy = N-1;

    int density;
    printf("Enter obstacle density (10 low, 30 medium, 50 high): ");
    scanf("%d", &density);

    generateGrid(density);

    grid[sx][sy] = 0;
    grid[gx][gy] = 0;

    dynamicUGV(sx, sy, gx, gy);

    return 0;
}
