# 出典と採用の境界

公式資料の全文・コード・素材は同梱せず、考え方を独自に要約・適応した。政府の公認、統合規格、適合宣言を意味しない。参照先の現行版・利用条件・案件の適用基準を確認する。

## 公式資料

- DADS：[スタイルガイド](https://design.digital.go.jp/dads/guidance/style-guides/)、[アクセシビリティ](https://design.digital.go.jp/dads/guidance/accessibility/)、[タイポグラフィ](https://design.digital.go.jp/dads/foundations/typography/)、[カラー](https://design.digital.go.jp/dads/foundations/color/)、[ダークモードの範囲](https://design.digital.go.jp/dads/foundations/elevation/accessibility/)、[React例](https://github.com/digital-go-jp/design-system-example-components-react)。日本語Webの基盤と、部品だけで全体の適合を保証できない境界を参照する。
- GOV.UK：[Government Design Principles](https://www.gov.uk/guidance/government-design-principles)、[Service Standard](https://www.gov.uk/service-manual/service-standard)、[Question pages](https://design-system.service.gov.uk/patterns/question-pages/)、[Writing guidelines](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/)。利用者の必要、単純さ、接点の連続性、質問の必要性、分かる言葉を参照する。政府の審査制度や英語固有の規則は持ち込まない。
- Canada.ca：[GC Design System](https://design-system.canada.ca/en/)、[Canada.ca design](https://design.canada.ca/)、[Information architecture and findability](https://design.canada.ca/specifications/information-findability.html)、[Designing content](https://design.canada.ca/continuous-improvement/designing.html)、[Monitoring and measuring task success](https://design.canada.ca/continuous-improvement/monitoring.html)。情報を見つけ理解して使う構造と課題達成の検証を参照する。英仏二言語、政府ブランド、指定ドメインは案件の条件と区別する。

## 参考資料と独自の採用判断

- [minorun365/minorun-marp-skillのslide-story](https://github.com/minorun365/minorun-marp-skill/blob/c6b20bbb8a1f2d2059e3764e2acd539c312785e4/skills/slide-story/SKILL.md)：Minoru Onda、commit `c6b20bbb8a1f2d2059e3764e2acd539c312785e4`、2026-09-21確認。[Apache-2.0](https://github.com/minorun365/minorun-marp-skill/blob/c6b20bbb8a1f2d2059e3764e2acd539c312785e4/LICENSE)。読者、説明順序、主張と実例、構成確認の考え方を独自に要約した。配布元のコードや素材は複製していない。
- [Design Convergence共有資料](https://design-convergence.info185987.chatgpt.site/)：2026-09-18取得の書体方針と、用途別の入口・共通データ・可変高レイアウトを参考にした。特定のビュー数・分類・項目数や未実装の保存機能は要件にしない。

ユーザー指定と既存ブランドを優先すること、DADSを新規Webの既定とすること、IBM Plex Sans JPとfallback、44pxの操作領域、ライト／ダーク、縦の単一HTML読み物、媒体別の確認課題は本パッケージの採用方針。公式DADSのフォント指定・完成済みダークテーマ・PowerPoint仕様とは呼ばない。複数国の部品ライブラリを重ねて導入しない。

元のローカルガイドから汎用部分を再構成した版。元の既定CI公開は、外部環境では既知の承認済み公開先と経路が必要になる。専用サービスの運用手順・配布元エンジン・テンプレートは含まない。
