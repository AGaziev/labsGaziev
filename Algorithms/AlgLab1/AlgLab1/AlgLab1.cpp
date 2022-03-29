#include <iostream>
#include <vector>
#include <queue>
#include <stack>

using namespace std;

struct Edge {
	int beginNode;
	int endNode;
};

struct Node {
	int number;
	int status=0;
	vector<int> conWith;
};

int main()
{

	int start = 0;//вершина от которой ищем пути
	int N;//количество вершин
	
	cout << "From which node number set routes:"; cin >> start;
	cout << "Amount of Nodes:"; cin >> N; cout << "\nFor each node write their connection(0 to next):\n";

	vector<vector<bool>> graphMatrix(N, vector<bool>(N));//матрица смежности
	vector<vector<int>> components(1);//Массив компонент связности
	stack<Edge> edges;//стэк ребер
	vector<Node> nodes(N);//массив вершин

	//инициализация графа
	for (int i = 0; i < N; i++) {
		int t;
		nodes[i].number = i+1;
		vector<bool> temp(N, 0);
		cout << i + 1 << ": ";
		do
		{
			cin >> t;
			if (t == 0)
				break;
			//Создание связей
			nodes[i].conWith.push_back(t);
			//
			temp[t-1] = true;
		} while (t);
		graphMatrix[i] = temp;
	}
	//матрица смежности
	for (int i = 0; i < graphMatrix.size(); i++) {
		for (int j = 0; j < graphMatrix.size(); j++) {
			cout << graphMatrix[i][j] << " ";
		}
		cout << endl;
	}

	//начало поиска в ширину
	queue<Node> q;//очередь для поиска в ширину
	start--;
	q.push(nodes[start]);//задание стартовой позиции в очереди для нахождения всех путей
	Edge tempEdge;
	
	while(!q.empty())
	{
		Node check = q.front();
		q.pop();
		nodes[check.number - 1].status = 2; //помечаем текущую ноду как посещенную
		for (int i = 0; i < check.conWith.size(); i++)
		{
			if (nodes[check.conWith[i] - 1].status == 0)
			{
				q.push(nodes[check.conWith[i] - 1]);
				nodes[check.conWith[i] - 1].status = 1;//помечаем все соединенные с CHECK как обнаруженные
				tempEdge.beginNode = check.number;	tempEdge.endNode = nodes[check.conWith[i] - 1].number; //заполняем ребро для вывода пути
				edges.push(tempEdge);
			}
		}
		components[0].push_back(check.number);//Заполнение первой компоненты связности
	}
	
	for (int endPoint = 1,i; endPoint	<= N; endPoint++)
	{
		if (endPoint == start+1)
			continue;
		i = endPoint;

		cout << "\nRoute to " << endPoint << " from " << (start+1) << "\n";
		if (nodes[i-1].status == 0)
		{
			cout << "There is no route from node " << (start+1);
			continue;
		}
		cout << i;

		stack<Edge> tempEdges = edges;
		while (!tempEdges.empty()) {
			tempEdge = tempEdges.top();
			tempEdges.pop();
			if (tempEdge.endNode == i) {
				i = tempEdge.beginNode;
				cout << " <- " << i;
			}
		}
	}

	//Поиск других компонент связности
	vector<int> tempComponent;
	for (int i = 0; i < N; i++)
	{
		if (nodes[i].status != 0)
			continue;
		q.push(nodes[i]);
		while (!q.empty())
		{
			Node check = q.front();//получаем текущую в очереди ноду
			q.pop();
			nodes[check.number - 1].status = 2; //помечаем текущую ноду как посещенную
			for (int i = 0; i < check.conWith.size(); i++)
			{
				if (nodes[check.conWith[i] - 1].status == 0)
				{
					q.push(nodes[check.conWith[i] - 1]);
					nodes[check.conWith[i] - 1].status = 1;//помечаем все соединенные с CHECK как обнаруженные
				}
			}
			tempComponent.push_back(check.number);//Заполнение еще одной компоненты связности
		}
		components.push_back(tempComponent);
		tempComponent.clear();
	}


	cout << "\nAll " << components.size() << " components:\n";
	for (int i = 0; i < components.size(); i++)
	{
		cout << i+1 << ": ";
		for (int j = 0; j < components[i].size(); j++)
		{
			cout << components[i][j] << " ";
		}
		cout << "\n";
	}
}
