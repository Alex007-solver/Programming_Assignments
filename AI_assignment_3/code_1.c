#include <stdio.h>
#include <math.h>
#include <string.h>
#include <limits.h>

#define M_PI 3.14159265358979323846
struct City {
    char name[50];
    double lat;
    double lon;
};

struct City cities[162];


double distance(int a,int b)
{
    double lat1 = cities[a].lat * M_PI / 180;
    double lon1 = cities[a].lon * M_PI / 180;

    double lat2 = cities[b].lat * M_PI / 180;
    double lon2 = cities[b].lon * M_PI / 180;

    double dlat = lat2 - lat1;
    double dlon = lon2 - lon1;

    double R = 6371;

    double x = pow(sin(dlat/2),2) +
               cos(lat1)*cos(lat2)*pow(sin(dlon/2),2);

    double c = 2 * atan2(sqrt(x),sqrt(1-x));

    return R*c;
}
void printPath(int parent[], int j)
{
    if(parent[j]==-1)
        return;

    printPath(parent,parent[j]);
    printf(" -> %s",cities[j].name);



}
int main(){

    char start[50], goal[50];

printf("Enter start city: ");
scanf("%s",start);

printf("Enter goal city: ");
scanf("%s",goal);
FILE *fp;
fp = fopen("city.csv","r");

if(fp == NULL){
    printf("Error opening file\n");
    return 0;
}

char header[200];
fgets(header,200,fp);   // skip header line

int i = 0;

while(fscanf(fp,"%[^,],%lf,%lf",
             cities[i].name,
             &cities[i].lat,
             &cities[i].lon) == 3)
{
    i++;

    // skip remaining columns
    char temp[200];
    fgets(temp,200,fp);
}

int startIndex=-1, goalIndex=-1;

for(int j=0;j<i;j++)
{
    if(strcmp(cities[j].name,start)==0)
        startIndex=j;

    if(strcmp(cities[j].name,goal)==0)
        goalIndex=j;
}
double dist[162];
int visited[162]={0};
int parent[162];

for(int j=0;j<i;j++)
{
    dist[j]=1e9;
    parent[j]=-1;
}

dist[startIndex]=0;
if(startIndex==-1 || goalIndex==-1)
{
    printf("City not found\n");
    return 0;
}

for(int count=0; count<i-1; count++)
{
    double min=1e9;
    int u=-1;

    for(int v=0; v<i; v++)
    {
        if(!visited[v] && dist[v] < min)
        {
            min = dist[v];
            u = v;
        }
    }

    visited[u]=1;

    for(int v=0; v<i; v++)
    {
        if(!visited[v])
        {
            double w = distance(u,v);

            if(dist[u] + w < dist[v])
            {
                dist[v] = dist[u] + w;
                parent[v] = u;
            }
        }
    }
}
printf("Shortest path:\n");

printf("%s",cities[startIndex].name);

printPath(parent,goalIndex);

printf("\nDistance: %.2f km\n",dist[goalIndex]);

}