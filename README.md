# 客户跟进工作台

单文件 HTML 客户管理工具，数据存储在浏览器本地（localStorage），不依赖后端。

## 在线访问

部署到 GitHub Pages 后，通过 `https://<用户名>.github.io/<仓库名>/客户跟进工作台.html` 访问。

## 功能

- 客户信息管理（增删改查、批量导入导出）
- 积分消耗看板（导入 AWB 客户积分消耗表：按源表列序原样呈现、分组表头、列排序、快捷视图与筛选、分层/待消耗/上期→当前消耗率变化图表、客户明细与跟进记录、多批次环比）
- 图片识别（千问视觉模型，自动填表）
- AI 跟进建议（千问文本模型）
- 合作方案书生成与导出 PDF
- 多皮肤 / 深色模式
- 数据本地存储，支持 JSON 备份

## 本地使用

双击 `启动本地服务器.bat`，从 `http://localhost:8000` 打开。

## 数据说明

所有数据存储在浏览器的 localStorage 中，不上传到任何服务器。
API Key 也存在本地浏览器中，不包含在本仓库代码中。

积分消耗看板的数据来自你自己在后台导出的表格，导入后同样只存在本机浏览器（localStorage 键：`df_customer_workbench_credits_v1`、`df_customer_workbench_credit_notes_v1`、`df_customer_workbench_credits_ui_v1`），仓库内不含任何真实客户数据；「导出 JSON / 导入 JSON」全量迁移包已包含这三个键。
