"""
conftest.py

このファイルは、pytestで使用される共通処理やグローバルな設定を行うためのファイルです。
テスト全体に影響を与えるフィクスチャやフック関数はここに定義されます。

一般的には、各テストで共通して使用される前処理や設定などが含まれますが、
テストファイルごとの固有の設定やフィクスチャはここには含めません。

例: pytestフック関数、全体で共通のフィクスチャ、共通の設定
"""

import logging.config
import yaml
import pytest
import os


# ログディレクトリを作成
log_dir = os.path.join(os.path.dirname(__file__), '..', 'logs')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# YAMLファイルのパスを指定
config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'logging_config.yml')

# YAMLファイルからログ設定を読み込む
with open(config_path, 'r') as file:
    config = yaml.safe_load(file.read())

    # 設定ファイルの検証
    if 'handlers' not in config or 'file' not in config['handlers']:
        raise ValueError("無効なログ設定: 'file' ハンドラーが見つかりません")

    logging.config.dictConfig(config)

# ロガーを取得
test_logger = logging.getLogger(__name__)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_setup(item):
    """
    テストの実行前にログを記録する。

    Args:
        item: pytestのテスト項目。テスト関数やその関連情報が含まれている。
    """
    test_logger.info(f"Starting: {item.name}")
    yield

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_teardown(item, nextitem):
    """
    テストの実行後にログを記録する。

    Args:
        item: pytestのテスト項目。テスト関数やその関連情報が含まれている。
        nextitem: 次のテスト項目。
    """
    yield
    test_logger.info(f"Finished: {item.name}")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    pytestフック関数。テストの実行結果をキャプチャし、エラーが発生した場合にログを記録する。

    Args:
        item: pytestのテスト項目。テスト関数やその関連情報が含まれている。
        call: テストの実行結果（成功、失敗、スキップのいずれか）。
    """
    outcome = yield
    report = outcome.get_result()

    if report.failed:
        test_logger.error(f"Test failed: {item.name}", exc_info=call.excinfo)
    elif report.skipped:
        test_logger.warning(f"Test skipped: {item.name}")

def pytest_runtest_call(item):
    """
    pytestフック関数。各テスト関数が実行される際に、そのテスト関数のdocstringを取得して表示する。

    この関数はpytestの実行中に自動的に呼び出され、実行中のテスト関数にdocstringが存在する場合、
    その内容をターミナルに出力する。出力後の改行を避けるため、print関数のendパラメータに空文字列を指定している。

    Args:
        item: pytestのテスト項目。テスト関数やその関連情報が含まれている。
    """
    doc = item.function.__doc__
    if doc:
        print(f"{doc}", end="")

