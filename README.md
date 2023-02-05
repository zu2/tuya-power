# tuya-power

tuya OEMのスマートプラグのデータを得るサンプル

買った製品: <a href="https://amzn.to/3wX41v6">スマートプラグ Wi-Fiコンセント</a>

<a href="https://www.amazon.co.jp/gp/product/B09QPGN2P3?ie=UTF8&psc=1&linkCode=li3&tag=zu-22&linkId=817ed1e3bce2f580788539ceaef9bfb7&language=ja_JP&ref_=as_li_ss_il" target="_blank"><img border="0" src="https://ws-fe.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B09QPGN2P3&Format=_SL250_&ID=AsinImage&MarketPlace=JP&ServiceVersion=20070822&WS=1&tag=zu-22&language=ja_JP" ></a><img src="https://ir-jp.amazon-adsystem.com/e/ir?t=zu-22&language=ja_JP&l=li3&o=9&a=B09QPGN2P3" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />

使用ライブラリ: https://github.com/jasonacox/tuyapower

# [tuya-munin.py](https://github.com/zu2/tuya-power/blob/main/tuya-munin.py)

munin用プラグイン

## TODO

- 機器が増えたらdevices.jsonを作り直す必要がある
- ネットワーク内のデバイスをスキャンしてるので遅い。Macアドレスから逆引きした方が良いか？
- 月間の電力消費量もグラフ化したい
