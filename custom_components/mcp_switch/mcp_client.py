import asyncio
import os
import subprocess
import logging

_LOGGER = logging.getLogger(__name__)

class MCPProcess:
    def __init__(self, xiaozhi_mcp_endpoint, ha_mcp_endpoint, ha_token):
        self.xiaozhi_mcp_endpoint = xiaozhi_mcp_endpoint
        self.ha_mcp_endpoint = ha_mcp_endpoint
        self.ha_token = ha_token
        self.process = None

    async def start(self):
        if self.process:
            return
        env = dict(**os.environ)
        env["XIAOZHI_MCP_ENDPOINT"] = self.xiaozhi_mcp_endpoint
        env["HA_MCP_ENDPOINT"] = self.ha_mcp_endpoint
        env["API_ACCESS_TOKEN"] = self.ha_token
        self.process = await asyncio.create_subprocess_exec(
            "python3", "custom_components/mcp_bridge/mcp_pipe.py",
            env=env,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.STDOUT,
        )
        _LOGGER.info("Started MCP process.")
        # 启动异步任务读取日志
        asyncio.create_task(read_process_output(self.process))

    async def stop(self):
        if self.process:
            self.process.kill()
            await self.process.wait()
            self.process = None
            _LOGGER.info("Killed MCP process.")

async def read_process_output(mcp_process):
    assert mcp_process.stdout is not None
    while True:
        line = await mcp_process.stdout.readline()
        if not line:
            break
        _LOGGER.info("[MCP] %s", line.decode().rstrip())