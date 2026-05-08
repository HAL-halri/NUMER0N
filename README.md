ブラウザで手軽に遊べる数当てゲーム「Numer0n」のWebアプリケーションです。  
実際のアプリはこちら：https://numer0n-3kgc.onrender.com/  
※起動までに数十秒かかる場合がございます。

**・実際のプレイ画像**  
**1.スタート画面**
<img width="960" height="497" alt="Numeron_starting" src="https://github.com/user-attachments/assets/0858b0d7-6c09-4b88-9a94-7657b9186279" />
**2.ゲーム中の画面**
<img width="960" height="498" alt="Numeron_gaming" src="https://github.com/user-attachments/assets/63823970-d932-4692-9133-f8f347ff4c8e" />
**3.リザルト画面**
<img width="958" height="497" alt="Numeron_result" src="https://github.com/user-attachments/assets/bf3d7258-fb67-4389-b33d-81e12a526dd4" />

**・使用技術**  
 ▸バックエンド：Python, Flask  
 ▸フロントエンド：HTML, CSS  
 ▸インフラ・デプロイ：Render  

**・開発時に苦労した点**  
単純なループ処理では、EatとBiteが重複してカウントされてしまうという課題がありました。
これを解決するためにEatで判定された数字を文字に置き換え、正確に判定されるようにしました。

**・今後の課題等**  
現状では完全に1人でしかプレイできないため、合言葉を用いた複数人での対戦形式や、各難易度でのクリアタイムを競うランキング形式などを実装したいと考えております。
