# FORK.md — 本发行版的来源与改动

这份文件是该 fork 的合规记录。**分发前请先读完「分发红线」一节。**

## 来源

| 项 | 值 |
|---|---|
| 上游仓库 | https://github.com/CursorTouch/Windows-MCP |
| 上游版本 | v0.8.8（`fbb2ac6`，2026-10-27） |
| 许可证 | MIT，© 2025 JEOMON GEORGE |
| 本发行版名称 | DeskBuddy（桌面搭子） |

## MIT 允许什么、要求什么

MIT 明确授予 *"to deal in the Software without restriction, including ... the rights to ... **sell** copies"*。
因此**改名、修改、闭源、收费分发都是允许的**，不需要向原作者支付任何费用，也不需要公开自己的改动。

代价只有一条（LICENSE.md 正文第二段）：

> The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

即：**版权声明和许可声明必须随每一份副本走**。`LICENSE.md` 已原样保留，请勿删除、改写或替换成自己的协议。MIT **不授予商标权**，这一条决定了下面「分发红线」的第 2 点。

## 本 fork 相对上游改了什么

只改「用户能看到的东西」，包名 / 配置目录 / 线程名一律不动，目的是把与上游的分叉压到最小、便于以后合并上游更新。

| 文件 | 改动 | 原因 |
|---|---|---|
| `src/windows_mcp/branding.py` | 新增：产品名、中文名、MCP server 名、上游归属信息集中在此 | 品牌信息单点维护，改一行即全站生效 |
| `src/windows_mcp/__main__.py` | FastMCP 的 `name` 改为 `branding.MCP_SERVER_NAME` | 对外显示名 |
| `src/windows_mcp/__main__.py` | `--help` 文本改为产品名 + MIT 归属行 | 让许可证要求在用户可见处达成 |
| `src/windows_mcp/__main__.py` | 遥测默认值 `"true"` → `"false"`，判断改为 `== "true"` | 见下节 |
| `README.md` / `SECURITY.md` / `CLAUDE.md` | 同步遥测默认值与归属说明 | 文档不能和代码打架 |
| `LICENSE.md` | **未改动** | MIT 义务 |

**未改动且刻意不改**：Python 包名 `windows_mcp`、CLI 命令名 `windows-mcp`、配置目录 `~/.windows-mcp`、`server.json`。改这些会破坏已安装用户的环境，且对最终用户不可见。

## 遥测：从默认开启改为默认关闭

上游行为：`ANONYMIZED_TELEMETRY` 缺省为 `true`，启动即用**硬编码的 PostHog key** 向 `https://us.i.posthog.com` 上报（`disable_geoip=False`，含地理位置）。采集范围是工具名与错误信息，不含参数与输出。

转卖后这个默认值不能留，原因不是「技术上危险」，而是**法律主体变了**：

- 分发者成为该产品的个人信息处理者，需要具备合法性基础；
- 默认开启 = 用户没有选择，不构成「同意」；
- 数据出境到美国，属于《个人信息保护法》第 38/39 条要单独同意的情形。

所以本 fork 改为**默认不发**，想用上游指标的人自行设 `ANONYMIZED_TELEMETRY=true`。
判断写成 `== "true"` 而非 `!= "false"`，是为了让空值、拼错的值一律 fail-closed —— 少一次「以为关了其实没关」。

## 分发红线

1. **不要删 `LICENSE.md`**，也不要把它换成自己的闭源协议。
2. **不要用上游名字或 `Windows` 作产品名**。
   - 蹭上游名 → 混淆行为，《反不正当竞争法》第 6 条；
   - `Windows` 是微软商标，微软商标准则禁止把它作为产品名暗示与微软有关联。
3. **不要宣称「自主研发」「原创」**。写「基于开源项目 Windows-MCP 二次开发」没有风险，隐瞒才有 —— 虚假宣传按《反不正当竞争法》第 8 条，起步 20 万。
4. **不要往 MCP 官方 registry 注册**（`server.json` 里的 `io.github.CursorTouch/...` 标识不属于你）。
5. **不要抄别人的二次开发成果**。上游开源不等于「基于它做出来的东西都自由」——
   参考 (2021)最高法知民终51号：OpenWrt（GPLv2）二次开发的网关软件被前员工带走复制，判赔 50 万；法院明确「是否违反开源协议」与「是否享有著作权」相对独立。
6. **必须提示风险**：该软件按 MIT 是 AS IS 无担保，但它会接管键鼠与 UIA。误操作可能造成用户数据丢失，服务条款里要写明，并对高危操作做确认。

## 上游同步

```bash
git fetch upstream && git merge --ff-only upstream/main
```

合并时留意 `__main__.py` 的三处改动（`branding` import、`FastMCP(name=...)`、遥测判断）——上游若改动同一区域会产生冲突，按本文件的意图解决即可。
