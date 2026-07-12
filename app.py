import streamlit st
import networkx as nx

# ==========================================
# 1. 路線・駅名・施設データ
# ==========================================
def get_station_kana():
    return {
        "一ノ瀬": "いちのせ", "境港": "さかいみなと", "谷上町": "たにかみちょう", "第1拠点": "だいいちきょてん",
        "晴海坂": "はるみざか", "滝沢": "たきさわ", "終宮": "ついのみや", "新蒼海宮": "しんそうかいぐう",
        "蒼海宮": "そうかいぐう", "荒山村": "あらやまむら", "桜町一丁目": "さくらまちいっちょうめ",
        "谷上三丁目": "たにかみさんちょうme", "白浜崎": "しらはまざき", "砂炭江": "さずみえ",
        "霧ヶ峰": "きりがみね", "霧ヶ峰湖": "きりがみねこ", "風見野": "かざみの",
        "北茜ヶ原": "きたあかねがはら", "茜ヶ原": "あかねがはら", "桜坂": "さくらざか",
        "緑山": "みどりやま", "旭ヶ丘": "あさひがおか", "亀浜": "かめはま", "西霧ヶ峰": "にしきりがみね",
        "新都町": "しんmiyaこまち", "前哨基地": "ぜんしょうきち", "朝凪": "あさなぎ",
        "速見": "はやみ", "南新都町": "みなみしんmiyaこまち", "朝凪南": "あさなぎみなみ",
        "東晴海坂": "ひがしはるみざか"
    }

def get_facilities():
    return {
        "一ノ瀬": "たかのり拠点",
        "境港": "ブランチマイニング場",
        "谷上町": "初拠点付近",
        "桜町一丁目": "初期スポーン地点最寄り",
        "荒山村": "村人交易所",
        "東晴海坂": "天空トラップ",
        "終宮": "エンドポータル最寄り駅",
        "新蒼海宮": "吉岡拠点",
        "蒼海宮": "ガーディアントラップ",
        "亀浜": "霧ヶ峰空港, 竹製造機, 第二拠点中心部",
        "霧ヶ峰": "羊毛製造機",
        "霧ヶ峰湖": "畑, 牧場",
        "茜ヶ原": "メサ最寄り駅",
        "前哨基地": "前哨基地最寄り駅",
        "朝凪": "第3拠点周辺"
    }

LINES_STATIONS = {
    "中央線": ["一ノ瀬", "境港", "谷上町", "第1拠点", "晴海坂", "滝沢", "終宮", "新蒼海宮", "蒼海宮"],
    "桜町線(各停)": ["荒山村", "桜町一丁目", "谷上三丁目", "白浜崎", "砂炭江", "霧ヶ峰", "霧ヶ峰湖", "風見野", "北茜ヶ原", "茜ヶ原"],
    "桜町線(快速)": ["白浜崎", "霧ヶ峰", "茜ヶ原"],
    "東西線": ["一ノ瀬", "桜坂", "緑山", "旭ヶ丘", "霧ヶ峰", "亀浜"],
    "南北線": ["西霧ヶ峰", "新都町", "前哨基地"],
    "霧ヶ峰線": ["蒼海宮", "亀浜", "西霧ヶ峰", "霧ヶ峰湖"],
    "新都心線": ["終宮", "亀浜", "新都町", "朝凪"],
    "中央都市線": ["速見", "霧ヶ峰", "西霧ヶ峰", "南新都町", "朝凪南", "朝凪"],
    "南辺線": ["風見野", "前哨基地"],
    "中央新幹線": ["白浜崎", "新蒼海宮"],
    "晴海坂線": ["砂炭江", "晴海坂", "東晴海坂"]
}

def get_line_colors():
    return {
        "中央線": "#FF8C00",       # オレンジ
        "桜町線(各停)": "#FF69B4", # ピンク
        "桜町線(快速)": "#FF1493", # 濃いピンク
        "東西線": "#00BFFF",       # 水色
        "南北線": "#1E90FF",       # 青
        "霧ヶ峰線": "#FF0000",     # 赤
        "新都心線": "#8B4513",     # 茶色
        "中央都市線": "#228B22",   # 緑
        "南辺線": "#8A2BE2",       # 紫
        "中央新幹線": "#FFD700",   # 金色
        "晴海坂線": "#808080"      # グレー
    }

def get_lines_data():
    return {
        "中央線": [("一ノ瀬", "境港", 46), ("境港", "谷上町", 30), ("谷上町", "第1拠点", 14), ("第1拠点", "晴海坂", 15), ("晴海坂", "滝沢", 45), ("滝沢", "終宮", 54), ("終宮", "新蒼海宮", 90), ("新蒼海宮", "蒼海宮", 51)],
        "桜町線(各停)": [("荒山村", "桜町一丁目", 48), ("桜町一丁目", "谷上三丁目", 16), ("谷上三丁目", "白浜崎", 28), ("白浜崎", "砂炭江", 66), ("砂炭江", "霧ヶ峰", 104), ("霧ヶ峰", "霧ヶ峰湖", 26), ("霧ヶ峰湖", "風見野", 68), ("風見野", "北茜ヶ原", 91), ("北茜ヶ原", "茜ヶ原", 56)],
        "桜町線(快速)": [("白浜崎", "霧ヶ峰", 160), ("霧ヶ峰", "茜ヶ原", 240)],
        "東西線": [("一ノ瀬", "桜坂", 124), ("桜坂", "緑山", 92), ("緑山", "旭ヶ丘", 28), ("旭ヶ丘", "霧ヶ峰", 48), ("霧ヶ峰", "亀浜", 39)],
        "南北線": [("西霧ヶ峰", "新都町", 19), ("新都町", "前哨基地", 96)],
        "霧ヶ峰線": [("蒼海宮", "亀浜", 197), ("亀浜", "西霧ヶ峰", 22), ("西霧ヶ峰", "霧ヶ峰湖", 40)],
        "新都心線": [("終宮", "亀浜", 138), ("亀浜", "新都町", 27), ("新都町", "朝凪", 60)],
        "中央都市線": [("速見", "霧ヶ峰", 16), ("霧ヶ峰", "西霧ヶ峰", 13), ("西霧ヶ峰", "南新都町", 20), ("南新都町", "朝凪南", 20), ("朝凪南", "朝凪", 60)],
        "南辺線": [("風見野", "前哨基地", 62)],
        "中央新幹線": [("白浜崎", "新蒼海宮", 44)],
        "晴海坂線": [("砂炭江", "晴海坂", 57), ("晴海坂", "東晴海坂", 25)]
    }

def get_direction(line_name, from_station, to_station):
    if line_name in LINES_STATIONS:
        stations = LINES_STATIONS[line_name]
        if from_station in stations and to_station in stations:
            idx_from = stations.index(from_station)
            idx_to = stations.index(to_station)
            return f"{stations[-1]}方面" if idx_to > idx_from else f"{stations[0]}方面"
    return ""

# ==========================================
# 2. グラフ構築
# ==========================================
@st.cache_resource
def build_graph():
    G = nx.Graph()
    lines = get_lines_data()
    station_lines = {}
    
    for line_name, edges in lines.items():
        for u, v, w in edges:
            G.add_edge(f"{u}|{line_name}", f"{v}|{line_name}", weight_fast=w, weight_trans=1, line=line_name, is_transfer=False)
            station_lines.setdefault(u, set()).add(line_name)
            station_lines.setdefault(v, set()).add(line_name)
            
    # 駅内乗り換えの処理
    for sta, slines in station_lines.items():
        sorted_slines = sorted(list(slines))
        for i in range(len(sorted_slines)):
            for j in range(i+1, len(sorted_slines)):
                line_a = sorted_slines[i]
                line_b = sorted_slines[j]
                
                if sta == "白浜崎" and set([line_a, line_b]) == {"桜町線(各停)", "桜町線(快速)"}:
                    G.add_edge(f"{sta}|{line_a}", f"{sta}|{line_b}", weight_fast=0, weight_trans=0, line="直通", is_transfer=False)
                else:
                    G.add_edge(f"{sta}|{line_a}", f"{sta}|{line_b}", weight_fast=30, weight_trans=10000, line="乗り換え", is_transfer=True)

    # 🚶 徒歩連絡の処理
    walks = [
        ("谷上町", "谷上三丁目", 10), 
        ("新都町", "南新都町", 10)    
    ]
    for u, v, w in walks:
        if u in station_lines and v in station_lines:
            for l_u in station_lines[u]:
                for l_v in station_lines[v]:
                    G.add_edge(f"{u}|{l_u}", f"{v}|{l_v}", weight_fast=w, weight_trans=10000, line="徒歩連絡", is_transfer=True)
                    
    # 【追加機能】砂炭江からの特殊直通ルート設定
    G.add_edge("砂炭江|桜町線(各停)", "西霧ヶ峰|南北線", weight_fast=110, weight_trans=0, line="南北線(直通)", is_transfer=False)
    G.add_edge("砂炭江|桜町線(各停)", "亀浜|東西線", weight_fast=94, weight_trans=0, line="東西線(直通)", is_transfer=False)
    G.add_edge("砂炭江|桜町線(各停)", "亀浜|新都心線", weight_fast=94, weight_trans=0, line="新都心線(直通)", is_transfer=False)
    
    return G, station_lines

# ==========================================
# 3. UIメイン処理
# ==========================================
def main():
    st.set_page_config(page_title="Minecraft鉄道 乗り換え案内", layout="centered")
    st.title("水素鉄道 乗り換え案内 ver3.0")
    
    G_base, station_lines = build_graph()
    station_kana = get_station_kana()
    facilities = get_facilities()
    line_colors = get_line_colors()
    
    sorted_stations = sorted(list(station_lines.keys()), key=lambda x: station_kana[x])
    station_options = [f"{s} ({station_kana[s]})" for s in sorted_stations]

    st.markdown("### 出発・到着駅と条件を選択")
    col1, col2 = st.columns(2)
    
    default_start = [opt for opt in station_options if opt.startswith("荒山村")][0] if any(opt.startswith("荒山村") for opt in station_options) else station_options[0]
    default_end = [opt for opt in station_options if opt.startswith("霧ヶ峰 ")][0] if any(opt.startswith("霧ヶ峰 ") for opt in station_options) else station_options[1]
    
    start_str = col1.selectbox("出発駅", station_options, index=station_options.index(default_start))
    end_str = col2.selectbox("到着駅", station_options, index=station_options.index(default_end))
    
    start_sta = start_str.split(' ')[0]
    end_sta = end_str.split(' ')[0]

    search_mode = st.radio("優先する条件", ["最速（時間を優先／快速優先）", "乗り換え回数（乗換の少なさを優先）"], horizontal=True)

    if st.button("経路を検索", type="primary", use_container_width=True):
        if start_sta == end_sta:
            st.warning("出発駅と到着駅が同じです。")
            return

        G = G_base.copy()
        for line in station_lines[start_sta]:
            G.add_edge("START", f"{start_sta}|{line}", weight_fast=0, weight_trans=0, line="乗車", is_transfer=False)
        for line in station_lines[end_sta]:
            G.add_edge(f"{end_sta}|{line}", "END", weight_fast=0, weight_trans=0, line="降車", is_transfer=False)

        weight_key = "weight_fast" if "最速" in search_mode else "weight_trans"

        try:
            path = nx.shortest_path(G, "START", "END", weight=weight_key)
            
            steps = []
            transfer_count = 0
            total_ride_time = 0  # 乗車時間の合計秒数
            actual_path = path[1:-1]

            for i in range(len(actual_path)-1):
                u, v = actual_path[i], actual_path[i+1]
                data = G.get_edge_data(u, v)
                u_sta = u.split('|')[0]
                v_sta = v.split('|')[0]
                
                cost = data.get('weight_fast', 0)
                
                if data['is_transfer']:
                    transfer_count += 1
                    steps.append({
                        "from": u_sta, "to": v_sta, "line": data['line'], 
                        "is_transfer": True, "is_direct": False, "intermediates": [], "time": cost
                    })
                elif u_sta == v_sta and not data['is_transfer']:
                    steps.append({
                        "from": u_sta, "to": v_sta, "line": data['line'],
                        "is_transfer": False, "is_direct": True, "intermediates": [], "time": cost
                    })
                else:
                    total_ride_time += cost  # 純粋な乗車時間を加算
                    if steps and not steps[-1]['is_transfer'] and not steps[-1]['is_direct'] and steps[-1]['line'] == data['line']:
                        steps[-1]['to'] = v_sta
                        steps[-1]['intermediates'].append(u_sta)
                        steps[-1]['time'] += cost
                    else:
                        steps.append({
                            "from": u_sta, "to": v_sta, "line": data['line'], 
                            "is_transfer": False, "is_direct": False, "intermediates": [], "time": cost
                        })
            
            # 【新機能】1の位を四捨五入して10秒単位にするフォーマット関数
            def round_time_str(seconds):
                rounded = int((seconds + 5) // 10) * 10
                if rounded == 0:
                    return "0秒"
                m, s = divmod(rounded, 60)
                if m > 0:
                    return f"{m}分{s}秒"
                return f"{s}秒"
            
            total_time_formatted = round_time_str(total_ride_time)
            st.success(f"乗換: **{transfer_count}回** ｜ 総乗車時間: **{total_time_formatted}**")
            st.divider()
            
            for step in steps:
                if step['is_transfer']:
                    if step['line'] == "徒歩連絡":
                        st.markdown(f"<div style='text-align: center; color: #4CAF50; font-weight: bold; margin: 15px 0;'>🚶 {step['from']}駅から {step['to']}駅へ徒歩移動</div>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<div style='text-align: center; color: gray; margin: 15px 0;'>↑↓ {step['from']}駅で乗り換え</div>", unsafe_allow_html=True)
                elif step['is_direct']:
                    st.markdown(f"<div style='text-align: center; color: #ff4b4b; font-weight: bold; margin: 15px 0;'>✨ {step['from']}駅から直通（そのまま乗車）</div>", unsafe_allow_html=True)
                else:
                    color = line_colors.get(step['line'], "#555555")
                    ride_time_formatted = round_time_str(step['time'])
                    
                    with st.container():
                        st.markdown(
                            f"""
                            <div style='border-left: 6px solid {color}; padding-left: 15px; margin: 10px 0;'>
                                <h4 style='margin: 0 0 5px 0;'>{step['from']}駅</h4>
                                <p style='margin: 0; color: {color}; font-weight: bold;'>↓ {step['line']}{f" [{get_direction(step['line'], step['from'], step['to'])}]" if get_direction(step['line'], step['from'], step['to']) else ""} （乗車時間: {ride_time_formatted}）</p>
                            </div>
                            """, 
                            unsafe_allow_html=True
                        )
                        
                        if step['intermediates']:
                            with st.expander(f"途中駅（{len(step['intermediates'])}駅）"):
                                for inter in step['intermediates']:
                                    st.write(f"・ {inter}駅")
                                    
                        st.markdown(
                            f"""
                            <div style='border-left: 6px solid {color}; padding-left: 15px; margin: 10px 0;'>
                                <h4 style='margin: 5px 0 0 0;'>{step['to']}駅</h4>
                            </div>
                            """, 
                            unsafe_allow_html=True
                        )

        except nx.NetworkXNoPath:
            st.error("経路が見つかりませんでした。")

    st.divider()
    
    st.markdown("### 各路線の停車駅案内")
    selected_line = st.selectbox("路線を選択", list(LINES_STATIONS.keys()))
    if selected_line:
        stations_with_suffix = [f"{s}駅" for s in LINES_STATIONS[selected_line]]
        st.write(" → ".join(stations_with_suffix))

    st.divider()

    st.markdown("### 駅の接続路線を調べる")
    selected_str = st.selectbox("駅を選択", station_options, key="station_info")
    target_sta = selected_str.split(' ')[0]
    
    if target_sta in station_lines:
        lines = sorted(list(station_lines[target_sta]))
        with st.container(border=True):
            st.markdown(f"**{target_sta}駅 ({station_kana[target_sta]})** の接続路線")
            for line in lines:
                st.markdown(f"- {line}")

    st.divider()

    st.markdown("### 施設・拠点から最寄り駅を探す")
    with st.expander("主要施設・拠点一覧を表示"):
        for sta in sorted_stations:
            if sta in facilities:
                st.markdown(f"- **{sta}駅** …… {facilities[sta]}")

if __name__ == "__main__":
    main()