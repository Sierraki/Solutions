# Python 现代化开发指南：从零开始部署 uv (Windows 版)

这份文档旨在帮助你从 Anaconda 迁移到 **uv**。uv 是一个极速的 Python 包管理工具，它通过"项目级管理"替代了 Conda 的"全局环境管理"。

---

## 第一阶段：从零安装 (Installation)

### 1. 解决 PowerShell 权限问题

Windows 默认禁止运行脚本，必须先开启权限。打开 **Windows PowerShell** (无需管理员权限即可)，运行：

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

输入 `Y` 并回车确认。

### 2. 执行安装命令

运行官方安装脚本：

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 3. 重启终端

安装显示 "everything's installed" 后，**必须关闭当前 PowerShell 窗口**，重新打开一个新的窗口。

验证是否成功：

```powershell
uv --version
# 输出示例: uv 0.5.x (x86_64-pc-windows-msvc)
```

---

## 第二阶段：创建或接管项目 (Initialization)

uv 的核心逻辑是“原地管理”。你不需要去别的地方建环境，直接在你的代码文件夹里操作。

### 1. 进入你的项目目录

**PowerShell**

```
# 假设你的代码在 S 盘
S:
cd "S:\学习\coding\Solutions"
```

### 2. 初始化项目 (生成账本)

如果是第一次在这个文件夹用 uv，或者文件夹里只有代码没有环境：

```powershell
uv init
```

**效果**：
- 生成 `pyproject.toml` (配置文件) 和 `.python-version`
- 这不会删除你原本的任何代码

### 3. 安装依赖 (生成环境)

根据你的需求安装包（例如数据分析三剑客）：

```powershell
uv add numpy pandas matplotlib ipykernel
```

**效果**：
1. 自动下载 Python (如果不指定，默认用稳定版)
2. 自动创建 `.venv` 文件夹（这就是你的虚拟环境）
3. 自动生成 `uv.lock` (锁定文件，保证版本一致)

---

## 第三阶段：日常使用与 VS Code 配置

### 1. 在 VS Code 中选择环境

这是最重要的一步，否则代码会有波浪线报错。

1. 用 VS Code 打开你的项目文件夹 (`S:\学习\coding\Solutions`)
2. 按 `Ctrl + Shift + P`
3. 输入并选择：`Python: Select Interpreter`
4. **选择带星星/推荐的选项**：通常显示为 `('.venv': venv)`

### 2. 常用命令速查表

| 任务 | 旧 Conda 命令 | 新 uv 命令 |
|------|---------------|----------|
| 安装包 | `conda install numpy` | `uv add numpy` |
| 指定版本安装 | `conda install numpy=1.26` | `uv add "numpy==1.26"` |
| 开发专用包 | N/A | `uv add --dev black` |
| 运行脚本 | `python main.py` | `uv run main.py` |
| 更新锁文件 | N/A | `uv sync` |
| 清理缓存 | `conda clean --all` | `uv cache clean` |

---

## 第四阶段：多电脑同步 (Git Workflow)

如果你需要在两台电脑（A 和 B）之间同步代码。

### 1. 电脑 A (源头) 设置

确保 `.venv` 文件夹**不要**上传到 Git。

- 检查项目根目录下的 `.gitignore` 文件，确保包含一行：

```
.venv/
```

- 提交并推送 `pyproject.toml` 和 `uv.lock`

### 2. 电脑 B (新环境) 还原

在新电脑上拉取代码后，不需要 `init` 也不需要 `add`，直接运行：

```powershell
uv sync
```

**效果**：uv 会读取 `uv.lock`，瞬间还原出一个一模一样的环境。

---

## 第五阶段：常见报错与解决方案 (Troubleshooting)

这是你在部署过程中遇到过的实际问题及其解法。

### ❌ 问题 1: `uv: The term 'uv' is not recognized`

* **原因** ：安装后没有重启终端，或者环境变量没刷新。
* **解决** ：

1. 关闭所有终端窗口，重新打开。
2. 如果还不行，运行：`$env:Path = "C:\Users\$env:USERNAME\.local\bin;$env:Path"`。

### ❌ 问题 2: `os error 5: 拒绝访问` (Failed to remove directory)

* **原因** ：VS Code 或某个 Python 进程正在占用 `.venv` 文件夹，导致 uv 无法更新或删除它。
* **解决** ：

1. **彻底关闭 VS Code** 。
2. 在独立的 PowerShell 窗口运行 `uv sync`。
3. 如果还报错，手动删除 `.venv` 文件夹后重试。

### ❌ 问题 3: `requirements are unsatisfiable` (Python 版本冲突)

* **报错示例** ：`numpy==2.4.1 depends on Python>=3.11... but your project requires >=3.10`。
* **原因** ：`pyproject.toml` 里设置的最低 Python 版本太低，而你要装的包需要更高版本的 Python。
* **解决** ：

1. 打开 `pyproject.toml`。
2. 找到 `requires-python = ">=3.10"`。
3. **修改为更高的版本** ，例如 `">=3.11"` 或 `">=3.12"`。
4. 重新运行 `uv sync`。

### ❌ 问题 4: PowerShell 脚本无法运行

* **报错示例** ：`PowerShell requires an execution policy...`
* **解决** ：
  运行 `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`。

---

## 💡 最佳实践总结

1. **一个项目 = 一个环境** ：不要试图搞全局环境，每个项目文件夹里都 `uv init` 一次。
2. **只传图纸，不传房子** ：用 Git 同步 `uv.lock`，永远不要同步 `.venv`。
3. **遇到问题先 sync** ：环境乱了、换电脑了、报错了，先关掉 VS Code 运行 `uv sync`，通常能解决 90% 的问题。
