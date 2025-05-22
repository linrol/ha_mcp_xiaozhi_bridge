小智AI通过MCP Agent方式接入HA
# ha_mcp_xiaozhi_bridge
小智官方服务器(虾哥)对接home assistant的mcp server 桥接集成
### 原理
使用小智官方给的示例代码，结合mcp_proxy,实现小智官方服务器和home assistant的mcp server打通，并以插件形式接入HA

### 安装
请使用以下方式安装:

#### 方法 1： HACS安装

> 1. 确保`Home Assistant`中已安装HACS
> 2. 打开`HACS`, 点击`[Custom repositories]`, `Repository` 输入: `https://github.com/linrol/ha_mcp_xiaozhi_bridge`, `Category` 选择 `[Integration]`
> 3. **重启Home Assistant**.

#### 方法 2：手动安装

> 1. 从[Latest Release](https://github.com/linrol/ha_mcp_xiaozhi_bridge/releases/latest) 下载 `mcp_bridge.zip`
> 2. 解压并复制 `uiot_home` 到 `/custom_components/`.
> 3. **重启 Home Assistant**.

### 配置
XIAOZHI_MCP_ENDPOINT：你的小智 MCP 接入点
HA_MCP_ENDPOINT：你的 HA MCP SERVER 地址
API_ACCESS_TOKEN：你的长效 API 令牌

1.  **小智 MCP 接入点：** 登录小智官方服务器即可获取。
2.  **HA MCP SERVER 地址：** 通过 HA 官方的 `mcp_server` 集成获取。
    * 点击此链接：[Home Assistant MCP Server 集成](https://my.home-assistant.io/redirect/config_flow_start?domain=mcp_server)直达安装
    * 或 在 Home Assistant 中，前往 **设置 > 设备和服务 > 添加集成**。
    * 从列表中选择“**模型上下文协议服务器**”，并按照屏幕上的说明完成设置。
3.  **长效 API 令牌：** 用于授权访问你的 Home Assistant 实例。
    * 访问你的 [Home Assistant 账户配置文件设置](https://my.home-assistant.io/redirect/profile)，进入“**安全**”选项卡。
    * 创建**长期访问令牌**。

### 启动
配置完成后会出现一个switch的实体开关，控制集成的开启和关闭，
成功开启后，在小智 控制台 MCP接入点可看到接入点状态