# design-rules

UI・HTML資料・図解を作成、改稿、レビューするための日本語デザインルールと、外部のAIエージェントで使える独立したスキルです。利用者が情報を見つけ、理解し、判断し、目的を達成できることを優先します。

設計では、確認できた現状（As-Is）と将来構想（Vision）を分離し、採用済みの目標状態（To-Be）、実装済み、検証済みを区別します。詳細は[共通原則](skills/design/references/principles.md)を参照してください。

読む入口は [デザインスキル](skills/design/SKILL.md)。内容の一覧は [SITEMAP](SITEMAP.md) にあります。外部スキル、プラグイン、専用サービスへの依存はありません。

## AIに読ませる

[生のSKILL.md](https://raw.githubusercontent.com/hogehonya/design-rules/main/skills/design/SKILL.md) を渡し、そこから参照するガイドも必要な範囲で取得させてください。SKILL.mdだけでは具体的な実装基準を含む全ルールを読み込めません。

## インストール

リポジトリを対象プロジェクトとは別の作業場所へcloneします。

```sh
git clone https://github.com/hogehonya/design-rules.git
```

そのclone内から、対象エージェントが対応するスキルディレクトリへ `skills/design` 全体をコピーします。以下はプロジェクト内の `.agents/skills` を読むエージェント向けの例です。`/path/to/project` は実際の対象に置き換えてください。既存の `design` があれば停止し、上書きしません。

```sh
mkdir -p /path/to/project/.agents/skills
if [ -e /path/to/project/.agents/skills/design ]; then
  echo 'design already exists; choose another destination' >&2
else
  cp -R skills/design /path/to/project/.agents/skills/design
fi
```

エージェントごとに配置先とスキル呼び出し方法を確認してください。コピー単位の中で参照が完結するので、他のディレクトリは不要です。通常のMarkdownガイドとして読むこともできます。

## 適用と公開の境界

優先順位は「ユーザーの明示指示 → 既存のデザインシステム → DADS」です。IBM Plex Sans JP、テーマ、操作領域などの採用判断は、このパッケージの方針であり政府の公式指定とは区別します。[出典と採用範囲](skills/design/references/sources.md) を参照してください。

元の運用では閲覧用HTMLの制作に既定のCI公開が含まれます。本パッケージは特定の公開先や権限を配布しません。利用環境で公開先・承認範囲・CI経路が設定されている場合は公開と公開画面の検証まで進め、足りなければ不足を報告します。制作依頼だけから任意の場所への公開や外部配送を追加しません。

元ガイドの考え方を独立した文書として再構成しています。第三者のコード、フォント、コンポーネント、素材は同梱していません。参照先の利用条件は各配布元で確認してください。今回新規執筆した文書と検証コードは [MIT License](LICENSE) で配布します。参照先の元スキル、コード、画像、書体の権利とライセンスは対象外です。

## 検証

Python 3.9以上の標準ライブラリだけで実行できます。

```sh
python3 scripts/check.py
```

必須ファイル、スキルのfrontmatter、Markdownの相対リンク、代表的なローカル環境情報の混入を確認します。外部URLの到達性や、制作物のアクセシビリティを保証する検査ではありません。push・PRでも同じチェックを実行します。
