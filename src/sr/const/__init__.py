STANDARD_RESOLUTION_W = 1920
STANDARD_RESOLUTION_H = 1080
STANDARD_CENTER_POS = (STANDARD_RESOLUTION_W // 2, STANDARD_RESOLUTION_H // 2)

TEMPLATE_ARROW = "arrow"
TEMPLATE_ARROW_LEN = 31  # 箭头的图片大小
TEMPLATE_ARROW_LEN_PLUS = 35  # 箭头图片在拼接图中的大小
TEMPLATE_ARROW_R = TEMPLATE_ARROW_LEN // 2  # 箭头的图片半径
TEMPLATE_TRANSPORT_LEN = 51  # 传送点的图片大小

THRESHOLD_SP_TEMPLATE_IN_LARGE_MAP = 0.7  # 特殊点模板在大地图上的阈值
THRESHOLD_SP_TEMPLATE_IN_LITTLE_MAP = 0.7  # 特殊点模板在小地图上的阈值
THRESHOLD_SP_TEMPLATE_IN_LITTLE_MAP_CENTER = 0.4  # 特殊点模板在小地图中心的阈值
THRESHOLD_ARROW_IN_LITTLE_MAP = 0.9  # 小地图箭头的阈值
COLOR_WHITE_GRAY = 255  # 地图上道路颜色
COLOR_WHITE_BGR = (255, 255, 255)  # 白色
COLOR_WHITE_BGRA = (255, 255, 255, 255)  # 白色
COLOR_MAP_ROAD_GRAY = 0  # 地图上道路颜色
COLOR_MAP_ROAD_BGR = (60, 60, 60)  # 地图上道路颜色
COLOR_SP_BG_BGR = (0, 0, 0)  # 特殊点背景颜色
COLOR_MAP_EDGE_BGR = (0, 255, 0)  # 地图上边的颜色
COLOR_ARROW_BGR = (255, 200, 0)  # 小箭头颜色
COLOR_ARROW_ALPHA = (0, 0, 0, 0)  # 透明
