import pandas as pd
import folium

# csvからデータの読み込み
df_1 = pd.read_csv("inside_gate.csv")
df_2 = pd.read_csv("outside_gate.csv")

# データのリスト化
inside = df_1[["緯度","経度","店舗名","詳細"]].values
outside = df_2[["緯度","経度","店舗名","詳細"]].values

# 欠損値削除
df = df_1.dropna()
df = df_2.dropna()

# 地図生成・東京都中心
m = folium.Map(location=[35.72349, 139.749553], zoom_start=6)
for data in inside:
	folium.Marker(
                [data[0], data[1]],
                # 店舗名
                tooltip=data[2],
                # 詳細
                popup=data[3],  
                # アイコンの色・デザイン
                icon=folium.Icon(color="lightred", icon="star")
        ).add_to(m)
for data in outside:
        folium.Marker(
                [data[0], data[1]],
                # 店舗名
                tooltip=data[2],
                # 詳細
                popup=data[3],
                # アイコンの色・デザイン
                icon=folium.Icon(color="lightgreen", icon="star-empty")
        ).add_to(m)

# 地図表示
m.save('shinkansen_starbucks.html')
