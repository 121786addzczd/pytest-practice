# このリポジトリは pytest の練習用リポジトリです

## ライブラリの導入

以下のコマンドで必要なライブラリをインストールします。

```shell
pip install pytest pytest-subtests pytest-cov
```

## テストの実行方法

### 通常のテスト実行

```shell
pytest unit
```

### 詳細なテスト結果を表示して実行

```shell
pytest unit -v
```

### print 文の出力を表示しながら実行

```shell
pytest unit -v -s
```

### 特定のファイルのみをテスト実行

```shell
pytest -v -s unit/tests/test_calculator.py
```

### 特定のテスト関数のみを実行

```shell
pytest -v -s unit/tests/test_calculator.py::test_multiply_invalid_inputs
```

### 特定のファイルを対象にテストを実行し、カバレッジを出力

```shell
pytest --cov=src --cov-report=term-missing -v -s
```

### HTML 形式のカバレッジレポートを生成

```shell
pytest --cov=src --cov-report=html
```

htmlcov ディレクトリが生成され、index.html ファイルを見ることで可視化できます

### 特定のマーカーを付与したテストのみを実行する
```shell
pytest -m raises -v -s
```
このコマンドを実行すると、関数の上部に@pytest.mark.raisesと記載されたテストコードのみが実行されます。raisesマーカーの設定は、pytest.iniファイルに記載されています。

raisesマーカー以外のテストコードを実行する場合は、以下コマンドになります。
```shell
pytest -m "not raises" -v -s
```

### テストをスキップする場合
テスト関数の上部に@pytest.mark.skip(reason="作成途中")と記載することで、そのテストはスキップされます。reasonの文字列は任意の値で問題ありません。
例
```python
pytest.mark.skip(reason="作成途中")
def test_features_xyz():
    # 要件が決まり次第着手
    pass
```