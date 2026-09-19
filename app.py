import random
import urllib.parse
import streamlit as st

st.set_page_config(page_title="りらっくすサバーイ - ご感想作成", page_icon="🌿")

# --- Google Place ID 設定 ---
# ※お持ちのPlace ID（ChIJ...）が入っている場合は、そのまま変更せずにお使いください
PLACE_ID = "ChIJCax4JyVnPjURvwYJMJpQUXg"


def generate_review(menus, troubles, impressions, changes):
    intro_list = [
        "「りらっくすサバーイ」さんにお邪魔しました。",
        "日頃の疲れを癒やしたく、「りらっくすサバーイ」さんを利用しました。",
        "評判を聞いて「りらっくすサバーイ」さんに伺いました。",
        "体のお手入れとリフレッシュのために「りらっくすサバーイ」さんを訪問しました。",
        "ゆっくり自分の体をケアしたくて「りらっくすサバーイ」さんにお世話になりました。",
        "疲れた体をしっかりほぐしたくて「りらっくすサバーイ」さんへ行きました。",
    ]

    menu_str = "・" + "、".join(menus) if menus else ""
    trouble_str = "、".join(troubles) if troubles else ""
    impression_str = " ".join(impressions) if impressions else ""
    change_str = " ".join(changes) if changes else ""

    text = f"{random.choice(intro_list)}\n\n"

    if trouble_str:
        text += f"今回は{trouble_str}が気になって相談しました。\n"

    if menu_str:
        text += f"受けたメニュー：{menu_str}\n"

    if impression_str:
        text += f"{impression_str}\n"

    if change_str:
        text += f"施術後は{change_str}を実感できました！\n"

    text += "\n完全貸切の落ち着いた空間でとてもリフレッシュできました。また利用したいと思います！"
    return text


# --- UI表示 ---
st.title("🌿 りらっくすサバーイ")
st.subheader("ご来店ありがとうございました！")
st.write("簡単な選択肢を選ぶだけで、Google口コミ用の文章を作成できます（約15秒）。")

st.markdown("---")

menus = st.multiselect(
    "1. 本日受けられたメニュー（複数選択可）",
    [
        "タイ古式マッサージ",
        "アロマオイルトリートメント",
        "ヘッドマッサージ",
        "フットリフレ",
        "ハンドリフレ",
        "フェイシャルリンパ",
        "さとう式リンパケア",
    ],
    placeholder="タップして選択してください（複数可）",
)

troubles = st.multiselect(
    "2. 本日のお辛かったお悩み",
    [
        "首・肩のコリ",
        "腰痛・背中の張り",
        "全身の疲労感・だるさ",
        "頭痛・目の疲れ",
        "むくみ・冷え",
        "ストレス・眠りが浅い",
    ],
    placeholder="タップして選択してください（複数可）",
)

impressions = st.multiselect(
    "3. サロンの雰囲気や施術はいかがでしたか？",
    [
        "絶妙なストレッチで身体が芯から伸ばされた",
        "丁寧なカウンセリングで安心できた",
        "プライベート空間で周りを気にせずリラックスできた",
        "力加減がちょうどよく心地よかった",
        "セラピストさんの対応がとても温かかった",
    ],
    placeholder="タップして選択してください（複数可）",
)

changes = st.multiselect(
    "4. 施術後の身体の変化",
    [
        "体が軽くなり動きやすくなった",
        "頭がスッキリして視界が明るくなった",
        "肩や腰の重みが和らいだ",
        "ポカポカと温かくなった",
        "気分までリフレッシュできた",
    ],
    placeholder="タップして選択してください（複数可）",
)

st.markdown("---")

if st.button("🎉 口コミ文章を作成する", type="primary"):
    if not (menus or troubles or impressions or changes):
        st.warning("選択肢を1つ以上選んでから「作成する」を押してください。")
    else:
        review_text = generate_review(menus, troubles, impressions, changes)
        st.success("🎉 口コミ文章が作成されました！")

        st.markdown("### 📱 投稿のステップ")

        st.write("**Step 1: 下の文章を長押ししてコピー**")
        st.text_area("作成された口コミ", value=review_text, height=160)

        st.warning("⚠️ **投稿時の注意点**\n\nGoogle画面が開いたら、**一番右の星（★★★★★）をタップ**してから文章を貼り付けてください！")

        # Google Review Link (ボタン風デザイン)
        if PLACE_ID and PLACE_ID != "YOUR_PLACE_ID_HERE":
            google_url = f"https://search.google.com/local/writereview?placeid={PLACE_ID}"
            st.markdown(
                f"""
                <a href="{google_url}" target="_blank" style="
                    display: block;
                    width: 100%;
                    padding: 14px;
                    background-color: #2e7d32;
                    color: white;
                    text-align: center;
                    font-size: 16px;
                    font-weight: bold;
                    border-radius: 8px;
                    text-decoration: none;
                    margin-top: 10px;
                ">Step 2: ここを押してGoogleへ投稿する ➔</a>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.info("※Googleマップで「りらっくすサバーイ」を検索して口コミを投稿してください。")
