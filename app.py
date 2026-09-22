import random
import streamlit as st

st.set_page_config(
    page_title="りらっくすサバーイ - ご感想作成", page_icon="🌿"
)

# --- Google Place ID 設定 ---
PLACE_ID = "ChIJNTf6KqXmPzURa3cOnJ62S_g"


def generate_review(menus, troubles, impressions, changes):
    # --- 1. 書き出しバリエーション ---
    intros = [
        "「りらっくすサバーイ」さんにお世話になりました！",
        "日頃の疲れをリセットしたくて、「りらっくすサバーイ」さんを訪問しました。",
        "体のケアのために「りらっくすサバーイ」さんにお邪魔しました。",
        "ずっと気になっていた「りらっくすサバーイ」さんに行ってきました。",
        "疲れた体をしっかりほぐしたくて、今回「りらっくすサバーイ」さんを利用しました。",
    ]

    # --- 2. お悩みの表現変換 ---
    trouble_text = ""
    if troubles:
        t_str = "や".join(troubles)
        t_patterns = [
            f"最近は特に{t_str}がつらくて相談させていただいたのですが、",
            f"仕事柄{t_str}が溜まりがちだったのですが、",
            f"ずっと{t_str}に悩んでいたのですが、",
            f"特に{t_str}のケアを中心にお願いしたのですが、",
        ]
        trouble_text = random.choice(t_patterns)

    # --- 3. メニューと施術の感想 ---
    menu_text = ""
    if menus:
        m_str = "と".join(menus)
        m_patterns = [
            f"今回受けた{m_str}の施術が本当に心地よかったです。",
            f"今回は{m_str}をお願いしましたが、大満足の施術でした！",
            f"{m_str}を中心に丁寧にケアしていただきました。",
        ]
        menu_text = random.choice(m_patterns)

    # --- 4. サロンの雰囲気・印象 ---
    impression_text = ""
    if impressions:
        i_str = "、".join(impressions)
        i_patterns = [
            f"店内の雰囲気も良く、{i_str}のがとても印象的でした。",
            f"{i_str}ため、終始安心してリラックスすることができました。",
            f"カウンセリングから施術まで親切で、{i_str}と感じました。",
        ]
        impression_text = random.choice(i_patterns)

    # --- 5. 施術後の変化 ---
    change_text = ""
    if changes:
        c_str = "、".join(changes)
        c_patterns = [
            f"終わったあとは{c_str}、驚くほどスッキリしました！",
            f"施術を受ける前と後では段違いで、{c_str}のを実感しています。",
            f"帰り道にはすでに{c_str}、体も気分も軽くなりました。",
        ]
        change_text = random.choice(c_patterns)

    # --- 6. 締めくくり ---
    outros = [
        "貸切の落ち着いた空間で心身ともにリフレッシュできました。また定期的に通いたいと思います！",
        "親身になって対応してくださり感謝しています。また疲れた時にはぜひ伺いたいです。",
        "自分へのご褒美にぴったりの素晴らしいサロンでした。また次回もよろしくお願いします！",
    ]

    # 文章の組み立て（自然な接続を意識）
    parts = [random.choice(intros)]

    if trouble_text and menu_text:
        parts.append(f"{trouble_text}{menu_text}")
    elif trouble_text:
        parts.append(f"{trouble_text}とても丁寧に対応していただきました。")
    elif menu_text:
        parts.append(menu_text)

    if impression_text:
        parts.append(impression_text)

    if change_text:
        parts.append(change_text)

    parts.append(random.choice(outros))

    return "\n\n".join(parts)


# --- UI表示 ---
st.title("🌿 りらっくすサバーイ")
st.subheader("ご来店ありがとうございました！")
st.write(
    "簡単な選択肢を選ぶだけで、Google口コミ用の文章を作成できます（約15秒）。"
)

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
        st.text_area("作成された口コミ", value=review_text, height=200)

        st.warning(
            "⚠️ **投稿時の注意点**\n\n画面が開いたら**「クチコミ」タブ**を選び、**「クチコミを書く」**から**一番右の星（★★★★★）をタップ**して文章を貼り付けてください！"
        )

        # Googleマップの店舗ページ（口コミ表示）を開くURL
        google_url = f"https://www.google.com/maps/search/?api=1&query=Google&query_place_id={PLACE_ID}"
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
            ">Step 2: ここを押してGoogle口コミ画面へ移動する ➔</a>
            """,
            unsafe_allow_html=True,
        )
