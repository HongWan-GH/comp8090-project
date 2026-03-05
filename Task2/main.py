# main.py (可以在 Task2 下创建，展示图与 Dijkstra 的使用)
from graph import Graph
from dijkstra import dijkstra, shortest_path

def main():
    # 创建一个示例图
    g = Graph()
    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 2)
    g.add_edge("B", "C", 1)
    g.add_edge("B", "D", 5)
    g.add_edge("C", "D", 8)
    g.add_edge("C", "E", 10)
    g.add_edge("D", "E", 2)
    g.add_edge("D", "F", 6)
    g.add_edge("E", "F", 3)

    print("图结构（邻接表）：")
    print(g)

    start = "A"
    distances = dijkstra(g, start)
    print(f"\n从节点 {start} 出发的最短距离：")
    for node, dist in distances.items():
        print(f"  {node}: {dist}")

    # 路径查询
    end = "F"
    path = shortest_path(g, start, end)
    print(f"\n从 {start} 到 {end} 的最短路径：{path}")

if __name__ == "__main__":
    main()
