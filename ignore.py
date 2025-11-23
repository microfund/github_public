#!/usr/bin/env python3
"""
.gitignoreファイル生成スクリプト
Pythonプロジェクト用の標準的な.gitignoreファイルを作成します
"""

import os
from pathlib import Path

def create_gitignore(path=".gitignore", project_type="python"):
    """
    .gitignoreファイルを作成する
    
    Args:
        path: .gitignoreファイルのパス（デフォルト: カレントディレクトリ）
        project_type: プロジェクトタイプ（現在は'python'のみサポート）
    """
    
    # Pythonプロジェクト用の標準的な.gitignore内容
    python_gitignore = """# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
Pipfile.lock

# poetry
poetry.lock

# pdm
.pdm.toml

# PEP 582
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
.idea/

# VSCode
.vscode/
*.code-workspace

# macOS
.DS_Store
.AppleDouble
.LSOverride

# Windows
Thumbs.db
Thumbs.db:encryptable
ehthumbs.db
ehthumbs_vista.db
*.stackdump
[Dd]esktop.ini

# Linux
*~
.fuse_hidden*
.directory
.Trash-*
.nfs*

# プロジェクト固有の除外項目
# 必要に応じて以下に追加してください
# /data/
# /logs/
# /config/local.py
"""
    
    # ファイルが既に存在するか確認
    if os.path.exists(path):
        response = input(f"{path} は既に存在します。上書きしますか？ (y/n): ")
        if response.lower() != 'y':
            print("操作をキャンセルしました。")
            return False
    
    try:
        # .gitignoreファイルを作成
        with open(path, 'w', encoding='utf-8') as f:
            if project_type == "python":
                f.write(python_gitignore)
            else:
                print(f"警告: '{project_type}' タイプはサポートされていません。Pythonテンプレートを使用します。")
                f.write(python_gitignore)
        
        print(f"✅ {path} を正常に作成しました。")
        print(f"📁 ファイルサイズ: {os.path.getsize(path)} bytes")
        return True
        
    except Exception as e:
        print(f"❌ エラーが発生しました: {e}")
        return False


def add_custom_patterns(path=".gitignore", patterns=None):
    """
    既存の.gitignoreファイルにカスタムパターンを追加
    
    Args:
        path: .gitignoreファイルのパス
        patterns: 追加するパターンのリスト
    """
    if patterns is None:
        patterns = []
    
    if not os.path.exists(path):
        print(f"❌ {path} が存在しません。先に create_gitignore() を実行してください。")
        return False
    
    try:
        with open(path, 'a', encoding='utf-8') as f:
            f.write("\n# カスタム追加パターン\n")
            for pattern in patterns:
                f.write(f"{pattern}\n")
        
        print(f"✅ {len(patterns)} 個のパターンを追加しました。")
        return True
        
    except Exception as e:
        print(f"❌ エラーが発生しました: {e}")
        return False


def main():
    """メイン関数"""
    print("=== .gitignore ファイル生成ツール ===\n")
    
    # 基本的な.gitignoreを作成
    create_gitignore()
    
    # カスタムパターンを追加するか確認
    add_custom = input("\nカスタムパターンを追加しますか？ (y/n): ")
    if add_custom.lower() == 'y':
        patterns = []
        print("追加するパターンを入力してください（空行で終了）:")
        while True:
            pattern = input("> ")
            if pattern == "":
                break
            patterns.append(pattern)
        
        if patterns:
            add_custom_patterns(patterns=patterns)
    
    print("\n完了しました！")


if __name__ == "__main__":
    main()