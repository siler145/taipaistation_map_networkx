import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch
# 创建一个空的无向图
G = nx.Graph()

# 添加交叉口节点
crossroad_coordinates = {
    (2.75, 1): ['C01'],
    (2.75, 3.5): ['A15', 'A20', 'A21'],
    (2.75, 3.8): ['A16'],
    (2.2, 0.75): ['C02', 'C03', 'C04', 'C05', 'C06', 'C07'],
    (2.2, 1): ['B02'],
    (2.2, 2.35): ['B01'],
    (2.2, 3.5): ['A17', 'A18', 'A19', 'A22'],
    (4.75, 1): ['C08', 'C09', 'C10', 'C11', 'C12', 'E07', 'E08'],
    (4.75, 1.9): ['E05', 'E06'],
    (4.75, 2.6): ['E03', 'E04'],
    (4.75, 3.5): ['A10', 'A11', 'A13', 'A14', 'A12', 'E01', 'E02'],
    (5.8, 1): ['C13', 'C14', 'C15'],
    (5.8, 3.5): ['A04', 'A05', 'A06', 'A07', 'A08', 'A09'],
    (7.4, 1): ['C16', 'C17', 'C18', 'D01'],
    (7.4, 3.5): ['A03', 'D02', 'D03'],
    (8.3, 3.8): ['A01', 'A02']
}

# crossroad_coordinates = {
#     'C01': (2.75, 1.25),
#     'A15': (2.75, 3.5),
#     'A20': (2.75, 3.5),
#     'A21': (2.75, 3.5),
#     'A16': (2.75, 3.8),
#     'C02': (2.2, 0.75),
#     'C03': (2.2, 0.75),
#     'C04': (2.2, 0.75),
#     'C05': (2.2, 0.75),
#     'C06': (2.2, 0.75),
#     'C07': (2.2, 0.75),
#     'B02': (2.2, 1.25),
#     'B01': (2.2, 2.35),
#     'A17': (2.2, 3.5),
#     'A18': (2.2, 3.5),
#     'A19': (2.2, 3.5),
#     'A22': (2.2, 3.5),
#     'C08': (4.75, 1.25),
#     'C09': (4.75, 1.25),
#     'C10': (4.75, 1.25),
#     'C11': (4.75, 1.25),
#     'C12': (4.75, 1.25),
#     'E07': (4.75, 1.25),
#     'E08': (4.75, 1.25),
#     'E05': (4.75, 1.9),
#     'E06': (4.75, 1.9),
#     'E03': (4.75, 2.6),
#     'E04': (4.75, 2.6),
#     'A10': (4.75, 3.5),
#     'A11': (4.75, 3.5),
#     'A13': (4.75, 3.5),
#     'A14': (4.75, 3.5),
#     'A12': (4.75, 3.5),
#     'E01': (4.75, 3.5),
#     'E02': (4.75, 3.5),
#     'C13': (5.8, 1),
#     'C14': (5.8, 1),
#     'C15': (5.8, 1),
#     'A04': (5.8, 3.5),
#     'A05': (5.8, 3.5),
#     'A06': (5.8, 3.5),
#     'A07': (5.8, 3.5),
#     'A08': (5.8, 3.5),
#     'A09': (5.8, 3.5),
#     'C16': (7.3, 1),
#     'C17': (7.3, 1),
#     'C18': (7.3, 1),
#     'D01': (7.3, 1),
#     'A03': (7.4, 3.5),
#     'D02': (7.4, 3.5),
#     'D03': (7.4, 3.5),
#     'A01': (8.3, 3.8),
#     'A02': (8.3, 3.8)
# }

for coord, crossroads in crossroad_coordinates.items():
    G.add_node(coord, crossroads=crossroads)



# 创建底图和格线
map_width = 10
map_height = 5
bg_image = plt.imread('map.jpg')
scale_x = map_width / bg_image.shape[1]
scale_y = map_height / bg_image.shape[0]

fig, ax = plt.subplots(figsize=(8, 6))
ax.imshow(bg_image, extent=[0, map_width, 0, map_height])
grid_interval_x = 0.5
grid_interval_y = 0.5
x_ticks = np.arange(0, map_width + 1, grid_interval_x)
y_ticks = np.arange(0, map_height + 1, grid_interval_y)
for x in x_ticks:
    ax.axvline(x+0.1, color='gray', linestyle='--', linewidth=0.5)
for y in y_ticks:
    ax.axhline(y, color='gray', linestyle='--', linewidth=0.5)

# 获取节点坐标和交叉口列表
pos = dict(zip(G.nodes(), G.nodes()))  # 设置节点的位置为节点本身，即 (x, y) 座标

# 绘制节点
nx.draw_networkx_nodes(G, pos, node_size=20, node_color='red')
# pos = nx.get_node_attributes(G, 'pos')
# nx.draw_networkx_nodes(G, pos, node_size=20, node_color='red')


# 在地图上标记交叉口的座标和交叉口列表
for coord, (x, y) in pos.items():
    plt.text(x, y -0.25, f'({x}, {y})', color='red', ha='center', va='center', fontsize=8)
    crossroad_list = ','.join(crossroad_coordinates[coord])
    # plt.text(x, y - 0.25, crossroad_list, color='black', ha='center', va='center', fontsize=8)  # 添加交叉口列表
# 在地图上标记交叉口的坐标
# for crossroad, coord in pos.items():
#     plt.text(coord[0], coord[1] - 0.25, f'({coord[0]}, {coord[1]})', color='red', ha='center', va='center', fontsize=8)



# 添加连线
edges = [
    ((2.2, 0.75), (2.2, 1)),
    ((2.2, 1), (2.2, 2.35)),
    ((2.2, 2.35), (2.2, 3.5)),
    ((2.75, 1), (2.2, 1)),
    ((2.75, 3.5), (4.75, 3.5)),
    ((2.75, 3.5), (2.75, 3.8)),
    ((2.2, 3.5), (2.75, 3.5)),
    ((4.75, 1), (4.75, 1.9)),
    ((4.75, 1.9), (4.75, 2.6)),
    ((4.75, 2.6), (4.75, 3.5)),
    ((2.75, 1), (4.75, 1)),
    ((4.75, 1), (5.8, 1)),
    ((5.8, 1), (7.4, 1)),
    ((7.4, 3.5), (7.4, 1)),
    ((7.4, 3.5), (8.3, 3.8)),
    ((4.75, 3.5), (7.4, 3.5))
]
# edges = [
#     ('C02', 'C03'), ('C02', 'C04'), ('C02', 'C05'), ('C02', 'C06'), ('C02', 'C07'),
#     ('B02', 'C02'),
#     ('B01', 'B02'),
#     ('A17', 'B01'), ('A18', 'B01'), ('A19', 'B01'), ('A22', 'B01'),
#     ('C01', 'B02'),
#     ('A15', 'C01'), ('A20', 'C01'), ('A21', 'C01'),
#     ('A16', 'A15'), ('A16', 'A20'), ('A16', 'A21'),
#     ('A15', 'A17'), ('A15', 'A18'), ('A15', 'A19'), ('A15', 'A22'),
#     ('C08', 'C09'), ('C08', 'C10'), ('C08', 'C11'), ('C08', 'C12'), ('C08', 'E07'), ('C08', 'E08'),
#     ('E05', 'E06'),
#     ('E03', 'E04'),
#     ('A10', 'A11'), ('A10', 'A13'), ('A10', 'A14'), ('A10', 'A12'), ('A10', 'E01'), ('A10', 'E02'),
#     ('A11', 'C08'),
#     ('C13', 'C14'), ('C13', 'C15'),
#     ('C16', 'C17'), ('C16', 'C18'), ('C16', 'D01'),
#     ('A03', 'D02'), ('A03', 'D03'),
#     ('A01', 'A03'), ('A01', 'A02'),
#     ('A04', 'A05'), ('A04', 'A06'), ('A04', 'A07'), ('A04', 'A08'), ('A04', 'A09'),
#     ('A04', 'C16'),
#     ('A04', 'A01'),
#     ('A02', 'A04'),
#     ('A05', 'A04'),
#     ('A06', 'A05'),
#     ('A07', 'A06'),
#     ('A08', 'A07'),
#     ('A09', 'A08'),
#     ('D02', 'A04'),
#     ('D03', 'A03'),
#     ('C15', 'A09')
# ]

nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='blue')

# 在座标轴上标示刻度值
plt.xticks(np.arange(0, map_width + 1, grid_interval_x))
plt.yticks(np.arange(0, map_height + 1, grid_interval_y))

# 显示座标化地图
plt.axis('off')
plt.show()

def short_path(start,end):
  return nx.shortest_path(G, source=start, target=end)
  

# start_input = input('start:')
# end_input = input('end:')
start_input ='A01'
end_input = 'C01'

# start = crossroad_coordinates.get(start_input)
# end = crossroad_coordinates.get(end_input)
# 从交叉口标识转换为坐标
start = None
end = None

for coord, crossroads in crossroad_coordinates.items():
    if start_input in crossroads:
        start = coord
    if end_input in crossroads:
        end = coord

# result = short_path(start,end)
# print(result)