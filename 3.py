import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# 定义三棱柱的顶点
def create_prism_vertices(base_triangle, height):
    # 三棱柱的顶面和底面的顶点
    base_vertices = base_triangle
    top_vertices = [[x, y, height] for x, y, z in base_triangle]
    
    # 将顶面和底面顶点组合
    vertices = base_vertices + top_vertices
    return vertices

# 定义三角形底面顶点 (三角形边长分别为3, 4, 5)
triangle_vertices = [[0, 0, 0], [3, 0, 0], [0, 4, 0]]  # 3个顶点的坐标

# 三棱柱的高度
prism_height = 12

# 获取三棱柱的顶点
vertices = create_prism_vertices(triangle_vertices, prism_height)

# 定义三棱柱的面（顶面、底面和侧面）
faces = [
    [vertices[0], vertices[1], vertices[2]],  # 底面
    [vertices[3], vertices[4], vertices[5]],  # 顶面
    [vertices[0], vertices[1], vertices[4], vertices[3]],  # 侧面1
    [vertices[1], vertices[2], vertices[5], vertices[4]],  # 侧面2
    [vertices[2], vertices[0], vertices[3], vertices[5]],  # 侧面3
]

# 创建图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制三棱柱
ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

# 设置图形显示范围
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([0, 15])

# 设置标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 显示图形
plt.show()

