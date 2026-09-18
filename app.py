import streamlit as st

# ページの設定（スマホで見やすいよう中央寄せ）
st.set_page_config(
    page_title="りらっくすサバーイ - ご感想作成",
    page_icon="🌿",
    layout="centered"
)

# ヘッダーデザイン
st.title("🌿 りらっくすサバーイ")
st.caption("本日はご来店ありがとうございました！")
st.write("簡単な選択肢を選ぶだけで、Google口コミ用の文章を作成できます（約15秒）。")

# フォーム設定
with st.form("review_form"):
    menu = st.multiselect(
        "1. 本日受けられたメニュー（複数選択可）",
        [
            "タイ古式マッサージ",
            "タイ古式 ＋ 快眠ドライヘッドスパ",
            "タイ古式 ＋ アロマオイル",
            "タイ古式 ＋ フットリフレ"
        ]
    )

    trouble = st.multiselect(
        "2. 本日のお辛かったお悩み",
        [
            "デスクワークによる首・肩・背中のコリ",
            "PC・スマホによる眼精疲労・頭痛・脳疲労",
            "睡眠が浅い・疲れが取れない",
            "日常から離れて贅沢にリフレッシュしたい"
        ]
    )

    atmosphere = st.multiselect(
        "3. サロンの雰囲気や施術はいかがでしたか？",
        [
            "完全貸切のプライベート空間でリラックスできた",
            "他の人の目を気にせず静かに過ごせた",
            "絶妙なストレッチで身体が芯から伸ばされた",
            "強さやアプローチが自分にぴったりだった"
        ]
    )

    effect = st.multiselect(
        "4. 施術後の身体の変化",
        [
            "身体が嘘のように軽くなった",
            "頭がスッキリして視界が明るくなった",
            "もみ返しがなく爽快感がある",
            "仕事のパフォーマンスが上がりそう"
        ]
    )

    submitted = st.form_submit_button("✨ 口コミ文章を作成する", use_container_width=True)

if submitted:
    # 文章自動生成ロジック
    review_text = ""
    if trouble:
        review_text += f"{'・'.join(trouble)}が限界だったので「りらっくすサバーイ」さんにお邪魔しました。\n"
    if menu:
        review_text += f"今回は{'・'.join(menu)}のコースを受けましたが、"
    if atmosphere:
        review_text += f"{'。'.join(atmosphere)}。\n"
    if effect:
        review_text += f"施術後は{'。'.join(effect)}！\n"

    review_text += "完全貸切の落ち着いた空間でとてもリフレッシュできました。また自分へのご褒美に通いたいです！"

    st.success("🎉 口コミ文章が作成されました！")
    
    # 長押ししてコピーしやすいテキストエリア
    st.text_area(
        "▼ 以下の文章を長押し・全選択して「コピー」してください",
        value=review_text,
        height=160
    )

    # Googleビジネスプロフィールの直接口コミ投稿URL
    # ※「YOUR_PLACE_ID」の部分をご自身の店舗のPlace IDに書き換えます
    google_review_url = "https://search.google.com/local/writereview?placeid=ChIJm1G9QU5nPjUR2Xvm6gdBgjU"

    # デザイン付きの投稿ボタン
    st.markdown(f'''
        <a href="{google_review_url}" target="_blank" style="text-decoration:none;">
            <div style="background-color:#4285F4; color:white; font-weight:bold; text-align:center; padding:14px; border-radius:8px; font-size:16px; margin-top:10px;">
                👉 コピーしてGoogleマップに投稿する
            </div>
        </a>
    ''', unsafe_html=True)